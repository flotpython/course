# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


alphabet = "0123456789abcdef"

# on fabrique des jeux de données
import random

def args(connue, inconnue):
    # composite, connue
    return Args(connue + inconnue + connue, connue)

inconnue_inputs = [
    args("".join(random.sample(alphabet, random.randint(3, 6))),
         "".join(random.sample(alphabet, random.randint(5, 8))))
    for i in range(4)
]


# @BEG@ name=inconnue
# pour enlever à gauche et à droite une chaine de longueur x
# on peut faire composite[ x : -x ]
# or ici x vaut len(connue)
def inconnue(composite, connue):
    return composite[ len(connue) : -len(connue) ]
# @END@ 


# @BEG@ name=inconnue more=bis
# ce qui peut aussi s'écrire comme ceci si on préfère
def inconnue_bis(composite, connue):
    return composite[ len(connue) : len(composite)-len(connue) ]
# @END@


exo_inconnue = ExerciseFunction(
    inconnue, inconnue_inputs
)


def inconnue_ko(big, small):
    return big[len(small):-4]
