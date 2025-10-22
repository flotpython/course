---
jupytext:
  encoding: '# -*- coding: utf-8 -*-'
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
language_info:
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
nbhosting:
  title: 'Exercice: coronavirus'
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
%matplotlib ipympl
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
:tags: [gridwidth-1-2]

# voici ce qu'on obtient
type(decoded)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

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
:tags: [gridwidth-1-2]

us_data = decoded['US']
us_data[0]
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

us_data[-1]
```

```{code-cell} ipython3
len(france_data) == len(us_data)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# nombre de pays
len(decoded)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

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

Je vous signale une autre source de données, dans ce repo git <https://github.com/owid/covid-19-data/tree/master/public/data>; les données cette fois-ci sont au format excel, et publiées à cette adresse

```{code-cell} ipython3
alt_url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
```

```{admonition} mise à jour oct. 2025
:class: danger

il semble que cette URL est à présent inaccessible
je supprime donc le deuxième exercice de ce notebook
```

+++

## Comment partager ?

+++

Je ne publie pas de corrigés pour cet exercice.

+++

J'invite ceux d'entre vous qui le souhaitent à nous faire passer leur code; 
le plus simple étant de les ajouter dans le repo github dit de récréation, à cet endroit
https://github.com/flotpython/recreation/tree/master/corona-dashboards.
