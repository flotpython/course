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
  title: packages
---

# La notion de package

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Complément - niveau basique

+++

Dans ce complément, nous approfondissons la notion de module, qui a été introduite dans les vidéos, et nous décrivons la notion de *package* qui permet de créer des bibliothèques plus structurées qu'avec un simple module.

+++

Pour ce notebook nous aurons besoin de deux utilitaires pour voir le code correspondant aux modules et packages que nous manipulons :

```{code-cell} ipython3
from modtools import show_module
```

### Rappel sur les modules

+++

Nous avons vu dans la vidéo qu'on peut charger une bibliothèque, lorsqu'elle se présente sous la forme d'un seul fichier source, au travers d'un objet python de type **module**.

+++

Chargeons un module "jouet" :

```{code-cell} ipython3
import module_simple
```

Voyons à quoi ressemble ce module :

```{code-cell} ipython3
show_module(module_simple)
```

On a bien compris maintenant que le module joue le rôle d'**espace de nom**, dans le sens où :

```{code-cell} ipython3
# on peut définir sans risque une variable globale 'spam'
spam = 'eggs'
print("spam globale", spam)
```

```{code-cell} ipython3
# qui est indépendante de celle définie dans le module
print("spam du module", module_simple.spam)
```

Pour résumer, un module est donc un objet python qui correspond à la fois à :

* un (seul) **fichier** sur le disque ;
* et un **espace de nom** pour les variables du programme.

+++

### La notion de package

+++

Lorsqu'il s'agit d'implémenter une très grosse bibliothèque, il n'est pas concevable de tout concentrer en un seul fichier. C'est là qu'intervient la notion de **package**, qui est un peu aux **répertoires** ce que que le **module** est aux **fichiers**.

+++

Nous allons illustrer ceci en créant un package qui contient un module. Pour cela nous créons une arborescence de fichiers comme ceci :

```bash
package_jouet/
              __init__.py
              module_jouet.py
```

+++

On importe un package exactement comme un module :

```{code-cell} ipython3
import package_jouet
```

Voici le contenu de ces deux fichiers :

```{code-cell} ipython3
show_module(package_jouet)
```

```{code-cell} ipython3
show_module(package_jouet.module_jouet)
```

Comme on le voit, le package porte **le même nom** que le répertoire, c'est-à-dire que, de même que le module `module_simple` correspond au fichier `module_simple.py`, le package python `package_jouet` corrrespond au répertoire `package_jouet`.

+++

**Note historique** par le passé, pour définir un package, il fallait obligatoirement créer dans le répertoire (celui, donc, que l'on veut exposer à python), un fichier nommé **`__init__.py`**; ce n'est plus le cas depuis Python-3.3.

Comme on le voit, importer un package revient essentiellement à charger, lorsqu'il existe, le fichier `__init__.py` dans le répertoire correspondant (et sinon, on obtient un package vide).

+++

On a coutume de faire la différence entre package et module, mais en termes d'implémentation les deux objets sont en fait de même nature, ce sont des modules :

```{code-cell} ipython3
type(package_jouet)
```

```{code-cell} ipython3
type(package_jouet.module_jouet)
```

Ainsi, le package se présente aussi comme un espace de nom, à présent on a une troisième variable `spam` qui est encore différente des deux autres :

```{code-cell} ipython3
package_jouet.spam
```

L'espace de noms du package permet de référencer les packages ou modules qu'il contient, comme on l'a vu ci-dessus, le package référence le module au travers de son attribut `module_jouet` :

```{code-cell} ipython3
package_jouet.module_jouet
```

### À quoi sert `__init__.py` ?

+++

Vous remarquerez que le module `module_jouet` a été chargé au même moment que `package_jouet`. Ce comportement **n'est pas implicite**. C'est nous qui avons explicitement choisi d'importer le module dans le package (dans `__init__.py`).

+++

Cette technique correpond à un usage assez fréquent, où on veut exposer directement dans l'espace de nom du package des symboles qui sont en réalité définis dans un module.

Avec le code ci-dessus, après avoir importé `package_jouet`, nous pouvons utiliser

```{code-cell} ipython3
package_jouet.jouet
```

alors qu'en fait il faudrait écrire en toute rigueur

```{code-cell} ipython3
package_jouet.module_jouet.jouet
```

Mais cela impose alors à l'utilisateur d'avoir une connaissance sur l'organisation interne de la bibliothèque, ce qui est considéré comme une mauvaise pratique.

D'abord, cela donne facilement des noms à rallonge et du coup nuit à la lisibilité, ce n'est pas pratique.
Mais surtout, que se passerait-il alors si le développeur du package voulait renommer des modules à l'intérieur de la bibliothèque ? On ne veut pas que ce genre de décision ait un impact sur les utilisateurs.

+++

De manière générale, `__init__.py` peut contenir n'importe quel code Python chargé d'initialiser le package. 
Notez que depuis Python-3.3, **la présence de **`__init__.py` n'est plus strictement nécessaire**.

+++

Lorsqu'il est présent, comme pour les modules usuels, `__init__.py` n'est chargé qu'une seule fois par l'interpréteur Python; s'il rencontre plus tard à nouveau le même `import`, il l'ignore silencieusement.

+++

### Pour en savoir plus

+++

Voir la [section sur les modules](https://docs.python.org/3/tutorial/modules.html) dans la documentation python, et notamment la [section sur les packages](https://docs.python.org/3/tutorial/modules.html#packages).
