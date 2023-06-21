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
notebookname: La clause `import as`
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# La clause `import as`

+++

## Complément - niveau intermédiaire

+++

### Rappel

+++

Jusqu'ici nous avons vu les formes d'importation suivantes :

+++

##### Importer tout un module

+++

D'abord pour importer tout un module

+++

```python
import monmodule
```

+++

##### Importer un symbole dans un module

+++

Dans la vidéo nous venons de voir qu'on peut aussi faire :

+++

```python
from monmodule import monsymbole
```

+++

Pour mémoire, le langage permet de faire aussi des `import *`, qui est d'un usage déconseillé en dehors de l'interpréteur interactif, car cela crée évidemment un risque de collisions non contrôlées des espaces de nommage.

+++

### `import_module`

+++

Comme vous pouvez le voir, avec `import` on ne peut importer qu'un nom fixe. On ne peut pas calculer le nom d'un module, et le charger ensuite :

```{code-cell} ipython3
# si on calcule un nom de module
modulename = "ma" + "th" 
```

on ne peut pas ensuite charger le module math avec import puisque 

```python
import modulename
```

cherche un module dont le nom est "modulename"

+++

Sachez que vous pourriez utiliser dans ce cas la fonction `import_module` du module `importlib`, qui cette fois permet d'importer un module dont vous avez calculé le nom :

```{code-cell} ipython3
from importlib import import_module
```

```{code-cell} ipython3
:cell_style: center

loaded = import_module(modulename)
type(loaded)
```

Nous avons maintenant bien chargé le module `math`, et on l'a rangé dans la variable `loaded`

```{code-cell} ipython3
# loaded référence le même objet module que si on avait fait 
# import math
import math
math is loaded
```

La fonction `import_module` n'est pas d'un usage très courant, dans la pratique on utilise une des formes de `import` que nous allons voir maintenant, mais `import_module` va me servir à bien illustrer ce que font, précisément, les différentes formes de `import`.

+++

### Reprenons

+++

Maintenant que nous savons ce que fait `import_module`, on peut récrire les deux formes d'`import`  de cette façon :

```{code-cell} ipython3
:cell_style: split

# un import simple
import math
```

```{code-cell} ipython3
:cell_style: split

# peut se récrire
math = import_module('math')
```

Et :

```{code-cell} ipython3
:cell_style: split

# et un import from
from pathlib import Path
```

```{code-cell} ipython3
:cell_style: split

# est en gros équivalent à
tmp = import_module('pathlib')
Path = tmp.Path
del tmp
```

### `import`  `as`

+++

##### Tout un module

+++

Dans chacun de ces deux cas, on n'a pas le choix du nom de l'entité importée, et cela pose parfois problème.

Il peut arriver d'écrire un module sous un nom qui semble bien choisi, mais on se rend compte au bout d'un moment qu'il entre en conflit avec un autre symbole.

Par exemple, vous écrivez un module dans un fichier `globals.py` et vous l'importez dans votre code

+++

```python
import globals
```

+++

Puis un moment après pour débugger vous voulez utiliser la fonction *built-in* `globals`. Sauf que, en vertu de la règle de visibilité des variables (rappelez-vous de la règle "LEGB", que l'on a vue dans une vidéo de la Semaine 4), le symbole `globals` se trouve maintenant désigner votre module, et non la fonction.

+++

À ce stade évidemment vous pouvez (devriez) renommer votre module, mais cela peut prendre du temps parce qu'il y a de nombreuses dépendances. En attendant vous pouvez tirer profit de la clause `import as` dont la forme générale est :

+++

```python
import monmodule as autremodule
```

+++

ce qui, toujours à la grosse louche, est équivalent à :

+++

```python
autremodule = import_module('monmodule')
```

+++

##### Un symbole dans un module

+++

On peut aussi importer un symbole spécifique d'un module, sous un autre nom que celui qu'il a dans le module. Ainsi :

+++

```
from monmodule import monsymbole as autresymbole
```

+++

qui fait quelque chose comme :

+++

```python
temporaire = import_module('monmodule')
autresymbole = temporaire.monsymbole
del temporaire
```

+++

### Quelques exemples

+++

J'ai écrit des modules jouets :

* `un_deux` qui définit des fonctions `un` et `deux` ;
* `un_deux_trois` qui définit des fonctions `un`, `deux` et `trois` ;
* `un_deux_trois_quatre` qui définit, eh oui, des fonctions `un`, `deux`, `trois` et `quatre`.
 
Toutes ces fonctions se contentent d'écrire leur nom et leur module.

```{code-cell} ipython3
# changer le nom du module importé
import un_deux as one_two
one_two.un()
```

```{code-cell} ipython3
# changer le nom d'un symbole importé du module
from un_deux_trois import un as one
one()
```

```{code-cell} ipython3
# on peut mélanger tout ça
from un_deux_trois_quatre import un as one, deux, trois as three
```

```{code-cell} ipython3
one()
deux()
three()
```

### Pour en savoir plus

+++

Vous pouvez vous reporter à [la section sur l'instruction `import`](https://docs.python.org/3/reference/simple_stmts.html#the-import-statement) dans la documentation python.
