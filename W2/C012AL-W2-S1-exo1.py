# -*- coding: utf-8 -*-

## l'instruction print permet d'afficher simplement la valeur d'un
## objet sur le terminal. On dit également que l'on affiche une valeur
## sur la sortie standard

## print peut aussi bien accepter une variable (et dans ce cas il affiche
## la valeur de l'objet référencé par la variable) ou directement un objet.
## regardons cela en pratique

s = 'spam'
print s

print 'egg'

## l'instruction print permet aussi d'afficher plusieurs objets ou variable
## en les séparant par une virgule
## lorsqu'il y a une virgule entre les arguments (variable ou objet) passé
## à print, print ajoute un espace entre les valeurs des arguments retournés


i = 10

print i, s


## lorsque l'on est dans le terminal interactif (et uniquement dans ce cas)
## on peut aussi directement
## taper le nom de la variable suivi d'un retour chariot.

i

## On voit ainsi la représentation interne de l'objet.
## C'est la plupart du temps équivalent à print
## La représentation interne peut donner des informations
## supplémentaires.

