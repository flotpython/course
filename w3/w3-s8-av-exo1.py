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

## prenons un exemple un peu plus réaliste. Créons un objet phrase qui
## me permet de simplement analyser les mots d'une phrase.

[[TP: après avoir relu w6-s1 et w6-s2, je remarque que
  cet exemple est mot pour mot celui de w6-s2 (méthodes spéciales)
  et qu'il passe à coté de la méthode toute bête

je proposerais quelque chose de plus simple comme

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
  
    def norme(self):
        return (x**2 + y**2) ** 0.5

  v1 = Vector(1, 2)
  v1.norme()

  et là juste mentionner qu'on voudrait pouvoir faire aussi v1 + v2, et que ce sera expliqué en semaine 6
  ]]


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

## On aimerait maintenant pouvoir appeler len sur une Phrase pour
## avoir le nombre de mots. En Python, toutes les opérations sur les
## types built-in peuvent être implémentées dans nos propres classe
## avec une méthode spéciale. Regardons cela


class Phrase:
    def __init__(self, phrase):
        self.mots = phrase.split()

    def __len__(self):
        return len(self.mots)

p = Phrase("je fais un mooc sur python")

len(p)

## Pour finir implémentons le test d'appartenance qui ne prend pas en
## compte la casse des mots

class Phrase:
    def __init__(self, phrase):
        self.mots = phrase.split()
        self.mots_lowers = set([m.lower() for m in self.mots])

    def __len__(self):
        return len(self.mots)

    def __contains__(self, mot):  # mot est une référence vers le mot
                                  # avant in
        return mot.lower() in self.mots_lowers

p = Phrase("je fais un mooc sur Python")

print('pythoN' in p)


