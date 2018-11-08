# pylint: disable=c0111
import numpy as np

from nbautoeval.exercise_function import ExerciseFunctionNumpy
from nbautoeval.args import Args


# @BEG@ name=checkers
def checkers(taille, upper_left=True):
    """
    Un damier
    le coin (0, 0) vaut 1 ou 0 selon upper_left
    se souvenir que False == 0 et True == 1
    """
    # disons que 0=blanc et noir=1
    # on crée un tableau d'entiers
    # par défaut tout est blanc
    result = np.zeros(shape=(taille, taille), dtype=int)
    # on remplit les cases blanches en deux fois
    # avec un slicing astucieux; c'est le ::2 qui fait le travail
    result[1::2, 0::2] = 1
    result[0::2, 1::2] = 1
    # on renverse si upper_left est False
    if upper_left:
        result = 1 - result
    return result
# @END@


# faux parce qu'on ignore upper_left
# voir aussi si la correction est contente avec des float
def checkers_ko(taille, ignored=True):
    result = np.ones(shape=(taille, taille), dtype=float)
    # on remplit les cases blanches en deux fois
    result[1::2, 0::2] = 0
    result[0::2, 1::2] = 0
    return result


checkers_inputs = [
    Args(3),
    Args(3, False),
    Args(1),
    Args(2),
    Args(4),
]


exo_checkers = ExerciseFunctionNumpy(
    checkers,
    checkers_inputs,
    nb_examples=2,
    )
