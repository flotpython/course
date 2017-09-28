# -*- coding: utf-8 -*-

## prenons un exemple simple

y = 3
def incremente(x):
    return x + y

## y est une variable globale, donc increment n'est pas un terme clôt. 

## regardons maintenant ce deuxième exemple

def plus_n(y):
    def incremente(x):
        return x + y
    return incremente

## la fonction incremente référence deux variables, x qui est une
## variable locale et y qui est une variable libre. incremente est
## donc un terme clôt.

## à chaque fois qu'on appelle plus_n, on retourne un nouvel
## objet fonction qui garde un accès à la variable libre y.

## Cela veut donc dire qu'on a maintenant un moyen de garder de l'état
## dans la fonction incremente qui est initialisé lors de l'appel de
## plus_n puisque l'objet fonction garde l'accès à toutes
## les variables libres, on pourra donc utiliser ses variables libres
## lors de l'appel de la fonction.
plus3 = plus_n(3)

## Comment cela est possible, le terme clôt a un attribut __closure__
## qui est un tuple qui contient les références vers les variables
## libres.

plus3.__closure__

plus3.__closure__[0].cell_contents
