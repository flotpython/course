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
nbhosting:
  title: "Alg\xE8bre lin\xE9aire"
---

+++ {"slideshow": {"slide_type": "slide"}}

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Algèbre linéaire

+++

## Complément - niveau basique

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
plt.ion()
```

Un aspect important de l'utilisation de `numpy` consiste à manipuler des matrices et vecteurs. Voici une rapide introduction à ces fonctionnalités.

+++ {"slideshow": {"slide_type": "slide"}}

### Produit matriciel - `np.dot`

+++

**Rappel** : On a déjà vu que `*` entre deux tableaux faisait une multiplication terme à terme.

```{code-cell} ipython3
:tags: [gridwidth-1-2]

ligne = 1 + np.arange(3)
print(ligne)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

colonne = 1 + np.arange(3).reshape(3, 1)
print(colonne)
```

##### Ce n'est pas ce que l'on veut ici !

```{code-cell} ipython3
# avec le broadcasting, numpy me laisse écrire ceci
# mais **ce n'est pas** un produit matriciel
print(ligne * colonne)
```

L'opération de produit matriciel s'appelle `np.dot` :

```{code-cell} ipython3
:tags: [gridwidth-1-2]

m1 = np.array([[1, 1],
               [2, 2]])
print(m1)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

m2 = np.array([[10, 20],
               [30, 40]])
print(m2)
```

```{code-cell} ipython3
---
slideshow:
  slide_type: '-'
tags: [gridwidth-1-2]
---
# comme fonction
np.dot(m1, m2)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# comme méthode
m1.dot(m2)
```

Je vous signale aussi un opérateur spécifique, noté `@`, qui permet également de faire le produit matriciel.

```{code-cell} ipython3
:tags: [gridwidth-1-2]

m1 @ m2
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

m2 @ m1
```

C'est un opérateur un peu *ad hoc* pour `numpy`, puisqu'il ne fait pas de sens avec les types usuels de Python :

```{code-cell} ipython3
for x, y in ( (10, 20), (10., 20.), ([10], [20]), ((10,), (20,))):
    try:
        x @ y
    except Exception as e:
        print(f"OOPS - {type(e)} - {e}")
```

+++ {"slideshow": {"slide_type": "slide"}}

### Produit scalaire - `np.dot` ou `@`

+++

Ici encore, vous pouvez utiliser `dot` qui va intelligemment transposer le second argument :

```{code-cell} ipython3
:tags: [gridwidth-1-2]

v1 = np.array([1, 2, 3])
print(v1)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

v2 = np.array([4, 5, 6])
print(v2)
```

```{code-cell} ipython3
---
slideshow:
  slide_type: '-'
tags: [gridwidth-1-2]
---
np.dot(v1, v2)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

v1 @ v2
```

### Transposée

+++

Vous pouvez accéder à une matrice transposée de deux façons :

+++

* soit sous la forme d'un attribut `m.T` :

```{code-cell} ipython3
:tags: [gridwidth-1-2]

m = np.arange(4).reshape(2, 2)
print(m)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

print(m.T)
```

* soit par la méthode `transpose()` :

```{code-cell} ipython3
:tags: [gridwidth-1-2]

print(m)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

m.transpose()
```

### Matrice identité - `np.eye`

```{code-cell} ipython3
np.eye(4, dtype=np.int8)
```

### Matrices diagonales - `np.diag`

+++

Avec `np.diag`, vous pouvez dans les deux sens :

* extraire la diagonale d'une matrice ;

* construire une matrice à partir de sa diagonale.

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
M = np.arange(4) + 10 * np.arange(4)[:, np.newaxis]
print(M)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

D = np.diag(M)
print(D)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

M2 = np.diag(D)
print(M2)
```

### Déterminant - `np.linalg.det`

+++

Avec la fonction `np.linalg.det` :

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# une isométrie
M = np.array([[0, -1], [1, 0]])
print(M)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# et donc
np.linalg.det(M) == 1
```

### Valeurs propres - `np.linalg.eig`

+++

Vous pouvez obtenir valeurs propres et vecteurs propres d'une matrice avec `np.eig` :

```{code-cell} ipython3
# la symétrie par rapport à x=y
S = np.array([[0, 1], [1, 0]])
```

```{code-cell} ipython3
values, vectors = np.linalg.eig(S)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# pas de déformation
values
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# les deux diagonales
vectors
```

### Systèmes d'équations - `np.linalg.solve`

+++

Fabriquons-nous un système d'équations :

```{code-cell} ipython3
:tags: [gridwidth-1-2]

x, y, z = 1, 2, 3
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

3*x + 2*y + z
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

2*x + 3*y +4*z
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

5*x + 2*y + 6*z
```

On peut le résoudre tout simplement comme ceci :

```{code-cell} ipython3
:tags: [gridwidth-1-2]

coefficients= np.array([
    [3, 2, 1],
    [2, 3, 4],
    [5, 2, 6],
])
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

constants = [
    10,
    20,
    27,
]
```

```{code-cell} ipython3
X, Y, Z = np.linalg.solve(coefficients, constants)
```

Par contre bien sûr on est passé par les flottants, et donc on a le souci habituel avec la précision des arrondis :

```{code-cell} ipython3
Z
```

### Résumé

+++

En résumé, ce qu'on vient de voir :

+++

| outil             | propos                             |
|:------------------|:-----------------------------------|
| `np.dot`          | produit matriciel                  |
| `np.dot`          | produit scalaire                   |
| `np.transpose`    | transposée                         |
| `np.eye`          | matrice identité                   |
| `np.diag`         | extrait la diagonale               |
| `np.diag`         | ou construit une matrice diagonale |
| `np.linalg.det`   | déterminant                        |
| `np.linalg.eig`   | valeurs propres                    |
| `np.linalg.solve` | résout système équations           |

+++

### Pour en savoir plus

Voyez la [documentation complète](https://docs.scipy.org/doc/numpy/reference/routines.linalg.html) sur l'algèbre linéaire.
