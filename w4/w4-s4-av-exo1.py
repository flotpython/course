# -*- coding: utf-8 -*-

## La syntaxe de la compréhension de listes est simple
## et intuitive puisqu'elle est proche du langage naturel.
## Mais elle est également incroyablement puissante.
## Commençons par un exemple simple. Créons une liste
## des carrés des entiers allant de 0 à 10. 
## La compréhension de liste commence toujours par un crochet
## ouvrant et termine par un crochet fermant, indiquant que le
## résultat est une liste. On a ensuite une expression sur
## une suivi de for, du nom de
## variable utilisé dans l'expression suivi de in et de
## l'objet itérable que va parcourir la variable. 

print [x**2 for x in range(10)]

## On peut en plus ajouter une condition dans la
## compréhension de liste. Par exemple si l'on veut
## les carrès de tous les entiers allant de 0 à 100
## et qui sont divisible par 7, il suffit d'écrire

print [x**2 for x in range(101) if x % 7 == 0]

## notons que lorsque l'on lit cette expression on est proche
## du langage naturel et que la compréhension
## remplace en une seule expression les fonctions
## built-in map et filter.




