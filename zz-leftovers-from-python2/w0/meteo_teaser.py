#!/usr/bin/env python
# -*- coding: utf-8 -*-

# for flushing stdout
import sys
# dealing with filenames
import os.path
# for formatting timestamps
import time
# using izip rather than zip
import itertools
# downloading data
import urllib2
# uncompress data
import zlib
# unmarshalling JSON data
import json

# visualization
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt

daily14_gz_url = "http://78.46.48.103/sample/daily_14.json.gz"
daily14_gz_cache = "daily_14.json.gz.cache"
daily14_cache = "daily_14.json.cache"

upper_left_lat_lon = ( 50, -5)
lower_right_lat_lon = (42, 8)

date_format="%Y-%m-%d:%H-%M"

# chercher par exemple entry['city']['id'] a partir d'un chemin genre ('city','id')
# i.e. xpath ( {'city':{'id':12,'name':'Montreal'}}, ['city','id']) => 12
def xpath (entry, path):
    result=entry
    for key in path:
        result=result[key]
    return result

#################### peut-etre pas utile
# calculer un hash de toutes les entrees par une cle obtenue a partir d'un chemin
# e.g. 
# entries = [ {'city':{'name':'Grenoble'},'data':data1}, {'city':{'name':'Toulouse'},'data':data2} ]
# path = ('city','name')
# result = { 'Grenoble': [ {'city':{'name':'Grenoble'},'data':data1}],
#            'Toulouse': [ {'city':{'name':'Toulouse'},'data':data2} ],
# }
def hash_by_path (entries, path):
    result = {}
    for entry in entries:
        key=xpath(entry,path)
        if key not in result: result[key]=[]
        result[key].append(entry)
    return result
#################### peut-etre pas utile

# aller chercher les donnees a une url et les decompresser 
# ou les prendre dans le cache s'il exite
def fetch_compressed_data (url,cache):
    if os.path.isfile(cache):
        # il faudrait verifier la date de ce cache..
        print "%s: on utilise le cache %s"%(url,cache)
        with open(cache) as f: 
            return f.read()
    print "Téléchargement de %s ..."%url,
    sys.stdout.flush()
    network_file=urllib2.urlopen(url)
    compressed_json=network_file.read()
    with open(daily14_gz_cache, 'w') as gzip_cache:
        print "Saving gzip cache", daily14_gz_cache
        gzip_cache.write(compressed_json)
        
    print " OK - %s octets"%len(compressed_json)
    # http://stackoverflow.com/questions/3122145/zlib-error-error-3-while-decompressing-incorrect-header-check
    uncompressed_json=zlib.decompress(compressed_json, zlib.MAX_WBITS | 16)
    print "décompression terminée"
    with open(cache,'w') as f:
        print "%s: on sauve dans le cache %s"%(url,cache)
        f.write(uncompressed_json)
    return uncompressed_json

# determiner si une position est dans un rectangle donne
def in_area ( lat_lon_rec, upper_left_lat_lon, lower_right_lat_lon):
    (upper,left)=upper_left_lat_lon
    (lower,right)=lower_right_lat_lon
    lon=lat_lon_rec['lon']
    lat=lat_lon_rec['lat']
    return lon>=left and lon<=right and lat>=lower and lat <= upper

# enchainer le tout
def main ():
    raw_daily14 = fetch_compressed_data (daily14_gz_url, daily14_cache)

    print "Décodage json ...", 
    sys.stdout.flush()
    # nous avons a ce stade une entree json par ligne
    all_entries = [ json.loads(line) for line in raw_daily14.split("\n") if line ]
    print "OK, nous avons %s entrées de ville"%len(all_entries)
    
    # on filtre les entrees qui correspondent a notre aire d'interet
    entries_in_area = [ entry for entry in all_entries 
                        if in_area ( xpath (entry, ('city','coord')), 
                                     upper_left_lat_lon, lower_right_lat_lon) ]
    print "nous avons %s entrées dans la zone"%len(entries_in_area)

    # ajouter la date sous un format lisible par un humain
    for entry in all_entries:
        for cell in entry['data']:
            cell['date']= time.strftime(date_format,time.localtime(cell['dt'])) 

    # creer une table de hash sur le nom de la ville
    hash_by_city_name = hash_by_path (entries_in_area, ('city','name'))
    print "nous avons %s noms de villes différents"%len(hash_by_city_name)

    # on cherche l'entrée correspondant à Paris
    if 'Paris' in hash_by_city_name:
        entry=hash_by_city_name['Paris'][0]
        print "Il y a %s entrees pour Paris"%len(entry['data'])
        for cell in entry['data']: print cell['date'],'pression=',cell['pressure']

    # grouper les entrees par l'initiale du nom, afficher une ville par entree
    hash_by_first_letter = hash_by_path (entries_in_area, ('city', 'name', 0))
    for letter in [ str(chr(ord('A')+i)) for i in xrange(26) ]:
        try: 
            entry=hash_by_first_letter[letter][0]
            print letter,":",entry['city']['name'],"..."
        except: 
            # pas de ville commencant par cette lettre
            pass

    # montrer les villes qui font l'objet de plusieurs entrees
    duplicates = [ (name,l) for (name,l) in hash_by_city_name.iteritems() if len(l) >=2 ]
    for (name,l) in duplicates:
        print "DUP: ",name

    # visualiser l'ensemble des positions lon/lat
    LON_s = [ entry['city']['coord']['lon'] for entry in all_entries ]
    LAT_s = [ entry['city']['coord']['lat'] for entry in all_entries ]
    # mettre une taille et une couleur particuliere pour ceux qu'on a retenus
    for entry in entries_in_area: entry['selected']=True
    colors = [ 'r' if  'selected' in entry else 'b' for entry in all_entries ]
    sizes = [ 30 if 'selected' in entry else 1 for entry in all_entries ]
    plt.scatter(LON_s, LAT_s, c=colors, s=sizes)

    # génération d'un fichier csv et visualisation
    # pour faire simple on va visualiser la pression observee dans la zone le premier jour
    # xxx on admet que tous les tableaux de 'data' sont synchrones
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X = [ xpath (entry, ('city','coord','lon')) for entry in entries_in_area ]
    Y = [ xpath (entry, ('city','coord','lat')) for entry in entries_in_area ]
    names = [ xpath (entry, ('city','name')) for entry in entries_in_area ]
    for day in xrange(14): 
        dates = [ entry['data'][day]['date'] for entry in entries_in_area ]
        P = [ xpath (entry, ('data',day,'pressure')) for entry in entries_in_area ]
        T = [ xpath (entry, ('data',day,'temp','day')) for entry in entries_in_area ]
        # generer un fichier csv avec toutes ces donnees pour la derniere valeur de 'day'
        filename = "daily_14_day_%s.csv"%day
        with open(filename,'w') as csv:
            csv.write("nom;longitude;latitude;date;temperature;pression;\n")
            for (name,x,y,date,temp,p) in itertools.izip(names,X,Y,dates,T,P):
                csv.write("%s;%s;%s;%s;%s;%s;\n"%(name,x,y,date,temp,p))
        print "Données générées dans %s"%filename

        # on visualise la pression -- seulement pour le premier jour
        if day==0:
            date = dates[0]
            print "Visualisation de la pression observée le ",date
            ax.plot_trisurf(X,Y,P, cmap=cm.jet, linewidth=0.2, label="Pression le %s"%date)
    plt.show()

if __name__ == '__main__': main()
