---
jupytext:
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
  title: 'exercice: hundreds'
---

# Exercice - niveau intermédiaire

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## construire un tableau $100 * i + 10 * j$

+++

On vous demande d'écrire une fonction `hundreds` qui crée un tableau `numpy`.

La fonction prend en argument:

* deux entiers `lines, columns` 
* un nombre entier offset

Le résultat doit être un tableau de taille `lines` x `columns`, composé d'entiers, et on veut qu'en une case de coordonnées (i, j) la valeur du tableau soit égale à 

$$result[i, j] = 100 * i + 10 * j + offset$$

```{code-cell} ipython3
import numpy as np
from corrections.exo_hundreds import exo_hundreds

# voici deux exemples pour la fonction hundreds
exo_hundreds.example()
```

```{code-cell} ipython3
:latex-hidden-code-instead: hundreds=exo_hundreds.solution
:latex-hidden-silent: true

# à vous de jouer
def hundreds(lines, columns, offset):
    return "votre code"
```

```{code-cell} ipython3
# pour corriger votre code
exo_hundreds.correction(hundreds)
```

## Plusieurs angles possibles

+++

* la première idée peut-être, consiste à faire deux boucles imbriquées  
  c'est facile à écrire, ça fonctionne, mais ce n'est pas très élégant  
  et surtout très inefficace, je vous invite à éviter cette approche  

* vous pouvez aussi penser à utiliser du broadcasting  
  en fabricant par exemple la souche des lignes et des colonnes  
  à la main avec `np.arange()`

* si vous regardez `np.indices()`, vous trouverez sans doute une inspiration
* et sans doute d'autres auxquelles je n'ai pas pensé :)
