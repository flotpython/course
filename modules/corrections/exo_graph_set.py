# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


# @BEG@ name=graph_set
from collections import defaultdict

def graph_set(filename):
    g = defaultdict(set)
    with open(filename) as f:
        for line in f:
            begin, value, end = line.split()
            g[begin].add( (end, int(value)))
    return g
# @END@


inputs_graph_set = [
    Args("data/graph1.txt"),
    Args("data/graph2.txt"),
    Args("data/graph3.txt"),
]


exo_graph_set = ExerciseFunction(
    graph_set, inputs_graph_set,
    nb_examples = 1,
)


def graph_set_ko(filename):
    return {'ko' : []}
