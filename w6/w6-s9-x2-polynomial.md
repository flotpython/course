---
ipub:
  sphinx:
    toggle_input: true
    toggle_input_all: true
    toggle_output: true
    toggle_output_all: true
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
  title: classe Polynomial
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
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

```{code-cell} ipython3
from corrections.cls_polynomial import exo_polynomial
exo_polynomial.example()
```

*****

```{code-cell} ipython3
# votre code

class Polynomial:
    
    def __init__(self, *coefs):
        ...
```

```{code-cell} ipython3
# correction
exo_polynomial.correction(Polynomial)
```

*****

```{code-cell} ipython3
# peut-être utile pour debugger ?
P00 = Polynomial()
P0 = Polynomial(0)
P1 = Polynomial(1)
P = Polynomial(3, 2, 1)
Q = Polynomial(1, 2)
R = Polynomial(3, 8, 5, 2)
```

```{code-cell} ipython3
P0 == P00 == P0 * P1
```

```{code-cell} ipython3
:tags: [raises-exception]

P * Q == R
```

```{code-cell} ipython3
:tags: [raises-exception]

P(10)
```
