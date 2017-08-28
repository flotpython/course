# -*- coding: utf-8 -*-

## un set vide se crée toujours à partir de la fonction set

s = set()

## Pour initialiser un set avec des élements, on peut utiliser la
## notation accolade 

s = {1, 2, 3, 4, 4, 4, 5} # noter que ça ne garde que les éléments
                          # uniques

## Attention cependant que les accolades vides crées un dictionnaire
## vide et non un set vide. 

## on peut également passer une liste ou un tuple comme argument de la fonction
## set

a = [3, 4, 8]
s = set(a)

print(s1, s2)

## notons que utiliser un set pour ne garder que les éléments unique
## d'une liste est courant en Python

nom = ['eve', 'eve', 'bob', 'alice', 'bob']
s = set(nom)
len(s)

## on peut ajouter ou enlever des éléments d'un set
s.add('spam')
s.update([38, 9, 'egg']) # applique add à chaque élément de la sequence
s.remove(38) # enlève un élément


## je peux calculer la différence, l'union et l'intersection
## de deux sets

s1 = {1, 2, 3}
s2 = {3, 4, 5}

print s1 - s2 # enlève les élément des s2 dans s1
print s1 | s2
print s1 & s2

## Un des usages le plus important des set est le test d'appartenance.
## Le test d'appartenance est sans surprise fait avec l'instruction in
## et not in

print('eve' in s)
print(8 not in s)

########################## 3m50s ######################

## regardons maintenant l'efficacité du test d'appartenance sur les
## set.

## Nous savons que le temps du test d'appartenance est constant sur un
## set mais qu'il est lineaire avec le nombre d'éléments sur une
## liste. Toute la question est de savoir quel est l'ordre de grandeur
## de ce temps constant pour le test d'appartenance sur les set. Plus
## il sera grand, et moins il sera interessant d'utiliser un set pour
## faire un test d'appartenance sur un petit nombre
## d'éléments. Imaginons qu'il faille 1 seconde pour faire un test
## d'appartenance sur un set et 1 ms pour accéder à un élément d'une
## liste. Il faudra au maximum 3 ms pour tester l'apparteance d'un
## élément dans une liste.
##
## Essayons d'estimer ce temps et de le comparer avec le temps d'accès
## à l'élément d'une liste

a = [0]
s = set(a)

%timeit 0 in s
%timeit a[0]

## le temps pour faire un test d'appartenance sur un set est de
## l'ordre de grandeur de l'accès à un élément d'une liste. C'est
## extrêment rapide. 

## En résumé quelque soit le nombre d'élément dans votre set il faudra
## de l'ordre de 40 ns (sur ma machine) pour faire un test
## d'appartenance. Le même test d'appartenance sur une liste sera
## égale au temps d'accès d'un élément dans la liste, soit de l'ordre
## de 40 ns également, fois le nombre d'élément dans la liste. 

a = list(range(100))
s = set(a)
%timeit 'c' in a # environ 50 fois plus lent
%timeit 'c' in s # toujours 40ns

## Pour finir, convertir une liste en set prend du temps, mais c'est
## en général négligeable. En effet, convertir une liste en set prend
## à peu prêt le même temps que pour parcourir tous les éléments de la
## liste. Donc couvertir tous les éléments d'une liste en set prend
## environ le même temps que de faire un seul test d'appartenance sur
## cette liste qui retourne False.

## En conclusion, il faut toujours convertir vos liste en set pour
## faire vos tests d'appartenance.

############################### 7m00s ###########################
