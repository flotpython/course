from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args

# @BEG@ name=spreadsheet
def int_to_char(n):
    return chr(ord('A') + (n - 1) % 26)

def spreadsheet(index):
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

numeric_inputs = (
    1, 15, 26, 27, 26*27, 26*27+1, 1000, 200, 26**2-1,
    30_000, 100_000, 1_000_000
)

# l'objet Args permet de capturer les arguments
# pour un appel à la fonction
spreadsheet_inputs = [Args(n) for n in numeric_inputs]

exo_spreadsheet = ExerciseFunction(
    spreadsheet, spreadsheet_inputs, nb_examples=6
)
