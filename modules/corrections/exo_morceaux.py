# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


####################
# @BEG@ name=morceaux
def morceaux(x):
    if x <= -5:
        return -x - 5
    elif x <= 5:
        return 0
    else:
        return x / 5 - 1
# @END@


# @BEG@ name=morceaux more=bis
def morceaux_bis(x):
    if x <= -5:
        return -x - 5
    if x <= 5:
        return 0
    return x / 5 - 1
# @END@


# @BEG@ name=morceaux more=ter
# on peut aussi faire des tests d'intervalle
# comme ceci  0 <= x <= 10
def morceaux_ter(x):
    if x <= -5:
        return -x - 5
    elif -5 <= x <= 5:
        return 0
    else:
        return x / 5 - 1
# @END@


inputs_morceaux = [
    Args(x) for x in (-10, 0, 10, -6, -5, -4, 4, 5, 20)
]


exo_morceaux = ExerciseFunction(
    morceaux, inputs_morceaux,
    nb_examples = 3,
)


def morceaux_ko(x):
    return morceaux(x) if x <= 15 else x
