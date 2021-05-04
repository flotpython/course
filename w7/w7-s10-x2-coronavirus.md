---
jupytext:
  cell_metadata_filter: all, -hidden, -heading_collapsed, -run_control, -trusted
  encoding: '# -*- coding: utf-8 -*-'
  notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version, -jupytext.text_representation.format_version,
    -language_info.version, -language_info.codemirror_mode.version, -language_info.codemirror_mode,
    -language_info.file_extension, -language_info.mimetype, -toc
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
language_info:
  name: python
  pygments_lexer: ipython3
notebookname: 'Exercice: coronavirus'
version: '3.0'
---

# Coronavirus

+++

## Exercice - niveau intermédiaire

+++

Où on vous invite à visualiser des données liées au coronavirus.

Bon honnêtement à ce stade je devrais m'arrêter là, et vous laisser vous débrouiller complètement :)

Mais juste pour vous donner éventuellement des idées - voici des suggestions sur comment on peut s'y prendre.

```{code-cell} ipython3
import matplotlib.pyplot as plt
%matplotlib notebook
```

## Le dashboard de Johns Hopkins

+++

Le département *Center for Systems Science and Engineering* (CSSE), de l'Université Johns Hopkins, publie dans un dépôt github <https://github.com/CSSEGISandData/COVID-19> les données dans un format assez brut. C'est très détaillé et touffu :

```{code-cell} ipython3
# le repo github
official_url = "https://github.com/CSSEGISandData/COVID-19"
```

Le README mentionne aussi un *dashboard*, qui permet de visualiser les données en question. Il me semble que l'URL change tous les jours au fur et à mesure des updates, mais voici une capture d'écran pour donner une idée :
![](media/coronavirus-dashboard.png)

+++

Ce qu'on vous propose de faire, pour s'amuser, c'est quelque chose d'anologue - en version beaucoup plus modeste naturellement - pour pouvoir visualiser facilement telle ou telle courbe.

+++

## Exercice 1 : un jeu de données intéressant

+++

Pour ma part j'ai préféré utiliser un dépôt de seconde main, qui consolide en fait les données du CSSE, pour les exposer dans un seul fichier au jormat JSON. Cela est disponible dans ce second dépôt github <https://github.com/pomber/covid19>; la sortie de ce processus est mise à jour quotidiennement - à l'heure où j'écris ce texte en Mai 2020 - et est disponible (voir le README) à cette URL <https://pomber.github.io/covid19/timeseries.json>.

```{code-cell} ipython3
abridged_url = "https://pomber.github.io/covid19/timeseries.json"
```

Comme c'est du JSON, on peut charger ces données en mémoire comme ceci

```{code-cell} ipython3
# pour aller chercher l'URL
import requests

# pour charger le JSON en objets Python
import json
```

```{code-cell} ipython3
# allons-y
req = requests.get(abridged_url)
# en utilisant la property `text` on décode en Unicode
encoded = req.text
# que l'on peut décoder
decoded = json.loads(encoded)
```

```{code-cell} ipython3
## un peu de vérification
# si ceci n'est pas True, il y a un souci 
# avec le réseau ou cette URL
req.ok
```

### Les données sont indexées par pays

```{code-cell} ipython3
:cell_style: split

# voici ce qu'on obtient
type(decoded)
```

```{code-cell} ipython3
:cell_style: split

# une clé
list(decoded.keys())[0]
```

Les données d'un pays sont dans un format très simple, une liste

```{code-cell} ipython3
:cell_style: center

france_data = decoded['France']
type(france_data)
```

```{code-cell} ipython3
:cell_style: center

france_data[0]
```

```{code-cell} ipython3
:cell_style: center

france_data[-1]
```

### Homogénéité par pays

+++

Ce que j'ai constaté, et je suppose qu'on peut plus ou moins compter sur cette bonne propriété, c'est que
* pour chaque pays on trouve un enregistrement par jour
* tous les pays ont la même plage de temps - quitte à rajouter des enregistrements à 0, comme ci-dessus pour la France le 22 janvier

```{code-cell} ipython3
:cell_style: split

us_data = decoded['US']
us_data[0]
```

```{code-cell} ipython3
:cell_style: split

us_data[-1]
```

```{code-cell} ipython3
len(france_data) == len(us_data)
```

```{code-cell} ipython3
:cell_style: split

# nombre de pays
len(decoded)
```

```{code-cell} ipython3
:cell_style: split

# nombre de jours
len(france_data)
```

### Un sujet possible (#1)

+++

Vous pourriez interpréter ces données pour créer un dashbord dans lequel on peut choisir :
* la donnée à laquelle on s'intéresse (*confirmed*, *deaths* ou *recovered*)
* le pays auquel on s'intéresse (idéalement dans une liste triée)
* la période (en version simple: les *n* derniers jours)

et en fonction, afficher deux courbes qui montrent sur cette période
* la donnée brute (une fonction croissante donc)
* sa dérivée (la différence avec le jour précédent)

Selon votre envie, toutes les variantes sont possibles, pour simplifier (commencez sans dashboard), ou complexifier, comme vous le sentez. Pour revenir sur le dashboard de CSSE, on pourrait penser à utiliser un package comme `folium` pour afficher les résultats sur une carte du Monde; cela dit je vous recommande de bien réfléchir avant de vous lancer là-dedans, car c'est facile de se perdre, et en plus la valeur ajoutée n'est pas forcément majeure…

+++

### un mot par rapport à pandas

+++

Il y a plein d'approches possibles, et toutes raisonnables :

* si vous êtes à l'aise avec `pandas`, vous allez avoir le réflexe de construire immédiatement une grosse dataframe avec toutes ces données, et utiliser la puissance de `pandas` pour faire tous les traitements de type tris, assemblages, moyennes, roulements, etc.. et les affichages (et si vous êtes dans ce cas, vous préférerez l'exercice #2);
* si au contraire vous êtes réfractaire à pandas, vous pouvez absolument tout faire sans aucune dataframe;
* entre ces deux extrêmes, on peut facilement imaginer des hybrides, où on construit des dataframes de manière opportuniste selon les traitements.

La courbe d'apprentissage de pandas est parfois jugée un peu raide; c'est à vous de voir ce qui vous convient le mieux. Ce qui est clair c'est que quand on maitrise bien, et une fois qu'on a construit une grosse dataframe avec toutes les données, on dispose avec d'un outil surpuissant pour faire plein de choses en très peu de lignes. 

Mais pour bien maitriser il faut avoir l'occasion de pratiquer fréquemment, ce n'est pas forcément le cas de tout le monde (ce n'est pas le mien par exemple), donc à chacun de choisir son approche.

+++

Pour illustrer une approche disons hybride, voici ce qui pourrait être un début de mise en forme des données pour un pays et une caractéristique (parmi les 3 exposées dans ce jeu de donnéees)

```{code-cell} ipython3
import numpy as np
import pandas as pd

def extract_last_days(countryname, value, days):
    country = decoded[countryname]
    cropped = country[-(days):]
    dates = np.array([chunk['date'] for chunk in cropped])
    # take one more than requested for computing deltas including
    # for the first day (we need the value the day before the first day)
    cropped = country[-(days+1):]
    values = np.array([chunk[value] for chunk in cropped])
    # shift one day so we get the value from the day before
    shifted = np.roll(values, 1)
    # the daily increase; ignore first value which is wrong
    deltas = (values - shifted)[1:]
    relevant = values[1:]
    # all 3 arrays dates, deltas and relevant have the same shape
    data = {'dates': dates, value: relevant, 'daily': deltas}
    return pd.DataFrame(data=data)
    

df1 = extract_last_days('France', 'deaths', 45)
df1.plot();
```

## Exercice 2: idem mais à partir d'un autre jeu de données

+++

Je vous signale une autre source de données, dans ce repo git <https://github.com/owid/covid-19-data/tree/master/public/data>; les données cette fois-ci sont au format excel, et publiées à cette adresse

```{code-cell} ipython3
alt_url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
```

Dans ces cas-là il faut avoir le réflexe d'utiliser pandas; voici un aperçu (ayez de la patience pour le chargement)

```{code-cell} ipython3
import pandas as pd

df = pd.read_csv(alt_url)
```

```{code-cell} ipython3
df.head(2)
```

### Un sujet possible (#2)

+++

Le sujet à la base est le même bien entendu, essayer de visualiser ces données sous une forme où on y perçoit quelque chose :)

Les données sont bien entendu beaucoup plus riches, *a contrario* cela va demander davantage de mise en forme avant de pouvoir visualiser quoi que ce soit.

Je vous propose ce second point de vue si vous souhaitez vous entraîner avec `pandas`, puisqu'ici on a déjà une dataframe (ce qui ne veut pas dire qu'on ne peut pas traiter le premier exercice en utilisant `pandas`).

+++

### Explorons un peu

+++

Voici quelques éléments sur la stucture de ces données :

```{code-cell} ipython3
# beaucoup plus de détails
df.columns
```

```{code-cell} ipython3
# la colonne iso_code représente le pays :
df.iso_code.unique()[:5]
```

```{code-cell} ipython3
# rien que sur la france, on a ce nombre d'enregistrements
df_france = df[df.iso_code == 'FRA']
len(df_france)
```

```{code-cell} ipython3
# manifestement c'est un par jour
df_france.head(2)
```

```{code-cell} ipython3
df_france.tail(2)
```

Pour afficher, disons les décès par jour en France depuis le début de la pandémie, on pourrait faire :

```{code-cell} ipython3
df_france.plot(x='date', y='new_deaths');
```

```{code-cell} ipython3
# n'hésitez pas à installer des packages
# supplémentaires au besoin
!pip install plotly-express
```

```{code-cell} ipython3
# plusieurs courbes en une
# avec plotly express, pour changer un peu
import plotly.express as px

selection = ['USA', 'FRA']

start = '2020-03-15'
date_start = start
#date_start = pd.to_datetime(start)
sel = df[(df.iso_code.isin(selection)) & (df.date > date_start)]
fig1 = px.line(sel, x="date", y="total_deaths_per_million", color="location")
fig1.update_layout(height= 800, title_text="Décès Covid, cumulés (par million d'habitants)")
fig1.show()
```

## Comment partager ?

+++

Je ne publie pas de corrigés pour cet exercice.

+++

J'invite ceux d'entre vous qui le souhaitent à nous faire passer leur code; 
le plus simple étant de les ajouter dans le repo github dit de récréation, à cet endroit
https://github.com/flotpython/recreation/tree/master/corona-dashboards.
