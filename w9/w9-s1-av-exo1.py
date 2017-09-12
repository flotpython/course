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

class Phrase:
    nb_i = 0
    def __init__(self):
        Phrase.nb_i  = Phrase.nb_i + 1
        
    def num():
        return Phrase.nb_i
    
    num = staticmethod(num)         # new

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
class PhraseNoCasse(Phrase):
    pass

PhraseNoCasse.num()

## je redéfinis la méthode statique
class PhraseNoCasse(Phrase):
    def num():
        return f'PhraseNoCasse {Phrase.nb_i}'
    num = staticmethod(num)

# 5m00s
    
## Vous remarquez cependant un problème, que j'ai une instance de
## Phrase ou de PhraseNoCasse, j'ai un unique compteur dans Phrase qui
## est incrémenté.

## Comment faire, pour avoir une méthode capable de maintenir un
## compteur différent pour Phrase et pour PhraseNoCasse ? Il faudrait
## pour cela maintenir un compteur dans Phrase et un dans
## PhraseNoCasse, mais que surtout la méthode num() sache quand quand
## elle est appelée de Phrase elle accède au compteur de Phrase et que
## quand elle est accédé de PhraseNoCasse est accède au compteur de
## PhraseNoCasse. En d'autres termes, il faudrait que la méthode num()
## reçoivent un référence vers l'objet classe qui l'appelle.

## C'est exactement ce que permet une méthode de classe. C'est une
## méthode bound à la classe d'appelle, elle va donc automatiquement
## recevoir la classe comme premier argument, et si elle est appelée
## depuis une instance, elle recevra un référence de la classe qui a
## créé cette instance.

## On définit une method de class avec la fonction built-in
## classmethod() Si l'on revient à notre exemple, on peut avoir un
## compteur d'instance distinct pour chaque sous classe.

#6m00s

class Phrase:
    nb_i = 0
    def __init__(self):
        Phrase.nb_i  = Phrase.nb_i + 1
        
    def num(cls):                 # new
        return cls.nb_i           # new
    
    num = classmethod(num)         # new

    
class PhraseNoCasse(Phrase):
    nb_i = 0                                          
    def __init__(self):
        PhraseNoCasse.nb_i  = PhraseNoCasse.nb_i + 1
        
    def num(cls):
        return f'PhraseNoCasse {cls.nb_i}'

    num = classmethod(num)

p = Phrase()
Phrase()

p_no = PhraseNoCasse()

p.num()
p_no.num()

p.num # bound method à la classe
Phrase.num # bound method à la classe


#8m00s
