# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


# @BEG@ name=graph_dict
from collections import defaultdict

def graph_dict(filename):
    g = defaultdict(list)
    with open(filename) as f:
        for line in f:
            begin, value, end = line.split()
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
