# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args

####################
# @BEG@ name=divisible
def divisible(a, b):
    "renvoie True si un des deux arguments divise l'autre"
    # b divise a si et seulement si le reste
    # de la division de a par b est nul
    # et il faut regarder aussi si a divise b
    return a % b == 0 or b % a == 0
# @END@

# @BEG@ name=divisible more=v2
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


####################
# @BEG@ name=morceaux
def morceaux(x):
    if x <= -5:
        return -x - 5
    elif x <= 5:
        return 0
    else:
        return x / 5 - 1
# @END@

# @BEG@ name=morceaux more=v2
def morceaux_bis(x):
    if x <= -5:
        return -x - 5
    if x <= 5:
        return 0
    return x / 5 - 1
# @END@

# @BEG@ name=morceaux more=v3
# on peut aussi faire des tests d'intervalle
# comme ceci  0 <= x <= 10
def morceaux_ter(x):
    if x <= -5:
        return -x - 5
    elif -5 <= x <= 5:
        return 0
    else:
        return x / 5 - 1
# @END@

inputs_morceaux = [
    Args(x) for x in (-10, 0, 10, -6, -5, -4, 4, 5, 6)
]

exo_morceaux = ExerciseFunction(
    morceaux, inputs_morceaux,
    nb_examples = 3,
)

