# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


from .exo_aplatir import aplatir

# @BEG@ name=alternat
def alternat(l1, l2):
    """
    renvoie une liste des éléments
    pris alternativement dans l1 et dans l2
    """
    # pour réaliser l'alternance on peut combiner zip avec aplatir
    # telle qu'on vient de la réaliser
    return aplatir(zip(l1, l2))
# @END@


# @BEG@ name=alternat more=bis
def alternat_bis(l1, l2):
    """
    une deuxième version de alternat
    """
    # la même idée mais directement, sans utiliser aplatir
    return [element for conteneur in zip(l1, l2) for element in conteneur]
# @END@


alternat_inputs = [
    Args((1, 2), ('a', 'b') ),
    Args((1, 2, 3), ('a', 'b', 'c')),
    Args((1, (2, 3)), ('a', ['b', 'c'])),
]


exo_alternat = ExerciseFunction(
    alternat, alternat_inputs, nb_examples=2)


def alternat_ko(l1, l2):
    return l1 + l2
