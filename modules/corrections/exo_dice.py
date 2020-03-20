# pylint: disable=c0111
import numpy as np

from nbautoeval import Args, ExerciseFunctionNumpy

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
    for _dimension in range(nb_dice-1):
        # une dimension de plus
        line = line[:, np.newaxis]
        # on ajoute
        combinations = combinations + line
    # ce qui nous intéresse mainteant c'est le nombre
    # de cases dans le cube qui valent 'target'
    # on peut penser à np.count_nonzero, mais en
    # géneral on a tendance à trouver `sum` dans du code
    # de ce genre
    return np.sum(combinations == target)
# @END@


# @BEG@ name=dice more=bis
# on peut aussi utiliser itertools.product qui permet
# d'itérer sans aucune mémoire sur le même hypercube
#
# de manière un peu paradoxale, ces versions en python pur,
# bien que nécessitant en théorie beaucoup moins de mémoire,
# sont beaucoup moins efficaces que la version numpy
# je vous renvoie à la discussion sur le forum intitulée
# "Exercice dice"
from itertools import product

def dice_bis(target, nb_dice=2, sides=6):
    """
    Une autre méthode complètement, qui n'alloue aucun tableau
    du coup on n'a pas besoin de numpy
    """
    # en version facile, on peut utiliser le paramètre `repeat`
    # de product qui fait exactement ce qu'on veut, puisque
    # tous les dés ont le même nombre de faces
    #
    # par exemple le cas standard (2 dés, 6 faces) se ferait avec
    # quelque chose comme
    # (for (i, j) in itertools.product(range(1, 7), repeat=2))
    #
    # le premier sum compte les occurences de True dans l'itération
    return sum(
        # ici sum(x) fait la somme des tirages des dés
        sum(x) == target
        for x in product(range(1, sides+1), repeat=nb_dice))
# @END@


# @BEG@ name=dice more=ter
from itertools import product

def dice_ter(target, nb_dice=2, sides=6):
    """
    La même chose, mais on voit une méthode qui n'utilise pas
    `repeat=` dans itertools.product
    Ça pourrait être utile si par exemple les dés n'avaient
    pas tous la même taille
    """
    # on construit les <nb_dice> instances de range() qui serviront
    # de base à product
    iterators = (range(1, sides+1) for dimension in range(nb_dice))
    return sum(sum(x) == target for x in product(*iterators))
# @END@


# @BEG@ name=dice more=quat
def dice_quat(target, nb_dice=2, sides=6):
    """
    Cette version semble un peu plus rapide 
    que les deux  précédentes avec product,
    mais toujours beaucoup plus lente que la version numpy
    """
    iterators = (range(1, sides+1) for dimension in range(nb_dice))
    count = 0
    for sample in product(*iterators):
        if sum(sample) == target:
            count += 1
    return count
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
#    layout_args=(50, 10, 10),
    )
