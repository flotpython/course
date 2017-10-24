# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args

##############################
# @BEG@ name=aplatir
def aplatir(conteneurs):
    "retourne une liste des éléments des éléments de conteneurs"
    # on peut concaténer les éléments de deuxième niveau 
    # par une simple imbrication de deux compréhensions de liste
    return [element for conteneur in conteneurs for element in conteneur]
# @END@

def aplatir_ko(conteneurs):
    return conteneurs

aplatir_inputs = [
    Args([]),
    Args([(1,)]), 
    Args(([1],)), 
    Args([(0, 6, 2), [1, ('a', 4), 5]]),
    Args(([ 1, [2, 3]], ('a', 'b', 'c'))),
    Args(([ 1, 6 ], ('c', 'b'), [2, 3])),
    Args((( 1, [2, 3]), [], ('a'), ['b', 'c'])),
]

exo_aplatir = ExerciseFunction(
    aplatir, aplatir_inputs, nb_examples=0)

##############################
# @BEG@ name=alternat
def alternat(l1, l2):
    "renvoie une liste des éléments pris un sur deux dans l1 et dans l2"
    # pour réaliser l'alternance on peut combiner zip avec aplatir
    # telle qu'on vient de la réaliser
    return aplatir(zip(l1, l2))
# @END@

alternat_inputs = [
    Args((1, 2), ('a', 'b') ),
    Args((1, 2, 3), ('a', 'b', 'c')),
    Args((1, (2, 3)), ('a', ['b', 'c'])),
]

# @BEG@ name=alternat more=bis
def alternat_bis(l1, l2):
    "une deuxième version de alternat"
    # la même idée mais directement, sans utiliser aplatir
    return [element for conteneur in zip(l1, l2) for element in conteneur]
# @END@

def alternat_ko(l1, l2):
    return l1 + l2

exo_alternat = ExerciseFunction(
    alternat, alternat_inputs, nb_examples=2)

##############################
# @BEG@ name=intersect
def intersect(A, B):
    """
    prend en entrée deux listes de tuples de la forme
    (entier, valeur)
    renvoie la liste des valeurs associées dans A ou B
    aux entiers présents dans A et B
    """
    # pour montrer un exemple de fonction locale:
    # une fonction qui renvoie l'ensemble des entiers
    # présents dans une des deux listes d'entrée
    def keys(S):
        return {k for k, val in S}
    # on l'applique à A et B
    keys_A = keys(A)
    keys_B = keys(B)
    # 
    # les entiers présents dans A et B 
    # avec une intersection d'ensembles
    common_keys = keys_A & keys_B
    # et pour conclure on fait une union sur deux
    # compréhensions d'ensembles
    return {vala for k, vala in A if k in common_keys} \
         | {valb for k, valb in B if k in common_keys} 
# @END@

def intersect_ko(A, B):
    A_vals = { v for k, v in A }
    B_vals = { v for k, v in B }
    return A_vals & B_vals
    
intersect_inputs = []

A1 = {(12, 'douze'), (10, 'dixA'), (8, 'huit'),}
B1 = {(5, 'cinq'), (10, 'dixB'), (15, 'quinze'),}
intersect_inputs.append(Args(A1, B1))

A2 = {(1, 'unA'), (2, 'deux'), (3, 'troisA')}
B2 = {(1, 'unB'), (2, 'deux'), (4, 'quatreB')}
intersect_inputs.append(Args(A2, B2))

exo_intersect = ExerciseFunction(
    intersect, intersect_inputs, nb_examples=2)
##############################
