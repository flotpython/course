# -*- coding: utf-8 -*-

"""
un module pour illustrer les fonctions globals et locals
"""

globale = "variable globale au module"

def environnement (env):
    """
    affiche un environnement
    pour faire court on affiche juste le type de chaque nom
    """
    for variable,valeur in env.items():
        print variable.ljust(20),":",type(valeur).__name__

def temoin (x):
    "la fonction témoin"
    y = x ** 2
    print 20*'-','globals:'
    environnement(globals())
    print 20*'-','locals:'
    environnement(locals())

class Foo:
    "une classe vide"
