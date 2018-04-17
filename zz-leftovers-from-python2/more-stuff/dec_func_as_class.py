# exemple de decorator de fonction implemente comme une classe

# avec les memes notations que func_dec1.py

import time

####################
"""NOTE
je ne sais pas trop si on deja dit ce qu'est un objet callable
. une fonction
. une classe qui a une methode __call__
"""

####################  quatrieme version version : avec un decorateur implemente comme une classe

# on definit a present le decorateur comme une classe

class time_it_as_class (object):
    "the time_it decorator implemented as a class"

    # function to be decorated is passed here
    def __init__ (self, towrap):
        self.towrap = towrap
        # pour preserver __name__ et __doc__
        self.__name__ = towrap.__name__
        self.__doc__ = towrap.__doc__

    def __call__ (self, *args, **kwds):
        begin = time.time()
        # retrieve and call the function to decorate
        retcod = self.towrap (*args, **kwds)
        end = time.time()
        print 'duration {} {}s'.format(self.towrap.__name__,end-begin)
        return retcod

# et on l'utilise comme ceci
@time_it_as_class
def iterate_cube5 (n):
    "stupidly building a cubic list"
    result=[]
    for i in range (n**3):
        result.append(i)

iterate_cube5 (200)

#################### en option, examinons cet objet

def describe_function (function, expected_name):
    print '== type for function {name} is {type}'.format(name=expected_name,type=type(function))
    print 'attached doc is "{doc}"'.format(doc=function.__doc__)
    if function.__name__ == expected_name:
        print '__name__ OK'
    else:
        print 'WARNING : actual name is {actual_name}'.format(actual_name=function.__name__)

describe_function (iterate_cube5, 'iterate_cube5')

