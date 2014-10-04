import sys

"""
display the code for a module - or parts thereof
not the nicest code ever, but it does the job
"""

# do not even try files that end with these suffixes
excludes = [ ".so", ".pyc" ]

def line_mark (lineno, width):
    return str(lineno).rjust(width,'0')

def show_module (module, beg=None, end=None, prefix='|',lineno_width=0):
    """
    display the source code for a module (or package as a matter of fact)
    if beg is provided, listing starts with the first matching line
    if end is provided, listing ends with the first matching line (excluded)
    """
    # check this is a module
    if type(module) is not type(sys):
        print "show_module: Unexpected input {}".format(module)
        return
    try:
        name = module.__name__
        # use .py instead of .pyc if that's what we get
        file = module.__file__.replace(".pyc",".py")
        for exclude in excludes:
            if file.endswith(exclude):
                print "Cannot display {}, wrong type".format(file)
                return
        # we start in showing mode unless beg was provided
        showing = True if not beg else False
        with open(file) as input:
            print "Fichier {}".format(file)
            print 40*"-"
            if not showing: 
                print "<...>"
            lineno=0
            for line in input.readlines():
                lineno += 1
                # turn on showing mode if beg string is seen
                if beg and line.find(beg)>=0: 
                    showing = True
                # get out if in showing mode and end string is seen
                if showing and end and line.find(end)>=0:
                    print "<...>"
                    return
                # print this line if in showing mode
                if showing: 
                    mark = '' if lineno_width <= 0 else line_mark(lineno, lineno_width)
                    print mark+prefix+line,
    except AttributeError as e:
        print "show_module: Could not find module {}".format(module)
    except Exception as e:
        print "show_module: Could not show module {}".format(name)
        import traceback
        traceback.print_exc()

# this works for packages as well
show_package=show_module
