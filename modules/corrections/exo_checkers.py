# pylint: disable=c0111
import numpy as np

from nbautoeval import Args, ExerciseFunctionNumpy


# @BEG@ name=checkers
def checkers(size, corner_0_0=True):
    """
    Un damier
    le coin (0, 0) vaut 1 ou 0 selon corner_0_0
    se souvenir que False == 0 et True == 1

    credits: JeF29 pour avoir suggéré une simple
    addition plutôt qu'un xor
    """
    # on peut voir le damier comme une fonction sur
    # les coordonnées, du genre (i + j) % 2
    # pour choisir le coin, on ajoute avant de faire le % 2
    I, J = np.indices((size, size))
    return (I + J + corner_0_0) % 2
# @END@


# @BEG@ name=checkers more=2
def checkers_2(size, corner_0_0=True):
    """
    sur une ligne, avec
    * sum() pour l'addition I + J

    et, pour les illustrer un petit, les opérateurs bit-wise:
    * et logique (&) pour le modulo 2
    * et xor (^) pour inverser

    credits: j4l4y
    """
    # avec sum() sur indices()
    # on peut tout faire en une ligne:
    return sum(np.indices((size, size))) & 1 ^ corner_0_0
# @END@

# @BEG@ name=checkers more=3
def checkers_3(size, corner_0_0=True):
    """
    Une autre approche complètement
    """
    # on part de zéro
    result = np.zeros(shape=(size, size), dtype=int)
    # on remplit les cases à 1 en deux fois
    # avec un slicing astucieux; c'est le ::2 qui fait le travail
    result[1::2, 0::2] = 1
    result[0::2, 1::2] = 1
    # encore une autre façon de renverser,
    # plutôt que le xor, puisque False == 0 et True == 1
    if corner_0_0:
        result = 1 - result
    return result
# @END@

# @BEG@ name=checkers more=4
def checkers_4(size, corner_0_0=True):
    """
    Et encore une autre, sans doute pas très lisible
    mais très astucieuse

    credits: j4l4y
    """
    # une utilisation très astucieuse de resize,
    # broadcasting, décalage, bravo !
    return (np.resize((corner_0_0, 1-corner_0_0),
                      (1, size))
            ^ np.arange(size)[:, np.newaxis] & 1)
# @END@

# une solution qui NE MARCHE PAS pour les tailles paires
def checkers_ko_2(size, corner_0_0=True):
    return np.array([(i+corner_0_0) % 2 for i in range(size * size)],
                    dtype=np.int_).reshape(size, size)


# faux parce qu'on ignore corner_0_0
# voir aussi si la correction est contente avec des float
def checkers_ko(size, ignored=True):
    result = np.ones(shape=(size, size), dtype=float)
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
