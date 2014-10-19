# -*- coding: iso-8859-15 -*-
from exercice import Exercice, Exercice_1arg, Exercice_multiline

##############################
# @BEG@ 4 4 aplatir
def aplatir (conteneurs):
    "retourne une liste des éléments des éléments de conteneurs"
    # on peut concaténer les éléments de deuxième niveau 
    # par une simple imbrication de deux compréhensions de liste
    return [element for conteneur in conteneurs for element in conteneur]
# @END@

aplatir_inputs = [
    [] ,
    [ (1,) ], 
    ( [1], ), 
    [ (0,6,2), [ 1, ('a',4), 5 ] ],
    ( [ 1, [2, 3] ] , ( 'a', 'b', 'c' ) ),
    ( [ 1, 6 ] , ( 'c', 'b'), [ 2, 3] ),
    ( ( 1, [2, 3] ) , [] , ( 'a' ) , [ 'b', 'c' ] ),
]

exo_aplatir = Exercice_1arg (aplatir, aplatir_inputs, exemple_how_many=0)

##############################
# @BEG@ 4 4 alternat
def alternat (l1, l2):
    "renvoie une liste des éléments pris un sur deux dans l1 et dans l2"
    # pour réaliser l'alternance on peut combiner zip avec aplatir
    # telle qu'on vient de la réaliser
    return aplatir (zip (l1,l2))
# @END@

alternat_inputs = [
    ( (1,2), ('a','b') ),
    ( (1,2,3), ('a','b','c') ),
    ( (1,(2,3)), ('a',['b','c']) ),
]

exo_alternat = Exercice (alternat, alternat_inputs, exemple_how_many=2)

##############################
# @BEG@ 4 4 intersect
def intersect (A,B):
    """
avec en entrée deux listes de tuples de la forme
(entier, valeur)
renvoie la liste des valeurs associées dans A ou B
aux entiers présents dans A et B
    """
    # une fonction qui renvoie l'ensemble des entiers
    # présent dans une des deux listes d'entrée
    def values (S):
        return { i for i,val in S}
    # on l'applique à A et B
    val_A = values (A)
    val_B = values (B)
    # les entiers présents dans A et B 
    # avec une intersection d'ensembles
    common_keys = val_A & val_B
    # et pour conclure on fait une union sur deux
    # compréhensions d'ensembles
    return { vala for a,vala in A if a in common_keys} \
         | { valb for b,valb in B if b in common_keys} 
# @END@

intersect_inputs = []

A1 = { (12,'douze'), (10,'dixA'), (8, 'huit'),}
B1 = { (5, 'cinq'), (10, 'dixB'), (15, 'quinze'),}
intersect_inputs.append ( (A1, B1) )

A2 = { (1,'unA'), (2,'deux'), (3, 'troisA') }
B2 = { (1,'unB'), (2,'deux'), (4, 'quatreB') }
intersect_inputs.append ( (A2, B2) )

exo_intersect = Exercice_multiline (intersect, intersect_inputs, ('A', 'B'), 
                                    exemple_columns = (55,30))
##############################
