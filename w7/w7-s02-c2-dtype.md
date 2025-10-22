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
  title: Type - dtype
---

# Type d'un tableau `numpy`

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Complément - niveau intermédiaire

+++

Nous allons voir dans ce complément ce qu'il faut savoir sur le type d'un tableau `numpy`.

```{code-cell} ipython3
import numpy as np
```

Dans ce complément nous allons rester en dimension 1 :

```{code-cell} ipython3
a = np.array([1, 2, 4, 8])
```

### Toutes les cellules ont le même type

+++

Comme on l'a vu dans la vidéo, les très bonnes performances que l'on peut obtenir en utilisant un tableau `numpy` sont liées au fait que le tableau est **homogène** : toutes les cellules du tableau **possèdent le même type** :

```{code-cell} ipython3
:cell_style: center

# pour accéder au type d'un tableau
a.dtype
```

Vous voyez que dans notre cas, le système a choisi pour nous un type entier ; selon les entrées on peut obtenir :

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# si je mets au moins un flottant
f = np.array([1, 2, 4, 8.])
f.dtype
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# et avec un complexe
c = np.array([1, 2, 4, 8j])
c.dtype
```

+++ {"cell_style": "center"}

Et on peut préciser le type que l'on veut si cette heuristique ne nous convient pas :

```{code-cell} ipython3
:cell_style: center

# je choisis explicitement mon dtype
c2 = np.array([1, 2, 4, 8], dtype=np.complex64)
c2.dtype
```

##### Pertes de précision

+++

Une fois que le type est déterminé, on s'expose à de possibles pertes de précision, comme d'habitude :

```{code-cell} ipython3
:tags: [gridwidth-1-2]

a, a.dtype
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# a est de type entier
# je vais perdre le 0.14
a[0] = 3.14
a
```

##### Types disponibles

+++

[Voyez la liste complète https://docs.scipy.org/doc/numpy/user/basics.types.html](https://docs.scipy.org/doc/numpy/user/basics.types.html).

Ce qu'il faut en retenir :

* vous pouvez choisir entre `bool`, `int`, `uint` (entier non signé), `float` et `complex` ;
* ces types ont diverses tailles pour vous permettre d'optimiser la mémoire réellement utilisée ;
* ces types existent en tant que tels (hors de tableaux).

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# un entier sur 1 seul octet, c'est possible !
np_1 = np.int8(1)
# l'équivalent en Python natif
py_1 = 1
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# il y a bien égalité
np_1 == py_1
```

```{code-cell} ipython3
:cell_style: center

# mais bien entendu ce ne sont pas les mêmes objets
np_1 is py_1
```

Du coup, on peut commencer à faire de très substantielles économies de place ; imaginez que vous souhaitez manipuler une image d'un million de pixels en noir et blanc sur 256 niveaux de gris ; j'en profite pour vous montrer `np.zeros` (qui fait ce que vous pensez) :

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# pur Python
from sys import getsizeof
pure_py = [0 for i in range(10**6)]
getsizeof(pure_py)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# numpy
num_py = np.zeros(10**6, dtype=np.int8)
getsizeof(num_py)
```

Je vous signale enfin l'attribut `itemsize` qui vous permet d'obtenir la taille en octets occupée par chacune des cellules, et qui correspond donc en gros au nombre qui apparaît dans `dtype`, mais divisé par huit :

```{code-cell} ipython3
:tags: [gridwidth-1-2]

a.dtype
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

a.itemsize
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

c.dtype
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

c.itemsize
```
