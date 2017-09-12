# -*- coding: utf-8 -*-

## Commençons par un exemple simple. 

class C:
    pass

## créons une instance de cette classe

c = C()

## ces objets, l'instance et la classe, on des attributs spéciaux qui
## permettent de parcourir l'arbre d'héritage.

c.__class__ # référence la classe qui a créé cette instance (donc le
            # premier pas dans l'arbre d'héritage)

C.__bases__ # est un tuple qui référence les super classes de C

## vous remarquez que la classe object est la super classe de C alors
## qu'on n'a pas défini de super classe pour C. En fait, si vous ne
## définissez pas de super classe, object sera automatiquement la
## super classe de votre classe. Donc object est toujours tout en haut
## de l'arbre d'héritage. Mais à quoi cela sert-il ? object va définir
## certaines méthodes spéciales avec un comportement par défaut. C'est
## parce que object est la super classe de C que vous pouvez faire un
## print sur C ou son instance, sans définir aucune méthode.

print(C)

## on peut regarder l'ordre de résolution des attributs en appelant la
## méthode mro() sur une classe. Cette méthode va nous donner une
## liste des objets dans l'ordre où ils doivent être parcourus

C.mro()


# 2m00

## Regardons maintenant un exemple d'héritage multiple

class SuperA:
    pass

class SuperB:
    pass

class C(SuperA, SuperB):
    pass

## La classe C hérite de superA et superB, et ces deux super classes
## hérite de object. Regardons la mro

C.mro()

## on voit que l'ordre de résolution des attributs à partir de C est
## C, superA, superB et object

## L'ordre dans lequel on défini les super classes à un impact sur la
## MRO

class C(SuperB, SuperA):
    pass

C.mro()


#3m30s
