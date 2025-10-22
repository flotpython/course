---
ipub:
  sphinx:
    toggle_input: true
    toggle_input_all: true
    toggle_output: true
    toggle_output_all: true
jupytext:
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
nbhosting:
  title: Modules et chemins
---

# Où sont cherchés les modules ?

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Complément - niveau basique

+++

Pour les débutants en informatique, le plus simple est de se souvenir que si vous voulez uniquement charger vos propres modules ou packages, il suffit de les placer **dans le répertoire où se trouve le point d'entrée**.
Pour rappel, le point d'entrée c'est le nom du fichier que vous passez à l'interpréteur lorsque vous démarrez votre programme.

+++

Lorsque vous lancez l'interpréteur **en mode interactif** (sans lui donner de point d'entrée), c'est **le répertoire courant** qui sert alors d'emplacement par défaut pour votre code. 
Le répertoire courant, c'est celui où vous vous trouvez quand vous lancez la commande python. Si vous n'êtes pas sûr de cet emplacement vous pouvez le savoir en faisant :

```{code-cell} ipython3
from pathlib import Path
Path.cwd()
```

## Complément - niveau intermédiaire

+++

Dans ce complément nous allons voir, de manière générale, comment sont localisés (sur le disque dur) les modules que vous chargez dans python grâce à l'instruction `import` ; nous verrons aussi où placer vos propres fichiers pour qu'ils soient accessibles à Python.

+++

[Comme expliqué ici](https://docs.python.org/3/tutorial/modules.html#the-module-search-path), lorsque vous importez le module `spam`, python cherche dans cet ordre :

* un module *built-in* de nom `spam` - possiblement/probablement écrit en C,
* ou sinon un fichier `spam.py` (ou un dossier `spam/`  s'il s'agit d'un package, éventuellement assorti d'un `__init__.py`) ; pour le localiser on utilise la variable `sys.path` (c'est-à-dire l'attribut `path` dans le module `sys`), qui est une liste de répertoires, et qui est initialisée avec, dans cet ordre :
  * le répertoire où se trouve le point d'entrée ;
  * la variable d'environnement `PYTHONPATH` ;
  * un certain nombre d'emplacements définis au moment de la compilation de python.

+++

Ainsi sans action particulière de l'utilisateur, Python trouve l'intégralité de la librairie standard, ainsi que les modules et packages installés dans le même répertoire que le fichier passé à l'interpréteur.

+++

La façon dont cela se présente dans l'interpréteur des notebooks peut vous induire en erreur. Aussi je vous engage à exécuter plutôt, et sur votre machine, le programme suivant :

+++

```python
#!/usr/bin/env python3

import sys
from pathlib import Path

def show_argv_and_path():
    print(f"le répertoire courant est {Path.cwd()}")
    print(f"le point d'entrée du programme est {sys.argv[0]}")
    print(f"la variable sys.path contient")
    for i, path in enumerate(sys.path, 1):
        print(f"{i}-ème chemin dans sys.path {path}")

show_argv_and_path()
```

+++

En admettant que 

* vous rangez ceci dans le fichier `/le/repertoire/du/script/run.py`
* et que vous lancez Python depuis un répertoire différent, disons `/le/repertoire/ou/vous/etes`
* et avec une variable `PYTHONPATH` vide;

+++

```bash
$ cd /le/repertoire/ou/vous/etes/
/le/repertoire/ou/vous/etes 
$ python3 /le/repertoire/du/script/run.py
```

+++

alors vous devriez observer une sortie sur le terminal comme ceci :

+++

```
le répertoire courant est /le/repertoire/ou/vous/etes
le point d'entrée du programme est /le/repertoire/du/script/run.py
la variable sys.path contient
1-ème chemin dans sys.path /le/repertoire/du/script
... <snip> ... le reste dépend de votre installation*
```

+++

C'est-à-dire que :

* la variable `sys.argv[0]` contient - en tous cas ici - le chemin complet `/le/repertoire/du/script/run.py`,
* et le premier terme dans `sys.path` contient `/le/repertoire/du/script/`.

(NB que [d'après cette documentation](https://docs.python.org/3/library/sys.html#sys.argv) `sys.argv[0]` peut contenir un chemin complet ou un simple nom de fichier, selon votre OS et comment vous invoquez Python)

+++

La [variable d'environnement](http://en.wikipedia.org/wiki/Environment_variable) PYTHONPATH est définie de façon à donner la possibilité d'étendre ces listes depuis l'extérieur, et sans recompiler l'interpréteur, ni modifier les sources. Cette possibilité s'adresse donc à l'utilisateur final - ou à son administrateur système - plutôt qu'au programmeur. Je vous recommande du coup de **ne pas utiliser cette *feature***, qu'il faut réserver à des cas bien précis.

+++

En tant que programmeur, vous avez aussi la possibilité d'étendre `sys.path` avant de faire vos `import`. Ici encore, ce n'est **pas une pratique** très courante, ni **très recommandée**.

+++

### Distribuer sa propre librairie avec `setuptools`

+++

On préfère en effet de beaucoup diffuser une application python, ou une librairie, sous forme de packaging en utilisant le [module setuptools](https://pypi.python.org/pypi/setuptools). Il s'agit d'un outil qui **ne fait pas partie de la librairie standard**, et qui supplante `distutils` qui lui, fait partie de la distribution standard mais qui est tombé en déshérence au fil du temps.

+++

`setuptools` permet au programmeur d'écrire - dans un fichier qu'on appelle traditionnellement `setup.py` - le contenu de son application ; grâce à quoi on peut ensuite de manière unifiée :

* installer l'application sur une machine à partir des sources ;
* préparer un package de l'application ;
* diffuser le package dans [l'infrastructure PyPI](https://pypi.python.org/pypi) ;
* installer le package depuis PyPI en utilisant [`pip3`](http://pip.readthedocs.org/en/latest/installing.html).

+++

Pour installer `setuptools`, comme d'habitude vous pouvez faire simplement :

```bash
pip3 install setuptools
```

+++

On reviendra en Semaine 6 sur les bonnes pratiques pour organiser l'arborescence des sources de votre projet, et notamment sur les techniques qui permettent de manière sûre de se passer de tout tripotage intempestif de `PYTHONPATH` et/ou `sys.path`.
