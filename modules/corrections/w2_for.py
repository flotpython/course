# -*- coding: iso-8859-15 -*-
from exercice import Exercice, Exercice_1arg, Exercice_multiline

# @BEG@ 2 7 multi_tri
def multi_tri (listes):
    "trie toutes les sous-listes, et retourne listes"
    for liste in listes:
        # sort fait un effet de bord 
        liste.sort()
    # et on retourne la liste de départ
    return listes
# @END@

inputs_multi_tri = [
    [ [ 40, 12, 25], [ 'spam', 'egg', 'bacon' ], ], 
    [ [ 32, 45], [ 200, 12 ], [-25, 37] ], 
    [ [ ], range(10) ],
]

exo_multi_tri = Exercice_1arg (multi_tri, inputs_multi_tri,
                               correction_columns= (40,40,40),
                               exemple_columns=(60,60))
                               
####################
# @BEG@ 2 7 multi_tri_reverse
def multi_tri_reverse (listes, reverses):
    """trie toutes les sous listes, dans une direction
    precisée par le second argument"""
    # zip() permet de faire correspondre les éléments 
    # de listes avec ceux de reverses
    for liste, reverse in zip(listes, reverses):
        # on appelle sort en précisant reverse=
        liste.sort(reverse=reverse)
    # on retourne la liste de départ
    return listes
# @END@

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
# @BEG@ 2 7 liste_racines
from math import e, pi

def liste_racines (p):
    "retourne la liste des racines p-ièmes de l'unité"
    # une simple compréhension fait l'affaire
    # souvenez vous que 1j c'est notre 'i' complexe
    return [ e**((2*pi*1j*n)/p) for n in range(p)]

# Il est tout à fait possible aussi de contruire les racines pas à pas
# C'est un peu moins élégant mais ça fonctionne très bien aussi
def liste_racines_2 (p):
    "retourne la liste des racines p-ièmes de l'unité"
    # on va construire le résultat petit à petit
    # en partant d'une liste vide
    resultat = []
    # pour chaque n dans {0 .. p-1}
    for n in range(p):
        # on ajoute dans le résultat la racine d'ordre n
        resultat.append(e**((2*pi*1j*n)/p))
    # et on retourne le résultat
    return resultat
# @END@

inputs_liste_racines = [ 2,3,4 ] 

exo_liste_racines = Exercice_1arg (liste_racines, inputs_liste_racines,
                                   correction_columns=(7,40,40))

####################
# @BEG@ 2 7 produit_scalaire
def produit_scalaire (X,Y):
    # initialisation du resultat
    scalaire = 0
    # ici encore avec zip() on peut faire correspondre 
    # les X avec les Y
    for x,y in zip (X,Y):
        scalaire += x*y
    # on retourne le résultat
    return scalaire

# Il y a plein d'autres solutions qui marchent aussi
# en voici notamment une qui utilise la fonction builtin sum
# (que nous n'avons pas encore vue, nous la verrons en semaine 4)
# en voici toutefois un avant-goût: la fonction sum est très pratique
# pour faire la somme de toute une liste de valeurs
def produit_scalaire_2 (X,Y):
    """retourne le produit scalaire de deux listes de même taille"""
    return sum ( [x*y for x,y in zip (X,Y) ] )
# @END@

def produit_scalaire_3 (X,Y):
    scalaire = 0
    n = len(X)
    for i in range (n):
        scalaire += X[i] * Y[i]
    return scalaire


from fractions import Fraction

inputs_produit_scalaire = [
    ( range(3,13), range (5,15) ),
    ( [ -2, 10] , [20, 4]),
    ( [ Fraction (2,15), Fraction (3,4) ], [ Fraction (-7,19), Fraction (4,13) ] ),
    ( [],[]),
]

exo_produit_scalaire = Exercice (produit_scalaire, inputs_produit_scalaire,
                                 correction_columns =(42,15,15))

