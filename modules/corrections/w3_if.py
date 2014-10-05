# -*- coding: iso-8859-15 -*-
from corrections.tools import correction_table, correction_table_1arg, exemple_table, exemple_table_1arg

dispatch1_inputs = [ (a,b) for a in range (3,6) for b in range (7,10) ]

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

####################
samples_A = [ (2,4,6), [2,4,6] ]
samples_B = [ {6,8,10} ]

dispatch2_inputs = [
        (a,b,A,B) for a,A in zip(range (3,5), samples_A) for b in range (7,10) for B in samples_B
]

def dispatch2 (a,b,A,B):
    """dispatch2 as specified in W3-S7-E1"""
    if ( a in A and b in B) or ( a not in A and b not in B):
        return a*a+b*b
    elif b not in B: # in this case we know that a is in A
        return a*(b-1)
    else:
        return (a-1)*b

def correction_dispatch2 (student_dispatch2):
    return correction_table (student_dispatch2, dispatch2, dispatch2_inputs, columns = (50,30,30))

