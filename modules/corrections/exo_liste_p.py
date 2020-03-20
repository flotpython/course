from nbautoeval import Args, ExerciseFunction, PPrintCallRenderer, PPrintRenderer

# @BEG@ name=liste_P
def P(x):
    return 2 * x**2 - 3 * x - 2

def liste_P(liste_x):
    """
    retourne la liste des valeurs de P 
    sur les entrées figurant dans liste_x
    """
    return [P(x) for x in liste_x]
# @END@


# @BEG@ name=liste_P more=bis
# On peut bien entendu faire aussi de manière pédestre
def liste_P_bis(liste_x):
    liste_y = []
    for x in liste_x:
        liste_y.append(P(x))
    return liste_y
# @END@


inputs_liste_P = [
    Args(list(range(5))),
    Args(list(range(-7, 8, 2))),
    Args([-100, 0, 100]),
]


exo_liste_P = ExerciseFunction(
    liste_P,
    inputs_liste_P,
    call_renderer=PPrintCallRenderer(width=40, show_function=False),
    result_renderer=PPrintRenderer(width=25),
)


def liste_P_ko(liste):
    return [P(liste[0])]


