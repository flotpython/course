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
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
language_info:
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
notebookname: Broadcasting
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Le *broadcasting*

```{code-cell} ipython3
import numpy as np
```

## Complément - niveau intermédiaire

+++ {"slideshow": {"slide_type": "slide"}}

Lorsque l'on a parlé de programmation vectorielle, on a vu que l'on pouvait écrire quelque chose comme ceci :

```{code-cell} ipython3
X = np.linspace(0, 2 * np.pi)
Y = np.cos(X) + np.sin(X) + 2
```

+++ {"slideshow": {"slide_type": "slide"}}

Je vous fais remarquer que dans cette dernière ligne on combine :

* deux tableaux de mêmes tailles - quand on ajoute `np.cos(X)` avec `np.sin(X)` ;
* un tableau avec un scalaire - quand on ajoute `2` au résultat.

+++

En fait, le *broadcasting* est ce qui permet :

* d'unifier le sens de ces deux opérations ;
* de donner du sens à des cas plus généraux, où on fait des opérations entre des tableaux qui ont des *tailles différentes*, mais assez semblables pour que l'on puisse tout de même les combiner.

+++ {"slideshow": {"slide_type": "slide"}}

## Exemples en 2D

+++

Nous allons commencer par quelques exemples simples, avant de généraliser le mécanisme. Pour commencer, nous nous donnons un tableau de base :

```{code-cell} ipython3
---
cell_style: center
slideshow:
  slide_type: '-'
---
a = 100 * np.ones((3, 5), dtype=np.int32)
print(a)
```

Je vais illustrer le broadcasting avec l'opération `+`, mais bien entendu ce mécanisme est à l'œuvre dès que vous faites des opérations entre deux tableaux qui n'ont pas les mêmes dimensions.

Pour commencer, je vais donc ajouter à mon tableau de base un scalaire :

+++ {"slideshow": {"slide_type": "slide"}}

### Broadcasting entre les dimensions `(3, 5)` et `(1,)`

```{code-cell} ipython3
:cell_style: split

print(a)
```

```{code-cell} ipython3
:cell_style: split

b = 3
print(b)
```

***

+++

Lorsque j'ajoute ces deux tableaux, c'est comme si j'avais ajouté à `a` la différence :

```{code-cell} ipython3
:cell_style: split

# pour élaborer c
c = a + b
print(c)
```

```{code-cell} ipython3
:cell_style: split

# c'est comme si j'avais
# ajouté à a ce terme-ci
print(c - a)
```

C'est un premier cas particulier de *broadcasting* dans sa version extrême.

Le scalaire `b`, qui est en l'occurrence considéré comme un tableau dont le `shape` vaut `(1,)`, est dupliqué dans les deux directions jusqu'à obtenir ce tableau uniforme de taille `(5, 3)` et qui contient un `3` partout.

Et c'est ce tableau, qui est maintenant de la même taille que `a`, qui est ajouté à `a`.

+++

Je précise que cette explication est du domaine du modèle pédagogique ; je ne dis pas que l'implémentation va réellement allouer un second tableau, bien évidemment on peut optimiser pour éviter cette construction inutile.

+++ {"slideshow": {"slide_type": "slide"}}

### Broadcasting `(3, 5)` et `(5,)`

+++

Voyons maintenant un cas un peu moins évident. Je peux ajouter à mon tableau de base une ligne, c'est-à-dire un tableau de taille `(5, )`. Voyons cela :

```{code-cell} ipython3
---
cell_style: split
slideshow:
  slide_type: '-'
---
print(a)
```

```{code-cell} ipython3
:cell_style: split

b = np.arange(1, 6)
print(b)
```

```{code-cell} ipython3
:cell_style: split

b.shape
```

+++ {"cell_style": "center"}

****

+++

Ici encore, je peux ajouter les deux termes :

```{code-cell} ipython3
:cell_style: split

# je peux ici encore
# ajouter les tableaux
c = a + b
print(c)
```

```{code-cell} ipython3
:cell_style: split

# et c'est comme si j'avais
# ajouté à a ce terme-ci
print(c - a)
```

Avec le même point de vue que tout à l'heure, on peut se dire qu'on a d'abord transformé (broadcasté) le tableau `b` :

+++ {"cell_style": "split"}

depuis la dimension `(5,)`

+++ {"cell_style": "split"}

vers la dimension `(3, 5)`

```{code-cell} ipython3
:cell_style: split

# départ
print(b)
```

```{code-cell} ipython3
:cell_style: split

# arrivée
print(c - a)
```

Vous commencez à mieux voir comment ça fonctionne ; s'il existe une direction dans laquelle on peut "tirer" les données pour faire coincider les formes, on peut faire du broadcasting. Et ça marche dans toutes les directions, comme on va le voir tout de suite.

+++ {"slideshow": {"slide_type": "slide"}}

### Broadcasting `(3, 5)` et `(3, 1)`

+++

Au lieu d'ajouter à `a` une ligne, on peut lui ajouter une colonne, pourvu qu'elle ait la même taille que les colonnes de `a` :

```{code-cell} ipython3
---
cell_style: split
slideshow:
  slide_type: '-'
---
print(a)
```

```{code-cell} ipython3
:cell_style: split

b = np.arange(1, 4).reshape(3, 1)
print(b)
```

+++ {"cell_style": "center"}

****

+++

Voyons comment se passe le broadcasting dans ce cas-là :

```{code-cell} ipython3
:cell_style: split

c = a + b
print(c)
```

```{code-cell} ipython3
:cell_style: split

print(c - a)
```

Vous voyez que tout se passe exactement de la même façon que lorsqu'on avait ajouté une simple ligne, on a cette fois "tiré" la colonne dans la direction des lignes, pour passer :

+++ {"cell_style": "split"}

depuis la dimension `(3, 1)`

+++ {"cell_style": "split"}

vers la dimension `(3, 5)`

```{code-cell} ipython3
:cell_style: split

# départ
print(b)
```

```{code-cell} ipython3
:cell_style: split

# arrivée
print(c - a)
```

+++ {"slideshow": {"slide_type": "slide"}}

### Broadcasting `(3, 1)` et `(1, 5)`

+++

Nous avons maintenant tous les éléments en main pour comprendre un exemple plus intéressant, où les deux tableaux ont des formes pas vraiment compatibles à première vue :

```{code-cell} ipython3
:cell_style: split

col = np.arange(1, 4).reshape((3, 1))
print(col)
```

```{code-cell} ipython3
---
cell_style: split
slideshow:
  slide_type: '-'
---
line = 100 * np.arange(1, 6)
print(line)
```

+++ {"cell_style": "center"}

****

+++

Grâce au broadcasting, on peut additionner ces deux tableaux pour obtenir ceci :

```{code-cell} ipython3
:cell_style: split

m = col + line
print(m)
```

+++ {"cell_style": "split"}

Remarquez qu'ici les **deux** entrées ont été étirées pour atteindre une dimension commune.

+++

Et donc pour illustrer le broadcasting dans ce cas, tout se passe comme si on avait :

+++ {"cell_style": "split"}

transformé la colonne `(3, 1)`

+++ {"cell_style": "split"}

en tableau `(3, 5)`

```{code-cell} ipython3
:cell_style: split

print(col)
```

```{code-cell} ipython3
:cell_style: split

print(col + np.zeros(5, dtype=np.int64))
```

+++ {"cell_style": "split"}

et transformé la ligne `(1, 5)`

+++ {"cell_style": "split"}

en tableau `(3, 5)`

```{code-cell} ipython3
:cell_style: split

print(line)
```

```{code-cell} ipython3
:cell_style: split

print(line + np.zeros(3, dtype=np.int64).reshape((3, 1)))
```

avant d'additionner terme à terme ces deux tableaux 3 x 5.

+++ {"slideshow": {"slide_type": "slide"}}

## En dimensions supérieures

+++ {"slideshow": {"slide_type": "slide"}}

Pour savoir si deux tableaux peuvent être compatibles via *broadcasting*, il faut comparer leurs formes. Je commence par vous donner des exemples. Ici encore quand on mentionne l'addition, cela vaut pour n'importe quel opérateur binaire.

+++ {"slideshow": {"slide_type": "slide"}}

### Exemples de dimensions compatibles

+++ {"cell_style": "split"}

```python
A   15 x 3 x 5
B   15 x 1 x 5
A+B 15 x 3 x 5
```

+++ {"cell_style": "split"}

Cas de l'ajout d'un scalaire :
```python
A   15 x 3 x 5
B            1
A+B 15 x 3 x 5
```

+++ {"cell_style": "split"}

```python
A   15 x 3 x 5
B        3 x 5
A+B 15 x 3 x 5
```

+++ {"cell_style": "split"}

```python
A   15 x 3 x 5
B        3 x 1
A+B 15 x 3 x 5
```

+++ {"slideshow": {"slide_type": "slide"}}

### Exemples de dimensions **non compatibles**

+++ {"cell_style": "split"}

Deux lignes de longueurs différentes :
```python
A  3
B  4
```

+++ {"cell_style": "split", "slideshow": {"slide_type": "-"}}

Un cas plus douteux :
```python
A      2 x 1
B  8 x 4 x 3
```

+++

Comme vous le voyez sur tous ces exemples :

* on peut ajouter A et B lorsqu'il existe une dimension C qui "étire" à la fois celle de A et celle de B ;

* on le voit sur le dernier exemple, mais on ne peut broadcaster que de **1** vers $n$ ; lorsque $p>1$ divise $n$, on ne **peut pas** broadcaster de $p$ vers $n$, comme on pourrait peut-être l'imaginer.

+++

Comme c'est un cours de Python, plutôt que de formaliser ça sous une forme mathématique - je vous le laisse en exercice - je vais vous proposer plutôt une fonction Python qui détermine si deux tuples sont des `shape` compatibles de ce point de vue.

```{code-cell} ipython3
# le module broadcasting n'est pas standard
# c'est moi qui l'ai écrit pour illustrer le cours
from broadcasting import compatible, compatible2
```

```{code-cell} ipython3
:cell_style: split

# on peut dupliquer selon un axe
compatible((15, 3, 5), (15, 1, 5))
```

```{code-cell} ipython3
:cell_style: split

# ou selon deux axes
compatible((15, 3, 5), (5,))
```

```{code-cell} ipython3
:cell_style: split

# c'est bien clair que non
compatible((2,), (3,))
```

```{code-cell} ipython3
:cell_style: split

# on ne peut pas passer de 2 à 4
compatible((1, 2), (2, 4))
```
