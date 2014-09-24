# -*- coding: iso-8859-15 -*-
from corrections.tools import correction_table, correction_table_1arg, exemple_table, exemple_table_1arg

def diff (extended, abbreviated):
    extended_ids =          { ship[0] for ship in extended }
    abbreviated_ids =       { ship[0] for ship in abbreviated }
    abbreviated_only_ids =  abbreviated_ids - extended_ids
    both_ids =              abbreviated_ids & extended_ids
    extended_only_ids =     extended_ids - abbreviated_ids
    both_names =            { ship[4] for ship in extended if ship[0] in both_ids }
    extended_only_names =   { ship[4] for ship in extended if ship[0] in extended_only_ids }
    return extended_only_names, both_names, abbreviated_only_ids

# xxx celui-ci serait + élégant mais ne marche pas et je ne comprends pas pourquoi...
def diff2 (extended, abbreviated):
    extended_ids =     { ship[0] for ship in extended }
    abbreviated_only = { ship[0] for ship in abbreviated if ship[0] not in extended_ids }
    extended_only =    { ship[4] for ship in extended    if ship[0] not in abbreviated_only }
    both =             { ship[4] for ship in extended    if ship[0] in abbreviated_only }
    return extended_only, both, abbreviated_only

def correction_diff (student_diff, extended, abbreviated):
    return correction_table (student_diff, diff, [ ( extended, abbreviated,) ] )

def resultat_diff (extended, abbreviated):
    return diff (extended, abbreviated)
    
