# pylint: disable=c0111

import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import Output

from nbautoeval import Args, ExerciseFunctionNumpy, Renderer


# @BEG@ name=stairs
def stairs(taille):
    """
    la pyramide en escaliers telle que décrite dans l'énoncé
    """
    # on calcule n
    total = 2 * taille + 1
    # on calcule les deux tableaux d'indices
    # tous les deux de dimension total
    I, J = np.indices((total, total))
    # on décale et déforme avec valeur absolue, pour obtenir
    # deux formes déjà plus propices
    I2, J2 = np.abs(I-taille), np.abs(J-taille)
    # si ajoute on obtient un négatif,
    # avec 0 au centre et taille aux 4 coins
    negatif = I2 + J2
    # ne retse plus qu'à renverser
    return 2 * taille - negatif
# @END@


# @BEG@ name=stairs more=2
def stairs_2(taille):
    """
    même idée, modalités légèrement différentes
    Aussi on peut inverser plus tôt
    """
    total = 2 * taille + 1
    # on peut préciser le type, mais ce n'est pas
    # réellement nécessaire ici
    I, J = np.indices((total, total), dtype=np.int8)
    # on peut inverser avant d'ajouter si c'est plus naturel
    return  (taille - np.abs(I-taille)) + (taille - np.abs(J-taille))
# @END@


# @BEG@ name=stairs more=3
def stairs_3(taille):
    """
    en fait on n'a pas vraiment besoin d'indices
    """
    # la première ligne
    line = taille - np.abs(np.arange(-taille, taille+1))
    # la première colonne est la transposée
    # comme je n'aime pas utiliser .T
    # je préfère un reshape
    # et il n'y a qu'à ajouter
    return line + line.reshape((2*taille+1, 1))
# @END@

# @BEG@ name=stairs more=4
def stairs_4(taille):
    """
    une approche par mosaique
    on construit un quart, et on le duplique avec
    * np.hstack (une fonction d'empilement)
    * np.flip (une fonction de miroir)

    credits: JeF29
    """
    a = np.arange(taille)
    b = np.hstack((a, taille, np.flip(a)))
    return b + b.reshape(-1, 1) # ou b + b[:, np.newaxis]
# @END@



# @BEG@ name=stairs more=ter
def stairs_ter(taille):
    """
    Version proposée par j4l4y
    Dans la rubrique 'oneliner challenge'

    credits: j4l4y
    """
    # la forme np.abs(np.range(-n, n+1)) correspond à la forme
    # en V, par exemple pour n=3 : -3, -2, -1, 0, 1, 2, 3
    # dans cette version, on l'agrandit artificiellement en 2D
    # pour pouvoir prendre sa transposée
    return (lambda x: x + x.T)(
        taille - np.abs(range(-taille, taille+1))[:, np.newaxis]
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
