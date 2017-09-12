# -*- coding: utf-8 -*-

## < commencer avec le code ci dessous déjà dans IDLE >

class Phrase:
    def __init__(self, ma_phrase):  
        self.ma_phrase = ma_phrase
        self.mots = ma_phrase.split()

        
## Reprenons notre classe Phrase et supposons que vous souhaitions
## lever une exception quand la phrase est vide. On va créer pour cela
## une nouvelle exception.

## Lorsque vous voulez créer une nouvelle exception, dans 99% des cas
## vous avez uniquement besoin pour votre exception d'un nom et d'un
## message d'erreur.  Il est d'usage d'utiliser un terme explicite
## pour l'exception et de terminer un nom d'exception par le mot Error,
## comme pour les exception built-in.

## Il est en fait très simple de faire votre propre
## exception. Regardons un exemple...

class PhraseVideError(Exception):
    pass

## Pour lancer l'exception on utilise l'instruction raise.


class Phrase:
    def __init__(self, ma_phrase):  
        self.ma_phrase = ma_phrase
        if not ma_phrase:                  # new
            raise PhraseVideError()        # new
        self.mots = ma_phrase.split()

## Créons une phrase normale

Phrase('un mooc')

## et maintenant une phrase vide

Phrase('')

## On peut passer à l'exception une liste d'argument qui sera
## automatiquement mise dans un tuple nommé args. C'est le
## constructeur de Exception qui fait cela.


class Phrase:
    def __init__(self, ma_phrase):  
        self.ma_phrase = ma_phrase
        if not ma_phrase:
            raise PhraseVideError('phrase vide', 18) # message et code d'erreur
        self.mots = ma_phrase.split()
        
## on peut ensuite capturer cette exception et utiliser les arguments
## passés

try:
    Phrase("")
except PhraseVideError as e:
    print(e.args)


