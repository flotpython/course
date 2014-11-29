import sys
import os
import time

"""
display the code for a module - or parts thereof
not the nicest code ever, but it does the job
"""

# do not even try files that end with these suffixes
excludes = [".so", ".pyc"]

def line_mark(lineno, width):
    return str(lineno).rjust(width, '0')

def check_legit(module):
    "is this an attempt to sneak at corrections ?"
    module_name = module.__name__
    if "corrections" not in module_name:
        return True
    try:
        uid = os.getuid()
        md5 = os.path.basename(os.path.normpath(os.getenv("HOME")))
        now = time.strftime("%D-%H:%M", time.localtime())
        logname = os.path.join(os.getenv("HOME"), ".cheat")
        with open(logname, 'a') as log:
            line = "{now} {module_name}\n".format(**locals())
            log.write(line)
    except Exception as e:
        # import traceback
        # traceback.print_exc()
        # surprisingly enough if I leave these two lines in service I get his
        # Traceback (most recent call last):
        #   File "/appli/MoocExercices/ipython/modules/modtools.py", line 26, in check_legit
        #     with open(logname, 'a') as log:
        # IOError: [Errno 13] Permission denied: '/appli/students/d571a944a682f2a4fa95ea37bf527380/.cheat'
        # and the reason this is odd is we do the exact same thing with .correction
        # and that works fine, even recently new persons have tried
        pass

def show_module(module, beg=None, end=None, prefix='|',lineno_width=0):
    """
    display the source code for a module (or package as a matter of fact)
    if beg is provided, listing starts with the first matching line
    if end is provided, listing ends with the first matching line (excluded)
    """
    # check this is a module
    if type(module) is not type(sys):
        print "show_module: Unexpected input {}".format(module)
        return
    if not check_legit(module):
        print "Nice try"
        return
    try:
        name = module.__name__
        # use .py instead of .pyc if that's what we get
        file = module.__file__.replace(".pyc", ".py")
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
            lineno = 0
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

# this was not too bad on a mac retina but still not right
# with other environments
#html_style = 'max_height=300px; font-size:11px; line-height:15px;'
html_style = 'max_height=300px; font-size:x-small; line-height:15px;'

html = ""

from IPython.display import HTML
# ceci est un ajout de derniere minute, aussi pour ne pas casser ce qui
# marche je prefere copier-coller show_module
def show_module_html(module, beg=None, end=None, prefix='|',lineno_width=0):
    """
    display the source code for a module (or package as a matter of fact)
    if beg is provided, listing starts with the first matching line
    if end is provided, listing ends with the first matching line (excluded)
    """
    global html
    html = "<pre style='{}'>".format(html_style)
    def htmlprint(*args):
        global html
        html += " ".join(args) + "\n"
    def htmlprint_nonl(*args):
        global html
        html += " ".join(args)

    # check this is a module
    if type(module) is not type(sys):
        htmlprint("show_module: Unexpected input {}\n".format(module))
        return HTML(html+"</pre>")
    try:
        name = module.__name__
        # use .py instead of .pyc if that's what we get
        file = module.__file__.replace(".pyc", ".py")
        for exclude in excludes:
            if file.endswith(exclude):
                htmlprint("Cannot display {}, wrong type".format(file))
                return HTML(html+"</pre>")
        # we start in showing mode unless beg was provided
        showing = True if not beg else False
        with open(file) as input:
            htmlprint("Fichier {}".format(file))
            htmlprint(40*"-")
            if not showing: 
                htmlprint("<...>")
            lineno = 0
            for line in input.readlines():
                lineno += 1
                # turn on showing mode if beg string is seen
                if beg and line.find(beg)>=0: 
                    showing = True
                # get out if in showing mode and end string is seen
                if showing and end and line.find(end)>=0:
                    htmlprint("<...>")
                    return HTML(html+"</pre>")
                # print this line if in showing mode
                if showing: 
                    mark = '' if lineno_width <= 0 else line_mark(lineno, lineno_width)
                    htmlprint_nonl(mark+prefix+line)
    except AttributeError as e:
        htmlprint("show_module: Could not find module {}".format(module))
    except Exception as e:
        htmlprint("show_module: Could not show module {}".format(name))
        import traceback
        traceback.print_exc()
    return HTML(html+"</pre>")

########################################
# this works for packages as well
show_package = show_module
show_package_html = show_module_html
