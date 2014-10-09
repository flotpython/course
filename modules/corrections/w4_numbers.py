# -*- coding: iso-8859-15 -*-
from corrections.tools import correction_table, correction_table_1arg, exemple_table, exemple_table_1arg

from operator import mul

####################
def numbers (liste):
    """
retourne un tuple contenant
 la somme
 le produit
 le minimum
 le maximum
des elements de la liste
    """
    return ( sum(liste),
             reduce(mul,liste,1),
             min(liste),
             max(liste))

from random import randint

def input ():
    length = randint (3,6)
    result = []
    for i in xrange(length):
        result.append(randint(5,15))
    return result

numbers_inputs = [ input() for i in xrange (3) ]

def correction_numbers (student_numbers):
    return correction_table_1arg (student_numbers, numbers, numbers_inputs)

