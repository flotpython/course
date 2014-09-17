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

def main ():
    data_cities = find_data ()

    inspect_data (data_cities)

main()

exit()

# visualiser l'ensemble des positions lon/lat
print ("Les points de relèvement en Europe")
LON_s = [ entry['city']['coord']['lon'] for entry in all_cities ]
LAT_s = [ entry['city']['coord']['lat'] for entry in all_cities ]
# mettre une taille et une couleur particuliere pour ceux qu'on a retenus
for entry in europe_cities: entry['selected']=True
# les entrées dans la zone d'intérêt en rouge
colors = [ 'r' if  'selected' in entry else 'b' for entry in all_cities ]
# et un peu plus grosses
sizes = [ 30 if 'selected' in entry else 1 for entry in all_cities ]
plt.scatter(LON_s, LAT_s, c=colors, s=sizes)

print (40*'=')
plt.show()

# pour faire simple on va visualiser la pression observee dans la zone le premier jour
day=0
dt=xpath(europe_cities[0],('data',day,'dt'))
date=time.strftime(date_format,time.localtime(dt))
print ("Visualisation de la pression observée le ",date)
fig = plt.figure()
ax = fig.gca(projection='3d')
X = [ xpath (entry, ('city','coord','lon')) for entry in europe_cities ]
Y = [ xpath (entry, ('city','coord','lat')) for entry in europe_cities ]
T_celsius = [ xpath (entry, ('data',day,'temp','day')) - KELVIN for entry in europe_cities ]
ax.plot_trisurf(X,Y,T_celsius, cmap=cm.jet, linewidth=0.2, label="Température le %s"%date)
ax.set_title ("Pression en Europe relevee le %s"%date)

print (40*'=')
plt.show()

