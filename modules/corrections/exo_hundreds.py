# pylint: disable=c0111
import numpy as np

from nbautoeval.exercise_function import ExerciseFunctionNumpy
from nbautoeval.args import Args


# @BEG@ name=hundreds
def hundreds(lines, columns, offset):
    """
    Fabrique un tableau lines x columns où:

    tab[i, j] = 100 * i + 10 * j + offset
    """
    # avec indices(), on a directement
    # deux tableaux prêts à être broadcastés
    indx, indy = np.indices((lines, columns))
    return 100*indx + 10*indy + offset
# @END@


# @BEG@ name=hundreds more=bis
def hundreds_bis(lines, columns, offset):
    """
    ditto
    """
    ### à nouveau à base de broadcasting, mais cette fois
    ### on se fabrique soi-même la souche
    ### de la ligne et de la colonne
    # une colonne 0, 1, .. lines-1
    column = np.arange(lines)[:, np.newaxis]
    # une ligne 0, 1, ... columns-1
    line = np.arange(columns)
    # il n'y a plus qu'à broadcaster les deux
    # attention toutefois que c'est column qui contient
    # les indices en i
    return 100*column + 10*line + offset
# @END@


# @BEG@ name=hundreds more=ter
def hundreds_ter(lines, columns, offset):
    """
    encore
    """
    # à la Fortran; ça n'est pas forcément
    # la bonne approche ici bien sûr
    # mais si un élève a des envies de benchmarking...
    result = np.zeros(shape=(lines, columns), dtype=int)
    for i in range(lines):
        for j in range(columns):
            result[i, j] = 100 * i + 10 * j + offset
    return result
# @END@


def hundreds_ko(lines, columns, offset):
    result = np.ones(shape=(lines, columns), dtype=float)
    return result


hundreds_inputs = [
    Args(2, 4, 0),
    Args(3, 3, 1),
]


exo_hundreds = ExerciseFunctionNumpy(
    hundreds,
    hundreds_inputs,
    nb_examples=2,
    )
