# -*- coding: iso-8859-15 -*-
from exercice import Exercice, Exercice_1arg, Exercice_multiline

####################
def divisible (a,b): 
    return a%b==0 or b%a==0

inputs_divisible = [
    (20,10),
    (200,-10),
    (-200,10),
    (-200,-10),
    (10,200),
    (10,-200),
    (-10,200),
    (-10,-200),
    (8,12),
    (12,-8),
    (-12,8),
    (-12,-8),
]

exo_divisible = Exercice (divisible, inputs_divisible)

####################
def spam (l):
    if not l:
        pass
    elif len(l)%2 == 0:
        l[0],l[1]=l[1],l[0]
    else:
        l.pop()
    return l

inputs_spam = [
    [],
    [1],
    ['spam', 2 ],
    ['spam', 2, 'bacon' ],
    [1,2,3,4 ],
    [1,2,3,4,5],
]

exo_spam = Exercice_1arg (spam, inputs_spam, exemple_how_many=4)
