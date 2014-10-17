# -*- coding: iso-8859-15 -*-
from exercice import Exercice, Exercice_1arg, Exercice_multiline


# @BEG@ affichage
def affichage (s):
    s=s.replace(' ', '').replace('\t','')
    mots = s.split(',')
    if len (mots) < 2:
        return None
    prenom = mots.pop(0)
    nom = mots.pop(0)
    age = "??"
    if len(mots)>=2:
        age = mots.pop(1)
    return "N:>{}< P:>{}< A:>{}<".format(nom,prenom,age)
# @END@

inputs_affichage = [
    "Joseph, Dupont",
    "Jules , Durand, G123, 21",
    "Jean", 
    " Jacques , Martin, L119, \t24 ,",
    "Sheldon, Cooper ,",
    "Ted, Mosby, F321, ",
    "\t Sam, Does\t, F321, 23",
]

exo_affichage = Exercice_1arg (affichage, inputs_affichage,
                               correction_columns = (40,30,30),
                               exemple_columns = (40,40),
                               exemple_how_many = 3)

##############################
# @BEG@ carre
def carre (s):
    s=s.replace(' ', '').replace('\t','')
    entiers = [ int(token) for token in s.split(";") if token ]
    return ":".join ( [ "{}".format(entier**2) for entier in entiers ] )
# @END@

inputs_carre = [
    "1;2;3",
    " 2 ;  5;6;",
    "; 12 ;  -23;\t60; 1\t",
    "; -12 ; ; -23; 1 ;;\t",
]

exo_carre = Exercice_1arg (carre, inputs_carre)
