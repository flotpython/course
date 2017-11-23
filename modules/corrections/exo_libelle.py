# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args

##############################
# @BEG@ name=libelle
def libelle(ligne):
    # on enlève les espaces et les tabulations
    ligne = ligne.replace(' ', '').replace('\t','')
    # on cherche les 3 champs
    mots = ligne.split(',')
    # si on n'a pas le bon nombre de champs
    # rappelez-vous que 'return' tout court
    # est équivalent à 'return None'
    if len(mots) != 3:
        return
    # maintenant on a les trois valeurs
    nom, prenom, rang = mots
    # comment présenter le rang
    rang_ieme = "1er" if rang == "1" \
                else "2nd" if rang == "2" \
                else f"{rang}-ème"
    return f"{prenom}.{nom} ({rang_ieme})"
# @END@ ##########

def libelle_ko(ligne):
    try:
        nom, prenom, rang = ligne.split(',')
        return f"{prenom}.{nom} ({rang})"
    except:
        return None

inputs_libelle = [
    Args("Joseph, Dupont, 4"),
    Args("Jean"), 
    Args("Jules , Durand, 1"),
    Args(" Ted, Mosby, 2,"),
    Args(" Jacques , Martin, 3 \t"),
    Args("Sheldon, Cooper ,5,  "),
    Args("\t John, Doe\t, "),
    Args("John, Smith, , , , 3"),
]

exo_libelle = ExerciseFunction(
    libelle, inputs_libelle,
    nb_examples = 0,
    layout_args = (25, 25, 25),
    render_name = False,
)

