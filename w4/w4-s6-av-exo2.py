# -*- coding: utf-8 -*-

## Regardons les deux dernières manières de déclarer des arguments et
## de passer des arguments à une fonction.


## regardons maintenant la forme * qui est liée à la notion de tuple
## unpacking que nous avons déjà vu. Regardons un exemple

def f(*t):
    print t

## le nom "t" est juste un nom de variable, on peut prendre n'importe
## quel nom seul l'étoile est importante. Avec cette maniere de
## déclarer les arguments, on peut passer un nombre quelconque d'arguments,
## qui seront mis dans un tuple référencé par la variable "t".

f(1, 2, 3, 'a')

## il nous reste une dernière forme à voir, la forme **.  Ici encore
## c'est une forme d'unpacking, mais appliquée aux dictionnaires,
## regardons alors un exemple...

def f(**d):
    print d

## Ici aussi, "d" est juste un nom de variable, seule la double * est
## importante. Avec cette déclaration d'arguments, on pourra appeler
## notre fonction avec n'importe quel nomnbre d'arguments nommés
## et ces arguments seront mis dans un dictionnaire avec pour clef le nom de l'argument et
## pour valeur l'argument passé.

f(nom='idle', prenom='eric', tel='0720202020')

## On peut combiner les 4 déclarations d'arguments, mais toujours dans
## l'ordre suivant arguments ordonnés, arguments par défaut, forme *,
## forme **. Cependant, il ne faut pas que ça nuise à la clareté,
## c'est pourquoi on recommande d'éviter de mélanger plus de deux
## manières.
## [[TP: attention, ce n'est plus vrai:
## https://www.python.org/dev/peps/pep-3102/
## on peut mettre des arguments nommés après le *varargs
## ils deviennent alors des arguments qu'on *doit* nommer lors de l'appel]]

## Vous pouvez vous demander dans quel cas on souhaite avoir une
## fonction qui accepte un nombre quelconque d'arguments. Un exemple
## d'utilisation de ces déclarations est la fonction built-in print

print?

## print accepte un nombre quelconque d'argument à afficher, on a donc
## une forme *t, et quelques paramètres nommés : sep, end, file et
## flush


## Pour finir, il nous reste encore à voir deux manière
## d'appeler une fonction. Regardons un exemple

def f(a, b):
    print(a, b)

## Ma fonction prend deux arguments, mais supposons
## que j'ai mes arguments à passer à la fonction dans une liste
x = [1, 2]

## je peux passer x[0] comme premier argument et x[1] comme deuxième,

f(x[0], x[1])

## mais je peux aussi utiliser une forme * qui permet de passer les
## éléments d'une séquence comme arguments d'une fonction, c'est une
## forme de sequence unpacking

f(*x)

## TP:
## tu pourrais montrer que dans ce sens-là on peut mettre plusieurs
## varargs
f(*x, *x)

## Supposons, maintenant que j'ai mes arguments dans un
## dictionnaire
d = {'a' : 1, 'b' : 2}

## je peux utiliser ce dictionnaire pour passer des arguments
## nommés à ma fonction avec une forme **, il faut évidement
## que chaque clef du dictionnaire corresponde au nom d'un
## argument de la fonction

f(**d)

## Cette forme peut vous paraître artificielle, mais elle a plusieurs
## usages très important. Le premier est lorsque l'on veut appeler une
## fonction avec toujours les mêmes arguments nommés, sans avoir à les
## retaper à chaque fois. Regardons un exemple,

pp = {'sep':'_', 'end':'.', 'flush':True} ## pp pour pretty print
phrase = ['un', 'mooc', 'sur', 'python']

print(*phrase, **pp)


## Il y a un autre usage très important des formes * et **, c'est
## l'implémentation de wrappers. Nous verrons ce sujet en profondeur
## lorsque nous parlerons des décorateurs, mais je peux déjà vous
## donner une idée de cela. Imaginez que je veuille créer une fonction
## qui s'appelle comme la fonction print, mais qui affiche une ligne
## de dièse, puis appelle print, puis affiche une ligne de dièse. La
## difficulté ici est d'écrire une fonction qui a la même signature
## que print. La bonne solution est d'écrire un wrapper qui prend
## comme argument une forme * et **. Comme la forme * accepte
## n'importe quel argument ordonnés et que la forme ** accepte
## n'importes quels arguments nommés, notre wrapper va accepter
## n'importe quelle liste d'argument ordonnés et nommés, donc
## n'importe quelle signature.


def my_print(*t, **d):
    print('#'*30)
    print(*t, **d)
    print('#'*30)


my_print(1, 2, 3, sep='_')
 
