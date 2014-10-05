# -*- coding: iso-8859-15 -*-
from corrections.tools import correction_table, correction_table_1arg, exemple_table, exemple_table_1arg

dispatch1_inputs = [ (x,y) for x in range (3,6) for y in range (7,10) ]

def dispatch1 (a,b):
    """dispatch1 as specified in W3-S7-E1"""
    if a%2 == 0 and b%2 == 0:
        return a*a+b*b
    elif a%2 == 0 and b%2 != 0:
        return a*(b-1)
    elif a%2 != 0 and b%2 == 0:
        return (a-1)*b
    else:
        return a*a-b*b

def correction_dispatch1 (student_dispatch1):
    return correction_table (student_dispatch1, dispatch1, dispatch1_inputs)
