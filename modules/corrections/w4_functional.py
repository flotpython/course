# -*- coding: iso-8859-15 -*-
from exercice import Exercice, Exercice_1arg

##############################
from operator import mul

def numbers (liste):
    """
retourne un tuple contenant
 la somme
 le produit
 le minimum
 le maximum
des elements de la liste
    """
    return ( sum(liste),
             reduce(mul,liste,1),
             min(liste),
             max(liste))

from random import randint

def numbers_input ():
    length = randint (3,6)
    result = []
    for i in xrange(length):
        result.append(randint(5,15))
    return result
numbers_inputs = [ numbers_input() for i in xrange (3) ]

exo_numbers = Exercice_1arg (numbers, numbers_inputs)

##############################
def validation (f, g, entrees):
    """
retourne une liste de booleens, un par entree dans entrees
qui indique si f(entree) == g(entree)
    """
    return [ f(entree) == g(entree) for entree in entrees ]

validation_inputs = []

# factoriel
from operator import mul
def fact (n):
    "une version de factoriel à base de reduce"
    return reduce (mul, range(1,n+1), 1)
from math import factorial
fact_inputs = [0, 1, 5]

validation_inputs.append ( (fact, factorial, fact_inputs) )

def broken_fact (n):
    return 0 if n <= 0 \
        else 1 if n == 1 \
             else n*fact(n-1)

validation_inputs.append ( (broken_fact, factorial, fact_inputs) )

exo_validation = Exercice (validation, validation_inputs, 
                           correction_columns = (50,40,40))

##############################
