# commençons par créer deux tableaux
import numpy as np
a = np.array([1, 2, 3])
b = np.array([5, 5, 5])

# et calculons le produit ce ces deux tableaux
a * b

# numpy fait une simple multiplication sur élément par élément

# maintenant faisont l'opération suivante

c = np.array([5])
a * c

# on obtient le même résultat. En fait, numpy a fait une opération de broadcasting. 
# broadcast veut dire diffusion, on peut voir cette opération comme si numpy 
# avait diffusée la valeur 5 sur 3 case d'un tableau pour que le tableau c ait la même
# taille que le tableau a. 

# Un clef du broadcasting est que c'est fait sans  créer un nouveau tableau pour c, 
# c'est donc économe en memoire, et c'est fait en faisant de la vectorisation, 
# c'est donc rapide. 

# Dans le cas que l'on vient de voir, il n'est pas nécessaire de créer un tableau
# pour une seule valeur, on peut directement faire l'opération avec un nombre

a * 5
