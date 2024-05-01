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
  title: "Cr\xE9ation de tableaux"
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

# Création de tableaux

+++

## Complément - niveau basique

+++

Passons rapidement en revue quelques méthodes pour créer des tableaux `numpy`.

```{code-cell} ipython3
import numpy as np
```

### Non initialisé : `np.empty`

+++

La méthode la plus efficace pour créer un tableau `numpy` consiste à faire l'allocation de la mémoire mais sans l'initialiser :

```{code-cell} ipython3
:cell_style: center

memory = np.empty(dtype=np.int8,
                  shape=(1_000, 1_000))
```

J'en profite pour attirer votre attention sur l'impression des gros tableaux où l'on s'efforce de vous montrer les coins :

```{code-cell} ipython3
print(memory)
```

Il se *peut* que vous voyiez ici des valeurs particulières ; selon votre OS, il y a une probabilité non nulle que vous ne voyiez ici que des zéros. C'est un peu comme avec les dictionnaires qui, depuis la version 3.6, peuvent donner l'impression de conserver l'ordre dans lequel les clés ont été créées. Ici c'est un peu la même chose, vous ne devez pas écrire un programme qui repose sur le fait que `np.empty` retourne un tableau garni de zéros (utilisez alors `np.zeros`, que l'on va voir tout de suite).

+++

### Tableaux constants

+++

On peut aussi créer et initialiser un tableau avec `np.zeros` et `np.ones` :

```{code-cell} ipython3
zeros = np.zeros(dtype=np.complex128, shape=(1_000, 100))
print(zeros)
```

```{code-cell} ipython3
fours = 4 * np.ones(dtype=float, shape=(8, 8))
fours
```

### Progression arithmétique : `arange`

+++

En guise de rappel, avec `arange` on peut créer des tableaux de valeurs espacées d'une valeur constante. Ça ressemble donc un peu au `range` de Python natif :

```{code-cell} ipython3
:tags: [gridwidth-1-2]

np.arange(4)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

np.arange(1, 5)
```

Sauf qu'on peut y passer un pas qui n'est pas entier :

```{code-cell} ipython3
np.arange(5, 7, .5)
```

### Progression arithmétique : `linspace`

+++

Mais bien souvent, plutôt que de préciser *le pas* entre deux valeurs, on préfère préciser *le nombre* de points ; et aussi inclure la deuxième borne. C'est ce que fait `linspace`, c'est très utile pour modéliser une fonction sur un intervalle ; on a déjà vu des exemples de ce genre :

```{code-cell} ipython3
%matplotlib inline
import matplotlib.pyplot as plt
plt.ion()
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

X = np.linspace(-3., +3.)
Y = np.exp(X)

plt.plot(X, Y);
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# par défaut linspace crée 50 points
# avec moins de points

X = np.linspace(1/10, 10, num = 5)
plt.plot(X, np.log(X));
```

Pour des intervalles en progression géométrique, voyez `np.geomspace`.

+++

### Multi-dimensions : `indices`

+++

La méthode `np.indices` se comporte un peu comme `arange` mais pour plusieurs directions ; voyons ça sur un exemple :

```{code-cell} ipython3
ix, iy = np.indices((3, 5))
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

ix
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

iy
```

Cette fonction s'appelle `indices` parce qu'elle produit des tableaux (ici 2 car on lui a passé une `shape` à deux dimensions) qui contiennent, à la case *(i, j)*, $i$ (pour le premier tableau) ou $j$ pour le second.

+++

Ainsi, si vous voulez construire un tableau de taille (2, 4) dans lequel, par exemple :
```pythonpython
tab[i, j] = 200*i + 2*j + 50
```
Vous n'avez qu'à faire :

```{code-cell} ipython3
ix, iy = np.indices((2, 4))
tab = 200*ix + 2*iy + 50
tab
```

### Multi-dimensions : `meshgrid`

+++

Si vous voulez créer un tableau un peu comme avec `linspace`, mais en plusieurs dimensions : imaginez par exemple que vous voulez tracer une fonction à deux entrées :

$f : (x, y) \longrightarrow cos(x) + cos^2(y)$

Sur un pavé délimité par :

$x \in [-\pi, +\pi], y \in [3\pi, 5\pi]$

+++

Il vous faut donc créer un tableau, disons de 50 x 50 points, qui réalise un maillage uniforme de ce pavé, et pour ça vous pouvez utiliser `meshgrid`. Pour commencer :

```{code-cell} ipython3
# on fabrique deux tableaux qui échantillonnent
# de manière uniforme les intervalles en X et en Y
# on prend un pas de 10 dans les deux sens, ça nous donnera
# 100 points pour couvrir l'espace carré qui nous intéresse

Xticks, Yticks = (np.linspace(-np.pi, np.pi, num=10),
                  np.linspace(3*np.pi, 5*np.pi, num=10))
```

Avec meshgrid, on va créer deux tableaux, qui sont respectivement les (100) X et les (100) Y de notre maillage :

```{code-cell} ipython3
# avec meshgrid on les croise
# ça fait comme un produit cartésien, 
# en extrayant les X et les Y du résultat

X, Y = np.meshgrid(Xticks, Yticks)

# chacun des deux est donc de taille 10 x 10
X.shape, Y.shape
```

Que peut-on faire avec ça ? Eh bien, en fait, on a tout ce qu'il nous faut pour afficher notre fonction :

```{code-cell} ipython3
# un tableau 10 x 10 qui contient les images de f()
# sur les points de la grille
Z = np.cos(X) + np.cos(Y)**2
```

```{code-cell} ipython3
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z);
```

Je vous laisse vous convaincre qu'il est facile d'écrire `np.indices` à partir de `np.meshgrid` et `np.arange`.
