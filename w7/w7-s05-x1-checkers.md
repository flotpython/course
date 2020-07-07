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
from corrections.exo_checkers import exo_checkers
```

On vous demande d'écrire une fonction `checkers` qui crée un tableau `numpy`.

La fonction prend en argument:

* un entier `size` >= 1
* et un booléen `corner_0_0` - qui vaut par défaut `True`

Elle construit et retourne alors un tableau carré de taille `size` x `size`, qui est rempli comme un damier avec des entiers 0 et 1; la valeur de la cellule d'indice 0 x 0 est correspond au paramètre `corner_0_0`.

On rappelle par ailleurs que `False == 0` et `True == 1`.

```{code-cell}
---
slideshow:
  slide_type: fragment
---
# voici deux exemples pour la fonction checkers
exo_checkers.example()
```

```{code-cell}
:latex:hidden-code-instead: checkers=exo_checkers.solution
:latex:hidden-silent: true

# à vous de jouer
def checkers(size, corner_0_0=True):
    return "votre code"
```

```{code-cell}
# pour corriger votre code
exo_checkers.correction(checkers)
```

### Visualisation

```{code-cell}
import matplotlib.pyplot as plt
%matplotlib inline
plt.ion()
```

L'exercice est terminé, mais si vous avez réussi et que vous voulez visualisez le résultat, voici comment vous pouvez aussi voir ce type de tableau :

```{code-cell}
checkerboard = checkers(8, False)
```

Pour le voir comme une image:

```{code-cell}
---
slideshow:
  slide_type: fragment
---
# convertir en flottant pour imshow
checkerboard = checkerboard.astype(np.float)
# afficher avec une colormap 'gray' pour avoir du noir et blanc
plt.imshow(checkerboard, cmap='gray');
```
