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
  title: matrice diagonale
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

# Exercice - niveau intermédiaire

+++

## construire une matrice diagonale

+++

On vous demande d'écrire une fonction `matdiag` qui 

1. accepte un paramètre qui est une liste de nombres [$x_1$, $x_2$, …, $x_n$] 
1. retourne une matrice carrée diagonale dont les éléments valent

$$
m_{ii} = x_i 
$$
$$
m_{ij} = 0 \ pour\  i ≠ j
$$

Quelques précisions :

* il est raisonnable de retourner toujours un tableau de type  `float64`
* vous n'avez pas besoin de vérifier que l'appelant passe au moins un paramètre,
  ou dit autrement, les jeux de tests n'essaient pas d'appeler la fonction sans argument.

```{code-cell} ipython3
import numpy as np

# c'est ce qu'on voit sur cet exemple

from corrections.exo_matdiag import exo_matdiag

exo_matdiag.example()
```

```{code-cell} ipython3
# à vous de jouer
def matdiag(liste):
    ...
```

```{code-cell} ipython3
exo_matdiag.correction(matdiag)
```

## Indices

Vous trouverez dans les solutions 3 façons d'implémenter cette fonction; elles utilisent respectivement :  

une approche naïve, une approche à base de slicing, et une approche à base d'une fonction prédéfinie dans numpy.
