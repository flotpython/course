# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


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
                               

def multi_tri_ko(listes):
    return listes
