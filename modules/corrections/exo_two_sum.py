from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


# @BEG@ name=two_sum
def two_sum(liste, target):
    for i, item1 in enumerate(liste):
        for j, item2 in enumerate(liste):
            if j <= i:
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
    layout_args=(50, 15, 15),
)