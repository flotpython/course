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
  title: "Compr\xE9hensions"
---

# Compréhensions

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Exercice - niveau basique

Il vous est demandé d'écrire une fonction `aplatir` qui prend *un unique* argument `l_conteneurs` qui est une liste (ou plus généralement un itérable) de conteneurs (ou plus généralement d'itérables), et qui retourne la liste de tous les éléments de tous les conteneurs.

```{code-cell} ipython3
# par exemple
from corrections.exo_aplatir import exo_aplatir
exo_aplatir.example()
```

```{code-cell} ipython3
def aplatir(conteneurs):
    "<votre_code>"
```

```{code-cell} ipython3
# vérifier votre code
exo_aplatir.correction(aplatir)
```

## Exercice - niveau intermédiaire

À présent, on passe en argument deux conteneurs (deux itérables) `c1` et `c2` de même taille à la fonction `alternat`, qui doit construire une liste contenant les éléments pris alternativement dans `c1` et dans `c2`.

```{code-cell} ipython3
# exemple
from corrections.exo_alternat import exo_alternat
exo_alternat.example()
```

**Indice** pour cet exercice il peut être pertinent de recourir à la fonction *built-in* `zip`.

```{code-cell} ipython3
def alternat(c1, c2):
    "<votre_code>"
```

```{code-cell} ipython3
# pour vérifier votre code
exo_alternat.correction(alternat)
```

## Exercice - niveau intermédiaire

+++

On se donne deux ensembles A et B de tuples de la forme

```python
(entier, valeur)
```

On vous demande d'écrire une fonction `intersect` qui retourne l'ensemble des objets `valeur` associés (dans A ou dans B) à un entier qui soit présent dans (un tuple de) A *et* dans (un tuple de) B.

```{code-cell} ipython3
# un exemple
from corrections.exo_intersect import exo_intersect
exo_intersect.example()
```

```{code-cell} ipython3
def intersect(A, B):
    "<votre_code>"
```

```{code-cell} ipython3
# pour vérifier votre code
exo_intersect.correction(intersect)
```
