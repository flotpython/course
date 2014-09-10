# -*- coding: iso-8859-15 -*-

## Prenons une liste de 3 éléments

L = [1, 2, 3]

## essayons d'appeler next() sur la liste L
#L.next()

## ça retourne une exception parce que la liste L
## n'est pas un itérateur. Par contre les listes ont
## des itérateurs.

## recupérons l'itérateur de cette liste

it = L.__iter__()

## nous voyons que la liste et l'itérateur sont différents
print L is it

## par contre si on appelle __iter__() sur l'itérateur
## on remarque de l'on a le même objet, donc
## l'appelle de __iter__() sur un itérateur retourne bien
## l'itérateur lui même.

it2 = it.__iter__()

print it is it2

## on peut faire directement une boucle for sur l'itérateur
## c'est équivallent à faire une boucle for sur l'objet
## qui a cet itérateur puisque la boucle for appélera toujours
## en premier la fonction __iter__() sur l'objet.

for i in it:
    print i,

## par contre, une fois que l'itérateur a retourné tous les
## éléments, next() retournera toujours StopIteration, on ne
## peut donc plus faire de boucle for dessus. Il faudra dans
## ce cas créer un autre itérateur.

#iterateur.next()

for i in it:
    print i, 

it3 = L.__iter__() # nouvel itérateur

print
print it is it3

for i in it3:
    print i,
    
## Il faut faire attention lorsque l'on manipule directement des itérateurs
## de générer un nouvel itérateur à chaque fois que l'on fait une nouvelle
## boucle. On n'a pas de ce problème avec les objets qui ont des itérateurs
## puisque la boucle for se chargera elle même de génerer un nouvelle itérateur
    
