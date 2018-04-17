# -*- coding: utf-8 -*-
# exemple de decorator de fonction implemente comme une fonction

# on se donne une fonction volontairement stupide
# et on veut tracer le temps utilise pour le calcul

import time

#################### premiere version 'a la main' 
def iterate_cube (n):
    "stupidly building a cubic list"
    result=[]
    for i in range (n**3):
        result.append(i)

begin = time.time()
iterate_cube (200)
end = time.time()
print 'duration (manual) {}s'.format(end-begin)

print

#################### seconde version : avec un decorateur

# on definit le decorateur comme ceci

def time_it_as_func_1 (towrap):
    "the time_it decorator implemented as a function"
    def wrapper (*args, **kwds):
        begin = time.time()
        retcod = towrap (*args, **kwds)
        end = time.time()
        print 'duration (auto1) {}s'.format(end-begin)
        return retcod
    return wrapper


# et on l'utilise comme ceci, avec une fonction volontairement stupide
@time_it_as_func_1
def iterate_cube2 (n):
    "stupidly building a cubic list"
    result=[]
    for i in range (n**3):
        result.append(i)

iterate_cube2 (200)

print

#################### en option, examinons les caracteristiques de ces objets

def describe_function (function, expected_name):
    print '== type for function {name} is {type}'.format(name=expected_name,type=type(function))
    print 'attached doc is "{doc}"'.format(doc=function.__doc__)
    if function.__name__ == expected_name:
        print '__name__ OK'
    else:
        print 'WARNING : actual name is {actual_name}'.format(actual_name=function.__name__)

describe_function (iterate_cube, 'iterate_cube')
describe_function (iterate_cube2, 'iterate_cube2')

print

#################### troisieme version : amelioration du decorateur

# on voit qu'avec cette technique on a oublié de mettre à jour
# __name__ et __doc__ sur la fonction decoree

# il existe un utilitaire pour faire cela...
# on en profite pour ameliorer un peu le rendu en affichant le nom de la fonction
# la version amelioree du decorateur est donc

import functools

def time_it_as_func_2 (towrap):
    "the time_it decorator implemented as a function"
    @functools.wraps(towrap)
    def wrapper (*args, **kwds):
        begin = time.time()
        retcod = towrap (*args, **kwds)
        end = time.time()
        print 'duration for {} is {}s'.format(towrap.__name__,end-begin)
        return retcod
    return wrapper

@time_it_as_func_2
def iterate_cube3  (n):
    "stupidly building a cubic list"
    result=[]
    for i in range (n**3):
        result.append(i)

iterate_cube3 (200)

print

describe_function (iterate_cube3, 'iterate_cube3')

print

#################### quatrieme version : on invoque le decorator a la main
# la troisieme version est exactement equivalente a celle-ci
# ou l'on voit mieux comment le decorateur intervient

def iterate_cube4 (n):
    "stupidly building a cubic list"
    result=[]
    for i in range (n**3):
        result.append(i)

iterate_cube4 = time_it_as_func_2 ( iterate_cube4 )

iterate_cube4 (200)

