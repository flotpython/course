# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


# @BEG@ name=doubler_premier
def doubler_premier(f, first, *args):
    """
    renvoie le résultat de la fonction f appliquée sur
    f(2 * first, *args)
    """
    # une fois qu'on a écrit la signature on a presque fini le travail
    # en effet on a isolé la fonction, son premier argument, et le reste
    # des arguments
    # il ne reste qu'à appeler f, après avoir doublé first
    return f(2*first, *args)
# @END@


# @BEG@ name=doubler_premier more=bis
def doubler_premier_bis(f, *args):
    """
    marche aussi mais moins élégant
    """
    first = args[0]
    remains = args[1:]
    return f(2*first, *remains)
# @END@


doubler_premier_inputs = []
from operator import add
from operator import mul
from .exo_distance import distance

# pour l'exemple on choisit les 3 premiers inputs
# avec des fonctions différentes
for i in (1, 3, 5):
    doubler_premier_inputs.append(Args(add, i, 4))
    doubler_premier_inputs.append(Args(mul, i, 4))
doubler_premier_inputs.insert(2, Args(distance, 1.5, 4.))
doubler_premier_inputs.insert(3, Args(distance, 2.0, 4., 4., 4.))


exo_doubler_premier = ExerciseFunction(
    doubler_premier, doubler_premier_inputs,
    nb_examples=4,
    render_name=False,
    layout_args=(40,10,10),
    call_layout='truncate'
)


def doubler_premier_ko(f, first, *args):
    return f(3*first, *args)
