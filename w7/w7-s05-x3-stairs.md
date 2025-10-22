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
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
language_info:
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
nbhosting:
  title: 'exercice: stairs'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
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

```{code-cell} ipython3
import numpy as np

from corrections.exo_stairs import exo_stairs

# voici deux exemples pour la fonction stairs
exo_stairs.example()
```

```{code-cell} ipython3
:latex-hidden-code-instead: stairs=exo_stairs.solution
:latex-hidden-silent: true

# à vous de jouer
def stairs(taille):
    return "votre code"
```

```{code-cell} ipython3
# pour corriger votre code
exo_stairs.correction(stairs)
```

### Visualisation

```{code-cell} ipython3
import matplotlib.pyplot as plt
%matplotlib inline
plt.ion()
```

L'exercice est terminé, voyons à nouveau notre résultat sous forme d'image :

```{code-cell} ipython3
squares = stairs(100)
```

Pour le voir comme une image avec un niveau de gris comme code de couleurs (noir = 0, blanc = maximum = 201 dans notre cas) :

```{code-cell} ipython3
:tags: [raises-exception]

# convertir en flottant pour imshow
squares = squares.astype(float)
# afficher avec une colormap 'gray'
plt.imshow(squares, cmap='gray');
```
