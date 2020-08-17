---
jupytext:
  cell_metadata_filter: all
  notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
notebookname: m(i,j) = xi * xj
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Exercice - niveau intermédiaire

+++

## remplir une matrice : $m(i, j) = xi * xj$ 

+++

On vous demande d'écrire une fonction `xixj` qui 

1. accepte un nombre quelconque de paramètres, $x_1$, $x_2$, …, $x_n$, tous des flottants
1. retourne une matrice carrée symétrique $M$ dont les termes valent

$$
m_{ij} = x_i . x_j
$$

Vous n'avez pas besoin de vérifier que l'appelant passe au moins un paramètre, ou dit autrement, les jeux de tests n'essaient pas d'appeler la fonction sans argument.

```{code-cell} ipython3
import numpy as np

# c'est ce qu'on voit sur cet exemple

from corrections.exo_xixj import exo_xixj

exo_xixj.example()
```

```{code-cell} ipython3
# à vous de jouer
# n'oubliez pas de déclarer les paramètres de votre fonction
def xixj():
    ...
```

```{code-cell} ipython3
exo_xixj.correction(xixj)
```

## Indices

Vous trouverez dans les solutions 3 façons d'implémenter cette fonction; elles utilisent respectivement :  
l'opérateur `@`, la méthode `array.dot()`, le broadcasting.  
Souvenez vous que la transposée d'une matrice peut être obtenue en numpy avec l'attribut `.T` :

```{code-cell} ipython3
ligne = np.array([1, 2, 3])
ligne.reshape(3, 1)
```

```{code-cell} ipython3
ligne.T
```
