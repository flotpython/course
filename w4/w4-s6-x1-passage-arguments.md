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

# Passage d'arguments

+++

## Exercice - niveau basique

```{code-cell}
# pour charger l'exercice
from corrections.exo_distance import exo_distance
```

Vous devez écrire une fonction `distance` qui prend un nombre quelconque d'arguments numériques non complexes, et qui retourne la racine carrée de la somme des carrés des arguments. 

Plus précisément :
$distance$ ($x_1$, ..., $x_n$) = $\sqrt{\sum x_i^2}$

Par convention on fixe que $distance() = 0$

```{code-cell}
# des exemples
exo_distance.example()
```

```{code-cell}
# ATTENTION vous devez aussi définir les arguments de la fonction
def distance(votre, signature):
    return "votre code"
```

```{code-cell}
# la correction
exo_distance.correction(distance)
```

## Exercice - niveau intermédiaire

```{code-cell}
# Pour charger l'exercice
from corrections.exo_numbers import exo_numbers
```

On vous demande d'écrire une fonction `numbers` 

* qui prend en argument un nombre quelconque d'entiers,
* et qui retourne un tuple contenant
 * la somme
 * le minimum
 * le maximum
de ses arguments.

+++

Si aucun argument n'est passé, `numbers` doit renvoyer un tuple contenant 3 entiers `0`.

```{code-cell}
# par exemple
exo_numbers.example()
```

En guise d'indice, je vous invite à regarder les fonctions *built-in* [`sum`](https://docs.python.org/3/library/functions.html#sum), [`min`](https://docs.python.org/3/library/functions.html#min) et [`max`](https://docs.python.org/3/library/functions.html#max).

```{code-cell}
# vous devez définir votre propre signature
def numbers(votre, signature):
    "<votre_code>"
```

```{code-cell}
# pour vérifier votre code
exo_numbers.correction(numbers)
```
