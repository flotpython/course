# -*- coding: iso-8859-15 -*-
from exercice import Exercice, Exercice_1arg, Exercice_multiline

##############################
def aplatir (conteneurs):
    "retourne une liste des éléments des éléments de conteneurs"
    return [element for conteneur in conteneurs for element in conteneur]

aplatir_inputs = [
    [ (0,1,2), [ (3,4), 5 ] ],
    ( [ 1, [2, 3] ] , ( 'a', 'b', 'c' ) ),
]

exo_aplatir = Exercice_1arg (aplatir, aplatir_inputs)

##############################
def alternat (l1, l2):
    return aplatir (zip (l1,l2))

alternat_inputs = [
    ( (1,2), ('a','b') ),
    ( (1,2,3), ('a','b','c') ),
    ( (1,(2,3)), ('a',['b','c']) ),
]

exo_alternat = Exercice (alternat, alternat_inputs, exemple_how_many=2)

##############################
def intersect (A,B):
    # l'ensemble des entiers dans un des ensembles
    def values (S):
        return { i for i,val in S}
    val_A = values (A)
    val_B = values (B)
    common_keys = val_A & val_B
    return { vala for a,vala in A if a in common_keys} \
         | { valb for b,valb in B if b in common_keys} 

intersect_inputs = []

A1 = { (12,'douze'), (10,'dixA'), (8, 'huit'),}
B1 = { (5, 'cinq'), (10, 'dixB'), (15, 'quinze'),}
intersect_inputs.append ( (A1, B1) )

A2 = { (1,'unA'), (2,'deux'), (3, 'troisA') }
B2 = { (1,'unB'), (2,'deux'), (4, 'quatreB') }
intersect_inputs.append ( (A2, B2) )

exo_intersect = Exercice_multiline (intersect, intersect_inputs, ('A', 'B'), exemple_columns = (50,30))
##############################
