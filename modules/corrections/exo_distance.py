# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


# @BEG@ name=distance
import math

def distance(*args):
    "la racine de la somme des carrés des arguments"
    # avec une compréhension on calcule la liste des carrés des arguments
    # on applique ensuite sum pour en faire la somme
    # vous pourrez d'ailleurs vérifier que sum ([]) = 0
    # enfin on extrait la racine avec math.sqrt
    return math.sqrt(sum([x**2 for x in args]))
# @END@


# @BEG@ name=distance more=bis
def distance_bis(*args):
    "idem mais avec une expression génératrice"
    # on n'a pas encore vu cette forme - cf Semaine 6
    # mais pour vous donner un avant-goût d'une expression
    # génératrice on peut faire aussi ceci
    # observez l'absence de crochets []
    # la différence c'est juste qu'on ne
    # construit pas la liste des carrés,
    # car on n'en a pas besoin
    # et donc un itérateur nous suffit
    return math.sqrt(sum(x**2 for x in args))
# @END@


distance_inputs = [
    Args(),
    Args(1),
    Args(1, 1),
    Args(1, 1, 1),
    Args(1, 1, 1, 1),
    Args(*range(10)),
]


exo_distance = ExerciseFunction(
    distance, distance_inputs, nb_examples=3)


def distance_ko(*args):
    return sum([x**2 for x in args])

