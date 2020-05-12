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
#   notebookname: Organiser les sources de votre projet
# ---

# %% [markdown]
# # Comment organiser les sources de votre projet Python


# %% [markdown]
# Où on va voir que :
# * c'est bien de grouper son code dans un package
# * mais à première vue ça casse tout, mais pas de panique !
# * il ne **FAUT PAS** tripoter la variable **`PYTHONPATH`** 
# * il faut au contraire créer un `setup.py`, et ensuite lancer une fois  
#   `pip install -e .`  
#   pour pouvoir utiliser le code en mode développeur

# %% [markdown]
# ## complément - niveau intermédiaire

# %% [markdown]
# Vous venez d'écrire un super algorithme qui simule le climat de l'an 2100, et vous voulez le publier ? Nous allons voir ici comment organiser les sources de votre projet, pour que ce soit à la fois 
#
# * pratique pour vous de tester votre travail pendant le développement
# * facile de publier le code pour que d'autres puissent l'installer et l'utiliser
# * et éventuellement facile pour d'autres de contribuer à votre projet.

# %% [markdown]
# ## les infrastructures

# %% [markdown]
# En 2020 on ne travaille plus tout seul dans son coin; il est à la portée de tous d'utiliser et de tirer profit d'infrastructures, ouvertes et gratuites (pour les usages de base au moins) :
#
# Pour ce qui nous concerne ici, voici celles qui vont nous être utiles :
#
# * [PyPI](https://pypi.org) - (prononcer "paille - pis - ail") pour **Py**thon **P**ackage **I**ndex, est l'endroit où chacun peut publier ses librairies
# * [github](https://github.com) - ainsi que ses concurrents [gitlab](https://gitlab.com) et [bitbucket](https://bitbucket.org) - sont bien sûr des endroits où l'on peut déposer ses sources pour partage, sous la forme de  dépôt `git`
#
# Optionnellement, sachez qu'il existe également des infrastructures pour les deux grandes tâches que sont la documentation et le test, souvent considérées - à tort - comme annexes :
#
# * [readthedocs](https://readthedocs.io) est une infra qui permet d'exposer la documentation
# * [travis](https://travis-ci.com) est - parmi plein d'autres - une infrastructure permettant d'exécuter une suite de tests
#
# S'agissant de ces deux derniers points : souvent on s'arrange pour que tout soit **automatique**; quand tout est en place, il **suffit de pousser un nouveau commit** auprès de github (par exemple) pour que 
#
# * tous les **tests** soient **repassés** (d'où le terme de **CI*** = *Continuous Integration*); du coup on sait en permanence si tel ou tel commit a cassé ou non l'intégrité du code;
# * la **documentation** soit **mise à jour**, exposée à tout le monde, et navigable par numéro de version.

# %% [markdown]
# Alors bon bien sûr ça c'est le monde idéal; on ne passe pas d'un seul coup, d'un bout de code qui tient dans un seul module `bidule.py`, à un projet qui utilise tout ceci; on on n'a **pas forcément besoin** non plus d'utiliser **toutes** ces ressources (et bien entendu, aucun de ces trucs n'est obligatoire).
#
# Aussi nous allons commencer par le commencement.

# %% [markdown]
# ## le commencement : créer un package

# %% [markdown] trusted=true
# Le commencement, ça consiste à se **préparer à coexister** avec d'autres librairies.
#
# Si votre code expose disons une classe `Machine` dans le fichier/module `machine.py`, la première chose consiste à  trouver un nom unique; rien ne vous permet de penser qu'il n'y a pas une autre bibliothèque qui expose un module qui s'appelle aussi `machine` (il y a même fort à parier qu'il y en a plein !).  
# Aussi ce qu'on va commencer par faire c'est d'installer tout notre code **dans un package**.
#
# Concrètement ça va signifier se mettre dans un sous-dossier, mais surtout d'un point de vue des utilisateurs potentiels de la classe, ça veut dire qu'au lieu de faire juste :
#
# ```from machine import Machine```
#
# on va décider qu'à partir de maintenant il faut toujours faire
#
# ```from bidule.machine import Machine```
#
# et de cette façon tous les noms qui sont propres à notre code ne sont accessible que via l'espace de noms `bidule`, et on évite les conflits avec d'autres bibliothèques.

# %% [markdown]
# ### choisir le nom du package

# %% [markdown] trusted=true
# Bien sûr ceci ne fonctionne que si je peux **être sûr que `bidule` est à moi**, de sorte que **personne** demain ne publie une librairie qui utilise **le même nom**.  
#
# C'est pourquoi je **recommande**, à ce stade, de s'assurer de prendre un nom qui n'est **pas déjà pris**; en toute rigueur c'est optionnel, tant que vous ne prévoyez pas de publier votre appli sur pypi (car bien sûr c'est optionnel de publier sur pypi), mais ça coûte moins cher de le faire très tôt, ça évite des renommages fastidieux plus tard.

# %% [markdown] trusted=true
# Donc pour s'assurer de cela, on va tout simplement demander à `pypi`, qui va jouer le rôle de *registrar*, et nous garantir l'exclusivité de ce nom. vous pouvez soit chercher votre nom [directement dans le site pypi](https://pypi.org/search/?q=bidule), ou bien utiliser `pip`
#
#     pip search bidule

# %% [markdown]
# Le nom est libre, pour toute la suite **je choisis `bidule` comme mon nom de package**.  
# Vous trouverez dans ce repo git <https://github.com/flotpython/bidule> un microscopique petit projet qui illustre notre propos.

# %% [markdown]
# ### adapter son code

# %% [markdown]
# Une fois que j'ai chiosi mon nom de package, donc ici `bidule`, je dois :
#
# 1. mettre tout mon code dans un répertoire qui s'appelle `bidule`,
# 1. et modifier mes importations; maintenant j'importe tout au travers du seul package `bidule`

# %% [markdown]
# Donc je remplace les importations partout; ce qui avant aurait été simplement
#
#     from machine import Machine
#
# devient 
#
#     from bidule.machine import Machine

# %% [markdown]
# #### Remarque : imports relatifs
#
# Lorsqu'un fichier a besoin d'en importer **dans le même package**, on a le choix; par exemple ici, `machine.py` a besoin d'importer la fonction `helper` du fichier `helpers.py`, il peut faire
#
#     from bidule.helpers import helper
#     
# mais aussi plus simplement avec un **import relatif** :
#
#     from .helpers import helper
#     
# remarquez le `.` dans `.helpers`, qui signifie *dans le même package que moi*

# %% [markdown]
# Je recommande toutefois de ne pas se précipiter avec ces imports relatifs, et notamment de **ne pas les utiliser dans un point d'entrée** (le fichier qu'on passe à l'interpréteur Python) car ça ne fonctionne pas dans ce cas.

# %% [markdown]
# ### c'est tout cassé

# %% [markdown]
# À ce stade précisément, vous constatez .. que **plus rien ne marche** !
#
# En effet, comme on l'a vu dans le complément sur le chargement des modules, Python recherche vos modules dans l'ordre
#
# * le dossier du point d'entrée
# * la variable d'environnement `PYTHONPATH`
# * les dossiers système
#
# Et donc si vous m'avez suivi vous devez avoir quelque chose comme
#
# ```bash
# mon-repo-git/
#              bidule/
#                     main.py
#                     machine.py
#                     helpers.py
# ```
#
# mais alors quand vous faites 
#
# ```bash
# $ python bidule/main.py
# Traceback (most recent call last):
#   File "bidule/main.py", line 1, in <module>
#     from bidule.machine import Machine
# ModuleNotFoundError: No module named 'bidule'```
# ```
#
# on va chercher du coup un module `bidule` à partir du répertoire du point d'entrée qui est le dossier `bidule/`, donc on ne trouve pas. 
# ```

# %% [markdown]
# ### le mauvais réflexe

# %% [markdown]
# Du coup naturellement, on se dit, ça n'est pas grave, je vais tirer profit de la variable `PYTHONPATH`.  
# Alors disons-le tout net : **ce n'est pas une bonne idée**, ce n'est pas du tout pour ce genre de cas qu'elle a été prévue. 
#
# Le fait de modifier une variable d'environnement est un processus tarabiscoté, même sans parler de Windows, et cette approche est une bonne façon de se tirer une balle dans le pied; un jour ou l'autre la variable ne sera pas positionnée comme il faut, c'est sûr.
#
# Bref, il ne **faut pas faire comme ça !!**

# %% [markdown]
# ## le bon réflexe : `setup.py`

# %% [markdown]
# Non, le bon reflexe ici c'est d'écrire un fichier `setup.py`, et de l'utiliser pour faire ce qu'on pourrait une *installation en mode développeur*. Voyons cela :
#
# Je commence donc par créer un fichier `setup.py` à la racine de mon repo git, dans lequel je mets, pour commencer, le minimum :

# %% [markdown]
# ```
# # minimal setup.py to install in develop mode
#
# from setuptools import setup, find_packages
#
# setup(
#     name="bidule",
#     packages=find_packages(),
# )
# ```

# %% [markdown]
# **Attention**: nous sommes en 2020 et il faut utiliser le package `setuptools`, qui ne fait pas partie de la librairie standard (**et non pas** le module `distutils` qui, lui, en fait pourtant partie); donc comme d'habitude si c'est nécessaire, faites dans le terminal :
#
#     pip install setuptools

# %% [markdown]
# ### installation en mode developpeur : `pip install -e .`

# %% [markdown]
# Avec ce fichier en place, et toujours à la racine de mon repo, je peux maintenant faire la formule magique (toujours dans le terminal)
#
# ```bash
# $ pip install -e .
# Obtaining file:///Users/tparment/git/flotpython-course/w6/mon-repo-git
# Installing collected packages: bidule
#   Attempting uninstall: bidule
#     Found existing installation: bidule 0.0.0
#     Uninstalling bidule-0.0.0:
#       Successfully uninstalled bidule-0.0.0
#   Running setup.py develop for bidule
# Successfully installed bidule
# ```
#
# L'effet de cette commande est de modifier mon environnement pour que le répertoire courant 
# (le `.` dans `pip install -e .`) soit utilisé pour la recherche des modules. Ça signifie que
# je peux maintenant lancer mon programme sans souci :
#
#   ```bash
#   $ python bidule/main.py
#   ... déroulement normal
#   ```
#   
# Et je peux modifier mon code dans le répertoire courant, ce sera bien ce code là qui sera utilisé; cette précision pour ceux qui penseraient que, comme on fait une installation, cela pourrait être fait par copie, mais ce n'est pas le cas, donc sauf gros changement dans le contenu, on n'a **plus besoin de refaire** le `pip install -e .`
#

# %% [markdown]
# ### un `setup.py` plus raisonnable

# %% [markdown]
# Au delà de cette première utilité, `setup.py` sert à configurer plein d'aspects de votre application; lorsque votre projet va gagner en maturité, il sera exécuté lorsque vous préparez le packaging, lorsque vous uploadez le package, et au moment d'installer (comme on vient de le voir).  

# %% [markdown]
# Du coup en pratique, les besoins s'accumulent au fur et à mesure de l'avancement du projet, et on met de plus en plus d'informations dans le `setup.py`; voici, que j'essaie de mettre dans l'ordre chronologique, quelques ajouts très fréquents; [reportez-vous à la doc](https://setuptools.readthedocs.io/en/latest/setuptools.html#developer-s-guide) pour une liste complète :
#
# * `name` est le nom sous lequel votre projet sera rangé dans PyPI
#
# * `packages` est une liste de noms de packages; tel qu'on l'a écrit cela sera calculé à partir du contenu de votre dépôt; dans notre cas on aurait pu aussi bien écrire en dur `['bidule']`;  
#   dans les cas les plus simples on a `packages == [ name ]`
#
# * `version` est bien entendu important dès que vous commencez à publier sur PyPI (et même avant) pour que PyPI puisse servir la version la plus récente, et/ou satisfaire des exigences précises (les applis qui vous utilisent peuvent par exemple préciser une version minimale, etc...)
#
# * `install_requires` : si votre package a besoin d'une librairie non-standard, disons par exemple `numpy`, il est **très utile** de le préciser ici; de cette façon, lorsqu'un de vos utilisateurs installera votre appli avec `pip install bidule`, `pip` pourra **gérer les dépendances** et s'assurer que `numpy` est installé également; 
#   bien sûr on n'en est pas là, mais je vous recommande de maintenir **dès le début** la liste de vos dépendances ici;
#   
# * informatifs : `author`, `author_email`, `description`, `keywords`, `url` pour affichage sur PyPI;  
#   une mention spéciale à propos de `description_long`, qu'en général on veut afficher à partir de `README.md`, d'où l'idiome fréquent :
#   
#   ```
#   setup( 
#      ...
#      long_description=open('README.md').read(),
#      long_description_content_type = "text/markdown",
#      ...
#   ```

# %% [markdown]
# ## publier sur PyPI

# %% [markdown]
# Pour publier votre application sur PyPI, rien de plus simple :
#
# * il faut naturellement obtenir un login/password
# * avant de pouvoir utiliser le nom `bidule`, il faut l'enregistrer :  
#   `python setup.py register`
# * aussi il vous faudra installer `twine`  
#   `pip install twine`
#
# Ensuite à chaque version, une fois que les tests sont passés et tout :
#
# * préparer le packaging  
#   `python setup.py sdist bdist_wheel`
# * pousser sur PyPI  
#   `twine upload dist/*`
#   
# Signalons enfin qu'il existe une infra PyPI "de test" sur `https://test.pypi.org` utile quand on ne veut pas polluer l'index officiel.

# %% [markdown]
# ## utiliser `pip` pour installer

# %% [markdown]
# Ensuite une fois que c'est fait, le monde entier peut profiter de votre magnifique contribution en faisant bien sûr  
# `pip install bidule`  
#
# Remarquez que l'on conseille parfois, pour éviter d'éventuels soucis de divergence entre les commandes `python`/`python3` et `pip`/`pip3`, 
# * de remplacer tous les appels à `pip` 
# * par plutôt `python -m pip`, qui permet d'être sûr qu'on installe dans le bon environnement
#
# D'autres formes utiles de `pip` :
#
# * `pip show bidule` : pour avoir des détails sur un module précis
# * `pip freeze` : pour une liste complète des modules installés dans l'environnement, avec leur numéro de version
# * `pip list` : sans grand intérêt, si ce n'est dans sa forme  
#   `pip list -o` qui permet de lister les modules qui pourraient être mis à jour
# * `pip install -r requirements.txt` : pour installer les modules dont la liste est dans le fihuer `requirements.txt`
#

# %% [markdown]
# ## packages et `__init__.py`

# %% [markdown]
# Historiquement avant la version 3.3 pour qu'un dossier se comporte comme un package il était **obligatoire** d'y créer un fichier de nom `__init__.py` - même vide au besoin.
#
# Ce n'est plus le cas depuis cette version. Toutefois, il peut s'avérer utile de créer ce fichier, et si vous lisez du code vous le trouverez très fréquemment.
#
# L'intérêt de ce fichier est de pouvoir agir sur :
# * le contenu du package lui-même, c'est-à-dire les attributs attachés à l'objet module associé à ce dossier,
# * et accessoirement d'exécuter du code supplémentaire.
#
# Un usage particulièrement fréquent consiste à "remonter" au niveau du package les symboles définis dans les sous-modules. Voyons ça sur un exemple.

# %% [markdown]
# Dans notre repo de démonstration, nous avons une classe `Machine` définie dans le module `bidule.machine`. Donc de l'extérieur pour me servir de cette classe je dois faire
#
#     from bidule.machine import Machine
#
# C'est très bien, mais dès que le contenu va grossir, je vais couper mon code en de plus en plus de modules. Ce n'est pas tellement aux utilisateur de devoir suivre ce genre de détails. Donc si je veux pouvoir changer mon découpage interne sans impacter les utilisateurs, je vis vouloir qu'on puisse faire plutôt, simplement
#
#     from bidule.machine import Machine
#     
# pour y arriver il me suffit d'ajouter cette ligne dans le `__init__.py` du package `bidule` :
#
#     import Machine from .machine
#     
# qui du coup va définir le symbole `Machine` directement dans l'objet package.

# %% [markdown]
# ## virtual environments

# %% [markdown]
# Terminons ce tour d'horizon pour dire un mot des environnements virtuels.
#
# Par le passé, on installait python une seule fois dans le système; en 2020, c'est une approche qui n'a que des inconvénients :
#
# * quand on travaille sur plusieurs projets, on peut avoir besoin de Python-3.6 sur l'un et Python-3.8 sur un autre ;
# * ou alors on peut avoir un projet qui a besoin de `Django==2.2` et un autre qui ne marche qu'avec `Django>=3.0` ;
# * en plus par dessus le marché, dans certains cas il faut être super utilisateur pour modifier l'installation; typiquement on passe son temps à faire `sudo pip` au lieu de `pip`…
#
# et le seul avantage, c'est que tous les utilisateurs de l'ordi peuvent partager l'installation; sauf que, plus de 99 fois sur 100, il n'y a qu'un utilisateur pour un ordi ! bref, c'est une pratique totalement dépassée.

# %% [markdown]
# La création et la gestion d'environnements virtuels est très facile aujourd'hui; par contre il reste le choix entre plusieurs outils, que j'essaie de lister ici :
#
# * [`venv`](https://docs.python.org/3/library/venv.html) un module de la librairie standard
#
# * [`virtualenv`](https://virtualenv.pypa.io/en/latest/) un module externe, qui préexistait à `venv` et qui a fourni la base des fonctionnalités de `venv`
#
# * [`miniconda`](https://docs.conda.io/en/latest/miniconda.html) un sous-produit de anaconda

# %% [markdown]
# Actuellement j'utilise quant à moi `miniconda`.  
# Voici à titre indicatif une session sous MacOS en guise de rapide introduction;  
# Vous remarquerez comme le *prompt* reflète **l'environnement dans lequel on se trouve**, ça semble relativement impératif si on ne veut pas s'emmêler les pinceaux.

# %% [markdown]
# ##### la liste de mes environnements
# ```
# [base] ~ $ conda env list
# # conda environments:
# #
# base                  *  /Users/tparment/miniconda3
# <snip ...>
# ```

# %% [markdown]
# ##### j'en crée un nouveau avec Python-3.8
#
# ```
# [base] ~ $ conda create -n demo-py38 python=3.8
# Collecting package metadata (current_repodata.json): done
# Solving environment: done
# <snip ...>
# ```

# %% [markdown]
# ##### on le voit
# ```
# [base] ~ $ conda env list
# # conda environments:
# #
# base                  *  /Users/tparment/miniconda3
# demo-py38                /Users/tparment/miniconda3/envs/demo-py38
# <snip...>
# ```

# %% [markdown]
# ##### pour entrer dans le nouvel environnement
#
# ```
# [base] ~ $ conda activate demo-py38
# [demo-py38] ~ $
# ```

# %% [markdown]
# ##### les packages installés
#
# très peu de choses
#
# ```
# [demo-py38] ~ $ pip list
# Package    Version
# ---------- -------------------
# certifi    2020.4.5.1
# pip        20.0.2
# setuptools 46.2.0.post20200511
# wheel      0.34.2
# ```

# %% [markdown]
# ##### on y installe ce qu'on veut
# ```
# [demo-py38] ~ $ pip install numpy==1.15.3
# ```

# %% [markdown]
# ##### la version de python
# ```
# [demo-py38] ~ $ python --version
# Python 3.8.2
# ```

# %% [markdown]
# ##### sortir 
# ```
# [demo-py38] ~ $ conda deactivate
# [base] ~ $
# ```

# %% [markdown]
# ##### la version de python
# ```
# [base] ~ $ python --version
# Python 3.7.6
# ```

# %% [markdown]
# ##### on n'a pas perturbé l'environnement de départ
# ```
# [base] ~ $ pip show numpy
# Name: numpy
# Version: 1.18.1
# ```

# %% [markdown]
# ##### pour détruire l'environnement en question
# ```
# [base] ~ $ conda env remove -n demo-py38
#
# Remove all packages in environment /Users/tparment/miniconda3/envs/demo-py38:
# ```
