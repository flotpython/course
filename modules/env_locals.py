# -*- coding: utf-8 -*-

"""
un module pour illustrer la fonction locals
"""

# pour afficher
from env_locals_globals import environnement

def temoin (x):
    "la fonction témoin"
    y = x ** 2
    print 20*'-','locals - entrée:'
    environnement(locals())

    for i in [1]:
        for j in [1]:
            print 20*'-','locals - boucle:'
            environnement(locals())
            
