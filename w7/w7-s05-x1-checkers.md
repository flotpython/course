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
  title: 'exercice: checkers'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

# Exercice - niveau basique

+++

## construire un tableau en damier

+++

On vous demande d'écrire une fonction `checkers` qui crée un tableau `numpy`.

La fonction prend en argument:

* un entier `size` >= 1
* et un booléen `corner_0_0` - qui vaut par défaut `True`

Elle construit et retourne alors un tableau carré de taille `size` x `size`, qui est rempli comme un damier avec des entiers 0 et 1; la valeur de la cellule d'indice 0 x 0 est correspond au paramètre `corner_0_0`.

On rappelle par ailleurs que `False == 0` et `True == 1`.

```{code-cell} ipython3
import numpy as np

from corrections.exo_checkers import exo_checkers

# voici deux exemples pour la fonction checkers
exo_checkers.example()
```

```{code-cell} ipython3
:latex-hidden-code-instead: checkers=exo_checkers.solution
:latex-hidden-silent: true

# à vous de jouer
def checkers(size, corner_0_0=True):
    return "votre code"
```

```{code-cell} ipython3
# pour corriger votre code
exo_checkers.correction(checkers)
```

### Visualisation

```{code-cell} ipython3
import matplotlib.pyplot as plt
%matplotlib inline
plt.ion();
```

L'exercice est terminé, mais si vous avez réussi et que vous voulez visualisez le résultat, voici comment vous pouvez aussi voir ce type de tableau :

```{code-cell} ipython3
checkerboard = checkers(8, False)
```

Pour le voir comme une image:

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
# convertir en flottant pour imshow
checkerboard = checkerboard.astype(float)
# afficher avec une colormap 'gray' pour avoir du noir et blanc
plt.imshow(checkerboard, cmap='gray');
```
