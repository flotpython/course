# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


# @BEG@ name=parse_graph
from collections import defaultdict

def parse_graph(filename):
    g = defaultdict(list)
    with open(filename) as f:
        for line in f:
            begin, value, end = line.split()
            g[begin].append( (end, int(value)))
    return g
# @END@


inputs_parse_graph = [
    Args("data/graph1.txt"),
    Args("data/graph2.txt"),
    Args("data/graph3.txt"),
]


exo_parse_graph = ExerciseFunction(parse_graph,
                                   inputs_parse_graph,
                                   nb_examples = 1,
)


def parse_graph_ko(filename):
    return {'ko' : False}
