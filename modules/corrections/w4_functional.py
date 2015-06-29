# -*- coding: utf-8 -*-
from exercice_function import ExerciceFunction
from args import Args

##############################
# @BEG@ 4 3 numbers
from operator import mul

def numbers(liste):
    """
    retourne un tuple contenant
    (*) la somme
    (*) le produit
    (*) le minimum
    (*) le maximum
    des éléments de la liste
    """
    
    return ( 
        # la builtin 'sum' renvoie la somme
        sum(liste),
        # pour la multiplication, reduce est nécessaire
        reduce(mul, liste, 1),
        # les builtin 'min' et 'max' font ce qu'on veut aussi
        min(liste),
        max(liste)
    )
# @END@

from random import randint

def numbers_input():
    length = randint(3,6)
    result = []
    for i in xrange(length):
        result.append(randint(5, 15))
    return result
numbers_inputs = [Args(numbers_input()) for i in xrange (3)]

exo_numbers = ExerciceFunction(numbers, numbers_inputs)

##############################
# @BEG@ 4 3 validation
def validation(f, g, entrees):
    """
    retourne une liste de booléens, un par entree dans entrees
    qui indique si f(entree) == g(entree)
    """
    # on vérifie pour chaque entrée si f et g retournent
    # des résultats égaux avec ==
    # et on assemble le tout avec une comprehension de liste 
    return [f(entree) == g(entree) for entree in entrees]
# @END@

validation_inputs = []

# factoriel
from operator import mul
def fact(n):
    "une version de factoriel à base de reduce"
    return reduce(mul, range(1, n+1), 1)
from math import factorial
fact_inputs = [0, 1, 5]

validation_inputs.append(Args(fact, factorial, fact_inputs))

def broken_fact(n):
    return 0 if n <= 0 \
        else 1 if n == 1 \
             else n*fact(n-1)

validation_inputs.append(Args(broken_fact, factorial, fact_inputs))

exo_validation = ExerciceFunction(
    validation, validation_inputs, 
    correction_columns=(50, 40, 40))

##############################
