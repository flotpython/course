from nbautoeval import Args, ExerciseFunction, PPrintCallRenderer


# @BEG@ name=two_sum
def two_sum(liste, target):
    """
    retourne un tuple de deux indices de deux nombres
    dans la liste dont la somme fait target
    """
    for i, item1 in enumerate(liste):
        for j, item2 in enumerate(liste):
            # prune the loop on j altogether once we reach i
            if j >= i:
                break
            if item1 + item2 == target:
                return j, i
# @END@


# @BEG@ name=two_sum more=bis
from itertools import product


def two_sum_bis(liste, target):
    """
    pareil en utilisant itertools.product
    pour éviter les deux for imbriqués
    un tout petit peu moins efficace ici car on est dans une seule
    boucle et donc on ne peut pas avorter la boucle interne
    avec break
    """
    for (i, item1), (j, item2) in product(
        enumerate(liste), enumerate(liste)):
        for j, item2 in enumerate(liste):
            if i >= j:
                continue
            if item1 + item2 == target:
                return i, j
# @END@


# @BEG@ name=two_sum more=ter
def two_sum_ter(liste, target):
    """
    toujours avec product, pour illustrer l'usage de repeat=
    """
    for (i, item1), (j, item2) in product(
        enumerate(liste), repeat=2):
        for j, item2 in enumerate(liste):
            if i >= j:
                continue
            if item1 + item2 == target:
                return i, j
# @END@



inputs = [
    Args([10, 32, 46, 27, 55, 82, 16, 19], 128),
    Args([0, 64, 1, 2, 128, 4, 8, 16, 32], 96),
    Args([0, 64, 1, 128, 4, 8, 16, 32, 2], 3),
    Args([0, 64, 1, 127, 4, 8, 16, 32, 2], 128),
]


exo_two_sum = ExerciseFunction(
    two_sum,
    inputs,
    nb_examples=0,
    call_renderer=PPrintCallRenderer(width=40),
    font_size='x-small',
)
