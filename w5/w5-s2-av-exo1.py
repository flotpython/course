# -*- coding: utf-8 -*-

## La syntaxe d'une fonction lambda est simple.  Elle commence par le
## mot clef lambda, suivi d'une liste d'arguments séparés par des
## virgules et d'une expression pouvant utiliser ces arguments.

lambda x: x**2 - 1

## Cependant les fonctions lambda n'ont pas de nom alors comment les
## utiliser ? Le résultat de l'évaluation du code de la fonction
## lambda est une référence vers l'objet fonction qui vient d'être
## créé

## On peut donc utiliser une fonction lambda de deux manieres, soit on
## lui donne un nom en l'assignant à une variable, soit on la définit
## directement là où elle va être utilisée.

carre = lambda x: x**2 - 1

print(carre(1))

[[TP l'exemple suivant n'apporte peut-etre pas grand-chose de plus..]]
[[AL: c'est pour montrer, que l'usage réel des lambda n'est pas de
leur donner un nom, mais de les utiliser directement]]

d = {'carre': lambda x: x**2 - 1, 'cube': lambda x: x**3 - 2}

print(d['carre'](10), d['cube'](10))

## comme les fonctions en python sont des objets, on peut les passer
## en paramètres à d'autres fonctions; c'est la base de ce qu'on
## appelle la programmation fonctionnelle 

## par exemple je peux écrire

def image(f):
    for x in range(10):
        print(x, f(x))

## Je suppose lors de l'écriture de ma fonction image que l'argument f
## sera une fonction. Si f n'est pas une fonction j'aurai une
## exception

## maintenant je peux appeler image avec comme argument une fonction
## lambda

image(lambda x: x**2 -3)

## il est très important de comprendre que je peux faire exactement la
## même chose avec une fonction classique. Après tout en Python, tout
## est un objet et une variable n'est qu'un nom qui référence un
## objet, en particulier, le nom d'une fonction référence l'objet
## fonction défini par le def.

def carre(x):
    return x**2 - 1

image(carre)

## la fonction lambda permet simplement d'écrire plus rapidement une
## fonction qui est limitée à une seule expression. On a donc un code
## plus compact et potentiellement plus expressif. Par contre, dans
## une fonction lambda, on ne peut pas mettre d'instructions comme des
## if ou des for, une fonction lambda est donc limitée par rapport à
## une fonction classique.


# 4m30s

## les fonction lambda sont souvent utilisée avec les fonctions
## builtin map et filter qui sont des primitives de programmation
## fonctionnelle qui permettent d'appliquer une fonction à chaque
## élément d'une séquence ou de filtrer les éléments d'une séquence.
## Ça ne vous rappelle rien ? Les compréhensions de liste !  En effet,
## tout ce que l'on peut faire avec map et filter peut être fait avec
## une compréhension de liste. Par conséquent, même s'il faut
## connaitre ces fonctions map et filter, leur usage est comme pour
## les fonctions lambda largement une affaire de goût.

## les fonctions map et filter supportent le protocole d'itération, on
## peut donc leur passer n'importe quel itérable.

## La fonction map prend comme argument une fonction et un objet
## itérable, et retourne un itérateur qui applique la fonction à
## chaque élément de l'itérable. Je vous rappelle qu'un itérateur ne
## peut être parcouru qu'une fois. 

m = map(carre, range(10))
list(m)

## les fonctions lambda permette d'avoir un code
## plus compact et plus rapide à écrire. Ce code
## est aussi plus facile à lire pour ceux habitués
## à la syntaxe des fonctions lambda, mais plus difficile
## à lire pour les débutants. On s'habitue cependant vite
## aux fonctions lambda. 

m = map(lambda x: x**2 -3, range(10))
list(m)

## regardons maintenant la fonction filter. Comme la fonction map, la
## fonction filter prend comme argument une fonction et un objet
## itérable, mais elle retourne un itérateur qui produit les éléments
## de l'objet itérable pour lesquel la fonction retourne True. Je vous
## rappelle qu'en Python 0, None, les types de base vides et False
## sont faux, tout le reste est vrai.

## regardons un exemple de fonction filter, je veux
## obtenir tous les éléments d'une séquence qui sont pairs.

filter(lambda x: x % 2 == 0, range(10))

# 7 minutes 30 seconces
