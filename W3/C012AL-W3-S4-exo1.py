# -*- coding: iso-8859-15 -*-

## Nous avons vu la notion de shallow copie pour les séquences

a = range(10)
a2 = a[:]

## mais on peut également faire une shallow copy pour un dictionnaire
## ou un set

d = {'marc' : 30, 'alice' : 35}
d2 = d.copy()

print d, d2

s = {1,2,7,89,0}
s2 = s.copy()

print s, s2

# xxx il y a un complement deja ecrit sur ce sujet, si tu veux gagner 
# un peu de temps tu peux zapper ca

## pour finir, j'aimerais aborder un problème d'optimisation de CPython
a = [1, 2]
b = a
print a == b
print a is b

b = [1, 2]
print a == b
print a is b

a = 18
b = 18
print a == b
print a is b

## Python réutilise certains objets immuables (petits entiers, petites
## chaînes de caractères) pour minimiser la consommation mémoire. Il n'y
## a jamais de problèmes avec les références partagées dans ce cas
## parce que ces objets réutilisés sont immuables et ne sont pas
## composites (c'est-à-dire qu'ils ne peuvent pas contenir d'autres objets). 
