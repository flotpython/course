from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


# @BEG@ name=longest_gap
def longest_gap(liste):
    result = 0
    begins = {}
    for index, item in enumerate(liste):
        if item not in begins:
            begins[item] = index
        else:
            result = max(result, index - begins[item])
    return result
# @END@ 


inputs = [
    Args([1, 2, 3, 1, 4, 10, 4, 3, -1, 4]),
    Args(["yes", "no", None, "yes", "no"]),
    Args([1, 2, 3, 4]),
]

exo_longest_gap = ExerciseFunction(
    longest_gap,
    inputs,
    nb_examples=0,
    layout_args=(50, 5, 5),
)