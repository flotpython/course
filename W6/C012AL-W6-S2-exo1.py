# -*- coding: iso-8859-15 -*-

## Il y a trois manieres d'implémenter un itérateur
## pour ses objets. Commençons par la permière.
## je veux que mon objet soit son propre itérateur,
## donc on ne peut itérer qu'un fois sur chaque objet.
## C'est ce que l'on a pour les fichiers 


class Mots():
    ## ma classe Objet prend un phrase à la contruction
    ## et la découpe en mots
    def __init__(self, phrase):
        self.list_mots = phrase.split()
        self.count = 0

    ## mon objet et son propre itérateur
    def __iter__(self):
        return self

    ## next retourne le mot suivant jusqu'à ce
    ## qu'il n'y ait plus de mots dans la phrase.
    def next(self):
        if self.count == len(self.list_mots):
            raise StopIteration
        self.count = self.count + 1
        return self.list_mots[self.count - 1]

m = Mots("spam spam spam egg beans spam")
print [x for x in m]
print [x for x in m] #il n'y a qu'un itérateur par instance
## il faut refaire une instance pour itérer à nouveau.
m = Mots("spam spam spam egg beans spam")
print [x for x in m]

## la deuxième manière consiste à avoir un nouvel
## objet itérateur à chaque fois que l'on itere sur
## une instance de Mot. C'est ce que l'on a pour les
## listes.

class Mots():
    def __init__(self, phrase):
        self.list_mots = phrase.split()

    def __iter__(self):
        return IterMots(self.list_mots)

class IterMots():
    def __init__(self, phrase):
        self.list_mots = phrase
        self.count = 0

    def __iter__(self):
        return self
    
    def next(self):
        if self.count == len(self.list_mots):
            raise StopIteration
        self.count = self.count + 1
        return self.list_mots[self.count - 1]

m = Mots("spam spam spam egg beans spam")
print [x for x in m]
print [x for x in m]        #il y a de multiples itérateurs 

## la dernière manière donne le même résultat que la
## précédente (de multiple itérateur par instance),
## mais en exploitant la puissance des fonctions génératrices

class Mots():
    def __init__(self, phrase):
        self.list_mots = phrase.split()

    def __iter__(self):
        for i in self.list_mots:
            yield i

m = Mots("spam spam spam egg beans spam")
print [x for x in m]
print [x for x in m]        #il y a de multiples itérateurs 
