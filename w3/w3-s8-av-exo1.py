# -*- coding: utf-8 -*-

## la notion de classes vous ouvre la porte de la programmation objet
## qui peut donner lieu à des schémas de programmation subtiles voir
## abscons.

## Cependant, il y a un certains nombre de cas où les classes
## s'imposent. Par exemple, si vous avez besoin d'objets multiples qui
## ont tous les mêmes caractéristiques.

[[TP: la classe vide ça n'a pas franchement d'intérêt pratique,
  je serais toi j'enlèverais carrément, on verra tout ça en semaine 5 ou je sais pas
combien ]]

 [[AL: ça n'a effectivement aucun intérêt
  pratique, mais ça me permet de commencer doucement sur la notion
  d'instance sans perturber l'auditeur avec les méthodes spéciales et
  la notion de self]]


## créeons un classe C

class C:
    pass

## créeons deux instance de C

c1 = C()
c2 = C()

## on voit que c1 et c2 sont deux objets différents (notons les
## adresses différentes) et que C est également un objet.

print(C, c1, c2)

## Évidement, comme la classe C ne définie aucune méthode, mes
## instances c1 et c2, ne font pas grand chose.

## prenons un exemple un peu plus réaliste. Créons un objet Phrase qui
## me permet de simplement analyser les mots d'une phrase.

class Phrase:
    def __init__(self, phrase):     # expliquer self et phrase
        self.mots = phrase.split()  # rappeler str.split()

## toutes les méthodes qui commencent et finissent avec 2 tirets bas
## sont des méthodes spéciales, c'est-à-dire que Python peut
## directement les appeler pour offrir certains comportements.

## toutes les méthodes dans une classe doivent prendre comme premier
## argument self qui est une référence vers l'instance. Le deuxième
## argument de __init__ est une référence vers l'objet de je passe à
## la classe lors de la création de l'instance. Regardons un exemple.

p = Phrase("je fais un mooc sur python")

## on peut vérifier que l'on a bien dans p un attribut mots qui
## contient la liste des mots

## Si on veut avoir tous les mots en majuscule, on peut implémenter
## une méthode upper() sur notre classe qui manipule l'attribut mots
## de l'instance.

class Phrase:
    def __init__(self, phrase):
        self.mots = phrase.split()

    def upper(self):
        self.mots = [m.upper() for m in self.mots]

        
## On aimerait maintenant pouvoir appeler print sur une Phrase pour
## voir le contenu des mots. Si vous faites print() sur une instance
## de Phrase, vous allez voir le nom et l'adresse de l'objet, mais pas
## son contenu. Pourtant, quand vous faites print() sur une liste,
## vous voyez bien son contenu.

## En Python, toutes les opérations sur les types built-in peuvent
## être implémentées dans nos propres classe avec une méthode
## spéciale. Pour avoir un affichage par print() is faut implémenter
## la méthode __str__. Regardons cela


class Phrase:
    def __init__(self, phrase):
        self.mots = phrase.split()

    def upper(self):
        self.mots = [m.upper() for m in self.mots]

    def __str__(self):
        return "\n".join(self.mots)

p = Phrase("je fais un mooc sur python")

print(p)
p.upper()
print(p)



