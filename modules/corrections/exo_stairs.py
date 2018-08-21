import numpy as np

from nbautoeval.exercise_function import ExerciseFunctionNumpy
from nbautoeval.args import Args


# @BEG@ name=stairs
def stairs(k):
    """
    la pyramide en escaliers telle que décrite dans l'énoncé
    """
    # on calcule n
    n = 2 * k + 1
    # on calcule les deux tableaux d'indices
    # tous les deux de dimension n 
    ix, iy = np.indices((n, n))
    # il n'y a plus qu'à appliquer la formule qui va bien
    return 2 * k - (np.abs(ix - k) + np.abs(iy - k))
# @END@
    

# @BEG@ name=stairs
def stairs_bis(k):
    """
    Bien sûr on peut préciser le type mais ce n'est pas 
    réellement nécessaire ici
    """
    n = 2 * k + 1
    ix, iy = np.indices((n, n), dtype=np.int8)
    return 2 * k - (np.abs(ix - k) + np.abs(iy - k))
# @END@



def stairs_ko(k):
    n = 2 * k + 1
    ix, iy = np.indices((n, n), dtype=np.float)
    return (k - 1) + 2 * k - (np.abs(ix - k) + np.abs(iy - k))


stairs_inputs = [
    Args(1),
    Args(2),
    Args(3),
    Args(4),
]


exo_stairs = ExerciseFunctionNumpy(
    stairs,
    stairs_inputs,
    nb_examples = 2,
    )

