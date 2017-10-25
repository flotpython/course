# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


# @BEG@ name=aplatir
def aplatir(conteneurs):
    "retourne une liste des éléments des éléments de conteneurs"
    # on peut concaténer les éléments de deuxième niveau 
    # par une simple imbrication de deux compréhensions de liste
    return [element for conteneur in conteneurs for element in conteneur]
# @END@


def aplatir_ko(conteneurs):
    return conteneurs


aplatir_inputs = [
    Args([]),
    Args([(1,)]), 
    Args(([1],)), 
    Args([(0, 6, 2), [1, ('a', 4), 5]]),
    Args(([ 1, [2, 3]], ('a', 'b', 'c'))),
    Args(([ 1, 6 ], ('c', 'b'), [2, 3])),
    Args((( 1, [2, 3]), [], ('a'), ['b', 'c'])),
]


exo_aplatir = ExerciseFunction(
    aplatir, aplatir_inputs, nb_examples=0)

