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
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Exercice - niveau basique

```{code-cell}
import numpy as np
```

```{code-cell}
from corrections.exo_hundreds import exo_hundreds
```

On vous demande d'écrire une fonction `hundreds` qui crée un tableau `numpy`.

La fonction prend en argument:

* deux entiers `lines, columns` 
* un nombre entier offset

Le résultat doit être un tableau de taille `lines` x `columns`, composé d'entiers, et on veut qu'en une case de coordonnées (i, j) la valeur du tableau soit égale à 

$$result[i, j] = 100 * i + 10 * j + offset$$

```{code-cell}
---
slideshow:
  slide_type: fragment
---
# voici deux exemples pour la fonction hundreds
exo_hundreds.example()
```

```{code-cell}
:latex:hidden-code-instead: hundreds=exo_hundreds.solution
:latex:hidden-silent: true

# à vous de jouer
def hundreds(lines, columns, offset):
    return "votre code"
```

```{code-cell}
# pour corriger votre code
exo_hundreds.correction(hundreds)
```

## Plusieurs angles possibles

+++

* La première idée peut-être, consiste à faire comme en Fortran, avec deux boucles imbriquées; c'est facile à écrire, ça fonctionne, mais ce n'est pas très élégant;
* vous pouvez aussi penser à utiliser du broadcasting:
  * dans ce cas-là `np.indices()` peut vous être utile;
  * vous pouvez aussi vous entrainer à fabriquer la souche des lignes et des colonnes à la main avec `np.arange()` en combinaison avec `np.newaxis`;
* et sans doute d'autres auxquelles je n'ai pas pensé :)
