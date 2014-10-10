# -*- coding: iso-8859-15 -*-
from corrections.exercice import correction_table, correction_table_1arg, exemple_table, exemple_table_1arg

def pgcd (a,b):
    "le pgcd de a et b par l'algorithme d'Euclide"
    # on suppose que a >= b, il faut inverser sinon
    if b > a : 
        a,b = b,a
    while True:
        r = a % b
        if r == 0:
            return b
        a,b = b,r

pgcd_inputs = [
    (36 * 2**i * 3**j * 5 **k, 36 * 2**j * 3 ** k * 5 ** i)
 for i in range(3) for j in range(3) for k in range(2)

]

def correction_pgcd (student_pgcd):
    return correction_table (student_pgcd, pgcd, pgcd_inputs)
