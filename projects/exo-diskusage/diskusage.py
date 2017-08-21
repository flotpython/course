#! /usr/bin/env python3

# we assume 3.6 as we use f-strings


"""
diskusage: a utility to estimate the size of a whole filesystem tree

this runs in 2 passes 

pass1: save the total size in each directory in a .du file

pass2: an interactive tool for navigating the tree
       and spotting the files to be cleaned up
"""

import os
import os.path
from argparse import ArgumentParser


########## helper class
class HumanReadableSize(int):
    """
    helper class for displaying size in bytes 
    in a human-readable form
    """

    # http://en.wikipedia.org/wiki/Petabyte
    ### the unit to use for a size in 2**n
    # 2**10 = 1024 = 1 kilo
    LABELS = [ (6, 'EiB'), (5, 'PiB'), (4, 'TiB'),
               (3, 'GiB'), (2, 'MiB'), (1, 'KiB'),
               (0, 'Byt') ]
    # compute 2**(10.n)
    UNIT_LABELS = [ (2**(10*n), s) for (n, s) in LABELS ]

    def __repr__ (self):
        """
        Display size in bytes 
        """
        for ( unit, label ) in self.UNIT_LABELS:
            if self >= unit:
                # small values usually show an int
                if self % unit == 0:
                    return f"{self//unit:3d} {label}"
                else:
                    return f"{self/unit:3.02f} {label}"

    # we have seen that __repr__ is used when __str__ is not defined
    # but in our case since we inherit int, __str__ does get found
    # so let's make it explicit that we want to use our own __repr__
    # for printing too
    __str__ = __repr__


class Cache(dict):
    """
    a dictionary {path: size_in_bytes}

    this is also linked to the file system and the .du files
    in the sense that 
    (*) cache[path] looks in path/.du if not yet in memory
        if nothing else works (not in memory and not in .du)
        we return 0
    (*) cache[path] = size also writes path/.du
        if permission is granted
    """

    special_name = ".du"

    def __init__(self, verbose = False):
        dict.__init__(self)
        self.verbose = verbose

    def __getitem__(self, path):
        """
        Look in memory cache first, then in the .du file
        returns 0 if nothing works
        """        
        if path in self: 
            return dict.__getitem__(self, path)
        else: 
            try:     
                with open(os.path.join(path, self.special_name)) as f:
                    return int(f.read())
            except IOError as e:
                if self.verbose:
                    print(f"Warning - unable to find size for {path}")
                return 0

    def __setitem__(self, path, size):
        """
        remembers path cache in dictionary
        and stores in special file as far as possible

        ignores if not possible for any reason 
        like Permission Denied or the like
        """
        dict.__setitem__(self, path, size)
        # store result in <dir>/.du for second/interactive pass
        special = os.path.join(path, self.special_name)
        try:
            with open(special, 'w') as store:
                store.write(f"{size}\n")
            if self.verbose:
                print(f"Saved size {size} in {special}")
        except IOError as e:
            if self.verbose:
                print (f"Warning, could not save special file {special}")
            # write error - permission denied - don't cache it then
            pass

####################
class ToplevelDir(object):
    """
    toplevel object - only one is created
    for the directory that diskusage.py is run on

    it can run pass1()
    it has one instance of Cache for keeping track
       of the sizes of all subdirs
    it can also run pass2 
    """

    def __init__(self, path, verbose=False):
        self.path = path
        self.verbose = verbose
        self.cache = Cache(verbose=verbose)

    def pass1(self):
        """
        scans a whole tree, and writes
        individual (total) size in .du

        this is done through a Cache object so
        that if we run both passes in the same process
        pass2 will not even need to read .du files
        """        
        if self.verbose:
            print(f"diskusage: running pass1 on {self.path}")
        for root, dirs, files in os.walk (self.path, topdown=False):
            # first deal with files
            filepaths = [os.path.join(root, file) for file in files]
            local_size = sum ([os.path.getsize(filepath) 
                                   for filepath in filepaths 
                                       if os.path.exists(filepath) ])
            # count the directory itself
            local_size += os.path.getsize(root)
            # because we do the traversal bottom up, we already have the size for our immediate sons
            # in the cache; however the disk is alive during this time so it might be
            # that a new son is showing up that we do not know about
            def subdir_size (subdir):
                subpath = os.path.join(root, subdir)
                # in which case we return 0 and not some exception
                return self.cache.get(subpath, 0) 
            # total on the immediate sons
            cumulated_size = sum ([ subdir_size (subdir) for subdir in dirs ])
            # add the local weight (files + this_dir)
            cumulated_size += local_size
            # store in dictionary for dealing with the upper directory
            self.cache [root] = cumulated_size

    help_message = """number\tgo to listed directory
+\tgo to last (and thus biggest) directory - this is the default 
u\tgo one step up - can be also '0' or '..'
.\tcome again (stay in place)
l\tlist files in the current directory
!\tre-run pass1
v\ttoggle verbose on and off
q\tquit
h\tthis help"""

    def move_to_subdir(self, subpath):
        """
        this is the active part of pass2
        it is the place where we prompt 
        for the user's answer and 
        where we implement the mainloop

        this method returns the path for the next
        subtree to visit (can also be one step up)

        we show the immediate subdirs sorted 
        biggest comes last, and can thus be selected using '+'

        subdirs are listed with a number that 
        can be selected for moving down the tree
        
        """
        print(f"{8*'-'} Path {subpath} "
              f"has a total size of {HumanReadableSize(self.cache[subpath])}")
        # we build a list of tuples
        # (lastname, full-path-from-toppath, size)
        sized_subdirs=[ (d, os.path.join(subpath, d), self.cache[os.path.join(subpath, d)])
                      for d in os.listdir(subpath)
                          if os.path.isdir(os.path.join(subpath, d)) ]
        # show biggest last
        sized_subdirs.sort(key=lambda t: t[2])
        for i, (name, _, size) in enumerate(sized_subdirs, 1):
            print(f"{i} {str(HumanReadableSize(size)):>12}   {name}")
        # the interactive mainloop for selecting the next dir
        while True:
            answer = input("Enter number (h for help) ")
            # case does not matter, let's do lowercase
            answer = answer.strip().lower()
            # '+' is the default
            answer = answer or '+'
    
            ### does this look like a number
            index = None
            if answer in '+':
                index = -1
            else:
                try:    index = int(answer)-1
                except: pass
            ### if is indeed is an index
            if index is not None:
                try:
                    _, path, _ = sized_subdirs[index]
                    return path
                except:
                    print ("No such index {}".format(answer))
            ### otherwise
            elif answer in ('..', '0', 'u'):
                return os.path.dirname(subpath)
            elif answer in 'l':
                self.list_files(subpath)
            elif answer in '.':
                return subpath
            elif answer in '!':
                print ("running pass1")
                self.pass1()
            elif answer in 'v':
                self.verbose = not self.verbose
                self.cache.verbose = self.verbose
                if self.verbose: print ("verbose")
            elif answer in 'q':
                exit(0)
            elif answer in 'h?':
                print(self.help_message)
            else:
                print("command not understood")

    def pass2 (self):
        """
        entry point for pass2
        """
        subpath = self.path
        print ("Welcome to inspection of path {}".format(subpath))
        while True:
            subpath = self.move_to_subdir (subpath)

    def list_files(self, subpath):
        """
        passive list of plain files in a given dir
        the ones in *that* directory, not the subtree
        just list with biggest file last

        it's easier to re-read the file size here
        as there is no recursion
        would need to be optimized for directories
        with a large number of plain files
        """
        sized_files = [ (f, os.path.getsize(os.path.join(subpath, f)))
                            for f in os.listdir(subpath)
                                 if os.path.isfile(os.path.join(subpath, f)) ]
        # show biggest last
        sized_files.sort(key=lambda t: t[1])
        print (4*'-', "Plain files in {}".format(subpath))
        for i, (name, size) in enumerate(sized_files):
            print("F {}   {}".format(str(HumanReadableSize(size)).rjust(12), name))


def main():
    """
    The entry point for diskusage.py
    
    This function parses the command line arguments 
    using an instance of ArgumentParser

    It essentially creates an instance of ToplevelDir 
    and sends it the pass1() and/or pass2() methods

    It returns an int suitable to be returned to the OS
    that is to say 0 when everything is fine and 1 otherwise

    """
    parser = ArgumentParser()
    # by default we only run a pass2
    parser.add_argument("-1", "--pass1", dest='pass1', default=False,
                        action='store_true',
                        help="Run pass1, that computes .du in all subdirs")
    parser.add_argument("-b", "--both-passes", dest='all_passes', default=False,
                        action='store_true',
                        help="""Run pass1, that computes .du in all subdirs,
                                and then pass2 that is interactive""")
    parser.add_argument("-v", "--verbose", dest='verbose', default=False,
                        action='store_true',
                        help="turn on verbose output")

    parser.add_argument("dir")

    args = parser.parse_args()
    if args.all_passes:
        run_pass1, run_pass2 = True, True
    elif args.pass1:
        run_pass1, run_pass2 = True, False
    else:
        run_pass1, run_pass2 = False, True

    toplevel_dir = ToplevelDir (args.dir, verbose=args.verbose)
    try:
        run_pass1 and toplevel_dir.pass1()
        run_pass2 and toplevel_dir.pass2()
        return 0
    # user typed End-of-File
    except EOFError as e:
        print()
        return 0
    except KeyboardInterrupt:
        print("Bye")
        return 1
    except Exception as e:
        print('Something went wrong', e)
        import traceback
        traceback.print_exc()
        return 1
        
if __name__ == '__main__':
    exit(main())
