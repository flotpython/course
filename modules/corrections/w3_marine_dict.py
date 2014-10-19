# -*- coding: iso-8859-15 -*-
from exercice import Exercice, Exercice_1arg, Exercice_multiline

# @BEG@ 3 2 merge
def merge (extended, abbreviated):
    """
Consolide des données étendues et des données abrégées
comme décrit dans l'énoncé
Le coût de cette fonction est linéaire dans la taille 
des données (longueur des listes)
    """
    # on initialise le résultat avec un dictionnaire vide
    result = {}
    # pour les données étendues
    for ship in extended:
        # on affecte les 6 premiers champs
        # et on ignore les champs de rang 6 et au delà
        id, latitude, longitude, timestamp, name, country = ship [:6]
        # on crée une entrée dans le résultat, 
        # avec la mesure correspondant aux données étendues
        result[id] = [ name, country, (latitude, longitude, timestamp) ]
    # maintenant on peut compléter le résultat avec les données abrégées
    for id, latitude, longitude, timestamp in abbreviated:
        # et avec les hypothèses on sait que le bateau a déjà été 
        # inscrit dans le résultat, donc on peut se contenter d'ajouter 
        # la mesure abrégée correspondant au bateau
        result [id] . append ( (latitude, longitude, timestamp) )
    # et retourner le résultat
    return result
# @END@

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
        self.datasets = [ ((extended, abbreviated), {}) ]
        return Exercice.correction (self, student_merge)

    # une fonction pour exposer le resultat attendu
    def resultat (self, extended, abbreviated):
        return self.solution (extended, abbreviated)

exo_merge = ExerciceMerge (merge, "inputs_gets_overridden")
    
