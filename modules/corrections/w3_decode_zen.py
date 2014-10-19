# -*- coding: iso-8859-15 -*-
from exercice import Exercice, Exercice_1arg, Exercice_multiline

# @BEG@ 3 5 decode_zen
def decode_zen (the_this_module):
    encoded = the_this_module.s
    code = the_this_module.d
    return ''.join([ code[c] if c in code else c for c in encoded ])
# @END@

def decode_zen2 (the_this_module):
    return "".join ( [ the_this_module.d.get(c,c) for c in the_this_module.s ] )

class ExerciceDecodeZen (Exercice):
    # on surcharge correction pour capturer les arguments
    def correction (self, student_decode_zen, this):
        self.inputs = [ (this,) ]
        return Exercice.correction (self, student_decode_zen)
    
    def resultat (self, this):
        return self.solution(this)

# cannot copy not deepcopy a module
exo_decode_zen = ExerciceDecodeZen (decode_zen, "inputs_gets_overridden", copy_mode='none')
