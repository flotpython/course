# -*- coding: iso-8859-15 -*-
from corrections.exercice import correction_table, correction_table_1arg, exemple_table, exemple_table_1arg

#
# example how to use
# 
def good_curve (a,b):
    return a ** 2 + 3 * a * b + 12
curve_inputs = [ (0,1), (0,2), (0,3), (0,4), (1,2), (1,3), (1,4), (1,5) ]

def correction_curve (student_curve):
    return correction_table (student_curve, good_curve, curve_inputs)
