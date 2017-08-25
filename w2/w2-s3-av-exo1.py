# -*- coding: utf-8 -*-

## une séquence est un ensemble fini d'éléments ordonnés qui sont
## indexés par des entiers commençant à 0

## Pour illustrer le fonctionnement des séquences commençons par
## regarder les chaînes de caractères

s = 'egg, bacon' # dix lettres

print(s[0])
print(s[9])

## il existe des fonctions et des opérations communes à toutes les
## séquences c'est-à-dire non seulement aux chaînes de caractères mais
## aussi aux listes et aux tuples. Commençons par regarder ces
## fonctions et opérations communes à toutes les séquences

## test d'appartenance

print('g' in s)
print('g' not in s) # noter que c'est presque du langage naturel

## concaténation, retourne une **nouvelle** séquence de même type

print(s + ' and spam')

## l'accès direct à un élément par un indice négatif

print(s[-3])

## le nombre d'éléments

print(len(s))

## le plus petit ou plus grand élément de la séquence

print(min(s))
print(max(s))

## premiere occurence dans s

print(s.index('g'))

## nombre d'occurence

print(s.count('g'))

## n shallow copy de s concaténés, on reviendra sur la notion de
## shallow copy dans une autre vidéo

print(s*3)

print('-'*30)

## et pour finir on a la notion de slicing qui s'applique à
## toutes les séquences. Le slicing permet d'obtenir une
## nouvelle séquence qui est un sous ensemble de la séquence
## d'origine. C'est une opération très puissante qu'il est
## important de bien maitriser. Regardons comment le slicing
## fonctionne

[[TP: je te suggère d'utiliser une astuce visuelle qui je trouve marche pas mal;
  c'est de montrer - je dessine en l'air avec mes doigts - que les bornes 
  de la slice sont prises comme ceci [ [,
  pour illustrer que la borne à gauche est incluse et la borne à droite est exclue

  et ainsi faire comprendre qu'on peut en quelque sorte "enficher" les slices
  les unes dans les autres, et que donc par exemple
  seq[0:3] + seq[3:6] == seq[0:6]

  je t'envoie par ailleurs un .png qui montre comment on pourrait modifier
  les animations dans ce sens, même si je comprends que c'est peut-être
  bcp de travail, je me rends pas compte avec ppt, en keynote ça a été simple à faire..
]]
[[AL: je verrai si j'ai le temps quand j'aurai tout fini]]





