# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


inputs_label = [
    Args( 'Rémi', 10  ),
    Args( 'Marie', 17 ),
    Args( 'Kevin', 8  ),
    Args( 'Jean', 14  ),
]

# @BEG@ name=label
def label(prenom, note):
    if note < 10:
        return f"{prenom} est recalé"
    elif note < 16:
        return f"{prenom} est reçu"
    else:
        return f"félicitations à {prenom}"
# @END@


# @BEG@ name=label more=bis
def label_bis(prenom, note):
    if note < 10:
        return f"{prenom} est recalé"
    # on n'en a pas vraiment besoin ici, mais
    # juste pour illustrer cette construction
    elif 10 <= note < 16:
        return f"{prenom} est reçu"
    else:
        return f"félicitations à {prenom}"
# @END@


# @BEG@ name=label more=ter
# on n'a pas encore vu l'expression conditionnelle
# et dans ce cas précis ce n'est pas forcément une
# idée géniale, mais pour votre curiosité on peut aussi
# faire comme ceci
def label_ter(prenom, note):
    return f"{prenom} est recalé" if note < 10 \
    else f"{prenom} est reçu" if 10 <= note < 16 \
    else f"félicitations à {prenom}"
# @END@



exo_label = ExerciseFunction(
    label, inputs_label, nb_examples=3,
)
