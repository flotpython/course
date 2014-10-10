# -*- coding: iso-8859-15 -*-
from corrections.exercice import correction_table, correction_table_1arg, exemple_table, exemple_table_1arg

def multi_tri (listes):
    "trie toutes les sous-listes"
    for liste in listes:
        liste.sort()
    return listes

multi_tri_input_args = [
    [ [ 40, 12, 25], [ 'spam', 'egg', 'bacon' ], ], 
    [ [ 32, 45], [ 200, 12 ], [-25, 37] ], 
    [ [ ], range(10) ],
]

def correction_multi_tri (multi_tri_student):
    return correction_table_1arg (multi_tri_student, multi_tri, multi_tri_input_args,
                                  columns = (40,40,40))


def exemple_multi_tri ():
    return exemple_table_1arg ('multi_tri',multi_tri, multi_tri_input_args, columns = (60,60))

####################
def multi_tri_reverse (listes, reverses):
    """trie toutes les sous listes, dans une direction
    precisée par le second argument"""
    for liste, reverse in zip(listes, reverses):
        liste.sort(reverse=reverse)
    return listes

multi_tri_reverse_inputs = [ 
    ( [ [1,2], [3,4] ], [ True, False] ),
    ( [ [1,2], [3,4] ], ( True, True ) ),
    ( [ [1,3,2], [3,4] ], [ False, True] ),
    ( [ [1,2], [3,5,4] ], [ False, False] ),
    ( [ [ 1,3], [ 9,5 ], [4,2] ], (True, False, True) ),
    ( [ [ ], ['a', 'z', 'c' ] ], [False, True ], ),
]

def correction_multi_tri_reverse (multi_tri_reverse_student):
    return correction_table (multi_tri_reverse_student, multi_tri_reverse, multi_tri_reverse_inputs,
                                columns = (50,40,40))

def exemple_multi_tri_reverse ():
    return exemple_table ('multi_tri_reverse',multi_tri_reverse, multi_tri_reverse_inputs, columns = (60,60), how_many=2)

####################
from math import e, pi
def liste_racines (p):
    "retourne la liste des racines p-ièmes de l'unité"
    resultat = []
    for n in range(p):
        resultat.append(e**((2*pi*1j*n)/p))
        # ou pour la variante
        #resultat.append(n*(n+1)/2)
    return resultat

liste_racine_input_args = [ 2,3,4 ] 

def correction_liste_racines (liste_racines_student):
    return correction_table_1arg (liste_racines_student, liste_racines, liste_racine_input_args, 
                                  columns=(7,40,40))

####################
def produit_scalaire (X,Y):
    """retourne le produit scalaire de deux listes de même taille"""
    # la dimension
    n = len(X)
    # initialisation du resultat
    scalaire = 0
    # on calcule la somme de tous les xi*yi
    for i in range (n):
        scalaire += X[i] * Y[i]
    # ne pas oublier
    return scalaire

from fractions import Fraction

produit_scalaire_inputs = [
    ( range(3,13), range (5,15) ),
    ( [ -2, 10] , [20, 4]),
    ( [ Fraction (2,15), Fraction (3,4) ], [ Fraction (-7,19), Fraction (4,13) ] ),
]

def correction_produit_scalaire (produit_scalaire_student):
    return correction_table (produit_scalaire_student, produit_scalaire, produit_scalaire_inputs,
                             columns=(40,10,10))

