# -*- coding: iso-8859-15 -*-
from exercice import Exercice, Exercice_1arg, Exercice_multiline

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

inputs_pgcd = [
    (36 * 2**i * 3**j * 5 **k, 36 * 2**j * 3 ** k * 5 ** i)
 for i in range(3) for j in range(3) for k in range(2)

]

exo_pgcd = Exercice (pgcd, inputs_pgcd)
