# -*- coding: utf-8 -*-

## Pour définir un tuple on utilise des paranthèses

t = () #tuple vide

t = (4,) # tuple avec un seul élément. Attention à la virgule à la fin,
         # Python pense que les parenthèse sont juste pour regrouper des
         # opérations
print(t)

## les parenthèses sont facultatives. !! attention ça n'est pas le cas
## avec les listes

t = 5,

## lorsque j'ai plusieurs éléments, je les sépare par des virgules

t = (3, 4.1, 'spam')

t = 3, 4.1, 'spam'

## on a sur les tuples, toutes les opérations des séquences

print(3 in t)
print(len(t))

## par contre on ne peut pas modifier un tuple et on a donc aucune
## fonction pour modifier en place un tuple

#t[1] = 8

## on peut facilement convertir un tuple en list et une liste en tuple
## en utilisant les fonction built-in list() et tuple()

a = list(t)

print(a)

a.append(11)
print(a)

t = tuple(a)

print(t)

## Pour finir avec le tuple, je vais parler d'une opération très
## fréquente en Python, le tuple unpacking. Cette opération est
## utilisée pour faire plusieurs affectations de variables à la
## fois. Regardons un exemple

(a, b) = (1, 2)

## a va référencer 1 et b va référencer 2. Une des raisons de pouvoir
## écrire un tuple sans paranthèse est d'alléger cette notation
## en écrivant

a, b = 1, 2

## Cette opération de tuple unpacking fonctionne pour toutes les
## séquence (on l'appelle également sequence unpacking), du moment que
## l'on a le même nombre d'éléments à gauche et à droite

a, b, c = 'xyz'

a, b = 'xyz'

## python supporte également un opération appelée extended unpacking
## qui est très pratique lorsque l'on veut séparer le premier ou
## dernier élément du reste, regardons un exemple

a, *b = range(10)
print(a)
print(b)

## avec l'extended unpacking, la variable b référencera tous les
## éléments restant dans un tuple.
*b, c = range(10)
print(b)
print(c)

