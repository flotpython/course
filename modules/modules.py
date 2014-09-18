import sys

def show_module (module):
    """
    display the source code for a module
    and more stuff
    """
    # check this is a module
    if type(module) is not type(sys):
        print "show_module: Unexpected input {}".format(module)
        return
    try:
        name = module.__name__
        file = module.__file__
        with open(module.__file__) as input:
            for line in input.readlines():
                print line,
    except AttributeError as e:
        print "show_module: Could not find module {}".format(module)
    except Exception as e:
        print "show_module: Could not find module {}".format(name)

