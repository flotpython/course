# pylint: disable=c0111

import numpy as np



from nbautoeval.exercise_function import ExerciseFunctionNumpy
from nbautoeval.args import Args


# @BEG@ name=stairs
def stairs(taille):
    """
    la pyramide en escaliers telle que décrite dans l'énoncé
    """
    # on calcule n
    n = 2 * taille + 1
    # on calcule les deux tableaux d'indices
    # tous les deux de dimension n
    ix, iy = np.indices((n, n))
    # il n'y a plus qu'à appliquer la formule qui va bien
    return 2 * taille - (np.abs(ix - taille) + np.abs(iy - taille))
# @END@


# @BEG@ name=stairs more=bis
def stairs_bis(taille):
    """
    Bien sûr on peut préciser le type mais ce n'est pas
    réellement nécessaire ici
    """
    n = 2 * taille + 1
    ix, iy = np.indices((n, n), dtype=np.int8)
    return 2 * taille - (np.abs(ix - taille) + np.abs(iy - taille))
# @END@

# @BEG@ name=stairs more=ter
def stairs_ter(taille):
    """
    Version proposée par j4l4y
    Dans la rubrique 'oneliner challenge'
    """
    # la forme np.abs(np.range(-n, n+1)) correspond à la forme
    # en V, par exemple pour n=3 : -3, -2, -1, 0, 1, 2, 3
    # dans cette version, on l'agrandit artificiellement en 2D
    # pour pouvoir prendre sa transposée
    return (lambda x: x + x.T)(
        taille - np.abs(range(-taille, taille+1))[:, np.newaxis]
    )
# @END@

# @BEG@ name=stairs more=quater
def stairs_quater(taille):
    """
    Une variante pour se débarrasser de la transposition
    """
    # Je vous laisse vous convaincre que ça fonctionne aussi
    # en utilisant le broadcasting
    # pour s'économiser une transposition explicite
    return (lambda x: x + x[:, np.newaxis])(
        taille - np.abs(range(-taille, taille+1))
    )
# @END@


def stairs_ko(taille):
    n = 2 * taille + 1
    ix, iy = np.indices((n, n), dtype=np.float)
    return ((taille - 1) + 2 * taille
            - (np.abs(ix - taille) + np.abs(iy - taille)))


stairs_inputs = [
    Args(1),
    Args(2),
    Args(3),
    Args(4),
]


exo_stairs = ExerciseFunctionNumpy(
    stairs,
    stairs_inputs,
    nb_examples=2,
    )
