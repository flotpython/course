# -*- coding: utf-8 -*-
from nbautoeval.exercise_class import ExerciseClass, ScenarioClass
from nbautoeval.args import Args

# @BEG@ name=fifo
class Fifo:

    def __init__(self):
        self.queue = []

    def incoming(self, x):
        self.queue.insert(0, x)

    def outgoing(self):
        try:
            return self.queue.pop()
        # liste vide..
        except IndexError:
            return None
# @END@


fifo_scenarios = [
    ScenarioClass(
        # init arguments
        Args(),
        'incoming', Args(1),
        'incoming', Args(2),
        'incoming', Args(3),
        'outgoing', Args(),
        'outgoing', Args(),
        'outgoing', Args(),
    ),
    
    ScenarioClass(
        # init arguments
        Args(),
        'incoming', Args(1),
        'incoming', Args(2),
        'outgoing', Args(),
        'outgoing', Args(),
        'incoming', Args(3),
        'incoming', Args(4),
        'outgoing', Args(),
        'outgoing', Args(),
    ),

    ScenarioClass(
        # init arguments
        Args(),
        'outgoing', Args(),
        'incoming', Args(1),
        'outgoing', Args(),
        'outgoing', Args(),
    ),
]

exo_fifo = ExerciseClass (
    Fifo, fifo_scenarios,
    layout='pprint'
)

