# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunctionNumpy
from nbautoeval.args import Args


# @BEG@ name=xxt
import numpy as np

def xxt(column):
    """
    column est un tableau numpy en forme de colonne
    i.e. de shape (n, 1)
    
    cette fonction retourne une matrice carrée de taille
    n x n, et obtenue en multipliant le vecteur x avec son transposé
    """
    
    # on obtient la transposée avec l'attribut T
    # et pour la multiplication de matrices
    # multiplier on utilise l'opérateur @
    return column @ column.T
# @END@


# @BEG@ name=xxt more=bis
def xxt_bis(column):
    """
    pareil mais en utilisant .dot()
    """
    return column.dot(column.T)
# @END@

# @BEG@ name=xxt more=ter
def xxt_ter(column):
    """
    pareil mais en utilisant .. le broadcasting
    car dans ce cas précis si on multiplie un
    vecteur (n, 1) avec un vecteur (1, n)
    on fait du broadcasting et il se trouve
    que c'est équivalent au produit matriciel
    dans ce cas-là
    """
    return column * column.T
# @END@

# @BEG@ name=xxt more=quater
def xxt_quater(column):
    """
    et du coup quand on utilise le broadcasting
    on peut même faire la multiplication
    dans le sens qu'on veut !
    """
    return column.T * column
# @END@

def xxt_ko(array):
    # presque ça mais sans le reshape
    return array.T @ array

inputs_xxt = [
    Args(np.array([1])),
    Args(np.array([1, 2]).reshape(2, 1)),
    Args(np.array([1, 2, 3]).reshape(3, 1)),
]

exo_xxt = ExerciseFunctionNumpy(
    xxt, inputs_xxt,
    nb_examples = 0,
)

def xxt_nargs(*args):
    n = len(args)
    return xxt(np.array(args).reshape(n, 1))

def xxt_reshape(array):
    n = array.size
    return xxt(array.reshape(n ,1))