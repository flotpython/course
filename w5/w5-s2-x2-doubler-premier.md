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
notebookname: exo *args
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

## Exercice - niveau intermédiaire

+++

Les deux exercices de ce notebook font référence également à des notions vues en fin de semaine 4, sur le passage d'arguments aux fonctions.

On vous demande d'écrire une fonction qui prend en argument :

 * une fonction `f`, dont vous savez seulement que le premier argument est numérique, et qu'elle ne prend **que des arguments positionnels** (sans valeur par défaut) ;
 * un nombre quelconque - mais au moins 1 - d'arguments positionnels `args`, dont on sait qu'ils pourraient être passés à `f`.
 
Et on attend en retour le résultat de `f` appliqués à tous ces arguments, mais avec le premier d'entre eux multiplié par deux.

Formellement : `doubler_premier(f, x1, x2,..., xn) == f(2*x1, x2,..., xn)`

+++

Voici d'abord quelques exemples de ce qui est attendu. Pour cela on va utiliser comme fonctions:

* `add` et `mul` sont les opérateurs (binaires) du module operator;
* et `distance` est la fonction qu'on a vu dans un exercice précédent; pour rappel

$distance$ ($x_1$, ..., $x_n$) = $\sqrt{\sum x_i^2}$

```{code-cell}
# rappel sur la fonction distance:
from corrections.exo_distance import distance
distance(3.0, 4.0)
```

```{code-cell}
distance(4.0, 4.0, 4.0, 4.0)
```

```{code-cell}
# voici donc quelques exemples de ce qui est attendu.
from corrections.exo_doubler_premier import exo_doubler_premier
exo_doubler_premier.example()
```

```{code-cell}
# ATTENTION vous devez aussi définir les arguments de la fonction
def doubler_premier(votre, signature):
    return "votre code"
```

```{code-cell}
exo_doubler_premier.correction(doubler_premier)
```

## Exercice - niveau intermédiaire

Vous devez maintenant écrire une deuxième version qui peut fonctionner avec une fonction quelconque (elle peut avoir des arguments nommés avec valeurs par défaut).

La fonction `doubler_premier_kwds` que l'on vous demande d'écrire maintenant prend donc un premier argument `f` qui est une fonction, un second argument positionnel qui est le premier argument de `f` (et donc qu'il faut doubler), et le reste des arguments de f, qui donc, à nouveau, peuvent être nommés ou non.

```{code-cell}
# avec ces deux fonctions

def add3(x, y=0, z=0):
    return x + y + z

def mul3(x=1, y=1, z=1):
    return x * y * z
```

```{code-cell}
# voici des exemples de ce qui est attendu
from corrections.exo_doubler_premier_kwds import exo_doubler_premier_kwds
exo_doubler_premier_kwds.example()
```

Vous remarquerez que l'on n'a pas mentionné dans cette liste d'exemples

```python
doubler_premier_kwds (muln, x=1, y=1)
```
   
que l'on ne demande pas de supporter puisqu'il est bien précisé que doubler_premier a deux arguments positionnels.

```{code-cell}
# ATTENTION vous devez aussi définir les arguments de la fonction
def doubler_premier_kwds(votre, signature):
    "<votre code>"
```

```{code-cell}
exo_doubler_premier_kwds.correction(doubler_premier_kwds)
```
