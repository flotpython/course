---
ipub:
  sphinx:
    toggle_input: true
    toggle_input_all: true
    toggle_output: true
    toggle_output_all: true
jupytext:
  cell_metadata_filter: all
  formats: md:myst
  notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
livereveal:
  auto_select: code
  auto_select_fragment: true
  autolaunch: false
  backimage: media/nologo.png
  height: 100%
  start_slideshow_at: selected
  theme: simple
  transition: fade
  width: 100%
notebookname: exo. classes
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Exercice sur l'utilisation des classes

+++

### Introduction

+++

##### Objectifs de l'exercice

+++

Maintenant que vous avez un bagage qui couvre toutes les bases du langage, cette semaine nous ne ferons qu'un seul exercice de taille un peu plus réaliste. Vous devez écrire quelques classes, que vous intégrez ensuite dans un code écrit pas nos soins. 

L'exercice comporte donc à la fois une part lecture et une part écriture. 

Par ailleurs, cette fois-ci l'exercice n'est plus à faire dans un notebook ; vous êtes donc également incités à améliorer autant que possible l'environnement de travail sur votre propre ordinateur.

+++

##### Objectifs de l'application

+++

Dans le prolongement des exercices de la semaine 3 sur les données maritimes, l'application dont il est question ici fait principalement ceci :

* en entrée :
  * agréger des données obtenues auprès de marinetraffic ;
* et produire en sortie :
  * un fichier texte qui liste par ordre alphabétique les bateaux concernés, et le nombre de positions trouvées pour chacun ;
  * et un fichier KML, pour exposer les trajectoires trouvées à Google Earth, Google Maps ou autre outil similaire.
   
Les données générées dans ces deux fichiers sont triées dans l'ordre alphabétique, de façon à permettre une comparaison des résultats sous forme textuelle. Plus précisément, on trie les bateaux selon le critère suivant :

 * ordre alphabétique sur le nom des bateaux ;
 * et ordre sur les `id` en cas d'ex-aequo (il y a des bateaux homonymes dans cet échantillon réel).

+++

Voici à quoi ressemble le fichier KML obtenu avec les données que nous fournissons, une fois ouvert sous Google Earth :

<img src="media/ships-in-earth.png">

+++

##### Choix d'implémentation

+++

En particulier, dans cet exercice nous allons voir comment on peut gérer des données sous forme d'instances de classes plutôt que de types de base. Cela résonne avec la discussion commencée en Semaine 3, Séquence "Les dictionnaires", dans le complément "record-et-dictionnaire". 

Dans les exercices de cette semaine-là nous avions uniquement utilisé des types "standard" comme listes, tuples et dictionnaires pour modéliser les données, cette semaine nous allons faire le choix inverse et utiliser plus souvent des (instances de) classes.

+++

##### Principe de l'exercice

+++

On a écrit une application complète, constituée de 4 modules ; on vous donne le code de trois de ces modules et vous devez écrire le module manquant.

+++

##### Correction

+++

Tout d'abord nous fournissons un jeu de données d'entrées. De plus, l'application vient avec son propre système de vérification, qui est très rustique. Il consiste à comparer, une fois les sorties produites, leur contenu avec les sorties de référence, qui ont été obtenues avec notre version de l'application. 

Du coup, le fait de disposer de Google Earth sur votre ordinateur n'est pas strictement nécessaire, on ne s'en sert pas à proprement parler pour l'exercice.

+++

***

+++

### Mise en place

+++

##### Partez d'un répertoire vierge

+++

Pour commencer, créez-vous un répertoire pour travailler à cet exercice.

+++

##### Les données

+++

Commencez par y installer les données que nous publions dans les formats suivants :

* au format [tar](data/ships-json.tar)
* au format [tar compressé](data/ships-json.tgz)
* au format [zip](data/ships-json.zip)

Une fois installées, ces données doivent se trouver dans un sous-répertoire `json/` qui contient 133 fichiers `*.json` :

* `json/2013-10-01-00-00--t=10--ext.json`
* `...`
* `json/2013-10-01-23-50--t=10.json`

+++

Comme vous pouvez le deviner, il s'agit de données sur le mouvement des bateaux dans la zone en date du 10 Octobre 2013 ; et comme vous le devinez également, on a quelques exemplaires de données étendues, mais dans la plupart des cas il s'agit de données abrégées.

+++

##### Les résultats de référence

+++

De même il vous faut installer les résultats de référence que vous trouvez ici :

* au format [tar](data/ships-ref.tar)
* au format [tar compressé (tgz)](data/ships-ref.tgz)
* au format [zip](data/ships-ref.zip)

Quel que soit le format choisi, une fois installé ceci doit vous donner trois fichiers :

* `ALL_SHIPS.kml.ref`
* `ALL_SHIPS.txt.ref`
* `ALL_SHIPS-v.txt.ref`

+++

**Avertissement** l'idée de publier ces fichiers de référence, c'est bien sûr de vous permettre de vérifier vos propres résultats; dans l'idéal on peut faire une comparaison **exacte** des fichiers obtenus, mais j'attire votre attention sur le fait que, comme l'exercice fait pas mal de **calculs flottants**, il est tout à fait possible d'écrire un code correct qui obtienne des résultats **très légèrement différents**.

+++

##### Le code

+++

Vous pouvez à présent aller chercher les 3 modules suivants :

* [`merger.py`](data/merger.py)
* [`compare.py`](data/compare.py)
* [`kml.py`](data/kml.py)
 
et les sauver dans le même répertoire.

Vous remarquerez que le code est cette fois entièrement rédigé en anglais, ce que nous vous conseillons de faire aussi souvent que possible.

Votre but dans cet exercice est d'écrire le module manquant `shipdict.py` qui permettra à l'application de fonctionner comme attendu.

+++

***

+++

### Fonctionnement de l'application

+++

##### Comment est structurée l'application

+++

Le point d'entrée s'appelle `merger.py`

Il utilise trois modules annexes, qui sont :

* `shipdict.py`, qui implémente les classes
  * `Position` qui contient une latitude, une longitude, et un timestamp
  * `Ship` qui modélise un bateau à partir de son `id` et optionnellement  `name` et `country`
  * `ShipDict`, qui maintient un index des bateaux (essentiellement un dictionnaire)

* `compare.py` qui implémente
  * la classe `Compare` qui se charge de comparer les fichiers résultat avec leur version de référence

* `kml.py` qui implémente
  * la classe `KML` dans laquelle sont concentrées les fonctions liées à la génération de KML ; c'est notamment en fonction de nos objectifs pédagogiques que ce choix a été fait.

+++

##### Lancement

+++

Lorsque le programme est complet et qu'il fonctionne correctement, on le lance comme ceci :

```bash
$ python3 merger.py json/*
Opening ALL_SHIPS.txt for listing all named ships
Opening ALL_SHIPS.kml for ship ALL_SHIPS
Comparing ALL_SHIPS.txt and ALL_SHIPS.txt.ref -> OK
Comparing ALL_SHIPS.kml and ALL_SHIPS.kml.ref -> OK
```    

qui comme on le voit produit :

* `ALL_SHIPS.txt` qui résume, par ordre alphabétique les bateaux qu'on a trouvés et le nombre de positions pour chacun, et 
* `ALL_SHIPS.kml` qui est le fichier au format `KML` qui contient toutes les trajectoires.

+++

##### Mode bavard (verbose)

+++

On peut également lancer l'application avec l'option `--verbose` ou simplement `-v` sur la ligne de commande, ce qui donne un résultat plus détaillé. Le code KML généré reste inchangé, mais la sortie sur le terminal et le fichier de résumé sont plus étoffés :

```python
$ python3 merger.py --verbose json/*.json
Opening json/2013-10-01-00-00--t=10--ext.json for parsing JSON
Opening json/2013-10-01-00-10--t=10.json for parsing JSON
...
Opening json/2013-10-01-23-40--t=10.json for parsing JSON
Opening json/2013-10-01-23-50--t=10.json for parsing JSON
Opening ALL_SHIPS-v.txt for listing all named ships
Opening ALL_SHIPS.kml for ship ALL_SHIPS
Comparing ALL_SHIPS-v.txt and ALL_SHIPS-v.txt.ref -> OK
Comparing ALL_SHIPS.kml and ALL_SHIPS.kml.ref -> OK
```

À noter que dans le mode bavard toutes les positions sont listées dans le résumé au format texte, ce qui le rend beaucoup plus bavard comme vous pouvez le voir en inspectant la taille des deux fichiers de référence :

```python
$ ls -l ALL_SHIPS*txt.ref v2.0
-rw-r--r--  1 parmentelat  staff  1438681 Dec  4 16:20 ALL_SHIPS-v.txt.ref
-rw-r--r--  1 parmentelat  staff    15331 Dec  4 16:20 ALL_SHIPS.txt.ref
-rw-r--r--  1 parmentelat  staff        0 Dec  4 16:21 v2.0
```

+++

##### `merger.py --help`

+++

```bash
$ merger.py --help
usage: merger.py [-h] [-v] [-s SHIP_NAME] [-z] [inputs [inputs ...]]

positional arguments:
  inputs
    
optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Verbose mode
  -s SHIP_NAME, --ship SHIP_NAME
                        Restrict to ships by that name
  -z, --gzip            Store kml output in gzip (KMZ) format
```

+++

##### Un mot sur les données

+++

**Attention**, le contenu détaillé des champs `extended` et `abbreviated` peut être légèrement différent de ce qu'on avait pour les exercices de la semaine 3, dans lesquels certaines simplifications ont été apportées.

Voici ce avec quoi on travaille cette fois-ci :

```python
>>> extended[0]
[228317000, 48.76829, -4.334262, 75, 333, u'2013-09-30T21:54:00', u'MA GONDOLE', 30, 0, u'FGSA', u'FR', u'', u'', u'', u'CLASS B', u'', 13, 3, 0, u'', u'', u'']
```

c'est-à-dire :

```python
[ id, latitude, longitude, _, _, timestamp, name, _, _, _, country, ...]
```

et en ce qui concerne les données abrégées :

```python
>>> abbreviated[0]
[232005670, 49.39331, -5.939922, 33, 269, 3, u'2013-10-01T06:08:00']
```

c'est-à-dire :

```python
[ id, latitude, longitude, _, _, _, timestamp]
```

+++

Il y a unicité des `id` bien entendu (deux relevés qui portent le même `id` concernent le même bateau). 

**Note historique** Dans une première version de cet exercice, on avait laissé des doublons, c'est-à-dire des bateaux différents mais de même nom. Afin de rendre l'exercice plus facile à corriger (notamment parce que la comparaison des résultats repose sur l'ordre alphabétique), dans la présente version ces doublons ont été enlevés. Sachez toutefois que cette unicité est artificielle, aussi efforcez-vous de ne pas écrire de code qui reposerait sur cette hypothèse.

+++

***

+++

***

+++

## Niveaux pour l'exercice

+++

Quel que soit le niveau auquel vous choisissez de faire l'exercice, nous vous conseillons de commencer par lire intégralement les 3 modules qui sont à votre disposition, dans l'ordre :

* `merger.py` qui est le chef d'orchestre de toute cette affaire ;
* `compare.py` qui est très simple ;
* `kml.py` qui ne présente pas grand intérêt en soi si ce n'est pour l'utilisation de [la classe `string.Template`](https://docs.python.org/3/library/string.html#template-strings) qui peut être utile dans d'autres contextes également.

+++

****

+++

En **niveau avancé**, l'énoncé pourrait s'arrêter là ; vous lisez le code qui est fourni et vous en déduisez ce qui manque pour faire fonctionner le tout. En cas de difficulté liée aux arrondis avec le mode bavard, vous pouvez toutefois vous inspirer du code qui est donné dans la toute dernière section de cet énoncé (section "Un dernier indice"), pour traduire un flottant en représentation textuelle.

+++

Vous pouvez considérer que vous avez achevé l'exercice lorsque les deux appels suivants affichent les deux dernières lignes avec OK :

```python
$ python3 merger.py json/*.json
...
Comparing ALL_SHIPS.txt and ALL_SHIPS.txt.ref -> OK
Comparing ALL_SHIPS.kml and ALL_SHIPS.kml.ref -> OK
```

```
$ python3 merger.py -v json/*.json
...
Comparing ALL_SHIPS-v.txt and ALL_SHIPS-v.txt.ref -> OK
Comparing ALL_SHIPS.kml and ALL_SHIPS.kml.ref -> OK
```

+++

Le cas où on lance `merger.py` avec l'option bavarde est facultatif.

+++

***

+++

En **niveau intermédiaire**, nous vous donnons ci-dessous un extrait de ce que donne `help` sur les classes manquantes de manière à vous donner une indication de ce que vous devez écrire.

+++

##### Classe `Position`

+++

```python
    Help on class Position in module shipdict:
    
    class Position(__builtin__.object)
     |  a position atom with timestamp attached
     |  
     |  Methods defined here:
     |  
     |  __init__(self, latitude, longitude, timestamp)
     |      constructor
     |  
     |  __repr__(self)
     |      only used when merger.py is run in verbose mode
     |  
```

+++

**Notes**

 * certaines autres classes comme `KML` sont également susceptibles d'accéder aux champs internes d'une instance de la classe `Position` en faisant simplement `position.latitude`
 * La classe `Position` redéfinit `__repr__`, ceci est utilisé uniquement dans la sortie en mode bavard.

+++

##### Classe `Ship`

+++

```python
    Help on class Ship in module shipdict:
    
    class Ship(__builtin__.object)
     |  a ship object, that requires a ship id, 
     |  and optionally a ship name and country
     |  which can also be set later on
     |  
     |  this object also manages a list of known positions
     |  
     |  Methods defined here:
     |  
     |  __init__(self, id, name=None, country=None)
     |      constructor
     |  
     |  add_position(self, position)
     |      insert a position relating to this ship
     |      positions are not kept in order so you need 
     |      to call `sort_positions` once you're done
     |  
     |  sort_positions(self)
     |      sort list of positions by chronological order
```

+++

##### Classe `Shipdict`

+++

```python
    Help on class ShipDict in module shipdict:
    
    class ShipDict(__builtin__.dict)
     |  a repository for storing all ships that we know about
     |  indexed by their id
     |  
     |  Method resolution order:
     |      ShipDict
     |      __builtin__.dict
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self)
     |      constructor
     |  
     |  __repr__(self)
     |  
     |  add_abbreviated(self, chunk)
     |      adds an abbreviated data chunk to the repository
     |  
     |  add_chunk(self, chunk)
     |      chunk is a plain list coming from the JSON data
     |      and be either extended or abbreviated
     |      
     |      based on the result of is_abbreviated(), 
     |      gets sent to add_extended or add_abbreviated
     |  
     |  add_extended(self, chunk)
     |      adds an extended data chunk to the repository
     |  
     |  all_ships(self)
     |      returns a list of all ships known to us
     |  
     |  clean_unnamed(self)
     |      Because we enter abbreviated and extended data
     |      in no particular order, and for any time period,
     |      we might have ship instances with no name attached
     |      This method removes such entries from the dict
     |  
     |  is_abbreviated(self, chunk)
     |      depending on the size of the incoming data chunk, 
     |      guess if it is an abbreviated or extended data
     |  
     |  ships_by_name(self, name)
     |      returns a list of all known ships with name <name>
     |  
     |  sort(self)
     |      makes sure all the ships have their positions
     |      sorted in chronological order
```

+++

##### Un dernier indice

+++

Pour éviter de la confusion, voici le code que nous utilisons pour transformer un flottant en coordonnées lisibles dans le résumé généré en mode bavard.

+++

```python
    def d_m_s(f):
        """
        makes a float readable; e.g. transforms 2.5 into 2.30'00'' 
        we avoid using ° to keep things simple
        input is assumed positive
        """
        d = int (f)
        m = int((f-d)*60)
        s = int( (f-d)*3600 - 60*m)
        return f"{d:02d}.{m:02d}'{s:02d}''"
```
