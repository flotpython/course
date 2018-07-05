# commençons par créer un tableau d'entier
import numpy as np
a = np.arange(1000)

# La manière standard d'obtenir le carre de chaque 
# élément serait en Python de faire une compréhension
# regardons le temps d'exécution de cette opération

%timeit [x**2 for x in a]

# La bonne manière avec les tableaux numpy de faire ce 
# type d'opérations est d'utiliser la vectorisation. 

# La vectorisation consiste à appliquer une opération à chaque
# élément d'un tableau en exploitant le fait que le tableau
# est une zone de mémoire contiguë et que tous les éléments
# du tableau ont le même type et la même taille. Cela permet 
# une accélération majeur de l'opération. 

# Tous les opérateurs numériques sont vectorisé en numpy, on peut
# donc simplement obtenir le carré de chaque élément d'un tableau
# de la manière suivante

%timeit -r 1 a**2

# On voit que le gain de performance est de l'ordre de 150

# évidemment je peux comparer que j'obtiens bien le même résultat
# en faisant 
np.all(a**2 == [x**2 for x in a])

#2m00

# Le opérateur d'opération numérique (+, -, *, /, etc.), 
# les opérateurs de comparaison (<, >, ==, etc.)
# et les opérateurs bitwise (&, |, etc.) sont vectorisés. 

# De plus, chaque opérateur est associé à une fonction numpy
# que l'on appelle une fonction universelle ou ufunc. 
# par exemple l'opérateur ** est associé à la fonction np.power()
# et l'opérateur + à la fonction np.add()

np.all(a**2 == np.power(a, 2))

# On peut donc utiliser soit l'opérateur soit la fonction universelle. On 
# utilise en général directement l'opérateur, sauf si l'on a besoin
# d'utiliser un argument spécifique qui n'est disponible que par
# l'intermédiaire de la fonction universelle. 
# Notons qu'il existe un grand nombre  de fonctions 
# universelles qui ne sont pas lié à un opérateur, comme les
# fonction trigonométrique ou les fonctions logarithmes. 
# On vous donnera une liste dans les compléments. 

#3m30

# un argument important des fonctions universelle est l'arguement 
# out. Il permet de spécifier dans quel tableau le résultat de la fonction
# doit être écrit. Si on ne spécifie pas out, un nouveau tableau sera 
# créé pour le résultat. En spécifiant out, on peut utiliser un tableau
# existant et donc économiser le temps de création du nouveau tableau
# et surtout l'espace mémoire d'un nouveau tableau
# regardons cela

# Un usage classique est de réécrire dans le tableau original

a = np.arange(1, 1_000_000, dtype=np.float64)
%timeit -r 1 -n 1 np.sqrt(a)
%timeit -r 1 -n 1 np.sqrt(a, out=a)

#5m30

# Toutes les ufunc ont une méthode at qui permet d'appliquer 
# l'opération à un sous ensemble des éléments et d'écrire en place
a[:5]
np.log.at(a, [2, 4])
a[:5]

#6m30

# pour finir, notons qu'il existe en numpy beaucoup d'autres fonctions qui 
# exploite la vectorisation, mais qui ne sont pas des ufunc. D'une manière
# générale, en numpy, vous devez  éviter d'utiliser le protocol d'itération
# classique et donc éviter de faire des boucles for ou des compréhension. 

# Nous avons vu que les ufunc appliquaient une opération à chaque élément 
# d'un tableau. Il n'y a dans ce cas, pas de notion de dimension du tableau.
# Un certain nombre de fonctions vectorisée prennent en compte les dimensions
# regardons un exemple

a = np.arange(1, 10).reshape(3, 3)

np.sum(a) # calcul la somme de tous les éléments
# calcul la somme le long des lignes, c'est-à-dire qu'on fait
# la somme des éléments de la première colonne, puis de 
# la deuxième et de la troisième.
np.sum(a, axis=0) 
# calcul la somme le long des colonnes, c'est-à-dire qu'on 
# qu'on fait la somme des éléments de la première ligne, 
# puis de la deuxième, etc.
np.sum(a, axis=1) 

# 8m10

# vous avez beaucoup de méthodes comme prod, mean, std, min, max, median
# percentile, vous verrez ces méthodes dans les compléments

# Imaginons, maintenant qu'au lieu d'avoir un tableau d'entier, j'ai un 
# tableau de float avec une valeur nan
a = np.arange(1, 10, dtype=np.float).reshape(3, 3)
a[1, 1] = np.nan
print(a)

# comme le nan est contaminant, toute opération arithmétique avec un nan
# produit un nan, on ne peut plus utiliser les méthodes classiques.

np.mean(a) # me retourne nan

# Toutes ces méthodes ont un équivallent nan-safe qui va simplement ignorer
# les valeurs mises à nan, ces méthodes commencent toutes par nan

np.nanmean(a), np.nanmax(a)

10m00



