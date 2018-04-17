# -*- coding: utf-8 -*-

## Tous les types built-in ont un itérateur, et comme une boucle
## for peut directement itérer sur un objet qui a un itérateur,
## on peut faire une boucle for sur tous les types built-in.

s = {1, 2, 3, 'a'}
for i in s:
    print i, 

## Mais regardons comment une boucle for fait pour utiliser
## un objet qui a un itérateur.

## La boucle for commence par récupérer l'itérateur avec
## la méthode __iter__() sur l'objet

print

it = s.__iter__()
print it

## ensuite, la boucle for appelle la méthode next() pour obtenir
## chaque élément de l'objet. Lorsqu'on a parcouru tous les
## éléments de l'objet, la méthode next retourne une exception qui
## s'appelle StopIteration. La boucle for capture automatiquement
## cette exception et se termine

print it.next()
print it.next()
print it.next()
print it.next()
print it.next()

## Évidement, vous n'avez pas à appeler vous-même les méthodes
## __iter__() et next(), le but de cet exemple est de vous montrer le
## fonctionnement des itérateurs. La compréhension de ce
## fonctionnement sera utile lorsque vous créerez vos propres
## itérateurs.

## Vous pouvez aussi avoir le sentiment que ce fonctionnement, même s'il
## est pratique, est lourd et lent. Ça n'est pas le cas, le fonctionnement
## des itérateurs est parmi ce qui a été le plus optimisé dans la machine
## virtuelle CPython. 


