from nbautoeval import (
    Args, ExerciseGenerator, GeneratorArgs, PPrintRenderer)

# @BEG@ name=npsearch
import numpy as np

def npsearch(world, needle):
    """
    world est la "grande" matrice dans laquelle 
    on cherche les occurrences de needle
    qui peut être une matrice 2d ou une simple ligne

    npsearch est une fonction génératrice qui énumère
    les tuples (i, j) correspondant à une occurrence de 
    needle dans world
    """
    if len(needle.shape) == 1:
        needle = needle[np.newaxis, :]
    n, m = needle.shape
    # pas la peine de faire une grande boucle sur tout le tableau
    # s'il y a égalité c'est nécessairement que 
    # le world[i, j] == needle[0, 0]
    for i, j in np.argwhere(world == needle[0][0]):
        # c'est ici le point délicat
        # si vous comparez les deux tableaux à base de ==
        # (même en utiisant np.all)
        # vous allez potentiellement mettre en oeuvre
        # un broadcasting non souhaitable
        if np.array_equal(world[i:i+n, j:j+m], needle):
            yield i, j
# @END@


# une version qui ne MARCHE PAS 
def npsearch_ko(world, needle):
    if len(needle.shape) == 1:
        needle = needle[np.newaxis, :]
    n, m = needle.shape
    for i, j in np.argwhere(world == needle[0][0]):
        if np.all(world[i:i+n, j:j+m] == needle):
            yield i, j

z = np.arange(12).reshape(4, 3)
yz0 = np.array([[3, 4], [6, 7]])
nz0 = np.array([[0, 0], [0, 0]])

a = np.array(3*[[1, 1, 1, 0, 0, 0]] + 3*[[0, 0, 0, 1, 1, 1]])

ya0 = np.array(4*[[1]]).reshape((2, 2))
ya1 = np.array(6*[[1]]).reshape((2, 3))
ya2 = np.array([1, 0, 0, 1, 0, 0, 0, 1, 1]).reshape((3, 3))
ya3 = np.array(9*[[1]]).reshape((3, 3))

na1 = np.array([1, 1, 0, 0, 0, 0]).reshape(2, 3)


b = np.array(np.arange(25)).reshape((5, 5))
yb1 = np.array([1, 2, 3, 6, 7, 8, 11, 12, 13]).reshape((3, 3))
yb2 = np.array([13, 14, 0, 18, 19, 0, 23, 24, 0]).reshape((3, 3))
yn1 = np.array([13, 14, 18, 19, 23, 24]).reshape((3, 2))

inputs_npsearch = [
    GeneratorArgs(z, yz0),
    GeneratorArgs(z, nz0),
    GeneratorArgs(a, ya0),
    GeneratorArgs(a, ya1),
    GeneratorArgs(a, ya2),
    GeneratorArgs(a, ya3),
    GeneratorArgs(a, na1),
    GeneratorArgs(b, yb1),
    GeneratorArgs(b, yb2),
    GeneratorArgs(b, yn1),
]

exo_npsearch = ExerciseGenerator(
    npsearch, inputs_npsearch,
    nb_examples = 3,
    result_renderer=PPrintRenderer(width=15),
    header_font_size='150%',
    font_size='120%',
)
