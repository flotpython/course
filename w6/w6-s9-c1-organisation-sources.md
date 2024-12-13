# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
#   language_info:
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#   nbhosting:
#     title: Organiser les sources
# ---

# Licence CC BY-NC-ND, Thierry Parmentelat & Arnaud Legout

# # Comment organiser les sources de votre projet Python
#
# Où on va voir que :
#
# * c'est bien de grouper son code dans un package
# * mais à première vue ça casse tout, cependant pas de panique !
# * il ne **FAUT PAS** tripoter la variable **`PYTHONPATH`**
# * il faut au contraire créer un packaging minimal
#   et ensuite lancer une fois `pip install -e .` pour pouvoir utiliser le code en mode développeur
#
# ````{admonition} code compagnon
#
# Vous trouverez dans le dépôt git ici: <https://github.com/flotpython/bidule> un microscopique petit projet qui illustre notre propos.
# ````

from IPython.display import HTML
HTML(filename="_static/style.html")

# ## Complément - niveau intermédiaire
#
# Vous venez d'écrire un super algorithme qui simule le climat de l'an 2100, et vous voulez le publier ? Nous allons voir ici comment organiser les sources de votre projet, pour que ce soit à la fois
#
# * pratique pour vous de tester votre travail pendant le développement
# * facile de publier le code pour que d'autres puissent l'installer et l'utiliser
# * et éventuellement facile pour d'autres de contribuer à votre projet.

# ## Les infrastructures
#
# En 2024, on ne travaille plus tout seul dans son coin ; il est à la portée de tous d'utiliser et de tirer profit d'infrastructures, ouvertes et gratuites (pour les usages de base au moins) :
#
# Pour ce qui nous concerne ici, voici celles qui vont nous être utiles :
#
# * [PyPI](https://pypi.org) - (prononcer "paille - pis - ail") pour **Py**thon **P**ackage **I**ndex, est l'endroit où chacun peut publier ses librairies
# * [github](https://github.com) - ainsi que ses concurrents [gitlab](https://gitlab.com) et [bitbucket](https://bitbucket.org) - sont bien sûr des endroits où l'on peut déposer ses sources pour partage, sous la forme de  dépôt `git`
#
# Optionnellement, sachez qu'il existe également des infrastructures pour les deux grandes tâches que sont la documentation et le test, souvent considérées - à tort - comme annexes :
#
# * [readthedocs](https://readthedocs.io) est une infra qui permet d'exposer la documentation
# * [travis](https://travis-ci.com) est - parmi plein d'autres - une infrastructure permettant d'exécuter une suite de tests; une autre alternative populaire, ce sont les *github actions*
#
# S'agissant de ces deux derniers points : souvent on s'arrange pour que tout soit **automatique** ; quand tout est en place, il **suffit de pousser un nouveau commit** auprès de github (par exemple) pour que
#
# * tous les **tests** soient **repassés** (d'où le terme de **CI** = *Continuous Integration*) ; du coup on sait en permanence si tel ou tel commit a cassé ou non l'intégrité du code ;
# * la **documentation** soit **mise à jour**, exposée à tout le monde, et navigable par numéro de version.

# Alors bon bien sûr ça c'est le monde idéal ; on ne passe pas d'un seul coup, d'un bout de code qui tient dans un seul module `bidule.py`, à un projet qui utilise tout ceci ; et bien entendu, aucun de ces trucs n'est obligatoire, on n'a **pas forcément besoin** non plus d'utiliser **toutes** ces ressources.
#
# Aussi nous allons commencer par le commencement.

# ## Le commencement : créer un package
#
# Vous [pouvez voir ici un repo git](https://github.com/parmentelat/bidule) qui contient le mini package dont on parle ici.
#
# Le commencement, ça consiste à se **préparer à coexister** avec d'autres librairies.
#
# Si votre code expose disons une classe `Machine` dans le fichier/module `machine.py`, la première chose consiste à  **trouver un nom unique** ; rien ne vous permet de penser qu'il n'y a pas une autre bibliothèque qui expose aussi un module qui s'appelle `machine` (il y a même fort à parier qu'il y en a plein !).
# Aussi ce qu'on va commencer par faire c'est d'installer tout notre code **dans un package**.
#
# Concrètement ça va signifier **mettre notre code dans un sous-dossier**, mais surtout d'un point de vue des utilisateurs potentiels de la classe, ça veut dire qu'au lieu de faire juste :
#
# ```python
# from machine import Machine
# ```
#
# on va décider qu'à partir de maintenant il faut toujours faire
#
# ```python
# from bidule.machine import Machine
# ```
#
# et de cette façon, tous les noms qui sont propres à notre code ne sont accessibles que via l'espace de noms (du module) `bidule`, ainsi on évite les conflits avec d'autres bibliothèques.

# ### Choisir le nom du package
#
# Bien sûr ceci ne fonctionne que si je peux **être sûr que `bidule` est à moi**, de sorte que **personne** demain ne publie une librairie qui utilise **le même nom**.
#
# C'est pourquoi **on recommande**, à ce stade, de s'assurer de prendre un nom qui n'est **pas déjà pris** ; en toute rigueur c'est optionnel, tant que vous ne prévoyez pas de publier votre appli sur pypi (car bien sûr c'est optionnel de publier sur pypi), mais ça coûte moins cher de le faire très tôt, ça évite des renommages fastidieux plus tard.
#
# Donc pour s'assurer de cela, on va tout simplement demander à `pypi`, qui va jouer le rôle de *registrar*, et nous garantir l'exclusivité de ce nom. Je vous invite à chercher votre nom [directement dans le site pypi](https://pypi.org/search/?q=bidule) pour vous en assurer (à noter que `pip search bidule` n'est plus disponible depuis la ligne de commande)
#
# Le nom est libre, pour toute la suite **je choisis `bidule` comme mon nom de package**.

# ### Adapter son code
#
# Une fois que j'ai choisi mon nom de package, donc ici `bidule`, je dois :
#
# 1. mettre tout mon code dans un dossier qui s'appelle `bidule`,
# 1. et modifier mes importations ; maintenant j'importe tout au travers du seul package `bidule`.
#
# Donc je remplace les importations partout ; ce qui avant aurait été simplement
#
# ```python
# from machine import Machine
# ```
#
# devient
#
# ```python
# from bidule.machine import Machine
# ```

# ````{admonition} Remarque : imports relatifs
# :class: tip dropdown
#
# Lorsqu'un fichier a besoin d'en importer un autre **dans le même package**, on a le choix ; par exemple ici, `machine.py` a besoin d'importer la fonction `helper` du fichier `helpers.py`, il peut faire
#
# ```python
# from bidule.helpers import helper
# ```
#
# mais aussi plus simplement avec un **import relatif** :
#
# ```python
# from .helpers import helper
# ```
#
# remarquez le `.` dans `.helpers`, qui signifie *dans le même package que moi*.
#
# ```{admonition} mais pas de précipitation
#
# Je recommande toutefois de ne pas se précipiter avec ces imports relatifs, et notamment de **ne pas les utiliser dans un point d'entrée** (le fichier qu'on passe à l'interpréteur Python) car ça ne fonctionne pas tout seul dans ce cas.  
# C'est possible, mais scabreux; pour plus de détails, voyez le fichier `main.py` dans le repo compagnon
# ```
# ````

# ### C'est tout cassé
#
# À ce stade précisément, vous constatez... que **plus rien ne marche** !
#
# En effet, comme on l'a vu dans le complément sur le chargement des modules, Python recherche vos modules dans l'ordre
#
# * le dossier du point d'entrée
# * la variable d'environnement `PYTHONPATH`
# * les dossiers système
#
# Et donc si vous m'avez suivi, vous devez avoir quelque chose comme
#
# ```bash
# mon-depot-git/
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
# ModuleNotFoundError: No module named 'bidule'
# ```
#
# on va chercher du coup un module `bidule` à partir du répertoire du point d'entrée qui est déjà le dossier `bidule/`, donc on ne trouve pas.
#
# ````{admonition} import relatifs - suite
# :class: dropdown
#
# notez que ça ne fonctionne pas mieux - voire même encore moins bien - si j'utilise un import relatif dans le point d'entrée, le message d'erreur devient alors
# ```bash
# $ python bidule/main.py
# Traceback (most recent call last):
#   File "/Users/tparment/git/bidule/bidule/main.py", line 3, in <module>
#     from .machine import Machine
# ImportError: attempted relative import with no known parent package
# ```
# ````

# ### Le mauvais réflexe
#
# Du coup naturellement, on se dit, ça n'est pas grave, je vais tirer profit de la variable `PYTHONPATH`.
# Alors disons-le tout net : **ce n'est pas une bonne idée**, ce n'est pas du tout pour ce genre de cas qu'elle a été prévue.
#
# Le fait de modifier une variable d'environnement est un processus tarabiscoté, même sans parler de Windows, et cette approche est une bonne façon de se tirer une balle dans le pied ; un jour ou l'autre la variable ne sera pas positionnée comme il faut, c'est sûr.
#
# Bref, il ne **faut pas faire comme ça !!**

# ## Le bon réflexe : `pip install -e .`
#
# Non, le bon reflexe ici c'est d'écrire un fichier `pyproject.toml`, et de l'utiliser pour faire ce qu'on pourrait appeler une *installation en mode développeur*. Voyons cela :
#
# Je commence donc par créer un fichier `pyproject.toml` à la racine de mon dépôt git, dans lequel je mets, pour commencer, le minimum :
#
# ```python
# [project]
# name = "bidule"
# version = "0.1.0"
# ```

# ### Installation en mode developpeur : `pip install -e .`
#
# ````{admonition} environnement virtuel
# :class: dropdown warning
#
# il est généralement préférable de faire ce qui suit à l'intérieur d'un environnement virtuel; mais je ne veux pas tout mélanger  
# on parle des environnements virtuels à un autre endroit du cours
# ````
#
# Avec ce fichier en place, et toujours à la racine de mon dépôt, je peux maintenant faire la formule magique :
#
# ```bash
# $ pip install -e .
# pip install -e .
# Obtaining file:///le/chemin/ou/je/suis
# <snip>
# Successfully built bidule
# Installing collected packages: bidule
# Successfully installed bidule-0.1.0
# ```
#
# L'effet de cette commande est de modifier mon environnement pour que le répertoire courant (le `.` dans `pip install -e .`) soit utilisé pour la recherche des modules.
# Ça signifie que je peux maintenant lancer mon programme sans souci :
#
# ```bash
# $ python 
# >>> from bidule import Machine
# >>> Machine()
# ... déroulement normal
# >>>
# ```
#
# ```{admonition} une bonne fois pour toutes
#
# Et je peux modifier mon code dans le répertoire courant, ce sera bien ce code-là qui sera utilisé ; cette précision pour ceux qui penseraient que, comme on fait une installation, cela pourrait être fait par copie, mais ce n'est pas le cas, donc sauf gros changement dans le contenu, on n'a **plus besoin de refaire** le `pip install -e .`
# ```

# ### Un `pyproject.toml` plus raisonnable
#
# Au delà de cette première utilité, `pyproject.toml` sert à configurer plein d'aspects de votre application ; lorsque votre projet va gagner en maturité, il sera utilisé pour préparer le packaging, pour uploader le package, et au moment d'installer (comme on vient de le voir).
#
# Du coup en pratique, les besoins s'accumulent au fur et à mesure de l'avancement du projet, et on met de plus en plus d'informations dans `pyproject.toml`; voici quelques ajouts très fréquents que j'essaie de mettre dans l'ordre chronologique [reportez-vous à la doc pour une liste complète](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#basic-information) :
#
# * `name` est le nom sous lequel votre projet sera rangé dans PyPI
# * `version` est bien entendu important dès que vous commencez à publier sur PyPI (et même avant) pour que PyPI puisse servir la version la plus récente, et/ou satisfaire des exigences précises (les applis qui vous utilisent peuvent par exemple préciser une version minimale, etc...)
#   Cette chaine devrait être [compatible avec semver (semantic versioning)](https://semver.org/)
#   i.e. qu'un numéro de version usuel contient 3 parties (major, minor, patch), comme par ex. "2.1.3"
#   le terme `semantic` signifie ici que **toute rupture de compatibilité** doit se traduire par une incrémentation du numéro majeur (sauf s'il vaut `0`, on a le droit de tâtonner avec une 0.x; d'où l'importance de la version 1.0)
#
# * `dependencies`: si votre package a besoin d'une librairie non-standard, disons par exemple `numpy`, il est **très utile** de le préciser ici ; de cette façon, lorsqu'un de vos utilisateurs installera votre appli avec `pip install bidule`, `pip` pourra **gérer les dépendances** et s'assurer que `numpy` est installé également ;
#   bien sûr on n'en est pas là, mais je vous recommande de maintenir **dès le début** la liste de vos dépendances ici
#   ```toml
#   dependencies = [
#       "numpy",
#   ]
#   ```
# * informatifs : `description`, `readme`, `license`, `authors`, `keywords`, `url`, `license`,  pour affichage sur PyPI ;
#   voyez le package `bidule` sur github pour un exemple;
#   notamment le champ `description` est un résumé en une ligne, alors que `readme` vaut généralement `README.md`, fichier dans lequel on décrit le module plus en détails
#
# * on peut aussi préciser les urls du repo git et de la doc lorsque c'est disponible
#   cela se fait dans une autre section:
#   ```toml
#   [project.urls]
#   Homepage = "https://github.com/parmentelat/bidule"
#   # je ne suis pas allé jusque là...
#   Documentation = "https://bidule.readthedocs.io"
#   ```
#
# * etc… beaucoup d'autres réglages et subtilités autour de `pyproject.toml` ; je conseille de prendre les choses comme elles viennent : commencez avec la liste qui est ici, et n'ajoutez d'autres trucs que lorsque ça correspond à un besoin pour vous !

# ### Packager un point d'entrée
#
# Assez fréquemment on package des **librairies** ; dans ce cas on se soucie d'installer uniquement des modules Python.
#
# Mais imaginez maintenant que votre package contient aussi un **point d'entrée** - c'est-à-dire en fin de compte une **commande** que vos utilisateurs vont vouloir lancer **depuis le terminal**. Ce cas de figure change un peu la donne; il faut maintenant installer des choses à d'autres endroits du système (pensez par exemple, sur linux/macos, à quelque chose comme `/usr/bin`).
#
# Dans ce cas **surtout n'essayez pas de le faire vous-même**, c'est beaucoup trop compliqué à faire correctement !
#
# Pour illustrer la bonne façon de faire dans ce cas, je vous renvoie pour les détails à notre exemple réel, mais pour l'essentiel il vous suffit d'ajouter dans `pyproject.toml` une nouvelle section:
#
# ```toml
# [project.scripts]
# # l'installation va créer une commande 'bidule-cli' qu'on pourra appeler dans le terminal
# # et qui lancera la fonction 'main()' du fichier bidule/main.py
# bidule-cli = "bidule.main:main"
# ```
#
# ```{admonition} attention au :
# Notez la présence du `:`, c'est bien `bidule.main:main` et non pas `bidule.main.main`
# ```
#
# On a dit plus haut qu'on n'avait plus besoin de refaire un `pip install`, mais dans ce cas précis c'est nécessaire tout de même:
#
# ```bash
# $ pip install -e .
# $ bidule-cli
# ici le déroulement de la fonction `main()` dans le fichier `bidule/main.py`
# ```

# ## Packages et `__init__.py`
#
# Historiquement avant la version 3.3 pour qu'un dossier se comporte comme un package il était **obligatoire** d'y créer un fichier de nom `__init__.py` - même vide au besoin.
#
# Ce n'est plus le cas depuis cette version. Toutefois, il peut s'avérer utile de créer ce fichier, et si vous lisez du code vous le trouverez très fréquemment.
#
# L'intérêt de ce fichier est de pouvoir agir sur :
#
# * le contenu du package lui-même, c'est-à-dire les attributs attachés à l'objet module associé à ce dossier,
# * et accessoirement d'exécuter du code supplémentaire.
#
# Un usage particulièrement fréquent consiste à "remonter" au niveau du package les symboles définis dans les sous-modules. Voyons ça sur un exemple.
#
# Dans notre dépôt de démonstration, nous avons une classe `Machine` définie dans le module `bidule.machine`. Donc de l'extérieur pour me servir de cette classe je dois faire
#
# ```python
# # dans le code utilisateur
#
# from bidule.machine import Machine
# ```
#
# C'est très bien, mais dès que le contenu va grossir, je vais couper mon code en de plus en plus de modules. Ce n'est pas tellement aux utilisateurs de devoir suivre ce genre de détails. Donc si je veux pouvoir changer mon découpage interne sans impacter les utilisateurs, je vais vouloir qu'on puisse faire plutôt, simplement
#
# ```python
# # dans le code utilisateur
#
# from bidule import Machine
# ```
#
# et pour y arriver, il me suffit d'ajouter cette ligne dans le `__init__.py` du package `bidule` :
#
# ```python
# # dans notre __init__.py
# from .machine import Machine 
# ```
#
# qui du coup, si vous avez bien suivi la leçon sur les imports, va définir le symbole `Machine` .. directement dans l'objet package ! c'est ce qu'on voulait :)

# ## Exposer le numéro de version
#
# Nous avons défini le numéro de version dans `pyproject.toml`; comment faire à présent pour exposer cette information aux utilisateurs de la librairie ?  
# c'est-à-dire qu'on aimerait pouvoir faire
#
# ```python
# import bidule
# print(bidule.__version__)
# ```
#
# pour retrouver notre `0.1.0`
#
# Pour y parvenir, on peut - par exemple - procéder comme ceci:
#
# * créer un fichier `bidule/version.py` qui contient
#   ```python
#   import importlib.metadata
#
#   __version__ = importlib.metadata.version("bidule")
#   ```
# * et pour exposer l'attribut `__version__` directement dans le package, comme on vient de le voir, on ajoute dans `bidule/__init__.py` la ligne
#   ```python
#   from .version import __version__
#   ```
#
# et maintenant:
#
# ```bash
# $ python -c "import bidule; print(bidule.__version__)"
# 0.1.0
# ```

# ## Publier sur PyPI
#
# Pour publier votre application sur PyPI, rien de plus simple :
#
# * il faut naturellement obtenir un login/password
# * il vous faudra installer `build` et `twine` :  
#   `pip install build twine`
#
# Ensuite à chaque version, une fois que les tests sont passés et tout :
#
# * préparer le packaging  
#   `python -m build`
#
# * pousser sur PyPI  
#   `twine upload dist/*`
#
# Signalons enfin qu'il existe une infra PyPI "de test" sur `https://test.pypi.org` utile quand on ne veut pas polluer l'index officiel.

# ## Utiliser `pip` pour installer
#
# Ensuite une fois que c'est fait, le monde entier peut profiter de votre magnifique contribution en faisant bien sûr
# `pip install bidule`
#
# Remarquez que l'on conseille parfois, pour éviter d'éventuels soucis de divergence entre les commandes `python`/`python3` et `pip`/`pip3`,
#
# * de remplacer tous les appels à `pip`  
# * par plutôt `python -m pip`, qui permet d'être sûr qu'on installe dans le bon environnement.
#
# D'autres formes utiles de `pip` :
#
# * `pip show bidule` : pour avoir des détails sur un module précis
# * `pip freeze` : pour une liste complète des modules installés dans l'environnement, avec leur numéro de version
# * `pip list` : sans grand intérêt, si ce n'est dans sa forme
#   `pip list -o` qui permet de lister les modules qui pourraient être mis à jour
#
# * `pip install -r requirements.txt` : pour installer les modules dont la liste est dans le fichier `requirements.txt`

# ## Autres usages de `pyproject.toml`
#
# Naturellement il y a plein d'autres réglages possibles dans le fichier `pyproject.toml`  
#
# Enfin il s'agit d'un format ouvert, et qu'ainsi on peut y ranger au même endroit des réglages utilisés par d'autres outils complètement. C'est donc là qu'on va trouver les réglages de tous les outils autour de Python *per se* (builders, linters, ...)
