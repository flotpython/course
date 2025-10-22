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
  title: "exercice: compr\xE9hensions(1)"
---

# Compréhensions (1)

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Exercice - niveau basique

+++

### Liste des valeurs d'une fonction

On se donne une fonction polynomiale :

$P(x) = 2x^2 - 3x - 2$

+++

On vous demande d'écrire une fonction `liste_P` qui prend en argument une liste de nombres réels $x$ et qui retourne la liste des valeurs $P(x)$.

```{code-cell} ipython3
# voici un exemple de ce qui est attendu
from corrections.exo_liste_p import exo_liste_P
exo_liste_P.example()
```

Écrivez votre code dans la cellule suivante (*On vous suggère d'écrire une fonction `P` qui implémente le polynôme mais ça n'est pas strictement indispensable, seul le résultat de `liste_P` compte*) :

```{code-cell} ipython3
:latex-hidden-code-instead: liste_P = exo_liste_P.solution
:latex-hidden-silent: true

def P(x):
    "<votre code>"

def liste_P(liste_x):
    "votre code"
```

Et vous pouvez le vérifier en évaluant cette cellule :

```{code-cell} ipython3
:latex-skip-eval: true

# pour vérifier votre code
exo_liste_P.correction(liste_P)
```

******

+++

## Récréation

+++

Si vous avez correctement implémenté la fonction `liste_P` telle que demandé dans le premier exercice, vous pouvez visualiser le polynôme `P` en utilisant `matplotlib` avec le code suivant :

```{code-cell} ipython3
# on importe les bibliothèques
import numpy as np
import matplotlib.pyplot as plt
```

```{code-cell} ipython3
# un échantillon des X entre -10 et 10
X = np.linspace(-10, 10)

# et les Y correspondants
Y = liste_P(X)
```

```{code-cell} ipython3
:tags: [raises-exception]

# on n'a plus qu'à dessiner
plt.plot(X, Y)
plt.show()
```
