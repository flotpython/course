# -*- coding: utf-8 -*-

## prenons l'exemple suivant


a, b, c = 1, 1, 1

def g():
    b, c  = 2, 4
    b = b + 10
    def h():
        c = 5
        print(a, b, c)
    h()
g()

## g est une fonction dans laquelle on a défini une fonction h. Donc g
## est une fonction englobant h. On a trois variable globales a, b, c
## et deux variable locales à g, b et c, et une variable locale à h c.
## Que va affichier print(a, b, c). Pour le savoir on applique la
## règle LEGB.
##
## Commençons avec a. a n'est pas locale à h, a n'est pas dans une
## fonction englobante, mais a est définie globalement. C'est donc le
## a global que l'on va utiliser, il référence l'objet 1.
##
## Regardons maintenant b. b n'est pas définie localement à h, mais b
## est définie dans la fonction englobante g, c'est donc ce b que l'on
## utilise, il référence au moment de l'appel de print l'objet 12.
##
## Finissons avec c, c est définie localement à h, c'est ce c que l'on
## utilise, il référence l'objet 5
##
## print va donc afficher 1, 12, 5

## Évidement, si je fait un print(a, b, c) en dehors de toutes
## fonctions, je vais référencer les variables globales je vais donc
## afficher 1, 1, 1

## Nous savons maintenant que la règle pour définir la portée d'une
## variable est la règle LEGB, mais à quel moment utilisons nous la
## recherche d'une variable dans le module builtins. On l'utilise à
## chaque fois que l'on référence un objet builtins. Dans notre
## exemple, print est une variable qui référence un objet fonction qui
## est défini dans le module builtins.

## vous remarquerez cependant que nous n'avons jamais importé le
## module builtins. Python l'importe automatiquement pour nous au
## démarrage de l'interpréteur. Cependant, nous pouvons l'importer et
## regarder ce qu'il y a dedans.

import(builtins)
dir(builtins)

## on trouve dans ce module tous les type builtins, toutes les
## exceptions builtins et toutes les fonction builtins comme, print,
## input ou len. C'est grace à l'import automatique de ce module et à
## la règle LEGB que l'on peut accéder à tous ces objets directement.

## Cependant, vous avez remarqué que la recherche dans le module
## builtins à la plus faible priorité. Que ce passe-t-il si on définit
## une variable qui a un nom d'une fonction builtins.

print = 10
print('spam')

## print est une variable qui référence l'entier 10. lorsque j'appelle
## print, je cherche la variable suivant la règle LEGB. print n'est
## pas dans une fonction, ni dans des fonctions englobantes, elle est
## définie globalement dans le module, c'est donc ce print que
## j'utilise. Comme print référence un entier, on ne peut pas écrire
## 10('spam')

## Cependant, cette redéfinition n'est jamais un problème en
## pratique. En effet, tout bon éditeur Python va colorer d'une
## manière particulière les variables définies dans le module
## builtins. Et évidement, même si vous faites cette erreur, c'est
## réversible.

print = builtins.print
print('spam')

## nous reviendrons sur ce dernier point lorsque nous parlerons des
## espaces de nommage et des modules. 
