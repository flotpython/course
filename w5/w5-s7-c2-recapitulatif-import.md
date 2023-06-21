---
jupytext:
  cell_metadata_filter: all, -hidden, -heading_collapsed, -run_control, -trusted
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
nbhosting:
  title: "R\xE9capitulatif import"
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Récapitulatif sur `import`

+++

## Complément - niveau basique

+++

Nous allons récapituler les différentes formes d'importation, et introduire la clause `import *` - et voir pourquoi il est déconseillé de l'utiliser.

+++

### Importer tout un module

+++

L'`import` le plus simple consiste donc à uniquement mentionner le nom du module

```{code-cell} ipython3
import un_deux
```

Ce module se contente de définir deux fonctions de noms `un` et `deux`. Une fois l'import réalisé de cette façon, on peut accéder au contenu du module en utilisant un nom de variable complet :

```{code-cell} ipython3
# la fonction elle-même
print(un_deux.un)

un_deux.un()
```

Mais bien sûr on n'a pas de cette façon défini de nouvelle variable `un` ; la seule nouvelle variable dans la portée courante est donc `un_deux` :

```{code-cell} ipython3
# dans l'espace de nommage courant on peut accéder au module lui-même
print(un_deux)
```

```{code-cell} ipython3
# mais pas à la variable `un`
try:
    print(un)
except NameError: 
    print("La variable 'un' n'est pas définie")
```

### Importer une variable spécifique d'un module

+++

On peut également importer un ou plusieurs symboles spécifiques d'un module en faisant maintenant (avec un nouveau module du même tonneau) :

```{code-cell} ipython3
from un_deux_trois import un, deux
```

À présent nous avons deux nouvelles variables dans la portée locale :

```{code-cell} ipython3
un()
deux()
```

Et cette fois, c'est le module lui-même qui n'est pas accessible :

```{code-cell} ipython3
try:
    print(un_deux_trois)
except NameError:
    print("La variable 'un_deux_trois' n'est pas définie")
```

Il est important de voir que la variable locale ainsi créée, un peu comme dans le cas d'un appel de fonction, est une **nouvelle variable** qui est initialisée avec l'objet du module. Ainsi si on importe le module **et** une variable du module comme ceci :

```{code-cell} ipython3
import un_deux_trois
```

alors nous avons maintenant **deux variables différentes** qui désignent la fonction `un` dans le module :

```{code-cell} ipython3
print(un_deux_trois.un)
print(un)
print("ce sont deux façons d'accéder au même objet", un is un_deux_trois.un)
```

En on peut modifier l'une **sans affecter** l'autre :

```{code-cell} ipython3
# les deux variables sont différentes
# un n'est pas un 'alias' vers un_deux_trois.un
un = 1
print(un_deux_trois.un)
print(un)
```

## Complément - niveau intermédiaire

+++

### `import` .. `as`

+++

Que l'on importe avec la forme `import unmodule` ou avec la forme `from unmodule import unevariable`, on peut toujours ajouter une clause `as nouveaunom`, qui change le nom de la variable qui est ajoutée dans l'environnement courant.

+++

Ainsi :

* `import foo` définit une variable `foo` qui désigne un module ;
* `import foo as bar` a le même effet, sauf que le module est accessible par la variable `bar` ;

+++

Et :

* `from foo import var` définit une variable `var` qui désigne un attribut du module ;
* `from foo import var as newvar` définit une variable `newvar` qui désigne ce même attribut.

+++

Ces deux formes sont pratiques pour éviter les conflits de nom.

```{code-cell} ipython3
# par exemple
import un_deux as mod12
mod12.un()
```

```{code-cell} ipython3
from un_deux import deux as m12deux
m12deux()
```

### `import *`

+++

La dernière forme d'`import` consiste à importer toutes les variables d'un module comme ceci :

```{code-cell} ipython3
from un_deux_trois_quatre import *
```

Cette forme, pratique en apparence, va donc créer dans l'espace de nommage courant les variables

```{code-cell} ipython3
un()
deux()
trois()
quatre()
```

### Quand utiliser telle ou telle forme

+++

Les deux premières formes - import d'un module ou de variables spécifiques - peuvent être utilisées indifféremment ; souvent lorsqu'une variable est utilisée très souvent dans le code on pourra préférer la deuxième forme pour raccourcir le code.

+++

À cet égard, citons des variantes de ces deux formes qui permettent d'utiliser des noms plus courts. Vous trouverez par exemple très souvent

```python
import numpy as np
```

qui permet d'importer le module numpy mais de l'utiliser sous un nom plus court - car avec `numpy` on ne cesse d'utiliser des symboles dans le module.

+++

**Avertissement :** nous vous recommandons de **ne pas utiliser la dernière forme `import *`** - sauf dans l'interpréteur interactif - car cela peut gravement nuire à la lisibilité de votre code.

+++

python est un langage à liaison statique ; cela signifie que lorsque vous concentrez votre attention sur un (votre) module, et que vous voyez une référence en lecture à une variable `spam` disons à la ligne 201, vous devez forcément trouver dans les deux cents premières lignes quelque chose comme une déclaration de `spam`, qui vous indique en gros d'où elle vient.

`import *` est une construction qui casse cette bonne propriété (pour être tout à fait exhaustif, cette bonne propriété n'est pas non plus remplie avec les fonctions *built-in* comme `len`, mais il faut vivre avec...) 

Mais le point important est ceci : imaginez que dans un module vous faites plusieurs `import *` comme par exemple

```python
from django.db import *
from django.conf.urls import *
```

Peu importe le contenu exact de ces deux modules, il nous suffit de savoir qu'un des deux modules expose la variable `patterns`. 

Dans ce cas de figure vécu, le module utilise cette variable `patterns` sans avoir besoin de la déclarer explicitement, si bien qu'à la lecture on voit une utilisation de la variable `patterns`, mais on n'a plus aucune idée de quel module elle provient, sauf à aller lire le code correspondant...

+++

## Complément - niveau avancé

+++

### `import` de manière "programmative"

+++

Étant donné la façon dont est conçue l'instruction `import`, on rencontre une limitation lorsqu'on veut, par exemple, **calculer le nom d'un module** avant de l'importer.

Si vous êtes dans ce genre de situation, reportez-vous au module [`importlib`](https://docs.python.org/3/library/importlib.html)
et notamment sa fonction `import_module` qui, cette fois, accepte en argument une chaîne.

+++

Voici une illustration dans un cas simple. Nous allons importer le module `modtools` (qui fait partie de ce MOOC) de deux façons différentes et montrer que le résultat est le même :

```{code-cell} ipython3
# on importe la fonction 'import_module' du module 'importlib'
from importlib import import_module

# grâce à laquelle on peut importer à partir d'un string 
imported_modtools = import_module('mod' + 'tools')

# on peut aussi importer modtools "normalement"
import modtools

# les deux objets sont identiques
imported_modtools is modtools
```

### Imports relatifs

+++

Il existe aussi en python une façon d'importer des modules, non pas directement en cherchant depuis `sys.path`, mais en cherchant à partir du module où se trouve la clause `import`. Nous détaillons ce trait dans un complément ultérieur.
