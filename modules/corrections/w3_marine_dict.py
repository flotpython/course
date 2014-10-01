# -*- coding: iso-8859-15 -*-
from corrections.tools import correction_table, correction_table_1arg, exemple_table, exemple_table_1arg

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

def correction_merge (student_merge, extended, abbreviated):
    return correction_table (student_merge, merge, [ ( extended, abbreviated,) ] )

def resultat_merge (extended, abbreviated):
    return merge (extended, abbreviated)
    
