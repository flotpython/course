# -*- coding: utf-8 -*-

## commençons par regarder la taille des types
## built-in

import sys
## en entier fait 12 bytes sur une machine 32 bits
## et 24 bytes sur une machine 64 bits

print '1', sys.getsizeof(1)

print '1L', sys.getsizeof(1L)

print 'grand entier', sys.getsizeof(23495873294572347598275973825833)

## une chaîne de caractère fait au minimum 22 bytes
## sur une machine 32 bits et 38 bytes sur une
## machine 64 bits
print 'a', sys.getsizeof('a')

## par contre chaque nouveau caractère ne compte que
## pour un byte de plus dans la chaîne
print 'ab', sys.getsizeof('ab')

print 'abc', sys.getsizeof('abc')

## None vaut 8 bytes sur une machine 32 bits
## et 16 bytes sur une machine 64 bits

print 'None', sys.getsizeof(None)

print '[]', sys.getsizeof([])
## la taille d'une liste est indépendante de la
## taille des objets dans une list. Elle ne garde
## que les références
print '[1, 2]', sys.getsizeof([1, 2])
print '["sdafasd", {1, 2}]', sys.getsizeof(['sdafasd', {1, 2}])

## Donc Python utilise  beaucoup de mémoire pour chaque
## objet, heureusement les références partagées permettent de
## limiter le nombre d'objets en mémoire.

## Il est également important de comprendre qu'occuper
## de la mémoire quand on en a n'est pas un problème.
## Toutes les machines modernes ont plusieurs Gigabytes
## de mémoire. Les avantages de Python viennent
## au prix d'avoir des objets partout, donc une plus
## grande occupation mémoire. C'est presque toujours un
## petit prix à payer pour tant d'avantages.

## Dans les rares cas où les types built-in consomment
## trop de mémoire pour votre usage, il est toujours
## possible d'implémenter vos propres strucutures de
## données en C et d'interfacer ces structures avec
## du code Python. Nous donnerons dans les compléments
## le lien de la documentation qui explique comment
## interfacer du code C et du code Python.

## regardons maintenant quelques résultats suprenants sur
## la performance de Python. On va utiliser pour cela
## la fonction timeit dans le module timeit. Cette fonction
## permet d'exécuter plusieurs fois un morceau code et retourne
## le temps d'exécution de ce code.

import timeit

## commençons par répondre à une question simple, à partir
## de quand vaut-il mieux utiliser les set que les listes
## dans les test d'appartance. 
print timeit.timeit(setup= "x = range(40)", stmt = '"a" in x', number = 6000000)
print timeit.timeit(setup= "x = set(range(40))", stmt = '"a" in x', number = 6000000)


print timeit.timeit(setup= "x = range(2)", stmt = '"a" in x', number = 6000000)
print timeit.timeit(setup= "x = set(range(2))", stmt = '"a" in x', number = 6000000)

print timeit.timeit(setup= "x = range(2)", stmt = '0 in x', number = 6000000)
print timeit.timeit(setup= "x = set(range(2))", stmt = '0 in x', number = 6000000)

## la liste est légèrement plus rapide que quand le test d'appertance
## est vrai dès le premier élément de la liste

## regardons maintenant un résultat très surprenant pour les personnes
## habituées aux langages compilés. Nous avons vu avec la surcharge
## d'opérateur qu'il existait des méthodes pour toutes les opérations
## sur les built-in. Par exemple la méthode __contains__ est appelée
## lors du test d'appartenance avec in. Les personnes habituées
## aux langage compilé pourrait croire que l'appel direct à la fonction
## est plus rapide que d'utiliser l'opérateur in. Regardons cela

print timeit.timeit(setup = "L = range(1000)", number = 30000000, stmt = "0 in L")

print timeit.timeit(setup = "L = range(1000)", number = 30000000, stmt = "L.__contains__(0)")

## L'interpréteur Python est optimisé pour l'utilisation des opérateurs.
## il faut donc toujours favoriser les opérateurs sur les appels directs
## aux fonctions. 


## regardons maintenant la différence de performance entre une boucle
## for et une compréhension de liste

def f():
    L = []
    for i in xrange(1000):
        L.append(i**2)
    return L

def g():
    return [x**2 for x in xrange(1000)]

print timeit.timeit(number = 10000, stmt = f)
print timeit.timeit(number = 10000, stmt = g)

## on voir donc que la compréhension de liste n'est pas une
## expression qui exécute en réalité une boucle for.
## Les compréhensions sont exécuté plus efficacement
## que les boucles for par l'interpréteur Python.


## nous aurions pu faire beaucoup d'autres tests, mais vous
## devez commencer à comprendre le principe. N'hésitez
## pas à jouer avec timeit pour comprendre quels sont
## les meilleurs choix d'implémentation dans votre contexte. 
