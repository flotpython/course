# -*- coding: iso-8859-15 -*-
from exercice import Exercice, Exercice_1arg, Exercice_multiline

# @BEG@ diff
def diff (extended, abbreviated):
    extended_ids =          { ship[0] for ship in extended }
    abbreviated_ids =       { ship[0] for ship in abbreviated }
    abbreviated_only_ids =  abbreviated_ids - extended_ids
    both_ids =              abbreviated_ids & extended_ids
    extended_only_ids =     extended_ids - abbreviated_ids
    both_names =            { ship[4] for ship in extended if ship[0] in both_ids }
    extended_only_names =   { ship[4] for ship in extended if ship[0] in extended_only_ids }
    return extended_only_names, both_names, abbreviated_only_ids
# @END@

# xxx celui-ci serait + élégant mais ne marche pas et je ne comprends pas pourquoi...
def diff2 (extended, abbreviated):
    extended_ids =     { ship[0] for ship in extended }
    abbreviated_only = { ship[0] for ship in abbreviated if ship[0] not in extended_ids }
    extended_only =    { ship[4] for ship in extended    if ship[0] not in abbreviated_only }
    both =             { ship[4] for ship in extended    if ship[0] in abbreviated_only }
    return extended_only, both, abbreviated_only

import copy

class ExerciceDiff (Exercice):
    def correction (self, student_diff, extended, abbreviated):
        # start with the full dataset
        self.inputs = [ (extended, abbreviated) ]
        # make up a samples by taking only <sample> entries in each
        for sample in [ 10, 20, 40]:
            extended_sample = copy.deepcopy (extended[:sample])
            abbreviated_sample = copy.deepcopy (abbreviated[:sample])
            self.inputs.append ( (extended_sample, abbreviated_sample ) )
        return Exercice.correction (self,student_diff)

    def resultat (self, extended, abbreviated):
        return self.solution (extended, abbreviated)

exo_diff = ExerciceDiff (diff, "inputs_gets_overridden")
    
