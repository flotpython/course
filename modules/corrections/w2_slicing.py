# -*- coding: iso-8859-15 -*-
from exercice import Exercice, Exercice_1arg, Exercice_multiline

alphabet = "0123456789abcdef"

# on calcule connue et inconnue comme une chaine aleatoire
import random
connue   = "".join(random.sample(alphabet, random.randint(3,6)))
inconnue = "".join(random.sample(alphabet, random.randint(5,8)))
composite = connue + inconnue + connue

class ExerciceInconnue (Exercice):
    def __init__ (self, connue, composite):
        # on appelle Exercice.__init__ pour remplir tous les champs
        Exercice.__init__ (self,None,None)
        self.connue = connue
        self.composite = composite
        # a small closure evey now and then can help out
        def target (inconnue): 
            return composite
        self.solution = target
    def correction (self, inconnue):
        self.inputs = [ (inconnue,) ]
        def check (inconnue):
            return self.connue + inconnue + self.connue
        return Exercice.correction (self, check)

exo_inconnue = ExerciceInconnue (connue, composite)

####################
# la solution est bien sûr
inconnue = composite [ len(connue) : len(composite)-len(connue) ]
