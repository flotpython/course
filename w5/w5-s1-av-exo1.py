# -*- coding: utf-8 -*-

## Tous les types built-in sont itérable, on peut donc utiliser un
## mécanisme d'itération comme une boucle for ou une compréhension
## directement sur tous les types built-in.

s = {1, 2, 3, 'a'}
for i in s:
    print(i) 

[x for x in s if type(x) is int]


## 1m00s

## Regardons maitenant comment le protocole d'itération fonctionne.

## On doit commencer par récupérer l'itérateur de l'objet itérable
## avec la méthode iter() sur l'objet

it = iter(s)
print(it)

## ensuite, on appelle la méthode next() pour obtenir chaque élément
## de l'objet. Lorsqu'on a parcouru tous les éléments de l'objet, la
## méthode next retourne une exception qui s'appelle
## StopIteration. Cette exception est le signal que l'itération est
## terminée. 

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))


## Évidement, vous n'avez pas à appeler vous-même les méthodes iter()
## et next(), ni a capturer l'exception StopIteration, tous les
## mécanismes d'itération en Python, boucle for, compréhension de
## listes, le font pour vous. Le but de cet exemple est de vous
## montrer le protocole d'itération dont la compréhension sera utile
## lorsque vous créerez vos propres objets itérables.

## Vous pouvez aussi avoir le sentiment que ce fonctionnement est
## lent. Ça n'est pas le cas, L'interface commune de tous les
## itérateurs permet une implémentation optimisée des mécanismes
## d'itération et le protocole d'itération est parmi ce qui a été le
## plus optimisé en Python.


