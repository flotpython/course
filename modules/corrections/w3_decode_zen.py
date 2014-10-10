# -*- coding: iso-8859-15 -*-
from corrections.exercice import correction_table, correction_table_1arg, exemple_table, exemple_table_1arg

def decode_this (the_this_module):
    encoded = the_this_module.s
    code = the_this_module.d
    return ''.join([ code[c] if c in code else c for c in encoded ])

def decode_this2 (the_this_module):
    return "".join ( [ the_this_module.d.get(c,c) for c in the_this_module.s ] )

def correction_decode_this (student_decode_this,this):
    # cannot copy not deepcopy a module
    return correction_table_1arg (student_decode_this, decode_this, [this], copy_mode='none')

def resultat_decode_this (this):
    return decode_this(this)
