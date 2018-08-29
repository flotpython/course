# -*- coding: utf-8 -*-

# pylint: disable=c0111, c0411, c0103

from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


# @BEG@ name=graph_dict
# une première solution avec un defaultdict

from collections import defaultdict

def graph_dict(filename):
    """
    construit une stucture de données de graphe
    à partir du nom du fichier d'entrée
    """
    # un dictionnaire vide normal
    graph = {}

    with open(filename) as feed:
        for line in feed:
            begin, value, end = line.split()
            # c'est cette partie
            # qu'on économise avec un defaultdict
            if begin not in graph:
                graph[begin] = []
            # sinon c'est tout pareil
            graph[begin].append((end, int(value)))
    return graph
# @END@


# @BEG@ name=graph_dict more=bis
def graph_dict_bis(filename):
    """
    pareil mais avec defaultdict
    """
    # on déclare le defaultdict de type list
    # de cette façon si une clé manque elle
    # sera initialisée avec un appel à list()
    graph = defaultdict(list)

    with open(filename) as feed:
        for line in feed:
            # on coupe la ligne en trois parties
            begin, value, end = line.split()
            # comme c'est un defaultdict on n'a
            # pas besoin de l'initialiser
            graph[begin].append((end, int(value)))
    return graph
# @END@




inputs_graph_dict = [
    Args("data/graph1.txt"),
    Args("data/graph2.txt"),
    Args("data/graph3.txt"),
]


exo_graph_dict = ExerciseFunction(
    graph_dict, inputs_graph_dict,
    nb_examples=1,
    layout_args=(10, 40, 40),
)


def graph_dict_ko(filename):
    return {'ko' : []}
