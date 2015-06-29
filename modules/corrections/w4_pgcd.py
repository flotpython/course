# -*- coding: utf-8 -*-
from exercice_function import ExerciceFunction
from args import Args

# @BEG@ 4 2 pgcd
def pgcd(a, b):
    "le pgcd de a et b par l'algorithme d'Euclide"
    # l'algorithme suppose que a >= b
    # donc si ce n'est pas le cas 
    # il faut inverser les deux entrées
    if b > a : 
        a, b = b, a
    # boucle sans fin
    while True:
        # on calcule le reste 
        r = a % b
        # si le reste est nul, on a terminé
        if r == 0:
            return b
        # sinon on passe à l'itération suivante
        a, b = b, r
# @END@

inputs_pgcd = [
    Args(36 * 2**i * 3**j * 5 **k, 36 * 2**j * 3 ** k * 5 ** i)
 for i in range(3) for j in range(3) for k in range(2)
]

exo_pgcd = ExerciceFunction(pgcd, inputs_pgcd)
