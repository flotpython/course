# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


# @BEG@ name=pgcd
def pgcd(a, b):
    "le pgcd de a et b par l'algorithme d'Euclide"
    # l'algorithme suppose que a >= b
    # donc si ce n'est pas le cas 
    # il faut inverser les deux entrées
    if b > a : 
        a, b = b, a
    if b == 0:
        return a
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


# @BEG@ name=pgcd more=bis
# il se trouve qu'en fait la première inversion n'est
# pas nécessaire
# en effet si a <= b, la première itération de la boucle
# while va faire
# r = a % b = a
# et ensuite
# a, b = b, r = b, a
# ce qui provoque l'inversion
def pgcd_bis(a, b):
    # si l'on des deux est nul on retourne l'autre
    if a * b == 0:
        return a or b
    # sinon on fait une boucle sans fin
    while True:
        # on calcule le reste 
        r = a % b
        # si le reste est nul, on a terminé
        if r == 0:
            return b
        # sinon on passe à l'itération suivante
        a, b = b, r
# @END@

# @BEG@ name=pgcd more=ter
# une autre alternative, qui fonctionne aussi
# plus court, mais on passe du temps à se convaincre
# que ça fonctionne bien comme demandé
def pgcd_ter(a, b):
    # si on n'aime pas les boucles sans fin
    # on peut faire aussi comme ceci
    while b:
        a, b = b, a % b
    return a
# @END@


def pgcd_ko(a, b):
    return a % b

inputs_pgcd = [
    Args(0, 0),
    Args(0, 1),
    Args(1, 0),
    Args(15, 10),
    Args(10, 15),
    Args(3, 10),
    Args(10, 3),
    Args(10, 1),
    Args(1, 10),
]

inputs_pgcd += [
    Args(36 * 2**i * 3**j * 5**k,
         36 * 2**j * 3**k * 5**i)
    for i in range(3) for j in range(3) for k in range(2)
]

exo_pgcd = ExerciseFunction(
    pgcd, inputs_pgcd,
    nb_examples = 6,
)
