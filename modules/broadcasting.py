from operator import mul
from functools import reduce
from itertools import zip_longest

import numpy as np

"""
Une fonction `compatible` (en deux versions)
qui permet de vérifier si deux dimensions 
de tableaux numpy sont ou non compatibles 
pour le broadcasting
"""


#################### 
# v1: la version qui triche
# on fait faire le travail à numpy et on
# regarde comment ça se passe
def compatible(t1, t2):
    """
    Une fonction qui indique si deux tableaux numpy 
    de formes (shapes) t1 et t2 
    sont compatibles par broadcasting
    Si oui, retourne la forme commune
    Si non, retourne False
    """

    # la version qui triche
    s1 = reduce(mul, t1, 1)
    s2 = reduce(mul, t2, 1)

    try:
        result = np.zeros(s1, dtype=np.int8).reshape(t1) + \
            np.zeros(s2, dtype=np.int8).reshape(t2)
        return result.shape
    except ValueError as e:
        return False


####################
# v2:
# on calcule nous-mêmes si deux tuples
# sont compatibles ou non


def dmax(d1, d2):
    "compare deux longueurs dans une dimension donnée"
    # same lengths
    if d1 == d2:
        return d1
    # both != 1 : can't work
    elif d1 != 1 and d2 != 1:
        return False
    # at least one is 1
    else:
        return max(d1, d2)


def compatible_bool(t1, t2):
    """
    calcule un booléen, ne retourne pas la dimension 
    du broadcasting
    """
    # on renverse les deux dimensions
    # ce qui fait qu'avec zip on va couper à la plus courte
    # des deux, en ne regardant que les plus à droite
    return all(
        dmax(d1, d2)
        for d1, d2 in zip(reversed(t1), reversed(t2)))


def compatible2(t1, t2):
    """
    même comportement que compatible, 
    mais calculé plutôt qu'en essayant
    """
    rev_dmaxes = [
        dmax(d1, d2)
        for (d1, d2) in zip_longest(
            reversed(t1), reversed(t2), fillvalue=1)]
    if not all(rev_dmaxes):
        return False
    rev_dmaxes.reverse()
    return rev_dmaxes
