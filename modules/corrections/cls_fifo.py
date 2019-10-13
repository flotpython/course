# -*- coding: utf-8 -*-

# pylint: disable=c0111, c0103

from nbautoeval.exercise_class import ExerciseClass, ClassScenario
from nbautoeval.args import Args

# @BEG@ name=fifo
class Fifo:
    """
    Une classe FIFO implémentée avec une simple liste
    """

    # dans cette première version on utilise 
    # un object 'list' standard
    # on ajoute à la fin avec    queue.append(x), 
    # et on enlève au début avec queue.pop(0)
    # 
    # remarquez qu'on pourrait aussi 
    # ajouter au début avec queue.insert(0, x)
    # enlever à la fin avec queue.pop()

    def __init__(self):
        # l'attribut queue est un objet liste
        self.queue = []

    def __repr__(self):
        contents = ", ".join(str(item) for item in self.queue)
        return f"[Fifo {contents}]"

    def incoming(self, item):
        # on insère au début de la liste
        self.queue.append(item)

    def outgoing(self):
        # pas la peine d'utiliser un try/except dans ce cas
        if self.queue:
            return self.queue.pop(0)
        # si on utilise pylint on va avoir envie de rajouter ceci
        # qui n'est pas vraiment indispensable..
        else:
            return None
# @END@


# @BEG@ name=fifo more=bis
from collections import deque

class FifoBis:
    """
    une alternative en utilisant exactement la même stratégie
    mais avec un objet de type collections.deque
    en effet, l'objet 'list' standard est optimisé pour 
    ajouter/enlever **à la fin** de la liste
    et on a vu dans la première version du code qu'il nous faut
    travailler sur les deux cotés de la pile, quel que soit le sens
    qu'on choisit pour implémenter la pile
    donc si la pile a des chances d'être longue de plusieurs milliers
    d'objets, il est utile de prendre un 'deque' 
    'deque' vient de 'double-entry queue', et est optimisée 
    pour les accès depuis le début et/ou la fin de la liste
    """
    def __init__(self):
        self.queue = deque()
        
    # ici pour faire bon poids on utilise la stratégie inverse
    # de la première version de la pile, on insère au début et on
    # enlève de la fin
    # du coup on les affice dans l'autre sens
    def __repr__(self):
        contents = ", ".join(str(item) for item in reversed(self.queue))
        return f"[Fifo {contents}]"

    def incoming(self, item):
        self.queue.insert(0, item)

    def outgoing(self):
        if self.queue:
            return self.queue.pop()

# @END@

fifo_scenarios = [
    ClassScenario(
        # init arguments
        Args(),
        "INSTANCE.outgoing()",
        "INSTANCE.incoming(1)",
        "INSTANCE.incoming(2)",
        "INSTANCE",
        "INSTANCE.outgoing()",
        "INSTANCE.outgoing()",
        "INSTANCE.outgoing()",
    ),
    ClassScenario(
        # init arguments
        Args(),
        "INSTANCE.incoming(1)",
        "INSTANCE.incoming(2)",
        "INSTANCE",
        "INSTANCE.outgoing()",
        "INSTANCE.incoming(3)",
        "INSTANCE",
        "INSTANCE.outgoing()",
        "INSTANCE",
        "INSTANCE.outgoing()",
        "INSTANCE.outgoing()",
    ),

    ClassScenario(
        # init arguments
        Args(),
        "INSTANCE.incoming(1)",
        "INSTANCE.incoming(2)",
        "INSTANCE.outgoing()",
        "INSTANCE.outgoing()",
        "INSTANCE.incoming(3)",
        "INSTANCE.incoming(4)",
        "INSTANCE.outgoing()",
        "INSTANCE.outgoing()",
    ),

]

exo_fifo = ExerciseClass(
    Fifo, fifo_scenarios,
    obj_name = "F",
)
