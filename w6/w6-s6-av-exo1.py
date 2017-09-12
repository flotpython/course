# -*- coding: utf-8 -*-

## Nous allons commencer par implémenter directement un itérateur. Je
## vous rappelle que lorsqu'un objet est un itérateur on ne peut le
## parcourir qu'une fois

## Reprenons notre classe Phrase et augmentons la pour qu'elle
## deviennent un itérateur. N'hésitez pas à mettre la vidéo en pause
## pour avoir le temps de retrouver la class Phrase. 

class Phrase:
    def __init__(self, ma_phrase):  
        self.ma_phrase = ma_phrase
        self.mots = ma_phrase.split()

    def __len__(self):
        return len(self.mots)

    def __contains__(self, mot):                             
        return mot in self.mots
    
    def __str__(self):               
        return "\n".join(self.mots)

    ## mon objet est son propre itérateur
    def __iter__(self):                            #new
        return self                                #new

    ## next retourne le mot suivant jusqu'à ce
    ## qu'il n'y ait plus de mots dans la phrase.
    def __next__(self):                            #new
        if not self.mots:                          #new
            raise StopIteration                    #new
        return self.mots.pop(0)                    #new

p = Phrase("je fais un mooc sur python")
[m for m in p]
[m for m in p] #il n'y a qu'un itérateur par instance
## il faut refaire une instance pour itérer à nouveau.
p = Phrase("je fais un mooc sur python")
[m for m in p]

# 2m30

## Il est bien souvent plus pratique d'avoir un objet itérable qui
## produit autant d'itérateurs que nécessaire. Regardons un manière de
## rendre Phrase itérable.

class Phrase:
    def __init__(self, ma_phrase):  
        self.ma_phrase = ma_phrase
        self.mots = ma_phrase.split()

    def __len__(self):
        return len(self.mots)

    def __contains__(self, mot):                             
        return mot in self.mots
    
    def __str__(self):               
        return "\n".join(self.mots)

    ## mon objet est son propre itérateur
    def __iter__(self):                            #new
        return IterPhrase(self.mots)               #new

class IterPhrase():                                #new
    def __init__(self, mots):
        self.mots = mots[:]

    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.mots:
            raise StopIteration
        return self.mots.pop(0)

    
p = Phrase("je fais un mooc sur python")
[m for m in p]
[m for m in p]      #il y a de multiples itérateurs 


#5m22

## nous voyons donc que rendre Phrase itérable demande un petit
## effort, il faut créer une nouvelle classe itérateur. Il est
## cependant possible en exploitant la puissance des fonctions
## génératrice de se passer de l'implémentation de cet objet
## itérateur.

## Je vous rappelle qu'une fonction génératrice est une fonction qui
## lorsqu'on l'appelle crée automatiquement un nouvel objet
## itérateur. Par conséquent, si on implémente la méthode __iter__
## comme une fonction génératrice, on aura automatiquement un objet
## itérable. Regardons cela. 


class Phrase:
    def __init__(self, ma_phrase):  
        self.ma_phrase = ma_phrase
        self.mots = ma_phrase.split()

    def __len__(self):
        return len(self.mots)

    def __contains__(self, mot):                             
        return mot in self.mots
    
    def __str__(self):               
        return "\n".join(self.mots)

    ## La fonction génératrice produit un nouvel itérateur à chaque
    ## appel
    def __iter__(self):                            #new
        for m in self.mots:                        #new
            yield m                                #new

    
p = Phrase("je fais un mooc sur python")
[m for m in p]
[m for m in p]      #il y a de multiples itérateurs 


# 7m45s
