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
  title: Taxes
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

# Exercice

+++

Cet exercice, comme tous les autres, a pour but de vous faire travailler les notions vues dans la partie courante, mais aussi dans les cours précédents.
Ainsi, même si le chapitre en cours concerne les boucles while, vous n'êtes pas tenu.e.s d'utiliser une boucle while pour résoudre le problème proposé ci-dessous.

## Niveau basique

On se propose d'écrire une fonction `taxes` qui calcule le montant de l'impôt sur le revenu au Royaume-Uni.

+++

Le barème est [publié ici par le gouvernement anglais](https://www.gov.uk/income-tax-rates), voici les données de 2020 qui sont utilisées pour l'exercice :

+++

| Tranche             | Revenu imposable    | Taux  |
|--------------------:|--------------------:|------:|
| Non imposable       | jusque £12.500      | 0%    |
| Taux de base        | £12.501 à £50.000   | 20%   |
| Taux élevé          | £50.001 à £150.000  | 40%   |
| Taux supplémentaire | au delà de £150.000	| 45%   |

+++

Donc naturellement il s'agit d'écrire une fonction qui prend en argument le revenu imposable, et retourne le montant de l'impôt, **arrondi à l'entier inférieur**.

```{code-cell} ipython3
from corrections.exo_taxes import exo_taxes
exo_taxes.example()
```

**Indice**

* évidemment on parle ici d'une fonction continue (enfin disons: elle serait continue si on ne faisait pas l'arrondi à l'entier inférieur); mais sur le dessin on ne doit pas voir de 'saut' à l'endroit des changements de taux.

+++

**Consigne**

* aussi en termes de programmation, je vous encourage à **bien séparer**
  * la définition des tranches 
  * de la fonction en elle-même

on ne doit pas trouver de nombre 'en dur' dans le code de la fonction; c'est-à-dire pour être bien explicite il s'agit de ne pas écrire quelque chose comme
  ```
  if 0 <= income <= 12_500:
     ...
  ```
  mais plutôt de définir par exemple
  ```
  # c'est juste un exemple, par forcément une bonne idée hein...
  TICKS = (12_500, 50_000, 150_000)
  RATES = (20, 40, 45)
  ```
  ou **tout autre structure de données** qui vous paraitra adaptée à décrire le barême, mais **extérieure** à la fonction proprement dite, pour qu'on puisse facilement réutiliser et/ou mettre à jour le code.

```{code-cell} ipython3
def taxes(income):
    # ce n'est pas la bonne réponse
    return (income-12_500) * (20/100)
```

```{code-cell} ipython3
exo_taxes.correction(taxes)
```

##### Représentation graphique

+++

Comme d'habitude vous pouvez voir la représentation graphique de votre fonction :

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
```

```{code-cell} ipython3
%matplotlib inline
plt.ion()
```

```{code-cell} ipython3
X = np.linspace(0, 200_000)
Y = [taxes(x) for x in X]
plt.plot(X, Y);
```

```{code-cell} ipython3
# et pour changer la taille de la figure
plt.figure(figsize=(10, 8))
plt.plot(X, Y);
```
