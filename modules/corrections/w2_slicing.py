# -*- coding: utf-8 -*-
from exercice import Exercice, Args

alphabet = "0123456789abcdef"

# on calcule connue et inconnue comme une chaine aleatoire
import random
connue   = "".join(random.sample(alphabet, random.randint(3, 6)))
inconnue = "".join(random.sample(alphabet, random.randint(5, 8)))
composite = connue + inconnue + connue

class ExerciceInconnue(Exercice):
    def __init__(self, connue, composite):
        # on appelle Exercice.__init__ pour remplir tous les champs
        # mais self.datasets sera en fait rempli plus tard
        # une petite clôture..
        def target(inconnue): 
            return composite
        Exercice.__init__(self, target, None)
        self.connue = connue
        self.composite = composite
    def correction(self, inconnue):
        # dans notre cas il n'y a qu'un seul jeu d'entrées
        self.datasets = [ Args(inconnue) ]
        def check(inconnue):
            return self.connue + inconnue + self.connue
        return Exercice.correction(self, check)

exo_inconnue = ExerciceInconnue(connue, composite)

####################
# la solution est bien sûr
# @BEG@ 2 3 composite
# Pour calculer inconnue, on extrait une sous-chaine de composite
# qui commence a l'index len(connue)
# qui se termine a l'index len(composite)-len(connue)
# ce qui donne en utilisant une slice
inconnue = composite [ len(connue) : len(composite)-len(connue) ]
#
# on peut aussi faire encore plus simplement
inconnue = composite [ len(connue) : -len(connue) ]
# @END@
