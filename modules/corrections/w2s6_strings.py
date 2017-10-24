# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args

### XXX
# un étudiant de la saison 2 a fait remarquer qu'on était trop laxiste
# avec par exemple en entrée
# John, Smith, , , , 3
# on ne se plaint pas
# la solution proposée par l'étudiant
## l = ligne.replace(" ","").replace("\t","").split(',')
## if (len(l) < 3):
##     return None
## if (len([x for x in l[3:] if x]) != 0):
##     return None

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
    # comment presenter le rang
    msg_rang = "1er" if rang == "1" \
               else "2nd" if rang == "2" \
                    else "{}-ème".format(rang)
    return f"{prenom}.{nom} ({msg_rang})"
# @END@ ##########

def libelle_ko(ligne):
    try:
        nom, prenom, rang = ligne.split(',')
        return "{prenom}.{nom} ({rang})"\
            .format(**locals())
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

##############################
# @BEG@ name=carre
def carre(s):
    # on enlève les espaces et les tabulations
    s = s.replace(' ', '').replace('\t','')
    # la ligne suivante fait le plus gros du travail
    # d'abord on appelle split() pour découper selon les ';'
    # dans le cas où on a des ';' en trop, on obtient dans le 
    #    résultat du split un 'token' vide, que l'on ignore 
    #    ici avec le clause 'if token'
    # enfin on convertit tous les tokens restants en entiers avec int()
    entiers = [int(token) for token in s.split(";")
               # en éliminant les entrées vides qui correspondent
               # à des point-virgules en trop
               if token]
    # il n'y a plus qu'à mettre au carré, retraduire en strings,
    # et à recoudre le tout avec join et ':'
    return ":".join([str(entier**2) for entier in entiers])
# @END@

inputs_carre = [
    Args("1;2;3"),
    Args(" 2 ;  5;6;"),
    Args("; 12 ;  -23;\t60; 1\t"),
    Args("; -12 ; ; -23; 1 ;;\t"),
]

exo_carre = ExerciseFunction(
    carre, inputs_carre,
    nb_examples=0,
    layout_args = (40, 20, 20)
    )


