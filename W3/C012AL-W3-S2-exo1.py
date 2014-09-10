# -*- coding: iso-8859-15 -*-

## Il existe deux manières de créer un dictionnaire, la
## plus simple lorsque l'on crée un dictionnaire à la main
## est d'utiliser les accolades

d = {}

d = {'marc':35, 'alice':30, 'eric':38}

## la deuxième manière est très utile lorsque les couples
## clefs-valeurs sont obtenues par une opération, dans
## ce cas on peut automatiquement créer un dictionnaire
## à partir d'une liste de tuples clef,valeur

a = [('marc', 35), ('alice', 30), ('eric', 38)]
d = dict(a)

# xxx je ferais remarquer qu'il s'agit d'un cas particulier de conversion
# comme on en a déjà vu pour les types numériques e.g. float(12)

## je rappelle qu'il n'y a pas d'ordre dans un dictionnaire
## donc le dictionnaire n'affiche pas nécéssairement
## les valeurs dans l'ordre dans lequel on les a entrées

print d

## il existe de très nombreuse opérations et fonctions
## sur les dictionnaires, nous allons voir les principales
## commençons par les deux suivantes

print len(d)
print 'marc' in d
print 'marc' not in d

## même si les dictionnaires ne sont pas des séquences,
## dans un soucis d'uniformité et de simplification,
## la fonction len et l'opérateur in ont été implémentés
## sur les dictionnaires.

## on peut accéder et modifier la valeur d'une clef de la
## manière suivante

print d['marc']
d['marc'] = 40

## on peut effacer la clef et sa valeur dans le dictionnaire
## avec l'instruction del

del d['marc']

d.copy() # shallow copie du dictionnaire
print 

## et on a des méthodes pour récupérer sous forme de liste:
## les clefs, les valeurs, et les tuples (clefs, valeur)

print d.keys()
print d.values()
print d.items()


# xxx on a a ce stade tout le bagage pour montrer ceci
#for k,v in d.items():
#    print "cle={} -> valeur={}".format(k,v)

# qui est tout de meme un truc majeur a montrer
# pour les dicts je pense
