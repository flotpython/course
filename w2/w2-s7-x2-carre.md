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
  title: "exercice: compr\xE9hensions(2)"
---

# Compréhensions (2)

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Exercice - niveau intermédiaire

+++

### Mise au carré

On vous demande à présent d'écrire une fonction dans le même esprit que la fonction polynomiale du notebook précédent.
Cette fois, chaque ligne contient, séparés par des points-virgules, une liste d'entiers, et on veut obtenir une nouvelle chaîne avec les carrés de ces entiers, séparés par des deux-points.

À nouveau les lignes peuvent être remplies de manière approximative, avec des espaces, des tabulations, ou même des points-virgules en trop, que ce soit au début, à la fin, ou au milieu d'une ligne.

```{code-cell} ipython3
# exemples
from corrections.exo_carre import exo_carre
exo_carre.example()
```

```{code-cell} ipython3
# écrivez votre code ici
def carre(ligne):
    "<votre_code>"
```

```{code-cell} ipython3
# pour corriger
exo_carre.correction(carre)
```
