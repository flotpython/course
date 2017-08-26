# -*- coding: utf-8 -*-

## Il existe deux manières de créer un dictionnaire, la
## plus simple lorsque l'on crée un dictionnaire à la main
## est d'utiliser les accolades

age = {}

## avec le caractère ':' pour séparer clé et valeur:

age = {'ana':35, 'eve':30, 'bob':38}

## la deuxième manière est très utile lorsque les couples
## clefs-valeurs sont obtenues par une opération dans notre programme,
## dans ce cas on peut automatiquement créer un dictionnaire à partir
## d'une liste de tuples clef,valeur

a = [('ana', 35), ('eve', 30), ('bob', 38)]
age = dict(a)

## je rappelle qu'il n'y a pas d'ordre dans un dictionnaire
## donc le dictionnaire n'affiche pas nécéssairement
## les valeurs dans l'ordre dans lequel on les a entrées

print(age)

## il existe de très nombreuse opérations et fonctions
## sur les dictionnaires, nous allons voir les principales

## on peut accéder et modifier la valeur d'une clef de la
## manière suivante

print age['ana']

## le dictionnaire est donc un objet mutable:
age['ana'] = 40

## je peux ajouter une nouvelle clef ainsi
age['bill'] = 12

## on peut effacer la clef et sa valeur dans le dictionnaire
## avec l'instruction del

del age['ana']

## même si les dictionnaires ne sont pas des séquences,
## dans un soucis d'uniformité et de simplification,
## la fonction len et l'opérateur in ont été implémentés
## sur les dictionnaires.
print(len(age))
print('eve' in age)
print('eve' not in age)


## et on a des méthodes pour récupérer sous forme de vues:
## les clefs, les valeurs, et les tuples (clefs, valeur)

print age.keys()
print age.values()
print age.items()

## mais qu'est-ce qu'une vue et comment l'utilise-t on ?  une vue est
## un objet compact (dont la taille est indépendante de nombre
## d'éléments dans le dictionnaire) que l'on peut parcourir comme une
## liste (il dit qu'une vue est itérable) et autorise le test
## d'appartenance.

k = age.keys()

'eve' in k


## Une caractéristique majeur de la vue est que comme son nom
## l'indique, elle est une vue sur l'objet dictionnaire, donc si le
## dictionnaire change, la vue change avec.

age['meg'] = 20

list(k)

## une précaution sur les vue est de ne jamais changer le dictionnaire
## pendant que l'on parcours la vue. Le résultat pourrait être
## inconsistant. [[TP: on en reparlera lorsqu'on étudiera plus en détails la boucle for ?]]

## pour finir, je vais vous montrer un schema classique en Python
## lorsque l'on veut parcourir les clefs et les valeurs en même temps

[[TP: on tire profit ici du 'tuple unpacking' dont on a déjà parlé]]

for k, v in age.items():
    print(f"{k}: {v}")

