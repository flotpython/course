# -*- coding: utf-8 -*-

## Je vous rappelle que Python utilise le typage dynamique, c'est-à-dire
## que l'on ne donne pas le type d'un objet à l'écriture du programme,
## ce type est déterminé à l'exécution. Ça simplifie beaucoup l'écriture
## des programmes.

## le type entier
## pour entrer un entier, on n'a rien d'autre à faire que d'écrire
## cet entier
1

## comme on l'a vu dans la vidéo 1, on peut également l'affecter à une variable
i = 1

## Comment on connait le type d'un objet en Python ?
## On utilise la fonction built-in type() qui accepte comme
## argument une variable ou un objet. 

type(i)

## en python on a deux type entiers, les int et les long
i = 10 ## codé sur 32 bits sur une machine 32 bits
l = 23480284028402840289482184018 # précision illimitée
print l * l     # précision illimitée sur les long

## Pourquoi avons nous deux types 'entier' en Python ?
## le type int est plus compact que le type long, par conséquent
## pour les petits entiers, Python va utiliser le type int pour réduire
## la consommation mémoire, et le type long s'il y a vraiment besoin de
## grands entiers.

## Heureusement, Python fait automatiquement la conversion
## de int vers long s'il y a besoin. Donc en pratique vous n'avez
## pas à vous préocupper du type d'entier que vous utilisez

type(i + l)     

## Les décimaux, qu'on appelle aussi 'flottants' on une
## précision limité à environ 15 chiffres significatifs
# On sépare la partie entière et décimale par un .
f = 4.3

## Pour finir on a les nombres complexes qui sont
## construit comme deux nombre décimaux. Ils ont donc
## les mêmes limitations de précision. 

c = 1 + 3j

print c.real, c.imag

## On peut 'mélanger' les types numériques dans une expression, 
## par exemple en ajoutant un entier et un flottant
## Par contre on peut perdre en précision.
## Un int et un long donne toujours un long
## Un type entier (int, long) et un float donne toujours un float
## Un type entier (int, long) ou un float et un complex
## donne toujours un complex

print i + l

print i + l + f

print i + l + f + c

## On peut convertir des types de bases entre eux (avec risque là aussi
## de perte de précision ou d'information, troncation).

print int(4.32)
print long(5.3)
print float(9879729572895792375948)
print complex(10)

## opérations de base

print 5 + 3
print 5 - 3
print -3
print 5/3       # division entière
print 5%3       # reste de la division entière
print 5/3.0     # division sur des floats
print 5/float(3)
print 5.2//3.1  # force la division sur des entiers (5.0/3.0)
print 2 ** 32   # puissances
print abs(-5.3) # valeur absolue

## pour finir, j'aimerais introduire un dernier type qui n'est pas
## à proprement parler un type numérique, mais qui est implémenté comme
## tel, c'est le type booléen. Ce type est utilisé pour le résultat
## de tous les tests en Python et ne contient que deux valeurs True et False
## On verra bientôt cette notion de test en Python, mais regardons un exemple
## simple pour illustrer les booléens

1 < 2
1 > 2

## noter la premiere lettre qui est une majuscule

## nous reviendrons très bientôt sur l'utilisation des Booléens
