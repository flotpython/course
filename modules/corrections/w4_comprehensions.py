# -*- coding: iso-8859-15 -*-
from corrections.tools import correction_table, correction_table_1arg, exemple_table, exemple_table_1arg, exemple_table_args

##############################
def aplatir (listes):
    return [x for liste in listes for x in liste]

inputs_aplatir = [
    [ (0,1,2), [ (3,4), 5 ] ],
    ( [ 1, [2, 3] ] , ( 'a', 'b', 'c' ) ),
]

def correction_aplatir (student_aplatir):
    return correction_table_1arg (student_aplatir, aplatir, inputs_aplatir)
def exemple_aplatir ():
    return exemple_table_1arg ("aplatir", aplatir, inputs_aplatir, columns =(40,40), how_many=2)

##############################
def alternat (l1, l2):
    return aplatir (zip (l1,l2))

inputs_alternat = [
    ( (1,2), ('a','b') ),
    ( (1,2,3), ('a','b','c') ),
    ( (1,(2,3)), ('a',['b','c']) ),
]

def exemple_alternat ():
    return exemple_table ("alternat",alternat,inputs_alternat,how_many=2)

def correction_alternat (student_alternat):
    return correction_table (student_alternat, alternat, inputs_alternat)

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

def correction_intersect (student_intersect):
    return correction_table (student_intersect, intersect, intersect_inputs)

def exemple_intersect ():
    return exemple_table_args ("intersect", ("A","B"), intersect, intersect_inputs,
                               columns=(50,30))

##############################
