# -*- coding: utf-8 -*-

## Supposons que l'on veuille compter le nombre d'instances créées par
## une classe. On peut facilement maintenir un compteur du nombre de
## référence dans contructeur de la classe. Regardons cela...


class Phrase:
    nb_i = 0
    def __init__(self):
        Phrase.nb_i  = Phrase.nb_i + 1


Phrase()
Phrase()
## je peux évidemment accéder à l'attribut de la
## classe directement. 
print Phrase.nb_i

## Mais comment faire une méthode sur la classe qui me retourne cet
## attribut.

class Phrase:
    nb_i = 0
    def __init__(self):
        Phrase.nb_i  = Phrase.nb_i + 1

    def num():                         # new
        return Phrase.nb_i                  # new

Phrase()

## Je peux appeler num() depuis la classe
Phrase.num()

## c'est en effet une fonction classique

Phrase.num # fonction classique

## par contre, je ne peux pas l'appeler depuis l'instance, puisqu'une
## méthode bound passe automatiquement l'instance comme premier
## argument, mais que ma num() méthode n'accepte aucun argument.

p = Phrase()
p.num   # méthode bound
p.num()

#2m15s

## La solution est de définir ma méthode num() comme méthode statique.
## Ainsi, une méthode statique ne prend jamais d'instance comme
## premier argument et s'appelle de la même manière depuis une classe
## ou une instance. En particulier, lorsqu'elle est appelé depuis une
## instance, elle reste une fonction classique et non une méthode
## bound.

## c'est très simple de déclarer une méthode comme statique...

[[TP: pourquoi tu montres toujours des trucs
  qui sont pas ce qu'on fait dans la vraie vie ?!?!
  ici sans réfléchir il FAUT que tu mettes les décorateurs, IMHO
  si ça te gêne parce qu'on n'a pas encore vu les décorateurs
  tu n'as qu'à dire qu'on les étudie dans la vidéo suivante
]]

class Phrase:
    nb_i = 0
    def __init__(self):
        Phrase.nb_i  = Phrase.nb_i + 1
        
    @staticmethod
    def num():
        return Phrase.nb_i

p = Phrase()
Phrase.num()
Phrase.num      # fonction classique
p.num()
p.num      # fonction classique

#3m30s

## Une sous classe hérite des méthodes statiques, par contre, si la
## sous classe surcharge la méthode statique, elle doit être de
## nouveau déclarée comme statique dans la sous classe.

## je ne redéfinis pas la méthode statique
class PhraseSansCasse(Phrase):
    pass

PhraseSansCasse.num()

## je redéfinis la méthode statique
class PhraseSansCasse(Phrase):
    @staticmethod
    def num():
        return f'PhraseSansCasse {Phrase.nb_i}'

# 5m00s
    
## Vous remarquez cependant un problème, que j'ai une instance de
## Phrase ou de PhraseSansCasse, j'ai un unique compteur dans Phrase qui
## est incrémenté.

## Comment faire, pour avoir une méthode capable de maintenir un
## compteur différent pour Phrase et pour PhraseSansCasse ? Il faudrait
## pour cela maintenir un compteur dans Phrase et un dans
## PhraseSansCasse, mais que surtout la méthode num() sache que quand
## elle est appelée de Phrase elle accède au compteur de Phrase et que
## quand elle est accédé de PhraseSansCasse est accède au compteur de
## PhraseSansCasse. En d'autres termes, il faudrait que la méthode num()
## reçoivent un référence vers l'objet classe qui l'appelle.

## C'est exactement ce que permet une méthode de classe. C'est une
## méthode bound à la classe d'appel, elle va donc automatiquement
## recevoir la classe comme premier argument, et si elle est appelée
## depuis une instance, elle recevra un référence de la classe qui a
## créé cette instance.

## On définit une method de class avec le décorateur built-in
## classmethod() Si l'on revient à notre exemple, on peut avoir un
## compteur d'instance distinct pour chaque sous classe.

#6m00s

class Phrase:
    nb_i = 0
    def __init__(self):
        [[TP pourquoi pas += 1 en plus pour la vidéo ce serait + court ?]]
        Phrase.nb_i = Phrase.nb_i + 1
        
    @classmethod
    def num(cls):                 # new
        return cls.nb_i           # new

    
class PhraseSansCasse(Phrase):
    nb_i = 0                                          
    def __init__(self):
        PhraseSansCasse.nb_i  = PhraseSansCasse.nb_i + 1
        
    @classmethod
    def num(cls):
        return f'PhraseSansCasse {cls.nb_i}'

p = Phrase()
Phrase()

p_no = PhraseSansCasse()

p.num()
p_no.num()

p.num # bound method à la classe
Phrase.num # bound method à la classe


#8m00s
