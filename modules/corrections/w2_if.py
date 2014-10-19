# -*- coding: iso-8859-15 -*-
from exercice import Exercice, Exercice_1arg, Exercice_multiline

####################
# @BEG@ 2 7 divisible
def divisible (a,b): 
    "renvoie True si un des deux arguments divise l'autre"
    # b divise a si et seulement si le reste 
    # de la division de a par b est nul
    # et il faut regarder aussi si a divise b
    return a%b==0 or b%a==0
# @END@

inputs_divisible = [
    (10,1),
    (10,-1),
    (1,10),
    (1,-10),
    (20,10),
    (200,-10),
    (-200,10),
    (-200,-10),
    (10,200),
    (10,-200),
    (-10,200),
    (-10,-200),
    (8,12),
    (12,-8),
    (-12,8),
    (-12,-8),
]

exo_divisible = Exercice (divisible, inputs_divisible)

####################
# @BEG@ 2 7 spam
def spam (l):
    """
Prend en argument une liste, et retourne la liste modifiée:
 * taille paire: on intervertit les deux premiers éléments
 * taille impaire, on retire le dernier élément
"""
    # si la liste est vide il n'y a rien à faire
    if not l:
        pass
    # si la liste est de taille paire
    elif len(l)%2 == 0:
        # on intervertit les deux premiers éléments
        l[0],l[1]=l[1],l[0]
    # si elle est de taille impaire
    else:
        # on retire le dernier élément
        l.pop()
    # et on n'oublie pas de retourner la liste dans tous les cas
    return l
# @END@

inputs_spam = [
    [],
    [1],
    ['spam', 2 ],
    ['spam', 2, 'bacon' ],
    [1,2,3,4 ],
    [1,2,3,4,5],
]

exo_spam = Exercice_1arg (spam, inputs_spam, exemple_how_many=4)
