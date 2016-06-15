# -*- coding: utf-8 -*-

## Pour définir un tuple on utilise des paranthèses

t = () #tuple vide

t = (4,) # tuple avec un seul élément. Attention à la virgule à la fin,
         # Python pense que les parenthèse sont juste pour regrouper des
         # opérations
print t
## les parenthèses sont facultatives. !! attention ça n'est pas le cas
## avec les listes

t = 5,

## lorsque j'ai plusieurs éléments, je les sépare par des virgules

t = (3, 4.1, 'spam')

t = 3, 4.1, 'spam'

## on a sur les tuples, toutes les opérations des séquences

print 3 in t

## par contre on ne peut pas modifier un tuple et on a donc aucune
## fonction pour modifier en place un tuple

#t[1] = 8

## on peut facilement convertir un tuple en list et une liste en tuple
## en utilisant les fonction built-in list() et tuple()

a = list(t)

print a

a.append(11)
print a

t = tuple(a)

print t
