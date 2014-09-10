# -*- coding: iso-8859-15 -*-

## La syntaxe d'une fonction lambda est simple.
## Elle commence par le mot clef lambda, suivi
## d'une liste d'arguments séparés par des virgules
## et d'une expression pouvant utiliser ses arguments.

lambda x: x**2 + 2*x -1

## Cependant les fonctions lambda n'ont pas de nom
## alors comment les utiliser ? Le résultat
## de l'évaluation du code de la fonction lambda est une
## référence vers l'objet fonction qui vient d'être créé

## On peut donc utiliser une fonction lambda de deux
## manieres, soit on lui donne un nom en l'assignant à
## une variable, soit on la définit directement là où
## elle va être utilisée. 

f = lambda x: x**2 + 2*x - 1

print f(1)

L = [lambda x: x**2 + 2*x - 1, lambda x: x**3 -2]

print L[0](10), L[1](10)

## on peut également directement passer une fonction
## lambda à une fonction

def func(x):
    for i in range(10):
        print i, x(i)

## Je suppose lors de l'écriture de ma fonction func
## que l'argument x sera une fonction. Si x n'est pas
## une fonction j'aurai une exception

# func(1)

func(lambda x: x**2 -3)

## il est très important de comprendre que je peux
## faire exactement la même chose avec une fonction
## classique. Après tout en Python, tout est un objet
## et une variable n'est qu'un nom qui référence un
## objet, en particulier, le nom d'un fonction
## référence l'objet fonction défini par le def.

def g(x):
    return x**2 -3
func(g)

## la fonction lambda permet simplement d'écrire
## plus rapidement une fonction qui est limitée
## à une seule expression. En effet, dans une fonction
## lambda, on ne peut pas mettre d'instructions comme
## des if ou des for. 

# 4 minutes

## Un usage classique des fonctions lambda en Python est
## de les utiliser avec les fonctions built-in map() et
## filter().

## Je vous rappelle qu'en Python les itérateurs sont au coeur
## de la programmation et qu'avec les boucles for,
## on peut de manière simple et efficace exploiter la
## puissance des itérateurs. Il existe cependant d'autres
## moyen d'exploiter les itérateurs en Python comme les
## fonctions map et filter que nous allons voir maintenant. 

## La fonction map prend comme argument une fonction et
## un objet itérable, et retourne une liste de la fonction
## appliquée à chaque élément de l'objet itérable. 

print map(g, range(10))

## les fonctions lambda permette d'avoir un code
## plus compact et plus rapide à écrire. Ce code
## est aussi plus facile à lire pour ceux habitués
## à la syntaxe des fonctions lambda, mais plus difficile
## à lire pour les débutants. On s'habitue cependant vite
## aux fonctions lambda. 

print map(lambda x: x**2 -3, range(10))

## regardons maintenant la fonction filter. Comme la fonction
## map, la fonction filter prend comme argument une
## fonction et un objet itérable, mais elle retourne une
## liste des éléments de l'objet itérable pour les lequels
## la fonction retourne True. Je vous rappelle qu'en Python
## 0, None, les types de base vides et False sont faux, tout le
## reste est vrai.

## regardons un exemple de fonction filter, je veux
## obtenir tous les éléments d'une séquence qui sont pairs.

print filter(lambda x: x % 2 == 0, range(10))

## ou divisible par 3
print filter(lambda x: x % 3 == 0, range(10))


# 6 minutes 30 seconces
