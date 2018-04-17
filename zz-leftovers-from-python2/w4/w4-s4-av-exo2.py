# -*- coding: utf-8 -*-

## Une compréhension de sets s'écrit exactement comme
## une compréhension de listes à la différence
## qu'au lieu de délimiter la compréhension par des crochets
## on la délimite par des accolades.

print {i**3 for i in range(10)}

## la compréhension de set est un moyen simple d'obtenir
## un set à partir d'une liste en effectuant au moment
## de la conversion des opérations et des filtres. Je
## rappelle qu'en Python, le set est la meilleure stucture
## de données pour faire des tests d'appartenance. 

print {i**2 + 3*i - 1 for i in range(100) if i % 11 == 0}

## Regardons maintenant la compréhension de dictionnaire.
## Elle s'écrit exactement comme une compréhension de set,
## sauf que l'on sépare les clefs et les valeurs par un :

print {i : i**2 for i in range(10)}

## Cette exemple est destiné à montrer de manière simple
## la syntaxe de la compréhension de dictionnaire. Mais
## il est évident qu'un dictionnaire qui à une clef
## entière associe comme valeur le carré de la clef n'a
## aucun intérêt.

## La compréhension de dictionnaires est par contre très utile
## pour convertir un dictionnaire déjà existant.
## Prenons un dictionnaire qui a pour clef un numéro client
## et pour valeur un nom

d = {123 : 'marc', 145 : 'eric', 543 : 'jean'}
print d

## Les dictionnaires sont optimisés pour accéder à des valeurs
## lorsque l'on connait la clef. Je rappelle que le temps
## d'accès, d'effacement et d'insertion est constant indépendamment
## de la taille du dictionnaire. Cependant, trouver une clef
## correspondant à une valeur donnée dans un dictionnaire
## est un processus itératif, donc lent.
## Si je connais un nom et que je veuille le numéro client
## correspondant, je ne pourrai pas avoir une recherche efficace
## avec le dictionnaire d. Pour avoir une recherche efficace, 
## il faudrait avoir un nouveau dictionnaire qui a pour clef
## les noms (je suppose ici qu'ils sont uniques) et pour valeur
## les numéros clients.
## 
## Avec la compréhension de dictionnaires je peux faire ça
## très simplement.

d2 = {d[k] : k for k in d}
print d2

## Je rappelle que lorsque j'itére sur un dictionnaire, je parcours
## les clefs. 

## Je peux aussi avec la compréhension de dictionnaires, ajouter des filtres
## comme avec les autres compréhensions

d3 = {d[k] : k for k in d if k < 300}
print d3
