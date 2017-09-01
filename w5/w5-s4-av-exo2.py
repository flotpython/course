# -*- coding: utf-8 -*-

## Vous savez que lors de l'appel d'une fonction, le bloc de code de
## la fonction est exécuté. Durant cet exécution des variables locales
## peuvent être créées et dès qu'une instruction return est rencontrée
## ou dès que l'on a fini le bloc de code de la fonction, la fonction
## retourne et toutes les variables locales sont détruites. Par
## conséquent, une fonction ne garde aucun état entre deux exécutions.
## Nous allons voir qu'une fonction génératrice se comporte
## différemment.

## Dès qu'on a une instruction yield dans la fonction, elle devient
## automatiquement une fonction génératrice. Regardons un exemple.

def gen():
    yield 10

print(gen())

## on voit que la fonction ne retourne pas 10, mais un objet
## generator. Cet objet est un itérateur qui fonctionne de la manière
## suivante. Lorsqu'on appelle next sur le generateur, le bloc de code
## de la fonction est exécuté jusqu'au premier yield. L'expression
## après le yield est alors retourné par le next(), mais contrairement
## à une fonction classique l'objet générateur garde toutes les
## variables locales et l'état et suspend son exécution. À l'appel du
## prochain next() le générateur va reprendre son exécution la où il
## s'était arrêté, jusqu'au prochain. S'il n'y a plus de yield et
## qu'on attend le fin du bloc de code, le generateur retourne
## StopIteration.


def gen(x):
    yield x
    x = x + 1
    yield x


it = gen(10)
next(it)
next(it)
next(it)

## 3m15s

## Évidemment, en pratique on ne met pas une multitude de yield, mais
## on utilise plutôt une boucle for ou while. Regardons comment écrire
## une fonction génératrice qui produit le carré des entiers entre a
## et b

def carre(a, b):
    for i in range(a, b):
        yield i**2

list(carre(1, 10))

## un exemple aussi simple est plus facile à écrire sous forme d'une
## expression génératrice. Regardons alors un exemple plus sophistiqué
## qui illustre bien l'usage d'une fonction génératrice. Faisons 
## une fonction génératrice qui accepte un itérable et retourne un
## itérateur sur les palindromes d'entier ou de chaînes de caractères.

def palindromes(it):
    for i in it:
        if (type(i) is int) and str(i) == str(i)[::-1]:
            yield i
        elif (type(i) is str) and i == i[::-1]:
            yield i
        else:
            continue

list(palindromes([121, 10, 12321, 'abc', 'abba']))

## l'intérêt de notre générateur palidromes est encore plus marquant
## si au lieu de lui passer une liste, je lui passe un itérateur,
## comme par exemple, un fichier. Notre générateur sera ainsi capable
## de retourner tous les palindromes d'un fichier à la volée sans
## structure de données temporaire. 
