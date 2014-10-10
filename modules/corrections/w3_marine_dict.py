# -*- coding: iso-8859-15 -*-
from exercice import Exercice, Exercice_1arg, Exercice_multiline

def merge (extended, abbreviated):
    result = {}
    for ship in extended:
        id, latitude, longitude, timestamp, name, country = ship [:6]
        result[id] = [ name, country, (latitude, longitude, timestamp) ]
    for id, latitude, longitude, timestamp in abbreviated:
        result [id] . append ( (latitude, longitude, timestamp) )
    return result

def merge2 (extended_data, abbreviated_data):
    result = {}
    for ship in extended_data:
        result [ship[0]] = ship[4:6]
        result [ship[0]] .append ( tuple (ship[1:4]))
    for ship in abbreviated_data:
        result [ship[0]] .append( tuple (ship[1:4]))
    return result

class ExerciceMerge (Exercice):

    # on surcharge correction pour capturer les arguments
    def correction (self, student_merge, extended, abbreviated):
        self.inputs = [ (extended, abbreviated) ]
        return Exercice.correction (self, student_merge)

    # une fonction pour exposer le resultat attendu
    def resultat (self, extended, abbreviated):
        return self.solution (extended, abbreviated)

exo_merge = ExerciceMerge (merge, "inputs_gets_overridden")
    
