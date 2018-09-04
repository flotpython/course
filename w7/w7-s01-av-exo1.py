# Commençons par créer une liste de 1000 éléments et un tableau numpy de 1000 éléments. 
# Nous reviendrons largement sur les tableaux numpy, l'objectif ici est de vous montrer le
# la gain de performance pour faire une même opération en Python et en numpy.

import numpy as np
L = list(range(1_000))
a = np.array(L)

# regardons si ces deux objets contiennent la même chose

all(L == a) # va comparer élément pas élément

# maintenant, comparons le temps pour élever au carré chaque élément
%timeit [x**2 for x in L]
%timeit [x**2 for x in a]

# la même compréhension sur un tableau numpy est 30% plus rapide que sur une liste
# Mais en réalité, en numpy on utilise un principe que l'on appelle la vectorization et qui
# n'existe pas sur les builtins Python. C'est avec la vectorization que l'on obtient le vrai
# gain de performance

%timeit a**2  #vectorisation

# sur ce simple exemple, on gagne un facteur 200. 

# Vérifions tout de même que ces deux opérations donnent le même résultat

all(a**2 == [x**2 for x in L])

# Mais alors quel est le prix à payer pour ce gain majeur de performance ?

# Vous noterez que les les tableaux numpy supportent le protocol d'itération. 
# On peut faire des boucles for ou des compréhensions. Mais le vrai gain de 
# performance apparait lorsqu'on utilise un nouveau concept à apprendre 
# et maitriser, la vectorization. Nous verrons que vous aurez à apprendre
# plusieurs nouveaux concepts pour maitriser numpy.
#
# Il a d'autres prix à payer, notamment la perte de souplesse, l'absence d'exception sur 
# certaines opérations fautives, et des conversions de type implicite.  
 # nous reviendrons largement sur ces pièges dans la suite.  
 
# Nous voyons donc que le gain de performance est majeur, en général de
# l'ordre de 100 fois plus rapide. On obtient essentiellement
# l'efficacité d'un code écrit en C. Par contre, on sort de la
# philosophie de Python, et on doit donc être très prudent et toujours
# parfaitement comprendre le code que l'on écrit. 

