# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args

####################
# @BEG@ name=liste_P
def P(x):
    return 2 * x**2 - 3 * x - 2


def liste_P(liste_x):
    """
    retourne la liste des valeurs de P 
    sur les entrées figurant dans liste_x
    """
    return [P(x) for x in liste_x]

# On peut bien entendu faire aussi de manière pédestre
def liste_P_bis(liste_x):
    liste_y = []
    for x in liste_x:
        liste_y.append(P(x))
    return liste_y
# @END@


def liste_P_ko(liste):
    return [P(liste[0])]

inputs_liste_P = [
    Args(list(range(5))),
    Args(list(range(-7, 8, 2))),
    Args([-100, 0, 100]),
]

exo_liste_P = ExerciseFunction(
    liste_P,
    inputs_liste_P,
)

####################
# @BEG@ name=multi_tri
def multi_tri(listes):
    """
    trie toutes les sous-listes
    et retourne listes
    """
    for liste in listes:
        # sort fait un effet de bord
        liste.sort()
    # et on retourne la liste de départ
    return listes
# @END@

inputs_multi_tri = [
    Args([[40, 12, 25], ['spam', 'egg', 'bacon']]),
    Args([[32, 45], [200, 12], [-25, 37]]),
    Args([[], list(range(6)) + [2.5], [4, 2, 3, 1]]),
]

exo_multi_tri = ExerciseFunction(
    multi_tri, inputs_multi_tri,
    layout_args=(20, 20, 20),
)
                               
####################
# @BEG@ name=multi_tri_reverse
def multi_tri_reverse(listes, reverses):
    """
    trie toutes les sous listes, dans une direction
    précisée par le second argument
    """
    # zip() permet de faire correspondre les éléments
    # de listes avec ceux de reverses
    for liste, reverse in zip(listes, reverses):
        # on appelle sort en précisant reverse=
        liste.sort(reverse=reverse)
    # on retourne la liste de départ
    return listes
# @END@

def multi_tri_reverse_ko(listes, reverses):
    return multi_tri(listes)

inputs_multi_tri_reverse = [
    Args([[1, 2], [3, 4]], [True, False]),
    Args([[1, 2], [3, 4]], (True, True)),
    Args([[1, 3, 2], [3, 4]], [False, True]),
    Args([[1, 2], [3, 5, 4]], [False, False]),
    Args([[1, 3], [9, 5], [4, 2]], (True, False, True)),
    Args([[], ['a', 'z', 'c']], [False, True],),
]

exo_multi_tri_reverse = ExerciseFunction(
    multi_tri_reverse, inputs_multi_tri_reverse,
    layout_args=(24, 24, 24),
    nb_examples=2)

####################
# @BEG@ name=produit_scalaire
def produit_scalaire(X, Y):
    """
    retourne le produit scalaire
    de deux listes de même taille
    """
    # initialisation du résultat
    scalaire = 0
    # ici encore avec zip() on peut faire correspondre
    # les X avec les Y
    for x, y in zip(X, Y):
        scalaire += x * y
    # on retourne le résultat
    return scalaire

# Il y a plein d'autres solutions qui marchent aussi
# en voici notamment une qui utilise la fonction builtin sum
# (que nous n'avons pas encore vue, nous la verrons en semaine 4)
# en voici toutefois un avant-goût: la fonction sum est très pratique
# pour faire la somme de toute une liste de valeurs
def produit_scalaire_bis(X, Y):
    return sum([x * y for x, y in zip(X, Y)])

# Et encore une; celle-ci par contre est
# assez peu "pythonique"
# on aime bien en général éviter
# les boucles du genre
# for i in range(l)
#     ... l[i]
def produit_scalaire_ter(X, Y):
    scalaire = 0
    n = len(X)
    for i in range(n):
        scalaire += X[i] * Y[i]
    return scalaire
# @END@

def produit_scalaire_ko(X, Y):
    return [x * y for x, y in zip(X, Y)]


from fractions import Fraction

inputs_produit_scalaire = [
    Args((1, 2), (3, 4)),
    Args(range(3, 9), range(5, 11)),
    Args([-2, 10], [20, 4]),
    Args([Fraction(2, 15), Fraction(3, 4)], [
         Fraction(-7, 19), Fraction(4, 13)]),
    Args([], []),
]

exo_produit_scalaire = ExerciseFunction(
    produit_scalaire,
    inputs_produit_scalaire,
)
