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
  title: npsearch
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

# Exercice - niveau intermédiaire

+++

## chercher une sous-matrice

+++

On vous demande d'écrire une fonction `npsearch`

1. qui accepte accepte en entrée deux paramètres
  * une matrice `world` (un tableau numpy de dimension 2)
  * un tableau `needle` à chercher dans la matrice; `needle` peut être de dimension 1 ou 2
1. `npsearch` est un générateur (i.e. une fonction génératrice), il doit énumérer tous les tuples d'indices `(i, j)` correspondant aux endroits de `world` qui coincident avec `needle`

```{code-cell} ipython3
import numpy as np

# c'est ce qu'on voit sur cet exemple

from corrections.exo_npsearch import exo_npsearch

exo_npsearch.example()
```

```{code-cell} ipython3
# à vous de jouer
# n'oubliez pas de déclarer les paramètres de votre fonction
def npsearch(world, needle):
    # souvenez-vous aussi que vous devez définir un générateur
    yield 0
```

```{code-cell} ipython3
exo_npsearch.correction(npsearch)
```

## Indices

* je vous invite autant que possible, comme toujours avec `numpy` :
  * à éviter  les boucles faites *à la main*
  * et à préférer des méthodes toutes faites pour faire des recherches
* essayez par exemple 
  * de définir une condition nécessaire sur `world[i, j]` lorsque `(i, j)` fait partie des solutions
  * et c'est peut-être l'occasion [de jeter un coup d'oeil à `numpy.argwhere`](https://numpy.org/doc/stable/reference/generated/numpy.argwhere.html)
* méfiez-vous aussi des expressions du genre `tableau_a == tableau_b` en ce sens que, si les deux tailles ne coincident pas, `numpy` va **essayer de faire du broadcasting** pour réconcilier les deux tailles, et ici clairement, ce **n'est pas ce qu'on veut**...

```{code-cell} ipython3
# enfin pour transformer une ligne en tableau 2D on a le choix entre 

a = np.array([1, 2, 3])
```

```{code-cell} ipython3
# version un peu poussive
n, = a.shape; a.reshape((1, n))
```

```{code-cell} ipython3
# version plus concise
a[np.newaxis, :]
```
