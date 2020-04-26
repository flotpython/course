from nbautoeval import Args, ExerciseFunction

####################
# @BEG@ name=laccess
def laccess(liste):
    """
    retourne un élément de la liste selon la taille
    """
    # si la liste est vide il n'y a rien à faire
    if not liste:
        return
    # si la liste est de taille paire
    if len(liste) % 2 == 0:
        return liste[-1]
    else:
        return liste[len(liste)//2]
# @END@


####################
# @BEG@ name=laccess more=bis
# une autre version qui utilise
# un trait qu'on n'a pas encore vu
def laccess_bis(liste):
    # si la liste est vide il n'y a rien à faire
    if not liste:
        return
    # l'index à utiliser selon la taille
    index = -1 if len(liste) % 2 == 0 else len(liste) // 2
    return liste[index]
# @END@


inputs_laccess = [
    Args([]),
    Args([1]),
    Args(['spam', 100]),
    Args(['spam', 100, 'bacon']),
    Args([1, 2, 3, 100]),
    Args([1, 2, 100, 4, 5]),
    Args(['si', 'pair', 'alors', 'dernier']),
    Args(['retourne', 'le', 'milieu', 'si', 'impair']),
]


exo_laccess = ExerciseFunction(
    laccess, inputs_laccess, nb_examples=0
)


def laccess_ko(liste):
    return liste[-1]

#################### le même code marche-t-il avec des strings ?
inputs_laccess_strings = [
    Args(""),
    Args("a"),
    Args("ab"),
    Args("abc"),
    Args("abcd"),
    Args("abcde"),
]

exo_laccess_strings = ExerciseFunction(
    laccess, inputs_laccess_strings
)
