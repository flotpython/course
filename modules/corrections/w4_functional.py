# -*- coding: iso-8859-15 -*-
from corrections.tools import correction_table, correction_table_1arg, exemple_table, exemple_table_1arg

from operator import mul

####################
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

def input ():
    length = randint (3,6)
    result = []
    for i in xrange(length):
        result.append(randint(5,15))
    return result

numbers_inputs = [ input() for i in xrange (3) ]

def correction_numbers (student_numbers):
    return correction_table_1arg (student_numbers, numbers, numbers_inputs)

##########
def validation (f, g, entrees):
    """
retourne une liste de booleens, un par entree dans entrees
qui indique si f(entree) == g(entree)
    """
    return [ f(entree) == g(entree) for entree in entrees ]

def correction_validation (student_validation):
    return correction_table (student_validation, validation, validation_inputs,
                             columns=(50,40,40))

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

