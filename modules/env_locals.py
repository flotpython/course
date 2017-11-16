"""
un module pour illustrer la fonction locals
"""

# pour afficher
from env_locals_globals import display_env

def temoin(x):
    "la fonction témoin"
    y = x ** 2
    print(20*'-', 'locals - entrée:')
    display_env(locals())

    for i in (1,):
        for j in (1,):
            print(20*'-', 'locals - boucles for:')
            display_env(locals())
            
