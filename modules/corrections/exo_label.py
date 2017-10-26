# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


inputs_label = [
    Args( 'Rémi', 10  ),
    Args( 'Marie', 17 ),
    Args( 'Kevin', 8  ),
    Args( 'Jean', 14  ),
]

def label(prenom, note):
    if note < 10:
        return f"{prenom} est recalé"
    elif note < 16:
        return f"{prenom} est reçu"
    else:
        return f"félicitations à {prenom}"

exo_label = ExerciseFunction(
    label, inputs_label, nb_examples=3,
)
