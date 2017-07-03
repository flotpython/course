# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args

####################
# @BEG@ name=divisible
def divisible(a, b):
    "renvoie True si un des deux arguments divise l'autre"
    # b divise a si et seulement si le reste
    # de la division de a par b est nul
    # et il faut regarder aussi si a divise b
    return a % b == 0 or b % a == 0
# @END@

def divisible_ko(a, b):
    return a % b == 0

inputs_divisible = [
    Args(10, 30),
    Args(10, -30),
    Args(-10, 30),
    Args(-10, -30),
    Args(8, 12),
    Args(12, -8),
    Args(-12, 8),
    Args(-12, -8),
    Args(10, 1),
    Args(30, 10),
    Args(30, -10),
    Args(-30, 10),
    Args(-30, -10),
]

exo_divisible = ExerciseFunction(
    divisible, inputs_divisible)

####################
# @BEG@ name=spam
def spam(liste):
    """
Prend en argument une liste, et retourne la liste modifiée:
 * taille paire: on intervertit les deux premiers éléments
 * taille impaire, on retire le dernier élément
"""
    # si la liste est vide il n'y a rien à faire
    if not liste:
        pass
    # si la liste est de taille paire
    elif len(liste) % 2 == 0:
        # on intervertit les deux premiers éléments
        liste[0], liste[1] = liste[1], liste[0]
    # si elle est de taille impaire
    else:
        # on retire le dernier élément
        liste.pop()
    # et on n'oublie pas de retourner la liste dans tous les cas
    return liste
# @END@

def spam_ko(liste):
    if len(liste) % 2 == 0:
        liste[0], liste[1] = liste[1], liste[0]
    return liste

inputs_spam = [
    Args([]),
    Args([1]),
    Args(['spam', 2]),
    Args(['spam', 2, 'bacon']),
    Args([1, 2, 3, 4]),
    Args([1, 2, 3, 4, 5]),
]

exo_spam = ExerciseFunction(
    spam, inputs_spam, nb_examples=4)
