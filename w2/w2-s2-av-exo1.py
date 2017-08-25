# -*- coding: utf-8 -*-

############################### str intro ####################### 2m30
## On peut définir une chaîne de caractères en Python en entourant
## notre chaine soit par des apostrophes soit par des guillemets

s1 = 'spam'
s2 = "spam"

## ces deux notations vont créer le même objet chaîne de caractère

print(s1, s2)
type(s1)
type(s2)

## Il exite un grand nombre de méthodes puissantes sur les chaînes de
## caractères. Python a une aide intégrée directement disponible
## depuis l'interpréteur, c'est extrêment pratique.  Pour avoir l'aide
## sur un type d'objet, par exemple, les chaines de caractères, il
## suffit de taper
help(str)

## Comme vous le notez, cette aide est complète et donne toutes les
## méthodes disponibles sur le type str. Je vous rappelle que le type
## str est l'objet qui fabrique les chaînes de caractères et que chaque
## chaîne hérite de toutes les méthodes de son type.

## En général, on n'a plus besoin de regarder toute l'aide lorsqu'on
## connaît un type, on a juste besoin de regarder les méthodes
## disponibles puisque leur nom est souvent explicite. Pour cela, on
## utilise la méthode dir
dir(str)

## Et ne se souvient plus du fonctionnement exacte d'une méthode,
## on peut demander l'aide directement dessus
help(str.replace) # attention pas de parenthèse, sinon on exécute la fonction
str.replace?      # uniquement sur iPython

################################################################## 2m00


## Les chaines de caractères sont des objets immuable en Python, cela
## veut dire qu'une fois l'objet créé, il ne peut plus être modifié.
## Par conséquent, toutes les méthodes sur les chaînes de caractères
## retourne un nouvel objet, elle ne modifie jamais l'objet initial,
## on dit qu'elle ne font pas de modifications en place.
## si l'on veut que notre variable référence le nouvel objet, il faut
## simplement faire une affectation. Regardons quelques exemples.

s = 'spam egg beans'

s.replace('spam', 'meat') # on n'a pas modifié s

print(s)

s = s.replace('spam', 'meat') # s est modifié

print(s)

s.upper()

# on peut également faire des tests sur les chaînes de caractères
s.endswith('ans')
'123'.isdecimal()

############################################################# 1m45

## Regardons maintenant comment formater 
## caractères

nom = 'sonia'
age = 30

s = "{} a {} ans".format(nom, age) # format classique

s = f"{nom} a {age} ans" # f-string, les f-strings n'existent que
                         # depuis Python 3.6

## Nous reviendrons dans les compléments sur les méthodes des chaînes
## de caractères et nous verrons les nombreuses possibilités de format
## pour gérer l'alignement d'un affichage en colonne ou l'affichage de
## nombre décimaux en contrôlant, par exemple, le nombre de chiffres
## après la virgule

