# pylint: disable=c0111
import numpy as np

from nbautoeval import Args, ExerciseFunctionNumpy

# @BEG@ name=dice
def dice(target, nb_dice=2, nb_sides=6):
    """
    Pour un jeu où on lance `nb_dice` dés qui ont chacun `sides` faces,
    quel est le nombre de tirages dont la somme des dés fasse `target`

    Version force brute, il y a bien sûr des outils mathématiques
    pour obtenir une réponse beaucoup plus rapidement

    Toutes les solutions procèdent en deux étapes

    * calcul de l'hypercube qui énumère les tirages,
      et calcule la somme des dés pour chacun de ces tirages
    * trouver le nombre de points dans le cube où la somme des dés
      correspond à ce qu'on cherche

    les deux étapes sont indépendantes, et peuvent donc être mélangées
    entre les solutions
    """

    # pour élaborer le cube, on procède par broadcating
    # on commence avec un simple vecteur de shape (nb_sides,) - e.g. de 1 à 6
    # on lui ajoute lui-même mais avec une forme (nb_sides, 1) - en colonne donc
    # et ainsi de suite avec
    # shape=(nb_sides, 1, 1) pour la dimension 3,
    # shape=(nb_sides, 1, 1, 1) pour la dimension 4
    sides = np.arange(1, nb_sides+1)
    cube = sides
    # une liste plutôt qu'un tuple pour décrire la shape,
    # car on va y ajouter '1' à chaque tour
    shape = [nb_sides]
    # on a déjà un dé
    for _dimension in range(nb_dice - 1):
        shape.append(1)
        cube = cube + sides.reshape(shape)

    # le cube est prêt,
    # pour chercher combien de cases ont la valeur target,
    # on peut faire par exemple
    return np.sum(cube == target)

# @END@

# @BEG@ name=dice more=2
def dice_2(target, nb_dice=2, nb_sides=6):
    """
    une variante de la première forme, qui utilise
    astucieusement une matrice diagonale pour énumérer
    les 'shapes' qui entrent en jeu

    credits: aurelien
    """
    sides = np.arange(1, nb_sides+1)
    shapes = np.diag([nb_sides-1]*nb_dice) + 1
    # attention ici c'est le sum Python
    # et non pas np.sum qui ferait complètement autre chose
    cube = sum(sides.reshape(s) for s in shapes)

    # une autre façon de faire le décompte
    return np.count_nonzero(cube == target)
# @END@

# @BEG@ name=dice more=3
def dice_3(target, nb_dice=2, nb_sides=6):
    """
    même logique globalement, mais en utilisant
    np.newaxis pour changer de dimension
    """
    sides = np.arange(1, nb_sides+1)
    cube = sides
    # on a déjà un dé
    for _dimension in range(nb_dice - 1):
        sides = sides[:, np.newaxis]
        cube = cube + sides

    # une autre façon de faire le décompte
    return np.count_nonzero(cube == target)
# @END@

# @BEG@ name=dice more=4
def dice_4(target, nb_dice=2, nb_sides=6):
    """
    on peut aussi tirer profit de indices()
    qui fait déjà presque le travail
    puisqu'il construit plusieurs cubes de la bonne dimension
    qu'il ne reste plus qu'à additionner
    """
    # il faut quand même faire attention
    # car indices() commence à 0
    all_indices = np.indices(nb_dice * (nb_sides,)) + 1
    cube = sum(all_indices)

    return np.count_nonzero(cube == target)
# @END@

# @BEG@ name=dice more=5
def dice_5(target, nb_dice=2, nb_sides=6):
    """
    une très légère variante
    """
    all_indices = np.indices(nb_dice * (nb_sides,))
    # une façon plus pédante mais plus propre de faire la somme
    # si on n'a pas rectifié avant, il faut maintenant ajouter nb_dice
    cube = np.add.reduce(all_indices) + nb_dice

    return np.count_nonzero(cube == target) # ou return len(res[res == target])
# @END@

# @BEG@ name=dice more=6
# on peut aussi utiliser itertools.product qui permet
# d'itérer sans aucune mémoire sur le même hypercube
#
# de manière un peu paradoxale, cette version en Python pur,
# bien que nécessitant en théorie beaucoup moins de mémoire,
# est beaucoup moins efficace que la version numpy
# je vous renvoie à la discussion sur le forum intitulée
# "Exercice dice"
from itertools import product

def dice_6(target, nb_dice=2, nb_sides=6):
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


def dice_ko(target, nb_dice=2, nb_sides=6):
    return nb_sides ** (nb_dice-1)

SIDES = 5

dice_inputs = [
    Args(7),
    Args(2),
    Args(20, nb_sides=10),
    Args(3, nb_dice=3),
    Args(4, nb_dice=3),
    Args(50, nb_dice=8),
    Args(28, nb_dice=8),
] + [
    Args(target, nb_sides=SIDES, nb_dice=3) for target in range(3, 3*SIDES+1)
]


exo_dice = ExerciseFunctionNumpy(
    dice,
    dice_inputs,
    nb_examples=5,
)
