# -*- coding: iso-8859-15 -*-


## Dans 99% des cas vous avez uniquement besoin
## pour votre exception d'un nom et d'un message
## d'erreur. C'est dans ce cas très simple de faire
## votre propre exception. Regardons un exemple...

## Il est d'usage d'utiliser un terme explicite pour
## l'excetion et de terminer un nom d'exception par
## le mot Error, comme pour les exception built-in.

class SplitError(Exception):
    pass

## Pour lancer l'exception on utilise l'instruction
## raise. On peut passer à l'exception une liste
## d'argument qui sera automatiquement mise dans un
## tuple nommé args. C'est le constructeur de Exception
## qui fait cela. 

x = 1
y = 'a'

#raise SplitError('message...', x, y)

## on peut ensuite capturer cette exception et utiliser
## les arguments passés

try:
    raise SplitError('message...', x, y)
except SplitError as e:
    print e.args


## Mais comme une exception est une vraie classe, on peut
## surcharger le constructeur et ajouter des méthodes.
## En particulier, on peut utiliser des arguments nommés
## dans le contructeur, mais il faut évidamment les
## documenter.

class SplitError(Exception):
    """Exception lors de l'operation splitting.

    Attributs:
        val -- message d'erreur
        res -- valeur lors de l'erreur
    """
    def __init__(self, val, res):
        self.val = val
        self.res = res

#raise SplitError(res = 8, val = 'message...')

try:
    raise SplitError(res = 8, val = 'message...')
except SplitError as e:
    print e.res, e.val

