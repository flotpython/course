"""
un module pour illustrer les fonctions globals et locals
"""

globale = "variable globale au module"

def display_env(env):
    """
    affiche un environnement
    on affiche juste le nom et le type de chaque variable
    """
    for variable, valeur in sorted(env.items()):
        print("{:>20} → {}".format(variable, type(valeur).__name__))

def temoin(x):
    "la fonction témoin"
    y = x ** 2
    print(20 * '-', 'globals:')
    display_env(globals())
    print(20 * '-', 'locals:')
    display_env(locals())

class Foo:
    "une classe vide"
