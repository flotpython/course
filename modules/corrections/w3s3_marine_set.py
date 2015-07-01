# -*- coding: utf-8 -*-
from exercice_function import ExerciceFunction
from args import Args

# @BEG@ week=3 sequence=3 name=diff
def diff(extended, abbreviated):
    """Calcule comme demandé dans l'exercice, et sous formes d'ensembles
(*) les noms des bateaux seulement dans extended
(*) les noms des bateaux présents dans les deux listes
(*) les ids des bateaux seulement dans abbreviated
    """
    ### on n'utilise que des ensembles dans tous l'exercice
    # les ids de tous les bateaux dans extended
    # une compréhension d'ensemble
    extended_ids = {ship[0] for ship in extended}
    # les ids de tous les bateaux dans abbreviated
    # idem
    abbreviated_ids = {ship[0] for ship in abbreviated}
    # les ids des bateaux seulement dans abbreviated
    # une difference d'ensembles
    abbreviated_only_ids = abbreviated_ids - extended_ids
    # les ids des bateaux dans les deux listes
    # une intersection d'ensembles
    both_ids = abbreviated_ids & extended_ids
    # les ids des bateaux seulement dans extended 
    # ditto
    extended_only_ids = extended_ids - abbreviated_ids
    # pour les deux catégories où c'est possible
    # on recalcule les noms des bateaux
    # par une compréhension d'ensemble
    both_names = \
          {ship[4] for ship in extended if ship[0] in both_ids}
    extended_only_names = \
          {ship[4] for ship in extended if ship[0] in extended_only_ids}
    # enfin on retourne les 3 ensembles sous forme d'un tuple
    return extended_only_names, both_names, abbreviated_only_ids
# @END@

# xxx celui-ci serait + élégant mais ne marche pas et je ne comprends pas pourquoi...
# possiblement parce que, comme l'a souligné une étudiante, il y a dans les données
# deux bateaux qui portent le même nom
def diff2(extended, abbreviated):
    extended_ids =     {ship[0] for ship in extended}
    abbreviated_only = {ship[0] for ship in abbreviated if ship[0] not in extended_ids}
    extended_only =    {ship[4] for ship in extended    if ship[0] not in abbreviated_only}
    both =             {ship[4] for ship in extended    if ship[0] in abbreviated_only}
    return extended_only, both, abbreviated_only

# on passe des copies pour éviter qu'un bout de code ne pollue
# tout l'exercice en modifiant le master 
import copy

class ExerciceDiff(ExerciceFunction):
    def correction(self, student_diff, extended, abbreviated):
        # start with the full dataset
        self.datasets = [Args(extended, abbreviated)]
        # make up a samples by taking only <sample> entries in each
        for sample in [10, 20, 40]:
            extended_sample = copy.deepcopy(extended[:sample])
            abbreviated_sample = copy.deepcopy(abbreviated[:sample])
            self.datasets.append(Args(extended_sample, abbreviated_sample))
        return ExerciceFunction.correction(self, student_diff)

    def resultat(self, extended, abbreviated):
        return self.solution(extended, abbreviated)

exo_diff = ExerciceDiff(diff, "inputs_gets_overridden")
    
