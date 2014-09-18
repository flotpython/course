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
        state = True if not beg else False
        with open(module.__file__) as input:
            for line in input.readlines():
                if beg and line.find(beg)>=0: state = True
                if state and end and line.find(end)>=0: return
                if state: print line,
    except AttributeError as e:
        print "show_module: Could not find module {}".format(module)
    except Exception as e:
        print "show_module: Could not find module {}".format(name)
        import traceback
        traceback.print_exc()

