# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args

from .exo_distance import distance
from .exo_doubler_premier import doubler_premier_inputs


# @BEG@ name=doubler_premier_kwds
def doubler_premier_kwds(f, first, *args, **keywords):
    """
    équivalent à doubler_premier 
    mais on peut aussi passer des arguments nommés
    """
    # c'est exactement la même chose
    return f(2*first, *args, **keywords)

# Complément - niveau avancé
# ----
# Il y a un cas qui ne fonctionne pas avec cette implémentation, 
# quand le premier argument de f a une valeur par défaut 
# *et* on veut pouvoir appeler doubler_premier
# en nommant ce premier argument 
#
# par exemple - avec f=muln telle que définie dans l'énoncé 
#def muln(x=1, y=1): return x*y

# alors ceci
#doubler_premier_kwds(muln, x=1, y=2)
# ne marche pas car on n'a pas les deux arguments requis
# par doubler_premier_kwds
# 
# et pour écrire, disons doubler_permier3, qui marcherait aussi comme cela
# il faudrait faire une hypothèse sur le nom du premier argument...
# @END@


def add3(x, y=0, z=0):
    return x + y + z

def mul3(x=1, y=1, z=1):
    return x * y * z

doubler_premier_kwds_inputs = [
    Args(add3, 1, 2, 3),
    Args(add3, 1, 2, z=3),
    Args(add3, 1, y=2, z=3),
    # Args(add3, x=1, y=2, z=3),
    Args(mul3, 1, 2, 3),
    Args(mul3, 1, 2, z=3),
    Args(mul3, 1, y=2, z=3),
    # Args(mul3, x=1, y=2, z=3),
]

# remettre les datasets de doubler_premier
doubler_premier_kwds_inputs \
    += [ arg_obj for arg_obj in doubler_premier_inputs
         if arg_obj.args[0] == distance ]


exo_doubler_premier_kwds = ExerciseFunction(
    doubler_premier_kwds, doubler_premier_kwds_inputs,
    call_layout='truncate',
    nb_examples=5, render_name=False,
)


def doubler_premier_kwds_ko(f, first, *args, **keywords):
    return f(3*first, *args, **keywords)

