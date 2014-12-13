# -*- coding: utf-8 -*-

## Supposons que l'on veuille compter le nombre d'instances
## créées par une classe. On peut facilement maintenir un
## compteur du nombre de référence dans contructeur de la
## classe, mais l'accès à ce compteur n'est pas trivial.
## Regardons cela...


class C:
    nb_i = 0
    def __init__(self):
        C.nb_i  = C.nb_i + 1


C()
C()
## je peux évidemment accéder à l'attribut de la
## classe directement. 
print C.nb_i

## Je peux aussi faire une fonction dans mon module

def num():
    return C.nb_i


print num()

## Mais cela complique la maintenance d'avoir une fonction
## travaillant sur une classe en dehors de la classe.

## Par contre, je ne peux pas faire une méthode d'instance
## dans ma classe puisqu'il me faut une instance pour accéder
## au compteur, et que cette instance va changer le compteur
## à sa création.

## La solution ici est d'avoir une méthode statique.
## une méthode statique s'écrit comme une fonction,
## mais doit être déclarée comme statique avec la
## fonction staticmethod. 

class C:
    nb_i = 0
    def __init__(self):
        C.nb_i  = C.nb_i + 1
    def num():
        return C.nb_i
    num = staticmethod(num)

C()
C()
print C.num()

## notons qu'une méthode statique peut aussi être appelée sur
## une instance, mais que l'instance n'est pas passée à la
## méthode

print C().num()

## Une sous classe hérite des méthodes statiques, par
## contre, si la sous classe surcharge la méthode
## statique, elle doit être de nouveau déclarée
## comme statique dans la sous classe. 

## je ne redéfinis pas la méthode statique
class SousC(C):
    pass

print SousC.num()

## je redéfinis la méthode statique
class SousC(C):
    def num():
        return 'de sousC {}'.format(C.num())
    num = staticmethod(num)

## L'inconvénient ici est que il y a un seul compteur
## pour les instances de C et SousC

SousC()
SousC.num()

## il existe en Python un autre type de methode pour
## les classes, ce sont les méthodes de classe.
## Lorsqu'une méthode de classe est appelée sur une
## classe C, elle reçoit comme premier argument une référence
## sur C. C'est très intéressant
## lorsque qu'une méthode de classe est défini dans une classe
## et hérité dans plusieurs sous classe. Il sera ainsi
## possible de faire un traitement différent en fonction
## de la sous classe. 

## On définit une method de class avec la fonction
## built-in classmethod()
## Si l'on revient à notre exemple, on peut avoir un
## compteur d'instance distinct pour chaque sous classe.

class C:
    nb_i = 0
    def __init__(self):
        self.count()
    ## affiche le nombre d'instances de la classe cls
    def num(cls):
        return cls.nb_i
    ## compte de nombre d'instances de la classe cls
    def count(cls):
        cls.nb_i = cls.nb_i + 1
    num = classmethod(num)
    count = classmethod(count)

class SousC(C):
    nb_i = 0

C()
C()
print C.num(), SousC.num()

