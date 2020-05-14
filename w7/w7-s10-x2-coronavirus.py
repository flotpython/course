# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     formats: py:percent
#     notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Coronavirus

# %% [markdown]
# ## Exercice - niveau intermédiaire

# %% [markdown]
# Où on vous invite à visualiser des données liées au coronavirus.
#
# Bon honnêtement à ce stade je devrais m'arrêter là, et vous laisser vous débrouiller complètement :)
#
# Mais juste pour vous donner éventuellement des idées - voici des suggestions sur comment on peut s'y prendre.

# %%
import matplotlib.pyplot as plt
# %matplotlib notebook

# %% [markdown]
# ## Le dashboard de Johns Hopkins

# %% [markdown]
# Le département *Center for Systems Science and Engineering* (CSSE), de l'Université Johns Hopkins, publie dans un dépôt github <https://github.com/CSSEGISandData/COVID-19> les données dans un format assez brut. C'est très détaillé et touffu :

# %%
# le repo github
official_url = "https://github.com/CSSEGISandData/COVID-19"

# %% [markdown]
# Le README mentionne aussi un *dashboard*, qui permet de visualiser les données en question. Il me semble que l'URL change tous les jours au fur et à mesure des updates, mais voici une capture d'écran pour donner une idée :
# ![](media/coronavirus-dashboard.png)

# %% [markdown]
# Ce qu'on vous propose de faire, pour s'amuser, c'est quelque chose d'anologue - en version beaucoup plus modeste naturellement - pour pouvoir visualiser facilement telle ou telle courbe.

# %% [markdown]
# ## Exercice 1 : un jeu de données intéressant

# %% [markdown]
# Pour ma part j'ai préféré utiliser un dépôt de seconde main, qui consolide en fait les données du CSSE, pour les exposer dans un seul fichier au jormat JSON. Cela est disponible dans ce second dépôt github <https://github.com/pomber/covid19>; la sortie de ce processus est mise à jour quotidiennement - à l'heure où j'écris ce texte en Mai 2020 - et est disponible (voir le README) à cette URL <https://pomber.github.io/covid19/timeseries.json>.

# %%
abridged_url = "https://pomber.github.io/covid19/timeseries.json"

# %% [markdown]
# Comme c'est du JSON, on peut charger ces données en mémoire comme ceci

# %%
# pour aller chercher l'URL
import requests

# pour charger le JSON en objets Python
import json

# %%
# allons-y
req = requests.get(abridged_url)
# en utilisant la property `text` on décode en Unicode
encoded = req.text
# que l'on peut décoder
decoded = json.loads(encoded)

# %%
## un peu de vérification
# si ceci n'est pas True, il y a un souci 
# avec le réseau ou cette URL
req.ok

# %% [markdown]
# ### Les données sont indexées par pays

# %% cell_style="split"
# voici ce qu'on obtient
type(decoded)

# %% cell_style="split"
# une clé
list(decoded.keys())[0]

# %% [markdown]
# Les données d'un pays sont dans un format très simple, une liste 

# %% cell_style="center"
france_data = decoded['France']
type(france_data)

# %% cell_style="center"
france_data[0]

# %% cell_style="center"
france_data[-1]

# %% [markdown]
# ### Homogénéité par pays

# %% [markdown]
# Ce que j'ai constaté, et je suppose qu'on peut plus ou moins compter sur cette bonne propriété, c'est que
# * pour chaque pays on trouve un enregistrement par jour
# * tous les pays ont la même plage de temps - quitte à rajouter des enregistrements à 0, comme ci-dessus pour la France le 22 janvier

# %% cell_style="split"
us_data = decoded['US']
us_data[0]

# %% cell_style="split"
us_data[-1]

# %%
len(france_data) == len(us_data)

# %% cell_style="split"
# nombre de pays
len(decoded)

# %% cell_style="split"
# nombre de jours
len(france_data)

# %% [markdown]
# ### Un sujet possible (#1)

# %% [markdown]
# Vous pourriez interpréter ces données pour créer un dashbord dans lequel on peut choisir :
# * la donnée à laquelle on s'intéresse (*confirmed*, *deaths* ou *recovered*)
# * le pays auquel on s'intéresse (idéalement dans une liste triée)
# * la période (en version simple: les *n* derniers jours)
#
# et en fonction, afficher deux courbes qui montrent sur cette période
# * la donnée brute (une fonction croissante donc)
# * sa dérivée (la différence avec le jour précédent)
#
# Selon votre envie, toutes les variantes sont possibles, pour simplifier (commencez sans dashboard), ou complexifier, comme vous le sentez. Pour revenir sur le dashboard de CSSE, on pourrait penser à utiliser un package comme `folium` pour afficher les résultats sur une carte du Monde; cela dit je vous recommande de bien réfléchir avant de vous lancer là-dedans, car c'est facile de se perdre, et en plus la valeur ajoutée n'est pas forcément majeure…

# %% [markdown]
# ## Exercice 2: idem mais à partir d'un autre jeu de données

# %% [markdown]
# Je vous signale une autre source de données, dans ce repo git <https://github.com/owid/covid-19-data/tree/master/public/data>; les données cette fois-ci sont au format excel, et publiées à cette adresse 

# %%
alt_url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'

# %% [markdown]
# Dans ces cas-là il faut avoir le réflexe d'utiliser pandas; voici un aperçu (ayez de la patience pour le chargement)

# %%
import pandas as pd

df = pd.read_csv(alt_url)

# %%
df.head(2)

# %% [markdown]
# ### Un sujet possible (#2)

# %% [markdown]
# Le sujet à la base est le même bien entendu, essayer de visualiser ces données sous une forme où on y perçoit quelque chose :)
#
# Les données sont bien entendu beaucoup plus riches, *a contrario* cela va demander davantage de mise en forme avant de pouvoir visualiser quoi que ce soit.
#
# Je vous propose ce second point de vue si vous souhaitez vous entraîner avec `pandas`, puisqu'ici on a déjà une dataframe (ce qui ne veut pas dire qu'on ne peut pas traiter le premier exercice en utilisant `pandas`).

# %% [markdown]
# ### Explorons un peu

# %% [markdown]
# Voici quelques éléments sur la stucture de ces données :

# %%
# beaucoup plus de détails
df.columns

# %% scrolled=false
# la colonne iso_code représente le pays :
df.iso_code.unique()[:5]

# %% scrolled=false
# rien que sur la france, on a ce nombre d'enregistrements
df_france = df[df.iso_code == 'FRA']
len(df_france)

# %%
# manifestement c'est un par jour
df_france.head(2)

# %%
df_france.tail(2)

# %% [markdown]
# Pour afficher, disons les décès par jour en France depuis le début de la pandémie, on pourrait faire :

# %%
df_france.plot(x='date', y='new_deaths');

# %%
# n'hésitez pas à installer des packages
# supplémentaires au besoin
# !pip install plotly-express

# %%
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

# %% [markdown]
# ## Comment partager ?

# %% [markdown]
# J'invite ceux d'entre vous qui le souhaitent à nous faire passer leur code; 
# le plus simple étant de les ajouter dans le repo github dit de récréation, à cet endroit
# https://github.com/flotpython/recreation/tree/master/corona-dashboards.
