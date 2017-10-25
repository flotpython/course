# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


# @BEG@ name=divisible
def divisible(a, b):
    "renvoie True si un des deux arguments divise l'autre"
    # b divise a si et seulement si le reste
    # de la division de a par b est nul
    # et il faut regarder aussi si a divise b
    return a % b == 0 or b % a == 0
# @END@


# @BEG@ name=divisible more=bis
def divisible_bis(a, b):
    if a % b == 0:
        return True
    if b % a == 0:
        return True
    return False
# @END@

def divisible_ko(a, b):
    return a % b == 0


inputs_divisible = [
    Args(10, 30),
    Args(10, -30),
    Args(-10, 30),
    Args(-10, -30),
    Args(8, 12),
    Args(12, -8),
    Args(-12, 8),
    Args(-12, -8),
    Args(10, 1),
    Args(30, 10),
    Args(30, -10),
    Args(-30, 10),
    Args(-30, -10),
]

exo_divisible = ExerciseFunction(
    divisible, inputs_divisible
)


