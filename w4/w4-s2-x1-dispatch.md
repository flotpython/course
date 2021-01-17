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
notebookname: exercices sur if
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# L'instruction `if`

+++

## Exercice - niveau basique

+++

### Répartiteur (1)

On vous demande d'écrire une fonction `dispatch1`, qui prend en argument deux entiers `a` et `b`, et qui renvoie selon les cas :

$$
\begin{array}{c|c|c}
\ & a\  pair & a\ impair \\
\hline
b\ pair & a^2+b^2 & (a-1)*b\\
\hline
b\ impair & a*(b-1)& a^2-b^2\\
\end{array}
$$

```{code-cell} ipython3
# un petit exemple
from corrections.exo_dispatch import exo_dispatch1
exo_dispatch1.example()
```

```{code-cell} ipython3
def dispatch1(a, b):
    "<votre_code>"
```

```{code-cell} ipython3
# pour vérifier votre code
exo_dispatch1.correction(dispatch1)
```

## Exercice - niveau basique

+++

### Répartiteur (2)

+++

Dans une seconde version de cet exercice, on vous demande d'écrire une fonction `dispatch2` qui prend en arguments :

* `a` et `b` deux entiers
* `A` et `B` deux ensembles (chacun pouvant être matérialisé par un ensemble, une liste ou un tuple)

et qui renvoie selon les cas :

$$
\begin{array}{c|c|c}
\ & a \in A & a\notin A \\
\hline
b\in B & a^2+b^2 & (a-1)*b\\
\hline
b\notin B & a*(b-1)& a^2+b^2\\
\end{array}
$$

```{code-cell} ipython3
# un exemple
from corrections.exo_dispatch import exo_dispatch2
exo_dispatch2.example()
```

```{code-cell} ipython3
# à vous
def dispatch2(a, b, A, B):
    "<votre_code>"
```

```{code-cell} ipython3
# pour vérifier votre code
exo_dispatch2.correction(dispatch2)
```
