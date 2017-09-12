# -*- coding: utf-8 -*-

def div(a, b):
    print(a / b)

## si b est 0, il y aura une exception ZeroDivisionError On voit que
## l'exception a un nom spécifique et contient un message
## d'explication. C'est le cas pour toutes les exceptions built-in

#div(1,0)

## prenons quelques instants pour regarder cette exception.  Le
## message d'erreur indique la ligne qui a produit l'exception, le nom
## (en fait le type) de l'exception est ZeroDivisionError et un
## message d'erreur

## Heureusement, il est possible de capturer une exception pour
## continuer le programme.  Les exceptions se capturent avec
## l'instruction try/except

def div(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Division par 0")
    print('continuons...')

print(div(10, 2))
print(div(1, 0))

## mais regardons ce que produit l'appel de div avec un entier et une
## chaine de caractère.

print(div(1, '2'))

## cette appel produit une nouvelle exception que je peux également
## capturer en ajoutant une nouvelle clause except


def div(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Division par 0")
    except TypeError:
        print("Il faut des int !")
    print('continuons...')

# 3m45
    
## Vous avez remarqué que je faisais toujours suivre une clause except
## d'un nom d'exception. Ça n'est pas une obligation, je peux avoir
## une clause except sans nom d'exception, et dans ce cas, ma clause
## va capturer toutes les exceptions. C'est souvent une très mauvaise
## idée de faire ça parce que vous risquez de capturer des exceptions
## que vous n'avez pas prévu ou que vous ne connaissez pas. Votre
## traitement ne sera donc pas approprié et votre programme risque de
## planter sans message d'erreur ou avec un message d'erreur ne
## correspondant pas au problème.

#4m45

### BUBBLING ###

## Une caractéristique importante des exceptions est qu'elles
## remontent (on dit bubble comme une bulle d'air dans l'eau) la pile
## d'exécution des fonctions qui contient toutes les fonctions
## actives, c'est-à-dire celles qui ont été appelées mais qui n'ont pas
## encore retourné une valeur.

## Lorsqu'une exception est produite et n'est pas capturée, elle
## arrête l'exécution de la fonction et remonte à la fontion
## appelante, puis elle arrête cette fonction et remonte à la fonction
## appelante jusqu'à remonter dans toutes les fonctions de la pile
## d'exécution. Regardons un exemple :

def div(a, b):
    print(a / b)

def f(x):
    div(1, x)
    
f(0)


## Quel est l'intérêt de ce mécanisme de bubbling ? Il est
## double. Premièrement, on peut capturer l'exception là ou elle se
## produit, mais également directement dans la fonction appelante ou
## n'importe ou dans sa remontée. Ainsi on la garantie qu'une
## exception n'est jamais perdue et si elle n'est pas correctement
## capturée, elle produit l'arrêt du programme.

## Deuxièmement, si on ne capture pas l'exception, elle va générer ce
## qu'on appelle une stack trace, c'est à dire une trace de la pile
## d'exécution qui permet de connaitre la successions d'appels de
## fonctions qui ont conduit à l'exception. Puisque l'exception bubble
## sur le chemin inverse.  C'est très utile pour diagnostiquer le
## problème.

#7m30
