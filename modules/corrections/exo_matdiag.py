from nbautoeval import Args, ExerciseFunctionNumpy

# xxx JeF29
def matdiag(liste):
    return np.eye(len(liste), dtype=np.float64) * liste


# @BEG@ name=matdiag
import numpy as np

def matdiag(liste):
    """
    si les arguments sont x1, x2, .. xn
    retourne une matrice carrée n x n
    dont les éléments valent
    m[i, j] = xi si i == j
    m[i, j] = 0 sinon

    credit: JeF29
    """
    # on crée une matrice diagonale unité avec np.eye
    # (car I se prononce comme eye en anglais)
    # et on la multiplie par broadcasting avec un vecteur
    # composé de nos arguments
    # on la crée de type `int64` de façon à obtenir
    # pour le résultat final un type entier, flottant
    # ou complexe, selon les valeurs dans liste
    return np.eye(len(liste), dtype=np.int64) * liste
# @END@

# @BEG@ name=matdiag more=2
def matdiag_2(liste):
    """
    même propos mais cette fois avec du slicing
    """
    #
    # on initialise un tableau de la bonne taille n x n
    # mais tout à plat, avec des zéros
    # ici si on veut que ça marche avec des complexes,
    # il faut alors créer tout de suite le tableau de type
    # complexe, sinon on n'a pas la place
    n = len(liste)
    plat = np.zeros((n * n,), dtype=np.complex)
    #
    # dans cette représentation là, la diagonale correspond
    # à un slice qui commence à 1 avec un pas de n+1
    plat[0 : : n+1] = liste
    #
    # maintenant on peut remettre
    # dans une forme n x n avec reshape
    #
    return plat.reshape((n, n))
# @END@

# @BEG@ name=matdiag more=3
def matdiag_3(liste):
    """
    bon maintenant qu'on s'est bien creusé les méninges
    pour le faire à la main, il se trouve qu'il y a
    - bien sûr - une fonction pour ça dans numpy
    """
    return np.diag(liste)
# @END@

def matdiag_ko(liste):
    # presque ça mais sans le reshape
    n = len(liste)
    return np.zeros((n, n))

inputs_matdiag = [
    Args([1]),
    Args([1, 2j]),
    Args([1, 2.5, 4]),
    Args([0, 1, 2, 4, 8]),
]

exo_matdiag = ExerciseFunctionNumpy(
    matdiag, inputs_matdiag,
    nb_examples = 3,
)
