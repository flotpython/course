# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args

##############################
# @BEG@ name=numbers
from functools import reduce

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
        max(liste),
    )
# @END@

def numbers_ko(liste):
    return ( 
        # la builtin 'sum' renvoie la somme
        sum(liste),
        # pour la multiplication, reduce est nécessaire
        2 * reduce(mul, liste, 1),
        # les builtin 'min' et 'max' font ce qu'on veut aussi
        max(liste),
        min(liste),
    )


from random import randint

def numbers_input():
    length = randint(3,6)
    result = []
    for i in range(length):
        result.append(randint(5, 15))
    return result
numbers_inputs = [Args(numbers_input()) for i in range (3)]

exo_numbers = ExerciseFunction(
    numbers, numbers_inputs,
    layout_args = (30, 25, 25) )

##############################
# @BEG@ name=compare
def compare(f, g, entrees):
    """
    retourne une liste de booléens, un par entree dans entrees
    qui indique si f(entree) == g(entree)
    """
    # on vérifie pour chaque entrée si f et g retournent
    # des résultats égaux avec ==
    # et on assemble le tout avec une comprehension de liste 
    return [f(entree) == g(entree) for entree in entrees]
# @END@

def compare_ko(*args):
    return [not x for x in compare(*args)]

compare_inputs = []

# factoriel
from operator import mul
def fact(n):
    "une version de factoriel à base de reduce"
    return reduce(mul, range(1, n+1), 1)
from math import factorial
fact_inputs = [0, 1, 5]

compare_inputs.append(Args(fact, factorial, fact_inputs))

def broken_fact(n):
    return 0 if n <= 0 \
        else 1 if n == 1 \
             else n*fact(n-1)

compare_inputs.append(Args(broken_fact, factorial, fact_inputs))

#################### the exercice instance
exo_compare = ExerciseFunction(
    compare, compare_inputs,
    nb_examples = 2,
    call_layout='truncate',
    layout_args=(50, 8, 8))

##############################
