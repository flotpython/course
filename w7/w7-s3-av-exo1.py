# Commençons par créer un tableau 3x3 d'entiers choisis au hasard. 
# Numpy permet de faire cela avec la méthod random.randint

import numpy as np
a = np.random.randint(1, 10, size=(3,3))
print(a)

# Il y a ici quelque chose d'agaçant qui est typique du manque de 
# maturité de numpy, on spécifie la forme, non pas avec l'argument shape
# comme on le ferait pour les méthodes zeros ou ones, mais avec l'argument
# size. 

# Je peux sur un tableau utiliser la notion de slice sur chaque dimension 
# avec les même conventions que sur une liste, je vais de i inclus à j exclus
# par pas de k

a[1:, :2]

# Il y a cependant une différence majeur avec les slices sur les séquences. 
# Les slices sur les tableaux numpy retournent des vues et non des shallow copie. 
# Le coût mémoire d'un slice d'un tableau est donc marginal. 

# Regardons cela

b = a[1:, :2]
print(b)

# maintenant, je change l'élément central dans a
a[1, 1] = 35

# et on voit que b est bien mis à jour. 

# 2m20


# On peut également redimensionner un tableau avec la méthode reshape. 
# De nouveau, cette méthode retourne une vue et non un nouveau tableau. 

a = np.random.randint(1, 10, size=(4,4))
print(a)

# attention, on ne peut faire un reshape que si la nouvelle
# forme contient le même nombre d'éléments que 
# le tableau original, c'est-à-dire le produit des dimensions
# est égal. 
b = a.reshape(8, 2)
print(b)
a[0, 0] = 100
print(b)

# 3m30

# Nous allons maintenant parler  la notion de tableau de booléens. 
# Prenons un  exemple, supposons que l'on ait un tableau des températures
# du mois de mars, le températures allant de -5 à 20 dégrés

mars = np.random.randint(-5, 20, size=31)
print(mars)

# maintenant, regardons quelles températures sont strictement positives

mars > 0

# l'opérateur de comparaison va appliquer la comparaison à 
# chaque élément du tableau et générer un tableau de booléen 
# de même dimension qui est mis à True si la comparaison est 
# vraie  et False sinon

# On peut utiliser les opérateurs <, <=, >, >=, ==, != pour générer d'autres
# tableaux de booléens. 

mars == 0

mars <= 10

# 5m00

# Mais vous devez vous demander à quoi sert d'avoir un tableau de booléens. 
# si vous vous souvenez que False vaut 0 et True vaut 1, vous pouvez 
# maintenant répondre aux questions suivantes

# combien de jours il a fait une température positive en mars
np.sum(mars>0)

# est-ce qu'il y a au moins un jour où il a fait 20 degré
np.any(mars==20)

# est-ce qu'il a fait une température positive tous les jours?
np.all(mars>0)

# 6m40

# on peut combiner les tableaux booléens avec les opérateurs bitwise. 
# Attention, comme il s'agit de tableaux de bits, on ne peut pas directement
# utiliser les opérateurs logique de Python and or et not, mais uniquement
# les opérateurs bitwise. Regardons un exemple

# créons un tableaux des jours du mois de mars
jours_mars = np.arange(1, len(mars)+1, dtype=np.int8)

# je peux maintenant calculer le nombre de jours où il a fait plus de 
# 10 dégrés à partir du 15 mars. Attention aux règles de priorité des opérateurs, 
# pour faire ce que l'on souhaite, il faut toujours mettre en paranthèses 
# les expressions à gauche et à droite de l'opérateur

np.sum((mars>10) & (jours_mars>=15)) # attention aux parenthèses

# 8m50

# Maintenant qu'on connait les tableaux de booléens que l'on appelle 
# également mask, on peut les appliquer 
# pour faire de l'indexation avancée. Lorsque l'on passe un mask
# comme indice d'un tableau, on va obtenir un nouveau tableau qui ne contient
# que les éléments pour lequels le mask est à True. Attention, il ne s'agit
# plus d'une vue contrairement aux slices, mais d'un nouveau tableau. 

mars[mars>10]

mars[(mars>10) & (jours_mars>=15)]

# cette notion de mask permet de filtrer de manière très expressive les tableaux. 
# on peut également faire des affectations sur un tableau qui a pour indices un mask.

#9m30

# supposons que l'on sache que les température négative soit des erreurs de mesure, 
#  et que l'on souhaite remplacer toutes les températures négative par
# la température moyenne (hors température négative). On pourra faire ça de la manière
# suivante

moy = np.mean(mars[mars>=0])
mars[mars<0] = moy
print(mars)

#11m00

# Pour finir, on peut également passer comme indice un tableau ou une liste d'entiers 
# (mais pas un tuple qui est réservé pour désigner un élément dans un tableau à plusieurs
# dimension). Dans ce cas, cela va produire un nouveau tableau qui va 
# contenir les éléments spécifiés dans la séquence d'entier. 

countries = np.array(['fr', 'us', 'jp'])
countries[[0, 0, 1, 2, 0]] # deux fois fr, puis us, puis, jp, puis fr

#12m00