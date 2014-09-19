import sys

def show_module (module, beg=None, end=None):
    """
    display the source code for a module
    if beg is provided, listing starts with the first matching line
    if end is provided, listing ends with the first matching line (excluded)
    """
    # check this is a module
    if type(module) is not type(sys):
        print "show_module: Unexpected input {}".format(module)
        return
    try:
        name = module.__name__
        file = module.__file__
        # we start in showing mode unless beg was provided
        showing = True if not beg else False
        with open(module.__file__) as input:
            print "Fichier {}".format(module.__file__)
            if not showing: 
                print "<...>"
            for line in input.readlines():
                # turn on showing mode if beg string is seen
                if beg and line.find(beg)>=0: 
                    showing = True
                # get out if in showing mode and end string is seen
                if showing and end and line.find(end)>=0:
                    print "<...>"
                    return
                # print this line if in showing mode
                if showing: 
                    print line,
    except AttributeError as e:
        print "show_module: Could not find module {}".format(module)
    except Exception as e:
        print "show_module: Could not show module {}".format(name)
        import traceback
        traceback.print_exc()
