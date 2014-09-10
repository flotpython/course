# -*- coding: iso-8859-15 -*-

## Nous avons déjà vu la déclaration d'arguments ordonnées

def agenda(nom, prenom, tel):
    return {'nom' : nom , 'prenom' : prenom,
            'tel' : tel}

## et l'appel de fonction avec le passage d'arguments
## ordonnés.

d = agenda('durant', 'marc', '0720202020')
print d

## Il y a cependant un problème avec cet appel : on doit
## connaître l'ordre des arguments. Lorsqu'il y a beaucoup
## d'arguments et que le nom des arguments est bien choisi
## il est plus facile de se souvenir du nom des arguments
## que de leur ordre. C'est pourquoi, il est possible
## d'appeler une fonction en plaçant les arguemnts dans
## un ordre quelconque du moments qu'on les nomme

d = agenda(tel='0720202020', nom='durant', prenom='marc')

## Même s'il est possible de mélanger des arguments ordonnés
## et des arguments nommés lors de l'appel, ça n'a
## pas de sens de le faire. En effet, soit on connait l'ordre
## des arguments et dans ce cas on utilise des arguments
## ordonnés lors de l'appel. Soit on ne connait pas l'ordre
## alors on utilise des arguments nommés. Si on les mélanges
## cela peut conduire à des erreurs subtiles que nous
## détaillerons dans les compléments. 

## Si l'on revient à notre déclaration de fonction,
## on pourrait vouloir créer une entrée dans l'agenda
## sans donner un téléphone. On pourrait donc appeler
## notre fonction avec un chaîne vide au lieu du numéro
## ou avec un point d'intérogation. Mais si notre programme
## a un comportement spécifique lorsqu'il n'y a pas de numéro
## il est important que ce champ numéro soit toujours le
## même lorsqu'il n'est pas fourni lors de l'appel.
## Le moyen le plus simple est d'utiliser les arguments
## par défaut. Regardons un exemple

def agenda(nom, prenom, tel='na'):
    return {'nom' : nom , 'prenom' : prenom,
            'tel' : tel}

## si on ne founit pas l'argument lors de l'appel, c'est
## l'argument par défaut qui est utilisé.
print agenda('durant', 'marc')

##sinon c'est l'argument que l'on passe. 
print agenda('durant', 'marc', '0720202020')

## lorsque dans la déclaration de notre fonction on a des
## arguments ordonnés et des arguments par défaut,
## il faut toujours mettre les arguments ordonnés en premier
## et les arguments par défaut après. On ne peut pas les
## mélanger. 

## Nous avons donc vu deux manières de déclarer les arguments
## d'une fonction : arguments ordonnés et arguments par défaut.
## Nous avons dit qu'il y avait 4 manières en tout, il nous
## en reste donc deux à voir.

## regardons maintenant la forme *. C'est un nom étrange
## pour quelque chose de très simple. Regardons un exemple

def f(*t):
    print t

## le nom Targs est juste un nom de variable, on peut prendre
## n'importe quel nom seul l'étoile est importante. Avec
## cette maniere de déclarer les arguments, on peut passer
## une liste quelconque qui sera mise dans un tuple
## référencé par la variable Targs. 

f(1, 2, 3, 'a')

## il nous reste une dernière forme à voir, la forme **.
## Ici encore c'est un nom étrange pour quelque chose
## de simple, regardons alors un exemple...

def f(**d):
    print d

## Ici aussi, Dargs est juste un nom de variable, seule
## la double * est importante. Avec cette déclaration
## d'arguments, on pourra appeler notre fonction avec
## des arguments nommés et ces arguments seront mis
## dans un dictionnaire avec pour clef le nom de l'argument
## et pour valeur l'argument passé.

f(nom='durant', prenom='marc', tel='0720202020')

## On peut combiner les 4 déclarations d'arguments, mais
## toujours dans l'ordre suivant arguments ordonnés,
## arguments par défaut, forme *, forme **. Cependant,
## il ne faut pas que ça nuise à la compréhension, c'est
## pourquoi on recommande d'éviter de mélanger plus
## de deux manières. 

# 7 minutes

## Pour finir, il nous reste encore à voir deux manière
## d'appeler une fonction. Regardons un exemple

def f(a, b):
    print a, b

## Ma fonction prend deux arguments, mais supposons
## que j'ai mes arguments à passer à la fonction dans une liste
L = [1, 2]

## je peux passer L[0] comme premier argument et L[1]
## comme deuxième, mais je peux aussi utiliser une forme
## * qui permet de passer les éléments d'une séquence
## comme arguments d'une fonction

f(*L)

## Supposons, maintenant que j'ai mes arguments dans un
## dictionnaire
d = {'a' : 1, 'b' : 2}

## je peux utiliser ce dictionnaire pour passer des arguments
## nommés à ma fonction avec une forme **, il faut évidement
## que chaque clef du dictionnaire corresponde au nom d'un
## argument de la fonction

f(**d)

## comme pour la déclaration des arguments, on peut combiner
## les différents appels, mais il faut ici aussi éviter de le
## faire d'autant plus que cela peut conduire à des erreurs
## subtiles que nous verrons dans les compléments. C'est
## donc une bonne pratique de se limiter à une seule manière
## d'appeler une fonction.

# 8 minutes 40 secondes
