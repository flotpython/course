# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args

from random import randint

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


def numbers_input():
    length = randint(3,6)
    result = []
    for i in range(length):
        result.append(randint(5, 15))
    return result


numbers_inputs = [Args(numbers_input()) for i in range (3)]

exo_numbers = ExerciseFunction(
    numbers, numbers_inputs,
    layout_args = (30, 25, 25)
)

