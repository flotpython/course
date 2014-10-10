# -*- coding: iso-8859-15 -*-
from corrections.exercice import correction_table, correction_table_1arg, exemple_table, exemple_table_1arg

def correction_inconnue (composite, connue, inconnue):
    def regroup ():
        return connue + inconnue + connue
    def right_answer (): 
        return composite
    return correction_table (regroup, right_answer, [()])
