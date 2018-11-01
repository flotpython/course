# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


# @BEG@ name=produit_scalaire
def produit_scalaire(vec1, vec2):
    """
    retourne le produit scalaire
    de deux listes de même taille
    """
    # avec zip() on peut faire correspondre les
    # valeurs de vec1 avec celles de vec2 de même rang
    #
    # et on utilise la fonction builtin sum sur une itération
    # des produits x1*x2
    #
    # remarquez bien qu'on utilise ici une expression génératrice
    # et PAS une compréhension car on n'a pas du tout besoin de
    # créer la liste des produits x1*x2
    #
    return sum(x1 * x2 for x1, x2 in zip(vec1, vec2))
# @END@


# @BEG@ name=produit_scalaire more=bis
# Il y a plein d'autres solutions qui marchent aussi
#
def produit_scalaire_bis(vec1, vec2):
    """
    Une autre version, où on fait la somme à la main
    """
    scalaire = 0
    for x1, x2 in zip(vec1, vec2):
        scalaire += x1 * x2
    # on retourne le résultat
    return scalaire
# @END@


# @BEG@ name=produit_scalaire more=ter
# Et encore une:
# celle-ci par contre est assez peu "pythonique"
#
# considérez-la comme un exemple de
# ce qu'il faut ÉVITER DE FAIRE:
#
def produit_scalaire_ter(vec1, vec2):
    """
    Lorsque vous vous trouvez en train d'écrire:

        for i in range(len(sequence)):
            x = iterable[sequence]
            # etc...

    vous pouvez toujours écrire à la place:

        for x in sequence:
            ...

    qui en plus d'être plus facile à lire,
    marchera sur tout itérable, et sera plus rapide
    """
    scalaire = 0
    # sachez reconnaitre ce vilain idiome:
    for i in range(len(vec1)):
        scalaire += vec1[i] * vec2[i]
    return scalaire
# @END@


from fractions import Fraction


inputs_produit_scalaire = [
    Args((1, 2), (3, 4)),
    Args(range(3, 9), range(5, 11)),
    Args([-2, 10], [20, 4]),
    Args([Fraction(2, 15), Fraction(3, 4)],
         [Fraction(-7, 19), Fraction(4, 13)]),
    Args([], []),
]


exo_produit_scalaire = ExerciseFunction(
    produit_scalaire,
    inputs_produit_scalaire,
)


def produit_scalaire_ko(vec1, vec2):
    return [x * y for x, y in zip(vec1, vec2)]
