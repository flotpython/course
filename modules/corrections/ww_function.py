# -*- coding: utf-8 -*-
from exercice_function import ExerciceFunction
from args import Args

#
# example how to use
# 

# @BEG@ week=0 sequence=0 name=curve
def curve(a, b):
    return a ** 2 + 3 * a * b + 12
# @END@

inputs_curve = [Args(0,1),
                Args(0,2),
                Args(0,3),
                Args(0,4),
                Args(1,2),
                Args(1,3),
                Args(1,4),
                Args(1,5),
]

exo_curve = ExerciceFunction(
    curve, inputs_curve)


exo_curve_name = ExerciceFunction(
    curve, inputs_curve, render_name=True)
