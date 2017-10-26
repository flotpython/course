# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args

####################
# @BEG@ name=surgery
def surgery(liste):
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

def surgery_ko(liste):
    if len(liste) % 2 == 0:
        liste[0], liste[1] = liste[1], liste[0]
    return liste

inputs_surgery = [
    Args([]),
    Args([1]),
    Args(['spam', 2]),
    Args(['spam', 2, 'bacon']),
    Args([1, 2, 3, 4]),
    Args([1, 2, 3, 4, 5]),
]

exo_surgery = ExerciseFunction(
    surgery, inputs_surgery, nb_examples=4
)
