"""
display the code for a module - or parts thereof
not the nicest code ever, but it does the job
"""

# pylint: disable=missing-function-docstring

import sys
import math
import traceback
from pathlib import Path

from IPython.display import HTML


# do not even try files that end with these suffixes
excludes = [".so", ".pyc"]


def line_mark(lineno, width):
    if width <= 0:
        return ''
    return str(lineno).rjust(width, '0')


def check_legit(module):
    "is this an attempt to sneak at corrections ?"
    module_name = module.__name__
    if "corrections" not in module_name:
        return True


def guess_lineno_width(filename):
    with open(filename, encoding="utf-8") as feed:
        nb_lines = sum(1 for x in feed)
    if nb_lines == 0:
        return 0
    return int(math.log(nb_lines, 10)) + 1


def show_module(module, beg=None, end=None, prefix='|', lineno_width=None):
    """
    display the source code for a module (or package as a matter of fact)
    if beg is provided, listing starts with the first matching line
    if end is provided, listing ends with the first matching line (excluded)
    """
    # check this is a module
    if type(module) is not type(sys):
        print(f"show_module: Unexpected input {module}")
        return
    if not check_legit(module):
        print("Nice try")
        return
    name = module.__name__
    try:
        # use .py instead of .pyc if that's what we get
        file = module.__file__.replace(".pyc", ".py")
        for exclude in excludes:
            if file.endswith(exclude):
                print(f"Cannot display {file}, wrong type")
                return
        # we start in showing mode unless beg was provided
        showing = True if not beg else False
        if lineno_width is None:
            lineno_width = guess_lineno_width(file)
        with open(file, encoding="utf-8") as feed:
            print(f"Fichier {file}")
            print(40 * "-")
            if not showing:
                print("<...>")
            for lineno, line in enumerate(feed, 1):
                # turn on showing mode if beg string is seen
                if beg and line.find(beg) >= 0:
                    showing = True
                # get out if in showing mode and end string is seen
                if showing and end and line.find(end) >= 0:
                    print("<...>")
                    return
                # print this line if in showing mode
                if showing:
                    mark = line_mark(lineno, lineno_width)
                    print(mark + prefix + line, end='')
    except AttributeError:
        print(f"show_module: Could not find module {module}")
    except Exception:                            # pylint: disable=broad-except
        print(f"show_module: Could not show module {name}")
        traceback.print_exc()


# this was a last minute addition, so in order to avoid breaking
# what works, it seems best to copy show_module

def show_module_html(module, beg=None, end=None, prefix='|', lineno_width=None):
    """
    display the source code for a module (or package as a matter of fact)
    if beg is provided, listing starts with the first matching line
    if end is provided, listing ends with the first matching line (excluded)
    """

    # this was not too bad on a mac retina but still not right
    # with other environments
    #html_style = 'max_height=300px; font-size:11px; line-height:15px;'
    html_style = 'max_height=300px; font-size:x-small; line-height:15px;'


    html = f"<pre style='{html_style}'>"

    def htmlprint(*args):
        nonlocal html
        html += " ".join(args) + "\n"

    def htmlprint_nonl(*args):
        nonlocal html
        html += " ".join(args)

    def html_finish():
        return HTML(html + "</pre>")

    # check this is a module
    if type(module) is not type(sys):
        htmlprint(f"show_module: Unexpected input {module}\n")
        return html_finish()
    name = module.__name__
    try:
        # use .py instead of .pyc if that's what we get
        file = module.__file__.replace(".pyc", ".py")
        for exclude in excludes:
            if file.endswith(exclude):
                htmlprint(f"Cannot display {file}, wrong type")
                return html_finish()
        # we start in showing mode unless beg was provided
        showing = True if not beg else False
        if lineno_width is None:
            lineno_width = guess_lineno_width(file)
        with open(file, encoding="utf-8") as feed:
            htmlprint(f"Fichier {file}")
            htmlprint(40 * "-")
            if not showing:
                htmlprint("<...>")
            for lineno, line in enumerate(feed):
                # turn on showing mode if beg string is seen
                if beg and line.find(beg) >= 0:
                    showing = True
                # get out if in showing mode and end string is seen
                if showing and end and line.find(end) >= 0:
                    htmlprint("<...>")
                    return html_finish()
                # print this line if in showing mode
                if showing:
                    mark = line_mark(lineno, lineno_width)
                    htmlprint_nonl(mark + prefix + line)
    except AttributeError:
        htmlprint(f"show_module: Could not find module {module}")
    except Exception:                            # pylint: disable=broad-except
        htmlprint(f"show_module: Could not show module {name}")
        traceback.print_exc()
    return html_finish()


def find_on_disk(package, modname):
    """
    Gory details of locating a .py file on the hard drive
    from a preloaded package (package_relatif) and a filename like 'loader1.py'
    """
    folder = Path(package.__file__).parent
    modfile = folder / modname
    if not modfile.exists():
        raise ValueError(f"Could not spot file for module {modname} "
                         f"in package {package}")
    return str(modfile)
