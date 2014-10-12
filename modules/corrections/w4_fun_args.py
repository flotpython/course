# -*- coding: iso-8859-15 -*-
from exercice import Exercice, Exercice_1arg

##############################
def doubler_premier (f, *args):
    to_double = args[0]
    to_preserve = args [1:]
    return f ( 2 * to_double, *to_preserve)

doubler_premier_inputs = []
from operator import add
from operator import mul
import math
def distance (*args):
    return math.sqrt(sum(x**2 for x in args))

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
# NICETOHAVE
# le début d'un exo qui pourrait être sympa ou on prolonge l'exo précédent 
# au passage de variables avec défaut
# cela dit le framework d'exercice ne permet pas encore cela
# il faudrait pouvoir décrire les entrées comme un liste de 
# ( (tuple_positionnels), {dict: defaults} )
# ce qui demande pas mal de rework dans la classe Exercice
# standby for now
def doubler_premier_defs (f, *args, **keywords):
    to_double = args[0]
    to_preserve = args [1:]
    return f ( 2 * to_double, *to_preserve, **keywords)

##############################
def validation (f, g, argument_tuples):
    """
retourne une liste de booleens, un par entree dans entrees
qui indique si f(*tuple) == g(*tuple)
    """
    return [ f(*tuple) == g(*tuple) for tuple in argument_tuples ]

#################### les jeux de données
validation_inputs = []

########## dataset #1
from math import factorial
from operator import mul

# factoriel is still valid
fact_inputs = [(0,), (1,), (5,), ]

def fact (n):
    "une version de factoriel à base de reduce"
    return reduce (mul, range(1,n+1), 1)

validation_inputs.append ( (fact, factorial, fact_inputs) )

########## dataset #2
def broken_fact (n):
    return 0 if n <= 0 \
        else 1 if n == 1 \
             else n*fact(n-1)

validation_inputs.append ( (broken_fact, factorial, fact_inputs) )

########## dataset #3
from operator import add

# addition can work too
add_inputs = [ (2,3), (0,4), (4,5) ]

def plus (x1, x2): 
    return x1+x2

validation_inputs.append ( (add, plus, add_inputs) )

########## dataset #4
def plus_broken (x1, x2):
    if x1 != 0: 
        return x1 + x2
    else:
        return 1 + x2

validation_inputs.append ( (add, plus_broken, add_inputs) )

#################### the exercice instance
exo_validation = Exercice (validation, validation_inputs, 
                           correction_columns = (50,40,40))

