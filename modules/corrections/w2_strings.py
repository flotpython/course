# -*- coding: iso-8859-15 -*-
from corrections.exercice import correction_table, correction_table_1arg, exemple_table, exemple_table_1arg

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

affichage_input_args = [
    "Joseph, Dupont",
    "Jules , Durand, G123, 21",
    "Jean", 
    " Jacques , Martin, L119, \t24 ,",
    "Sheldon, Cooper ,",
    "Ted, Mosby, F321, ",
    "\t Sam, Does\t, F321, 23",
]

def correction_affichage (affichage_student):
    return correction_table_1arg (affichage_student, affichage, affichage_input_args,
                                  columns=(40,30,30))

def exemple_affichage ():
    return exemple_table_1arg ('affichage',affichage, affichage_input_args, how_many=2,
                               columns= (40,40))

##############################
def carre (s):
    s=s.replace(' ', '').replace('\t','')
    entiers = [ int(token) for token in s.split(";") if token ]
    return ":".join ( [ "{}".format(entier**2) for entier in entiers ] )

carre_input_args = [
    "1;2;3",
    " 2 ;  5;6;",
    "; 12 ;  -23;\t60; 1\t",
    "; -12 ; ; -23; 1 ;;\t",
]

def correction_carre (carre_student):
    return correction_table_1arg (carre_student, carre, carre_input_args)

def exemple_carre ():
    return exemple_table_1arg ('carre', carre, carre_input_args)
