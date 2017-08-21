# -*- coding: utf-8 -*-

## Je vous rappelle que Python utilise le typage dynamique, c'est-à-dire
## que l'on ne donne pas le type d'un objet à l'écriture du programme,
## ce type est déterminé à l'exécution. Ça simplifie beaucoup l'écriture
## des programmes.

## Commençons par le type int qui représente les entiers. 
## Pour entrer un entier, on n'a rien d'autre à faire que d'écrire
## cet entier
1

## On peut également faire des opérations sur cet entier comme sur une calculatrice

5 + 3
5 / 3
5 - 3

## on peut affecter notre objet entier à une variable
i = 1

# ou affecter le résultat d'un calcul
i = 5 + 3

## Comment on connait le type d'un objet en Python ?
## On utilise la fonction built-in type() qui accepte comme
## argument une variable ou un objet. 

type(i)

## en python les int sont de taille illimité
i = 23480284028402840289482184018 # taille illimitée
i * i     # taille illimitée
i ** 32

## Les décimaux, qu'on appelle aussi 'flottants' on une
## précision limité à environ 15 chiffres significatifs (53 bits de précision)
# On sépare la partie entière et décimale par un .
f = 4.3

## Pour finir on a les nombres complexes qui sont
## construit comme deux nombre décimaux. Ils ont donc
## les mêmes limitations de précision. 

c = 1 + 3j

c.real, c.imag

## On peut 'mélanger' les types numériques dans une expression, 
## par exemple en ajoutant un entier et un flottant
## Par contre on peut perdre en précision.
## Un int et un float donne toujours un float
## Un int ou un float et un complex
## donne toujours un complex

i + f

i + c

## On peut convertir des types de bases entre eux (avec risque là aussi
## de perte de précision ou d'information, troncation).

int(4.32)
float(9879729572895792375948)
complex(10)

## Résumons les différentes opération que l'on peut faire sur les
## types numériques

5 + 3
5 - 3
-3
5 / 3     # division naturelle
5 // 3    # division entière
5 % 3     # reste de la division entière
2 ** 32   # puissances
abs(-5.3) # valeur absolue

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
