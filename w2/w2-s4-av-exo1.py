# -*- coding: utf-8 -*-

############################################### 4m00
## une liste est une séquence, donc toutes les fonctions et opérations
## que l'on a vues pour les séquences s'appliques aux listes : en
## particulier testes d'appartenance in, not in ; concaténation avec
## le signe + ; longeur avec la fonction built-in len ; récupération
## d'un élément par son index entre crochet ; et le slicing.

## on crée une liste vide ainsi
a = []

## on sépare les éléments d'une liste par des virgules
## notons que l'on peut directement mettre un objet dans
## la liste, ou utiliser une variable référencant l'objet

i = 4

a = [i, 'spam', 3.2, True]

print(a[0])

a[0] = 20

print(a)

## on peut également directement effectuer une opération et réaffecter
## cette opération à un élément de la liste. Je rappelle qu'en Python
## on évalue d'abord ce qu'il y a à droite du signe égal et ensuite
## on affecte le résultat à la variable de gauche.

a[0] = a[0] + 1

print(a)

## on peut utiliser le slicing dans une liste parce que c'est
## une séquence

print a[1:3]

## mais comme une liste est mutable on peut affecter sur un slice

a[1:2] = ['egg', 'beans']

print(a)

## il faut bien comprendre ce que fait cette opération. Python
## commence par effacer les éléments spécifiés par le slide dans a,
## puis il va ajouter les éléments de la liste de droite à la
## place. S'il y a plus d'éléments la liste est agrandie, s'il y en a
## moins, elle est raccourcie

## on peut donc supprimer des éléments sur un slice en affectant un
## slice à une liste vide

a[1:2] = []

print(a)

## je peux également utiliser l'instruction del pour effacer tous les
## éléments spécifiés dans un slice

del a[0:3:2]

print(a)

## par contre s'il on écrit a[1] = ['spam', 'good'], on va simplement
## ajouter une liste à la position 1 de la liste a

a[1] = ['spam', 'good']

print(a)


################################################### 2m10
## Regardons maintenant des fonctions qui permettent de modifier
## les listes en place.

a = [1, 2, 3, 4]

a.append(18)
print(a)

a.extend([5, 20])
print(a)

## insère l'objet juste avant la position, mais n'efface et ne
## remplace rien
a.insert(2, 30)
print(a)

a.sort() # attention sort ne retourne pas la liste, mais la modifie en
         # place

a.reverse() # renverse la liste en place
print(a)

print a.pop()

a.remove('30') # efface la premiere occurence de l'élément passé en
                # parametre


############################################################# 2m15

## Pour finir, j'aimerai parler d'une opération très courante qui
## permet de passer d'une chaine de caractère à une liste et d'une
## liste à une chaîne de caractère. C'est typiquement l'opération que
## l'on fait lorsqu'on lit un fichier et que l'on veut changer son
## format ou faire des opération par colonne. Regardons un exemple

s = 'spam,egg,beans'

a = s.split(',')

print(a)

a[1] = a[1].upper()

print(a)

s = " ".join(a)

print(s)

a = s.split()

print(a)

8 minutes
