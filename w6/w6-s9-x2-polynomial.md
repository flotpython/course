---
ipub:
  sphinx:
    toggle_input: true
    toggle_input_all: true
    toggle_output: true
    toggle_output_all: true
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
notebookname: classe Polynomial
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

## exercice - niveau avancé

+++

On se propose d'écrire une classe pour représenter les polynômes :

* avec un constructeur qui prend en argument les coefficients en commençant par les degrés les plus élevés ; ainsi par exemple
  * `Polynomial()` aussi bien que `Polynomial(0)` représentent le polynôme nul,
  * `Polynomial(3, 2, 1)` représente $3X^2 + 2X + 1$, et
  * `Polynomial(3, 0, 1, 0, 0)` représente $3X^4 + X^2$
  
* avec un **attribut `degree`** pour accéder au degré

* avec une **méthode `derivative()`** pour calculer le polynôme dérivé

* qui sait s'**additionner**, se **multiplier** et se **comparer** avec `==`

* et qu'on **peut appeler** (autrement dit qui est un *callable*)  
  ce qui signifie qu'on peut écrire par exemple
  
  ```python
  P = Polynomial(3, 2, 1)
  P(10) == 321
  ```
  
**Note importante**

Le système de correction automatique a besoin également que votre classe définisse son comportement vis-à-vis de `repr()` ; regardez les exemples pour voir la représentation choisie.

```{code-cell}
from corrections.cls_polynomial import exo_polynomial
exo_polynomial.example()
```

*****

```{code-cell}
# votre code

class Polynomial:
    
    def __init__(self, *coefs):
        ...
```

```{code-cell}
# correction
exo_polynomial.correction(Polynomial)
```

*****

```{code-cell}
# peut-être utile pour debugger ?
P00 = Polynomial()
P0 = Polynomial(0)
P1 = Polynomial(1)
P = Polynomial(3, 2, 1)
Q = Polynomial(1, 2)
R = Polynomial(3, 8, 5, 2)
```

```{code-cell}
P0 == P00 == P0 * P1
```

```{code-cell}
:tags: [raises-exception]

P * Q == R
```

```{code-cell}
:tags: [raises-exception]

P(10)
```
