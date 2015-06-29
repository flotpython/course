# -*- coding: utf-8 -*-
from exercice_function import ExerciceFunction
from args import Args

# @BEG@ 3 5 decode_zen
# le module this est implémenté comme une petite énigme 
# comme le laissent entrevoir les indices, on y trouve
# (*) dans l'attribut 's' une version encodée du manifeste
# (*) dans l'attribut 'd' le code à utiliser pour décoder
# 
# ce qui veut dire qu'en première approximation on pourrait 
# obtenir une liste des caractères du manifeste en faisant
# 
# [ this.d [c] for c in this.s ]
# 
# mais ce serait le cas seulement si le code agissait sur 
# tous les caractères; comme ce n'est pas le cas il faut
# laisser intacts les caractères dans this.s qui ne sont pas
# dans this.d (dans le sens "c in this.d")
#
# je fais exprès de ne pas appeler l'argument this pour
# illustrer le fait qu'un module est un objet comme un autre
#

def decode_zen(this_module):
    "décode le zen de python à partir du module this"
    # la version encodée du manifeste
    encoded = this_module.s
    # le 'code' 
    code = this_module.d
    # si un caractère est dans le code, on applique le code
    # sinon on garde le caractère tel quel
    # aussi, on appelle 'join' pour refaire une chaîne à partir
    # de la liste des caractères décodés
    return ''.join([code[c] if c in code else c for c in encoded])
# @END@

# @BEG@ 3 5 decode_zen
# une autre version qui marche aussi, en utilisant 
# dict.get(key, default)
def decode_zen2(this):
    return "".join([this.d.get(c, c) for c in this.s])
# @END@

class ExerciceDecodeZen(ExerciceFunction):
    def correction(self, student_decode_zen, this):
        self.datasets = [Args(this)]
        return ExerciceFunction.correction(self, student_decode_zen)
    
    def resultat(self, this):
        return self.solution(this)

# cannot copy nor deepcopy a module
exo_decode_zen = ExerciceDecodeZen(
    decode_zen, "inputs_gets_overridden", copy_mode='none')
