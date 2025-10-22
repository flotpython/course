---
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
nbhosting:
  title: Forme - shape
---

# Forme d'un tableau `numpy`

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

Nous allons voir dans ce complément comment créer des tableaux en plusieurs dimensions et manipuler la forme (`shape`) des tableaux.

```{code-cell} ipython3
import numpy as np
```

### Un exemple

+++

Nous avons vu précédemment comment créer un tableau `numpy` de dimension 1 à partir d'un simple itérable, nous allons à présent créer un tableau à 2 dimensions, et pour cela nous allons utiliser une liste imbriquée :

```{code-cell} ipython3
d2 = np.array([[11, 12, 13], [21, 22, 23]])
d2
```

Ce premier exemple va nous permettre de voir les différents attributs de tous les tableaux `numpy`.

+++

### L'attribut `shape`

+++

Tous les tableaux `numpy` possèdent un attribut `shape` qui retourne, sous la forme d'un tuple, les dimensions du tableau :

```{code-cell} ipython3
:cell_style: center

# la forme (les dimensions) du tableau
d2.shape
```

Dans le cas d'un tableau en 2 dimensions, cela correspond donc à **lignes** x **colonnes**.

+++

### On peut facilement changer de forme

+++

Comme on l'a vu dans la vidéo, un tableau est en fait une vue vers un bloc de données. Aussi il est facile de changer la dimension d'un tableau - ou plutôt, de créer une autre vue vers les mêmes données :

```{code-cell} ipython3
# l'argument qu'on passe à reshape est le tuple
# qui décrit la nouvelle *shape*
v2 = d2.reshape((3, 2))
v2
```

Et donc, ces deux tableaux sont deux vues vers la même zone de données ; ce qui fait qu'une modification sur l'un se répercute dans l'autre :

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# je change un tableau
d2[0][0] = 100
d2
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# ça se répercute dans l'autre
v2
```

### Les attributs liés à la forme

+++

Signalons par commodité les attributs suivants, qui se dérivent de `shape` :

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# le nombre de dimensions
d2.ndim
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# vrai pour tous les tableaux
len(d2.shape) == d2.ndim
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# le nombre de cellules
d2.size
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# vrai pour tous les tableaux
# une façon compliquée de dire
# une chose toute simple :
# la taille est le produit
# des dimensions
from operator import mul
from functools import reduce
d2.size == reduce(mul, d2.shape, 1)
```

Lorsqu'on utilise `reshape`, il faut bien sûr que la nouvelle forme soit compatible :

```{code-cell} ipython3
try:
    d2.reshape((3, 4))
except Exception as e:
    print(f"OOPS {type(e)} {e}")
```

### Dimensions supérieures

+++

Vous pouvez donc deviner comment on construit des tableaux en dimensions supérieures à 2, il suffit d'utiliser un attribut `shape` plus élaboré :

```{code-cell} ipython3
:cell_style: center

shape = (2, 3, 4)
size = reduce(mul, shape)

# vous vous souvenez de arange
data = np.arange(size)
```

```{code-cell} ipython3
:cell_style: center

d3 = data.reshape(shape)
d3
```

Cet exemple vous permet de voir qu'en dimensions supérieures la forme est toujours :

  n1 x n2 x ... x **lignes** x **colonnes**

+++

Enfin, ce que je viens de dire est arbitraire, dans le sens où, bien entendu, vous pouvez décider d'interpréter les tableaux comme vous voulez.

Mais en termes au moins de l'impression par `print`, il est logique de voir que l'algorithme d'impression balaye le tableau de manière mécanique comme ceci :
```python
for i in range(2):
    for j in range(3):
        for k in range(4):
            array[i][j][k]
```

+++

Et c'est pourquoi vous obtenez la présentation suivante avec des tableaux de dimensions plus grandes :

```{code-cell} ipython3
:cell_style: center

# la même chose avec plus de dimensions
shape = (2, 3, 4, 5)
size = reduce(mul, shape) # le produit des 4 nombres dans shape
size
```

```{code-cell} ipython3
:cell_style: center

data = np.arange(size)

# ce tableau est visualisé
# à base de briques de base
# de 4 lignes et 5 colonnes
d4 = data.reshape(shape)
d4
```

+++ {"cell_style": "center"}

Vous voyez donc qu'avec la forme :

```python
2, 3, 4, 5
```

cela vous donne l'impression que vous avez comme brique de base des tableaux qui ont :

```python
4 lignes
5 colonnes
```

+++

Et souvenez-vous que vous pouvez toujours insérer un `1` n'importe où dans la forme, puisque ça ne modifie pas la taille qui est le produit des dimensions :

```{code-cell} ipython3
:tags: [gridwidth-1-2]

d2.shape
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

d2
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

d2.reshape(2, 1, 3)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

d2.reshape(2, 3, 1)
```

Ou même :

```{code-cell} ipython3
:tags: [gridwidth-1-2]

d2.reshape((1, 2, 3))
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

d2.reshape((1, 1, 1, 1, 2, 3))
```

### Résumé des attributs

+++

Voici un résumé des attributs des tableaux `numpy` :

+++

| *attribut* | *signification*               | *exemple*    |
|-----------:|------------------------------:|-------------:|
| `shape`    | tuple des dimensions          | `(3, 5, 7)`  |
| `ndim`     | nombre dimensions             | `3`          |
| `size`     | nombre d'éléments             | `3 * 5 * 7`  |
| `dtype`    | type de chaque élément        | `np.float64` |
| `itemsize` | taille en octets d'un élément | `8`          |

+++

### Divers

+++

Je vous signale enfin, à titre totalement anecdotique cette fois, l'existence de la méthode `ravel` qui vous permet d'aplatir n'importe quel tableau :

```{code-cell} ipython3
d2
```

```{code-cell} ipython3
d2.ravel()
```

```{code-cell} ipython3
# il y a d'ailleurs aussi flatten qui fait
# quelque chose de semblable
d2.flatten()
```
