# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


# @BEG@ name=intersect
def intersect(tuples_a, tuples_b):
    """
    prend en entrée deux listes de tuples de la forme
    (entier, valeur)

    renvoie l'ensemble des valeurs associées, dans A ou B,
    aux entiers présents dans A et B

    il y a **plein** d'autres façons de faire, mais il faut
    juste se méfier de ne pas tout recalculer plusieurs fois
    si on veut faire trop court

    """

    # pour montrer un exemple de fonction locale:
    # une fonction qui renvoie l'ensemble des entiers
    # présents comme clé dans une liste d'entrée
    def keys(tuples):
        return {entier for entier, valeur in tuples}
    # on l'applique à A et B
    keys_a = keys(tuples_a)
    keys_b = keys(tuples_b)
    #
    # les entiers présents dans A et B
    # avec une intersection d'ensembles
    common_keys = keys_a & keys_b
    # et pour conclure on fait une union sur deux
    # compréhensions d'ensembles
    return {val_a for key, val_a in tuples_a if key in common_keys} \
         | {val_b for key, val_b in tuples_b if key in common_keys}
# @END@


def intersect_ko(A, B):
    A_vals = { v for k, v in A }
    B_vals = { v for k, v in B }
    return A_vals & B_vals


intersect_inputs = []

A1 = {(12, 'douze'), (10, 'dixA'), (8, 'huit'),}
B1 = {(5, 'cinq'), (10, 'dixB'), (15, 'quinze'),}
intersect_inputs.append(Args(A1, B1))

A2 = {(1, 'unA'), (2, 'deux'), (3, 'troisA')}
B2 = {(1, 'unB'), (2, 'deux'), (4, 'quatreB')}
intersect_inputs.append(Args(A2, B2))


exo_intersect = ExerciseFunction(
    intersect, intersect_inputs, nb_examples=2)
