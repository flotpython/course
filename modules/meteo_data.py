#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
import types
import time
# izip plutot que zip
import itertools
# une librairie pour les noms de fichier
import os.path
# une librairie pour décharger des donnees au dessus de http
import urllib2
# une librairie pour décompresser le format .gz
import zlib
# une librairie pour décortiquer le format json
import json

date_format="%Y-%m-%d:%H-%M"

KELVIN=273.15

cache_filename = "meteo_data.json"

# chercher par exemple entry['city']['id'] a partir d'un chemin genre ('city','id')
# i.e. xpath ( {'city':{'id':12,'name':'Montreal'}}, ['city','id']) => 12
def xpath (entry, path):
    result=entry
    for key in path: result=result[key]
    return result

# on a des megas...
def megas(bytes):
    megas=float(bytes)/1024**2
    megas=float(int(megas*10))/10
    return "%s Mo"%megas


# like in css we do: top right bottom left
france = ( 50, 8, 42, -5)
europe = ( 60, 26, 34, -12)

# determiner si une position est dans un rectangle donne
def in_area ( lat_lon_rec, css_4uple):
    (top, right, bottom, left)=css_4uple
    lon=lat_lon_rec['lon']
    lat=lat_lon_rec['lat']
    return lon>=left and lon<=right and lat>=bottom and lat<=top

def fetch_data ():

    print (40*'=')
    url = "http://78.46.48.103/sample/daily_14.json.gz"

    print ("Téléchargement de %s ..."%url)
    network_file=urllib2.urlopen(url)
    compressed_json=network_file.read()
    print ("OK - %s téléchargés"%megas(len(compressed_json)))
    uncompressed_json=zlib.decompress(compressed_json, zlib.MAX_WBITS | 16)
    print ("décompression terminée avec %s"%megas(len(uncompressed_json)))

    print ("Décodage json ...")
    all_cities = [ json.loads(line) for line in uncompressed_json.split("\n") if line ]
    print (40*'=')

    # nous avons a ce stade une entree json par ligne

    print ("Sur un total de %s villes"%len(all_cities))

    # on filtre les entrees qui correspondent a notre aire d'interet
    europe_cities = [ entry for entry in all_cities 
                      if in_area ( xpath (entry, ('city','coord')), europe ) ]
    print ("nous avons %s villes dans la zone 'europe'"%len(europe_cities))

    france_cities = [ entry for entry in all_cities 
                      if in_area ( xpath (entry, ('city','coord')), france ) ]
    print ("nous avons %s villes dans la zone 'france'"%len(france_cities))

    data_cities = france_cities
    with open(cache_filename,"w") as output:
        output.write (json.dumps(data_cities))
    print ("(Over)wrote {}".format(cache_filename))
    return data_cities

def find_data ():
    try:
        with open (cache_filename) as input:
            return json.loads(input.read())
    except:
        return fetch_data ()

def inspect_data (cities):
    city = cities [0]
    import pprint

    print ("Sample city")
    pprint.pprint (city)

    def nb_mesures (city): return len(city['data'])
    print ("sample city has {} measurement points".format(nb_mesures(city)))

    total_mesures = sum ( [ nb_mesures(city) for city in cities ] )
    extrapolated = nb_mesures (city) * len(cities)
    print ("there are a total of {} mesures (extrapolated was {})"\
           .format(total_mesures,extrapolated))

def meteo_data ():
    meteo_data = find_data ()
    print (40*'=', 'meteo_data ready')
    return meteo_data

meteo_data()
