# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


inputs_dispatch1 = [Args(a, b) for a in range (3, 6) for b in range (7, 10)]


# @BEG@ name=dispatch1
def dispatch1(a, b):
    """dispatch1 comme spécifié"""
    # si les deux arguments sont pairs
    if a%2 == 0 and b%2 == 0:
        return a*a + b*b
    # si a est pair et b est impair
    elif a%2 == 0 and b%2 != 0:
        return a*(b-1)
    # si a est impair et b est pair
    elif a%2 != 0 and b%2 == 0:
        return (a-1)*b
    # sinon - c'est que a et b sont impairs
    else:
        return a*a - b*b
# @END@


def dispatch1_ko(a, b, *args):
    return a*a + b*b


exo_dispatch1 = ExerciseFunction(
    dispatch1, inputs_dispatch1)



####################
samples_A = [(2, 4, 6), [2, 4, 6]]
samples_B = [{6, 8, 10}]

inputs_dispatch2 = [
    Args(a, b, A, B)
      for a, A in zip(range(3, 5), samples_A)
         for b in range(7, 10) for B in samples_B
]


# @BEG@ name=dispatch2
def dispatch2(a, b, A, B):
    """dispatch2 comme spécifié"""
    # les deux cas de la diagonale \ 
    if (a in A and b in B) or (a not in A and b not in B):
        return a*a + b*b
    # sinon si b n'est pas dans B
    # ce qui alors implique que a est dans A
    elif b not in B: 
        return a*(b-1)
    # le dernier cas, on sait forcément que
    # b est dans B et a n'est pas dans A
    else:
        return (a-1)*b
# @END@


dispatch2_ko = dispatch1_ko


exo_dispatch2 = ExerciseFunction(
    dispatch2, inputs_dispatch2,
    layout_args=(50, 30, 30))

