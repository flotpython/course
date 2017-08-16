# -*- coding: utf-8 -*-

## Pour charger un module il faut utiliser l'instruction
## import

import random

## ensuite, pour utiliser le module, on utilise le même nom que celui
## que l'on a utilisé pour l'import. donc random est une variable qui
## référence l'objet module.

print(random)

## On peut voir tous les attributs d'un module avec l'instruction dir

print(dir(random))

## ou voir l'aide du module avec help()
help(random)


## Cependant, on utilise rarement help directement sur un module,
## parce que ça produit beaucoup de texte dans lequel il est difficile
## de naviguer. On préfère en général l'aide en ligne sur le Web. 

## Par contre, help est tout à faire adapté pour accéder à l'aide
## d'une méthode dans un module. Pour accéder à l'attribut d'un
## module, on utilise le nom du module - point - le nom de l'attribut.

help(random.randint)

## Sous ipython on peut également obternir l'aide directement avec ?
random.randint?

random.randint(1, 10) # retourne un nombre aléatoire dans [1, 10]

