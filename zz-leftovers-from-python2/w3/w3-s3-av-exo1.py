# -*- coding: utf-8 -*-

## On peut créer un set de deux manières, soit avec un littéral
## soit en passant une une liste comme argument de la
## fonction set

s1 = {1, 2, 3, 4, 4, 4, 5}

a = [3, 4, 8]
s2 = set(a)

print s1, s2

## on peut ajouter ou enlever des éléments d'un set
s1.add('spam')
s2.update([38, 9, 'egg'])
s2.remove(38)

## le test d'appartenance est sans surprise fait avec
## l'instruction in et not in

print 'spam' in s1
print 8 not in s1

print len(s1)

## je peux calculer la différence, l'union et l'intersection
## de deux sets

print s1 - s2
print s1 | s2
print s1 & s2

## il y a d'autres opérations possibles sur les sets que je
## vous encourage à découvrir dans la documentation Python.

## pour finir vous pouvez créer un frozen set à partir
## d'une séquence ou d'un set ainsi

fs = frozenset(s1)
print fs
