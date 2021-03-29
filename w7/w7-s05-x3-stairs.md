---
jupytext:
  cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
  notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
notebookname: 'exercice: stairs'
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

## construire un tableau en escalier

+++

On vous demande d'écrire une fonction `stairs` qui crée un tableau `numpy`.

La fonction prend en argument un entier `taille` et construit un tableau carré de taille $2*taille+1$.

Aux quatre coins du tableau on trouve la valeur $0$. Dans la case centrale on trouve la valeur $2*taille$.

Si vous partez de n'importe quelle case et que vous vous déplacez d'une case horizontalement ou verticalement vers une cas plus proche du centre, vous incrémentez la valeur du tableau de `1`.

```{code-cell}
import numpy as np

from corrections.exo_stairs import exo_stairs

# voici deux exemples pour la fonction stairs
exo_stairs.example()
```

```{code-cell}
:latex:hidden-code-instead: stairs=exo_stairs.solution
:latex:hidden-silent: true

# à vous de jouer
def stairs(taille):
    return "votre code"
```

```{code-cell}
# pour corriger votre code
exo_stairs.correction(stairs)
```

### Visualisation

```{code-cell}
import matplotlib.pyplot as plt
%matplotlib inline
plt.ion()
```

L'exercice est terminé, voyons à nouveau notre résultat sous forme d'image :

```{code-cell}
squares = stairs(100)
```

Pour le voir comme une image avec un niveau de gris comme code de couleurs (noir = 0, blanc = maximum = 201 dans notre cas) :

```{code-cell}
# convertir en flottant pour imshow
squares = squares.astype(np.float)
# afficher avec une colormap 'gray'
plt.imshow(squares, cmap='gray');
```
