
# pour importer un module entier en mode relatif
from . import random as local_random_module


# la syntaxe pour importer seulement un symbole
from .random import alea


print(
    f"""On charge main.py
    __name__={__name__}
    alea={alea()}""")
