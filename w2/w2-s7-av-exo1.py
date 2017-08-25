# -*- coding: utf-8 -*-

## Imaginons que vous souhaitiez prendre le logarithme de chaque
## élément d'une liste. Avec une boucle for on utiliserait la méthode
## suivante

import math
my_list = [1, 3, 6, 9, 13, 5, 2]

log_list = []
for i in my_list:
    log_list.append(math.log(i))

## Il est très courant d'appliquer une opération ou une fonction à
## chaque élément d'une liste et de retourner une nouvelle liste qui
## contient le résultat. Pour cette raison, Python propose un
## mécanisme spécifique, plus rapide à écrire et plus efficace qu'une
## boucle for, la compréhension de liste  

## La syntaxe de la compréhension de listes est simple et intuitive
## puisqu'elle est proche du langage naturel.  Mais elle est également
## incroyablement puissante.  Reprenons l'exemple précédent.  La
## compréhension de liste commence toujours par un crochet ouvrant et
## termine par un crochet fermant, indiquant que le résultat est une
## liste. On a ensuite une expression sur chaque élément de la liste
## suivi de for, du nom de variable utilisé dans l'expression
## suivi de in et de l'objet itérable que va parcourir la variable.

log_list = [math.log(x) for x in my_list]

## notez que cette compréhension est quasiment du langage
## naturel. Elle se lit prenons le log de chaque x pour x qui parcours
## les éléments de my_list


## On peut en plus ajouter une condition dans la compréhension de
## liste. Par exemple si l'on veut le logarithme de tous les éléments
## de ma liste qui sont strictement plus grand que 1, je peux écrire

log_list = [math.log(x) for x in my_list if x > 1]

## notons de nouveau que lorsque l'on lit cette expression on est
## proche du langage naturel et que l'on peut en une seule expression
## appliquer une fonction à chaque élément d'une liste si une
## condition est vraie

## Regardons un autre exemple de compréhension de liste. J'ai une
## liste de prénoms et je veux le nombre de caractères pour tous les
## prénoms commençant par a.


nom = ['alice', 'bob', 'ana', 'bill']
a_nom = [len(n) for n in nom if n.startswith('a')]

[[TP: je vois pas trop l'intérêt de ce dernier exemple, ça n'apporte rien de nouveau..]] 
[[AL: j'ai du temps dans cette vidéo et je voulais montrer quelque chose sur
des chaînes de caractères]]
