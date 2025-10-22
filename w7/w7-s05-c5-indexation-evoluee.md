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
  title: "Indexation \xE9volu\xE9e"
---

# Indexation évoluée

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Complément - niveau avancé

+++

Nous allons maintenant voir qu'il est possible d'indexer un tableau `numpy` avec, non pas des entiers ou des tuples comme on l'a vu dans un complément précédent, mais aussi avec d'autres types d'objets qui permettent des manipulations très puissantes :

* indexation par une liste ;
* indexation par un tableau ;
* indexation multiple (par un tuple) ;
* indexation par un tableau de booléens.

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
plt.ion()
```

Pour illustrer ceci, on va réutiliser la fonction `background` que l'on avait vue pour les indexations simples :

```{code-cell} ipython3
# une fonction qui crée un tableau
# tab[i, j] = i + 10 * j
def background(n):
    i = np.arange(n)
    j = i.reshape((n, 1))
    return i + 10 * j
```

### Indexation par une liste

+++

On peut indexer par une liste d'entiers, cela constitue une généralisation des slices.

```{code-cell} ipython3
b = background(6)
print(b)
```

Si je veux référencer les lignes 1, 3 et 4, je ne peux pas utiliser un slice ; mais je peux utiliser une liste à la place :

```{code-cell} ipython3
# il faut lire ceci comme
# j'indexe b, avec comme indice la liste [1, 3, 4]
b[[1, 3, 4]]
```

```{code-cell} ipython3
# pareil pour les colonnes, en combinant avec un slice
b[:, [1, 3, 4]]
```

```{code-cell} ipython3
# et comme toujours on peut faire du broadcasting
b[:, [1, 3, 4]] = np.arange(1000, 1006).reshape((6, 1))
print(b)
```

### Indexation par un tableau

+++

On peut aussi indexer un tableau A … par un tableau ! Pour que cela ait un sens :

* le tableau d'index doit contenir des entiers ;
* ces derniers doivent être tous plus petits que la première dimension de A.

+++

#### Le cas simple : l'entrée et l'index sont de dimension 1.

```{code-cell} ipython3
# le tableau qu'on va indexer
cubes = np.arange(10) ** 3
print(cubes)
```

```{code-cell} ipython3
# et un index qui est un tableau numpy
# doit contenir des entiers entre 0 et 9
tab = np.array([1, 7, 2])
print(cubes[tab])
```

```{code-cell} ipython3
# donne - logiquement - le même résultat que
# si l'index était une liste Python
lis = [1, 7, 2]
print(cubes[lis])
```

#### De manière générale

+++

Dans le cas général, le résultat de `A[index]` :

* a la même forme "externe" que `index` ;
* où l'on a remplacé `i` par `A[i]` ;
* qui peut donc être un tableau si `A` est de dimension > 1

```{code-cell} ipython3
:cell_style: center

A = np.array([[0, 'zero'], [1, 'un'], [2, 'deux'], [3, 'trois']])
print(A)
```

```{code-cell} ipython3
:cell_style: center

index = np.array([[1, 0, 2], [3, 2, 3]])
print(index)
```

![parts](media/index-parts.png)

```{code-cell} ipython3
:tags: [gridwidth-1-2]

B = A[index]
print(B)
```

+++ {"tags": ["gridwidth-1-2"]}

![result](media/index-result.png)

```{code-cell} ipython3
:tags: [gridwidth-1-2]

B[1, 2, 1]
```

+++ {"tags": ["gridwidth-1-2"]}

![result](media/index-detail.png)

+++

Et donc si :

* `index` est de dimension `(i, j, k)` ;
* `A` est de dimension `(a, b)`.

Alors :

* `A[index]` est de dimension `(i, j, k, b)` ;
* il faut que les éléments dans `index` soient dans `[0 .. a[`.

+++

 Ce que l'on vérifie ici :

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# l'entrée
print(A.shape)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# l'index
print(index.shape)
```

```{code-cell} ipython3
# le résultat
print(A[index].shape)
```

#### Cas particulier : entrée de dimension 1,  `index` de dim. > 1

Lorsque l'entrée `A` est de dimension 1, alors la sortie a **exactement** la même forme que l'`index`.

C'est comme si `A` était une fonction que l'on applique aux indices dans `index`.

```{code-cell} ipython3
print(cubes)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

i2 = np.array([[2, 4], [8, 9]])
print(i2)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

print(cubes[i2])
```

#### Application au codage des couleurs dans une image

```{code-cell} ipython3
# je crée une image avec 6 valeurs disposées en diagonale
N = 32
colors = 6

image = np.empty((N, N), dtype = np.int32)
for i in range(N):
    for j in range(N):
       image[i, j] = (i+j) % colors
```

```{code-cell} ipython3
plt.imshow(image, cmap='gray');
```

Les couleurs ne sont pas significatives, ce sont des valeurs entières dans `range(colors)`. On voudrait pouvoir choisir la vraie couleur correspondant à chaque valeur. Pour cela on peut utiliser une simple indexation par tableau :

```{code-cell} ipython3
# une palette de couleurs
palette = np.array([
  [255, 255, 255], # 0 -> blanc
  [255, 0, 0],     # 1 -> rouge
  [0, 255, 0],     # 2 -> vert
  [0, 0, 255],     # 3 -> bleu
  [0, 255, 255],   # 4 -> cyan
  [255, 255, 0],   # 5 -> magenta
 ], dtype=np.uint8)
```

```{code-cell} ipython3
plt.imshow(palette[image]);
```

Remarquez que la forme générale n'a pas changé, mais le résultat de l'indexation a une dimension supplémentaire de 3 couleurs :

```{code-cell} ipython3
image.shape
```

```{code-cell} ipython3
palette[image].shape
```

### Indexation multiple (par tuple)

+++

Une fois que vous avez compris ce mécanisme d'indexation par un tableau, on peut encore généraliser pour définir une indexation par deux (ou plus) tableaux de formes identiques.

+++

Ainsi, lorsque `index1` et `index2` ont la même forme :

* on peut écrire `A[index1, index2]`
* qui a la même forme externe que les `index`
* où on a remplacé `i, j` par `A[i][j]`
* qui peut donc être un tableau si `A` est de dimension > 2.

```{code-cell} ipython3
# un tableau à indexer
ix, iy = np.indices((4, 3))
A = 10 * ix + iy
print(A)
```

```{code-cell} ipython3
# les deux tableaux d'indices sont carrés 2x2
index1 = [[3, 1], [0, 1]]  # doivent être < 4
index2 = [[2, 0], [0, 2]]  # doivent être < 3
# le résultat est donc carré 2x2
print(A[index1, index2])
```

Et donc si :

* `index1` et `index2` sont de dimension `(i, j, k)`
* et `A` est  de dimension `(a, b, c)`

Alors :

* le résultat est de dimension `(i, j, k, c)`
* il faut alors que les éléments  de `index1` soient dans `[0 .. a[`
* et les éléments de `index2` dans `[0 .. b[`

+++

#### Application à la recherche de maxima

+++

Imaginons que vous avez des mesures pour plusieurs instants :

```{code-cell} ipython3
times = np.linspace(1000, 5000, num=5, dtype=int)
print(times)
```

```{code-cell} ipython3
# on aurait 3 mesures à chaque instant
series = np.array([
    [10, 25, 32, 23, 12],
    [12, 8, 4, 10, 7],
    [100, 80, 90, 110, 120]])
print(series)
```

Avec la fonction `np.argmax` on peut retrouver les indices des points maxima dans `series` :

```{code-cell} ipython3
max_indices = np.argmax(series, axis=1)
print(max_indices)
```

Pour trouver les maxima en question, on peut faire :

```{code-cell} ipython3
# les trois maxima, un par serie
maxima = series[ range(series.shape[0]), max_indices ]
print(maxima)
```

```{code-cell} ipython3
# et ils correspondent à ces instants-ci
times[max_indices]
```

### Indexation par un tableau de booléens

+++

Une forme un peu spéciale d'indexation consiste à utiliser un tableau de booléens, qui agit comme un masque :

```{code-cell} ipython3
suite = np.array([1, 2, 3, 4, 5, 4, 3, 2, 1])
```

Je veux filtrer ce tableau et ne garder que les valeurs < 4 :

```{code-cell} ipython3
# je construis un masque
hauts = suite >= 4
print(hauts)
```

```{code-cell} ipython3
# je peux utiliser ce masque pour calculer les indices qui sont vrais
suite[hauts]
```

```{code-cell} ipython3
# et utiliser maintenant ceci par un index de tableau
# par exemple pour annuler ces valeurs
suite[hauts] = 0
print(suite)
```
