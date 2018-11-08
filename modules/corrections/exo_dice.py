# pylint: disable=c0111
import numpy as np

from nbautoeval.exercise_function import ExerciseFunctionNumpy
from nbautoeval.args import Args

# @BEG@ name=dice
def dice(target, nb_dice=2, sides=6):
    """
    Pour un jeu où on lance `nb_dice` dés qui ont chacun `sides` faces,
    quelle est le nombre de tirages dont somme des dés fasse `target`

    Version force brute, il y a bien sûr des outils mathématiques
    pour obtenir une réponse beaucoup plus rapidement
    """

    # première dimension
    line = np.arange(1, sides+1)
    combinations = line
    # construire l'hyper-cube avec une dimension de plus
    # on fait ça (nb-dice-1) fois car là on a déjà la dimension 1
    for dimension in range(nb_dice-1):
        # une dimension de plus
        line = line[:, np.newaxis]
        # on ajoute
        combinations = combinations + line
    # ce qui nous intéresse mainteant c'est le nombre
    # de cases dans le cube qui valent 'target'
    return np.count_nonzero(combinations == target)
# @END@


# @BEG@ name=dice more=bis
# la clé c'est d'utiliser itertools.product
# qui nous permet d'itérer sans aucune mémoire
# sur le même hypercube
from itertools import product

def dice_bis(target, nb_dice=2, sides=6):
    """
    Une autre méthode complètement, qui fonctionne sans numpy
    """
    # par exemple le cas standard se ferait avec
    # for (i, j) in itertools.product(range(1, 7), range(1, 7)):
    #    blabla
    matches = 0
    # on construit les <nb_dice> instances de range() qui serviront
    # de base à itertools
    iterators = (range(1, sides+1) for dimension in range(nb_dice))
    for sample in product(*iterators):
        # sample ici est un tuple
        if sum(sample) == target:
            matches += 1
    return matches
# @END@


def dice_ko(target, nb_dice=2, sides=6):
    return sides ** (nb_dice-1)

SIDES = 5

dice_inputs = [
    Args(7),
    Args(2),
    Args(20, sides=10),
    Args(3, nb_dice=3),
    Args(4, nb_dice=3),
    Args(50, nb_dice=8),
] + [
    Args(target, sides=SIDES, nb_dice=3) for target in range(3, 3*SIDES+1)
]


exo_dice = ExerciseFunctionNumpy(
    dice,
    dice_inputs,
    nb_examples=5,
    layout_args=(50, 10, 10),
    )
