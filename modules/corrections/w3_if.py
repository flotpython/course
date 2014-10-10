# -*- coding: iso-8859-15 -*-
from exercice import Exercice, Exercice_1arg, Exercice_multiline

inputs_dispatch1 = [ (a,b) for a in range (3,6) for b in range (7,10) ]

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

exo_dispatch1 = Exercice (dispatch1, inputs_dispatch1)

####################
samples_A = [ (2,4,6), [2,4,6] ]
samples_B = [ {6,8,10} ]

inputs_dispatch2 = [
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

exo_dispatch2 = Exercice (dispatch2, inputs_dispatch2,
                          correction_columns = (50,30,30))

