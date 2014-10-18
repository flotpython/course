# -*- coding: iso-8859-15 -*-
from exercice import ExerciceKeywords, Exercice

##############################
# @BEG@ 4 8 distance
def distance (*args):
    return math.sqrt(sum(x**2 for x in args)) if args else 0.
# @END@

distance_inputs = [
    (),
    (1,),
    (1,1),
    (1,1,1),
    (1,1,1,1),
]

exo_distance = Exercice (distance, distance_inputs, exemple_how_many = 3)

##############################
# @BEG@ 4 8 doubler_premier
def doubler_premier (f, first, *args):
    return f ( 2 * first, *args)
# @END@

# marche aussi mais moins élégant
def doubler_premier_bis (f, *args):
    first = args[0]
    remains = args[1:]
    return f ( 2*first, *remains)

doubler_premier_inputs = []
from operator import add
from operator import mul
import math

# pour l'exemple on choisit les 3 premiers avec des fonctions différentes
for i in [1]: 
    doubler_premier_inputs.append ( [add, i, 2] )
    doubler_premier_inputs.append ( (mul, i, 2) )
doubler_premier_inputs.append ( (distance, 1, 1, 1) )
doubler_premier_inputs.append ( (distance, 2, 2, 2, 2) )
doubler_premier_inputs.append ( (distance, 3, 3, 3, 3, 3) )
for i in [3,5]: 
    doubler_premier_inputs.append ( [add, i, 2] )
    doubler_premier_inputs.append ( (mul, i, 2) )

exo_doubler_premier = Exercice (doubler_premier, doubler_premier_inputs, exemple_how_many=4)

##############################
# @BEG@ 4 8 doubler_premier2
def doubler_premier2 (f, first, *args, **keywords):
    return f ( 2 * first, *args, **keywords)
# @END@

def addn (x, y=0):
    return x+y

def muln (x=1, y=1):
    return x+y

doubler_premier2_inputs = []
dataset = ( (addn,1), dict(y=2));       doubler_premier2_inputs.append (dataset)
dataset = ( (muln,1), dict(y=2));       doubler_premier2_inputs.append (dataset)

# remettre les datasets de doubler_premier
doubler_premier2_inputs += [ (arguments, {}) for arguments in doubler_premier_inputs ]

dataset = ( (addn,1,2), dict());        doubler_premier2_inputs.append (dataset)
dataset = ( (muln,1,2), dict());        doubler_premier2_inputs.append (dataset)
dataset = ( (addn,1), dict());          doubler_premier2_inputs.append (dataset)
dataset = ( (muln,1), dict());          doubler_premier2_inputs.append (dataset)

exo_doubler_premier2 = ExerciceKeywords (doubler_premier2, doubler_premier2_inputs,
                                         exemple_how_many = 5)
##############################
# @BEG@ 4 8 validation2
def validation2 (f, g, argument_tuples):
    """
retourne une liste de booleens, un par entree dans entrees
qui indique si f(*tuple) == g(*tuple)
    """
    return [ f(*tuple) == g(*tuple) for tuple in argument_tuples ]
# @END@

#################### les jeux de données
validation2_inputs = []

########## dataset #1
from math import factorial
from operator import mul

# factoriel is still valid
fact_inputs = [(0,), (1,), (5,), ]

def fact (n):
    "une version de factoriel à base de reduce"
    return reduce (mul, range(1,n+1), 1)

validation2_inputs.append ( (fact, factorial, fact_inputs) )

########## dataset #2
def broken_fact (n):
    return 0 if n <= 0 \
        else 1 if n == 1 \
             else n*fact(n-1)

validation2_inputs.append ( (broken_fact, factorial, fact_inputs) )

########## dataset #3
from operator import add

# addition can work too
add_inputs = [ (2,3), (0,4), (4,5) ]

def plus (x1, x2): 
    return x1+x2

validation2_inputs.append ( (add, plus, add_inputs) )

########## dataset #4
def plus_broken (x1, x2):
    if x1 != 0: 
        return x1 + x2
    else:
        return 1 + x2

validation2_inputs.append ( (add, plus_broken, add_inputs) )

#################### the exercice instance
exo_validation2 = Exercice (validation2, validation2_inputs, 
                            correction_columns = (50,40,40))

