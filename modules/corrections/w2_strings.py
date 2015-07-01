# -*- coding: utf-8 -*-
from exercice_function import ExerciceFunction
from args import Args


# @BEG@ week=2 sequence=8 name=affichage
# un élève a remarqué très justement que ce code ne fait pas
# exactement ce qui est demandé, en ce sens qu'avec
# l'entrée correspondant à Ted Mosby on obtient A:><
# je préfère toutefois publier le code qui est en
# service pour la correction en ligne, et vous laisse
# le soin de l'améliorer si vous le souhaitez
def affichage(s):
    # pour ignorer les espaces et les tabulations 
    # le plus simple est de les enlever
    s=s.replace(' ', '').replace('\t','')
    # la liste des mots séparés par une virgule 
    # nous est donnée par un simple appel à split
    mots = s.split(',')
    # si on n'a même pas deux mots, on retourne None
    if len(mots) < 2:
        return None
    # maintenant qu'on sait qu'on a deux mots
    # on peut extraire le prénom et le nom
    prenom = mots.pop(0)
    nom = mots.pop(0)
    # on veut afficher "??" si l'âge est inconnu
    age = "??"
    # mais si l'âge est précisé dans la ligne
    if len(mots) >= 2:
        # alors on le prend
        age = mots.pop(1)
    # il ne reste plus qu'à formater
    return "N:>{}< P:>{}< A:>{}<".format(nom, prenom, age)
# @END@

inputs_affichage = [
    Args("Joseph, Dupont"),
    Args("Jules , Durand, G123, 21"),
    Args("Jean"), 
    Args("Ted, Mosby, F321, "),
    Args(" Jacques , Martin, L119, \t24 ,"),
    Args("Sheldon, Cooper ,"),
    Args("\t Sam, Does\t, F321, 23"),
]

exo_affichage = ExerciceFunction(
    affichage, inputs_affichage,
    correction_columns=(40, 40, 40),
    exemple_columns=(40, 40),
    exemple_how_many=4)

##############################
# @BEG@ week=2 sequence=8 name=carre
def carre(s):
    # on enlève les espaces et les tabulations
    s = s.replace(' ', '').replace('\t','')
    # la ligne suivante fait le plus gros du travail
    # d'abord on appelle split() pour découper selon les ';'
    # dans le cas où on a des ';' en trop, on obtient dans le 
    #    résultat du split un 'token' vide, que l'on ignore 
    #    ici avec le clause 'if token'
    # enfin on convertit tous les tokens restants en entiers avec int()
    entiers = [int(token) for token in s.split(";") if token]
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

exo_carre = ExerciceFunction(
    carre, inputs_carre, exemple_how_many=0)
