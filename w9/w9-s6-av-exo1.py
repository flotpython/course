# -*- coding: utf-8 -*-

## **** PREPARATION ****

## Afficher l'éditeur sur la gauche et l'interpréteur sur la droite
## sur une demie hauteur (faire attention d'avoir un fond blanc,
## ouvrir par exemple notepad en full screen).
## Copier dans l'éditeur le code suivant.

class Temperature:
    def __get__(self, inst, instype):
        print("desc __get__")
        return inst._temperature

    def __set__(self, inst, t):   
        print(f"desc __set__ {t}")
        inst._temperature = t
    
class Maison:
    def __init__(self, t):
        [[TP le underscore est de trop ici, non ?]]
        self._temperature = t

    def __getattribute__(self, a):
        print(f"__getattribute__: {a}")
        return object.__getattribute__(self,a)
    
    def __setattr__(self, a, v):
        print(f"__setattr__: {a} = {v}")
        return object.__setattr__(self, a, v)

    def __str__(self):
        return f"Maison: {self._temperature}"

    [[et là je suis mais alors complètement perdu]]
    temperature = Temperature()

## **** FIN PREPARATION ****



## reprenons notre exemple des descripteurs en simplifiant un peu la
## méthode __set__ puisqu'ici nous voulons simplement tracer les
## appels des méthodes. Prenez quelques instants pour taper le
## descripteur Temperature et la classe Maison avec ses méthodes
## __getattribute__, __setattr__ et __str__

[[TP alors là je suis complètement perdu dans la logique temporelle
  on n'a encore jamais dit le mot descripteur à ce stade, si ?]]


## Créons une instance de maison

m = Maison(10)

## on voit qu'il y a une opération d'affectation sur l'instance de
## maison pour l'attribut _temperature

## et référençons l'attribut temperature, mais utilisons la complétion

m.temp[TAB]

## On voit que IDLE accède à l'espace de nommage de l'instance, puis
## accède à l'attribut __class__ de l'instance pour remonter l'arbre
## d'héritage, le reste de la recherche n'est pas tracé, on ne le voit
## donc pas.

m.temperature

## On passe dans __getattribute__ puis dans le descripteur, et pour
## finit on appelle __getattribute__ pour l'attribut _temperature

## regardons ce qu'il se passe si on désactive l'appel de
## __getattribute__ sur object

m.temperature

## on passe dans __getattribute__, mais il n'y a plus d'accès au
## descripteur et plus de valeur de retour. Notons qu'il est
## impossible ici de faire directement un self._temperature, cela
## créerait un appel récursif. Le seul moyen d'accéder à l'attribut
## dans l'instance est d'appeler __getattribute__ sur object (ou sur
## une autre classe)

## réactivons object.__getattribute__ et regardons maintenant
## l'affectation.

m.temperature = 20

## On passe dans __setattr__ puis dans le descripteur et finalement on
## appelle __setattr__ pour l'attribut _temperature. Comme avec
## __getattribute__ si on désactive l'appel de object.__setattr__ on
## n'a plus de descripteur et plus d'affectation. On a également le
## problème d'appel récursif si on essaie d'affecter directement sur
## l'instance. 

## regardons maintenant les appels si on accède à un attribut qui
## n'est pas un descripteur

m.x

## on passe par __getattribute__ puis on a une exception. 

m.x = 10

## on passe par __setattr__

m.x

## on passe par __getattribute__

## Les appels implicites des méthodes spéciales ne passent pas par
## __getattribute__, c'est un détail d'implémentation mais qui a un
## impact sur la performance. Un appel implicite est un appel fait par
## une fonction builtin, un opérateur ou une instruction,
## contrairement à un appel explicite qui est fait par l'appel direct
## de la méthode spéciale.

## Il s'agit d'une optimisation qui a un impact sur la performance,
## ouvrons un interpréteur ipython pour regarder cela. 

a = [1]

%timeit len(a)

%timeit a.__len__()

## et pour finir, les appels implicites des méthodes spéciales ne
## passent pas par l'instance, mais par son type (et puis remonte
## l'arbre d'héritage). C'est ce qui permet de définir
## __getattribute__ sur une classe et que la référence d'un attribut
## sur cette classe passe par le __getattribute__ de la métaclasse
## type et non par le __getattribute__ définis pour la classe. 

[[c'est sûrement clair pour toi mais moi j'ai rien compris]]
