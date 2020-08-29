from nbautoeval import Args, ExerciseFunctionNumpy


# @BEG@ name=xixj
import numpy as np

def xixj(*args):
    """
    si les arguments sont x1, x2, .. xn
    retourne une matrice carrée n x n
    dont les éléments valent
    m[i, j] = xi * xj

    dans cette première solution on va faire
    le produit de matrices entre un vecteur colonne
    et sa transposée
    """
    # par la déclaration '*args'
    # args désigne un tuple contenant x1, x2, ... xn
    #
    # on veut construire un vecteur colonne
    # donc de forme (n, 1) à partir des arguments
    #
    # pour bien décomposer on commence
    # par faire un vecteur ligne à partir de args
    line = np.array(args)
    # transformons en colonne
    n = len(args)
    column = line.reshape((n, 1))
    # on obtient la transposée avec l'attribut T
    # et pour la multiplication de matrices
    # multiplier on utilise l'opérateur @
    return column @ column.T
# @END@


# @BEG@ name=xixj more=bis
def xixj_bis(*args):
    """
    pareil mais en utilisant .dot()
    """
    # on calcule un vecteur colonne comme ci-dessus
    n = len(args)
    column = np.array(args).reshape((n, 1))
    # dans cette version on fait le produit de matrice
    # en utilisant la méthode dot sur les tableaux
    return column.dot(column.T)
    # remarquez qu'on aurait pu faire aussi bien
    # return np.dot(column, column.T)
# @END@

# @BEG@ name=xixj more=ter
def xixj_ter(*args):
    """
    pareil mais en utilisant .. le broadcasting
    car dans ce cas précis si on multiplie
    (au sens de la multiplication classique '*')
    un vecteur colonne (n, 1)
    avec un vecteur ligne (1, n)
    on fait du broadcasting et il se trouve
    que c'est équivalent au produit matriciel
    dans ce cas-là
    """
    n = len(args)
    column = np.array(args).reshape((n, 1))
    return column.T * column
    # le broadcasting c'est magique parfois
    # car avec cette méthode on peut multiplier
    # dans n'importe quel ordre !
    # ce qui fait que ceci marche ausi !
    # return column * column.T
# @END@

def xixj_ko(*args):
    # presque ça mais sans le reshape
    array = np.array(args)
    return array.T @ array

inputs_xixj = [
    Args(1),
    Args(1, 2),
    Args(1, 2, 4),
    Args(1, 0, 4),
    Args(8, 4, 2),
    Args(0, 1, 2, 4, 8),
]

exo_xixj = ExerciseFunctionNumpy(
    xixj, inputs_xixj,
    nb_examples = 3,
)
