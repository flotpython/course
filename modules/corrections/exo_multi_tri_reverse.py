# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


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
    for liste in listes:
        liste.sort()
    return listes


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


