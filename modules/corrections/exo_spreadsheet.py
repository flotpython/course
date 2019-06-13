from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args

# @BEG@ name=spreadsheet
def int_to_char(n):
    """
    traduit un entier entre 1 et 26 
    en un caractère entre 'A' et 'Z'
    """
    # si index était compris entre 0 et 25, on pourrait obtenir
    # la lettre comme étant chr(ord('A') + index)
    # on fait donc un changement de variable n -> n-1
    # de plus on va rendre le résultat cyclique modulo 26
    # pour pouvoir l'utiliser sur des nombres quelconques

    return chr(ord('A') + (n - 1) % 26)


def spreadsheet(index):
    """
    transforme un numéro de colonne en nom alphabétique
    dans l'ordre lexicographique
    1 -> A; 26 -> Z; 27 -> AA; 28 -> AB; etc..
    """
    # index peut être supérieur à 26
    # en remarquant que la dernière lettre s'incrémente à chaque fois 
    # qu'index augmente, et repasse à 'A' de manière cyclique, 
    # on voit qu'on peut utiliser notre version cyclique de `int_to_char` 
    # pour calculer la lettre la plus à droite dans le résultat.
    # et pour les autres lettres, il suffit de recommencer sur le quotient 

    result = int_to_char(index)
    while index > 26:
        index = (index - 1) // 26
        result = int_to_char(index) + result
    return result
# @END@


# si on veut montrer plusieurs versions dans les corrections
# on peut faire comme ceci

# @BEG@ name=spreadsheet more=bis
def spreadsheet_bis(index):
    """
    Accessoirement on peut vérifier que la variable index fournie
    est bien un entier supérieur à 0.
    """
    if not isinstance(index, int):
        raise TypeError("index must be an integer !")
    elif index < 1:
        raise ValueError("index must be positive !")

    result = chr(ord('A') + (index - 1) % 26)
    while index > 26:
        index = (index - 1) // 26
        result = chr(ord('A') + (index - 1) % 26) + result
    return result
# @END@

z   = 26
zz  =  26**2 + 26
zzz = 26**3 + 26**2 + 26

numeric_inputs = (
    1, 15, z, z+1, zz-1, zz, zz+1, zz+2, zzz-1, zzz, zzz+1, zzz+2, 26**2-1,
    30_000, 100_000, 1_000_000,
)

# l'objet Args permet de capturer les arguments
# pour un appel à la fonction
spreadsheet_inputs = [Args(n) for n in numeric_inputs]

exo_spreadsheet = ExerciseFunction(
    spreadsheet, spreadsheet_inputs, nb_examples=7,
)


def spreadsheet_ko(n):
    if 1 <= n <= 26:
        return int_to_char(n)
    else:
        return spreadsheet_ko(n//26) + int_to_char(n)
