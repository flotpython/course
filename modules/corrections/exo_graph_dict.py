# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


# @BEG@ name=graph_dict
# on va utiliser un defaultdict

from collections import defaultdict

def graph_dict(filename):
    # on le déclare de type list
    g = defaultdict(list)
    with open(filename) as f:
        for line in f:
            # on coupe la ligne en trois parties
            begin, value, end = line.split()
            # comme c'est un defaultdict on n'a
            # pas besoin de l'initialiser
            g[begin].append( (end, int(value)))
    return g
# @END@


# @BEG@ name=graph_dict more=bis
# la même chose mais sans defaultdict

def graph_dict_bis(filename):
    # un dictionnaire vide
    g = {}
    with open(filename) as f:
        for line in f:
            begin, value, end = line.split()
            # c'est ça qu'on économise avec un defaultdict
            if begin not in g:
                g[begin] = []
            # sinon c'est tout pareil
            g[begin].append( (end, int(value)))
    return g
# @END@




inputs_graph_dict = [
    Args("data/graph1.txt"),
    Args("data/graph2.txt"),
    Args("data/graph3.txt"),
]


exo_graph_dict = ExerciseFunction(
    graph_dict, inputs_graph_dict,
    nb_examples = 1,
)


def graph_dict_ko(filename):
    return {'ko' : []}
