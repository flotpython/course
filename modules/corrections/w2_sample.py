# -*- coding: utf-8 -*-
from exercice import Exercice, Exercice_1arg, Exercice_multiline

#
# example how to use
# 

# @BEG@ 0 0 curve
def curve(a, b):
    return a ** 2 + 3 * a * b + 12
# @END@

inputs_curve = [(0,1), (0,2), (0,3), (0,4), (1,2), (1,3), (1,4), (1,5)]

exo_curve = Exercice(curve, inputs_curve)
