# -*- coding: iso-8859-15 -*-
from exercice import Exercice, Exercice_1arg, Exercice_multiline

def multi_tri (listes):
    "trie toutes les sous-listes"
    for liste in listes:
        liste.sort()
    return listes

inputs_multi_tri = [
    [ [ 40, 12, 25], [ 'spam', 'egg', 'bacon' ], ], 
    [ [ 32, 45], [ 200, 12 ], [-25, 37] ], 
    [ [ ], range(10) ],
]

exo_multi_tri = Exercice_1arg (multi_tri, inputs_multi_tri,
                               correction_columns= (40,40,40),
                               exemple_columns=(60,60))
                               
####################
def multi_tri_reverse (listes, reverses):
    """trie toutes les sous listes, dans une direction
    precisée par le second argument"""
    for liste, reverse in zip(listes, reverses):
        liste.sort(reverse=reverse)
    return listes

inputs_multi_tri_reverse = [ 
    ( [ [1,2], [3,4] ], [ True, False] ),
    ( [ [1,2], [3,4] ], ( True, True ) ),
    ( [ [1,3,2], [3,4] ], [ False, True] ),
    ( [ [1,2], [3,5,4] ], [ False, False] ),
    ( [ [ 1,3], [ 9,5 ], [4,2] ], (True, False, True) ),
    ( [ [ ], ['a', 'z', 'c' ] ], [False, True ], ),
]

exo_multi_tri_reverse = Exercice (multi_tri_reverse, inputs_multi_tri_reverse,
                                  correction_columns = (50,40,40),
                                  exemple_columns = (60,60),
                                  exemple_how_many = 2)

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

inputs_liste_racines = [ 2,3,4 ] 

exo_liste_racines = Exercice_1arg (liste_racines, inputs_liste_racines,
                                   correction_columns=(7,40,40))

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

inputs_produit_scalaire = [
    ( range(3,13), range (5,15) ),
    ( [ -2, 10] , [20, 4]),
    ( [ Fraction (2,15), Fraction (3,4) ], [ Fraction (-7,19), Fraction (4,13) ] ),
]

exo_produit_scalaire = Exercice (produit_scalaire, inputs_produit_scalaire,
                         correction_columns =(40,10,10))

