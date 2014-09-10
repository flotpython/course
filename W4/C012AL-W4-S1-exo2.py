# -*- coding: iso-8859-15 -*-

## Supposons maintenant que dans le fichier que l'on vient
## de créer je veuille remplacer l'espace entre le nombre
## et son carré par une virgule, nous allons voir que grace
## à la puissance des itérateurs cela ne demande que quelques
## lignes de code. 

## Commençonms par ouvrir le fichier que l'on vient de créer
## en mode lecture
f = open('C:\Temp\spam.txt', 'r')

## et ouvrons un nouveau fichier en mode écriture
f2 = open('C:\Temp\spam2.txt', 'w')

## Les fichiers en Python sont des itérateurs
it = f.__iter__()

print it is f

## Donc on peut faire directement une boucle for sur un
## fichier. Chaque itération va retourner une nouvelle
## ligne du fichier.

## Cependant, comme le fichier est directement un itérateur
## (et non un objet qui peut avoir plusieurs itérateurs)
## on ne peut itérer qu'une seule fois sur un objet fichier.
## Pour itérer de nouveau, il faut créer un nouvel objet
## fichier avec la fonction built-in open()

## regardons maintenant comment lire le fichier,
## remplacer les espaces par des virgules et écrire
## le résultat dans un nouveau fichier.

for line in f:
    f2.write(line.replace(' ', ','))

f.close()
f2.close()

             
