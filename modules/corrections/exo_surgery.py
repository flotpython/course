# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args

####################
# @BEG@ name=surgery
def surgery(liste):
    """
    Prend en argument une liste, et retourne la liste modifiée:
    * taille paire: on intervertit les deux premiers éléments
    * taille impaire >= 3: on fait tourner les 3 premiers éléments
    """
    # si la liste est de taille 0 ou 1, il n'y a rien à faire
    if len(liste) < 2:
        pass
    # si la liste est de taille paire
    elif len(liste) % 2 == 0:
        # on intervertit les deux premiers éléments
        liste[0], liste[1] = liste[1], liste[0]
    # si elle est de taille impaire
    else:
        liste[-2], liste[-1] = liste[-1], liste[-2]
    # et on n'oublie pas de retourner la liste dans tous les cas
    return liste
# @END@

def surgery_ko(liste):
    if len(liste) % 2 == 0:
        liste[0], liste[1] = liste[1], liste[0]
    return liste

inputs_surgery = [
    Args(list(range(i))) for i in range(8)
]

exo_surgery = ExerciseFunction(
    surgery, inputs_surgery, nb_examples=5
)
