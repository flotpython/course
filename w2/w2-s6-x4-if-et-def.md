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
notebookname: if et def
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Instruction `if` et fonction `def`

+++

## Exercice - niveau basique

+++

### Fonction de divisibilité

+++

L'exercice consiste à écrire une fonction baptisée `divisible` qui retourne une valeur booléenne, qui indique si un des deux arguments est divisible par l'autre.

Vous pouvez supposer les entrées `a` et `b` entiers et non nuls, mais pas forcément positifs.

```{code-cell}
:tags: []

# par exemple
from corrections.exo_divisible import exo_divisible
exo_divisible.example()
```

```{code-cell}
def divisible(a, b):
    "<votre_code>"
```

Vous pouvez à présent tester votre code en évaluant ceci, qui écrira un message d'erreur si un des jeux de test ne donne pas le résultat attendu.

```{code-cell}
# tester votre code
exo_divisible.correction(divisible)
```

## Exercice - niveau basique

+++

##### Fonction définie par morceaux

On veut définir en Python une fonction qui est définie par morceaux :

+++

$$
f: x \longrightarrow \left\{
\begin{array}{ll}
-x - 5          & \mbox{si } x \leqslant -5 \\
0               & \mbox{si } x \in [-5, 5]  \\
\frac{1}{5}x -1 & \mbox{si } x \geqslant 5  \\
\end{array}
\right.
$$

```{code-cell}
# donc par exemple
from corrections.exo_morceaux import exo_morceaux
exo_morceaux.example()
```

```{code-cell}
# à vous de jouer

def morceaux(x):
    return 0 # "votre code"
```

```{code-cell}
# pour corriger votre code
exo_morceaux.correction(morceaux)
```

##### Représentation graphique

+++

L'exercice est terminé, mais nous allons maintenant voir ensemble comment vous pourriez visualiser votre fonction.

Voici ce qui est attendu comme courbe pour `morceaux` (image fixe) :
![graphe morceaux](media/morceaux.png)

+++

En partant de votre code, vous pouvez produire votre propre courbe en utilisant `numpy` et `matplotlib` comme ceci :

```{code-cell}
# on importe les bibliothèques
import numpy as np
import matplotlib.pyplot as plt
```

```{code-cell}
# un échantillon des X entre -10 et 20
X = np.linspace(-10, 20)

# et les Y correspondants
Y = np.vectorize(morceaux)(X)
```

```{code-cell}
# on n'a plus qu'à dessiner
plt.plot(X, Y)
plt.show()
```
