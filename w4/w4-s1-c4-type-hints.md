---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  name: python3
  display_name: Python 3 (ipykernel)
  language: python
language_info:
  name: python
  pygments_lexer: ipython3
  nbconvert_exporter: python
nbhosting:
  title: Type hints
---

# *Type hints*

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Complément - niveau intermédiaire

```{admonition} Avertissement
:class: danger

le système de *type hints* a **beaucoup évolué** depuis la rédaction de cet article.  
Nous nous sommes efforcés de le mettre à jour, mais n'hésitez pas à approfondir le sujet dans d'autres sources si nécessaire..

une référence possible pour cela: <https://typing.python.org/>
```

+++

### Langages compilés

+++

Nous avons évoqué en première semaine le typage, lorsque nous avons comparé Python avec les langages compilés. Dans un langage compilé avec typage statique, on **doit fournir du typage**, ce qui fait qu'on écrit typiquement une fonction comme ceci :

```C
int factoriel(int n) {
  return (n<=1) ? 1 : n * factoriel(n-1);
}
```

ce qui signifie que la fonction factoriel prend un premier argument qui est un entier, et qu'elle retourne également un entier.

+++

Nous avons vu également que, par contraste, pour écrire une fonction en Python, on n'a **pas besoin** de préciser **le type** des arguments ni du retour de la fonction.

+++

### Vous pouvez aussi typer votre code python

+++

Cependant depuis la version 3.5, python supporte un mécanisme **totalement optionnel** qui vous permet d'annoter les arguments des fonctions avec des informations de typage, ce mécanisme est connu sous le nom de *type hints*, et ça se présente comme ceci :

+++

##### typer une variable

```{code-cell} ipython3
# pour typer une variable avec les type hints
nb_items : int = 0
```

```{code-cell} ipython3
nb_items
```

##### typer les paramètres et le retour d'une fonction

```{code-cell} ipython3
# une fonction factorielle avec des type hints
def fact(n : int) -> int:
    return 1 if n <= 1 else n * fact(n-1)
```

```{code-cell} ipython3
fact(12)
```

### Usages

+++

À ce stade, on peut entrevoir les usages suivants à ce type d'annotation :

* tout d'abord, et évidemment, cela peut permettre de mieux documenter le code ; 
* les environnements de développement sont susceptibles de vous aider de manière plus effective ; si quelque part vous écrivez `z = fact(12)`, le fait de savoir que `z` est entier permet de fournir une complétion plus pertinente lorsque vous commencez à écrire `z.[TAB]` ;
* on peut espérer trouver des erreurs dans les passages d'arguments à un stade plus précoce du développement.

+++

Par contre ce qui est très très clairement annoncé également, c'est que ces informations de typage sont **totalement facultatives**, et que le langage les **ignore totalement**.

```{code-cell} ipython3
# l'interpréteur ignore totalement ces informations
def fake_fact(n : str) -> str:
    return 1 if n <= 1 else n * fake_fact(n-1)

# on peut appeler fake_fact avec un int alors 
# que c'est déclaré pour des str
fake_fact(12)
```

Le modèle préconisé est d'utiliser des **outils extérieurs**, qui peuvent faire une analyse statique du code pour exploiter ces informations à des fins de validation. Dans cette catégorie, le plus célèbre [est sans doute `mypy`](http://mypy-lang.org/). Notez aussi que les IDE comme PyCharm sont également capables de tirer parti de ces annotations.

+++

### Est-ce répandu ?

+++

Parce qu'ils ont été introduits pour la première fois avec python-3.5, en 2015 donc, puis améliorés dans la 3.6 pour le typage des variables, l'usage des *type hints* n'est pour l'instant pas très répandu, en proportion de code en tous cas. En outre, il aura fallu un temps de latence avant que tous les outils (IDE's, producteurs de documentation, outils de test, validateurs...) ne soient améliorés pour en tirer un profit maximal.

On peut penser que cet usage va se répandre avec le temps, peut-être / sans doute pas de manière systématique, mais *a minima* pour lever certaines ambiguïtés.

+++

### Comment annoter son code

+++

Maintenant que nous en avons bien vu la finalité, voyons un très bref aperçu des possibilités offertes pour la construction des types dans ce contexte de *type hints*. À nouveau n'hésitez pas à creuser le sujet par ailleurs.

+++

#### exemple simple

```{code-cell} ipython3
# une fonction qui 
# attend un paramètre qui soit une liste d'entiers,
# et qui retourne une liste de chaînes
def foo(x: list[int]) -> list[str]:
    pass    
```

#### un peu plus complexe

```{code-cell} ipython3
from collections.abc import Iterable
```

```{code-cell} ipython3
# attend
# - une chaine comme séparateur
# - un itérable de chaines en entrée
# retourne
# -> une chaine
def lower_split(sep: str, inputs : Iterable[str]) -> str:
    return sep.join([x.lower() for x in inputs])
```

```{code-cell} ipython3
lower_split('--', ('AB', 'CD', 'EF'))
```

On voit bien dans cet exemple que `Iterable` ne correspond pas à un type concret particulier, c'est un type abstrait dans le sens du *duck typing*.  
Ce code pourra fonctionner dès lors qu'on peut faire un `for` sur `inputs`

+++

#### typage partiel et `Any`

+++

Puisque c'est un mécanisme optionnel, vous pouvez tout à fait ne typer qu'une partie de vos variables et paramètres :

```{code-cell} ipython3
# imaginez que vous ne typez pas n2, ni la valeur de retour

# c'est équivalent de dire ceci
def partially_typed(n1: int, n2):
    return None
```

```{code-cell} ipython3
# ou cela
from typing import Any

def partially_typed(n1: int, n2: Any) -> Any:
    return None
```

:::{admonition} `collections.abc` *vs* `typing`
:class: warning
l'historique des *type hints* est assez tortueuse; on aurait pu espérer n'avoir qu'un module à utiliser, mais ce n'est malheureusement pas le cas; aussi on doit importer:
- `collections.abc` pour les types abstraits (genre `Iterable` ci-dessus)
- `typing` pour les constructeurs de type comme ici `Any` ou `Final`...
:::

+++

#### constantes et `Final`

+++

Pour indiquer qu'une variable est constante, on peut utiliser `Final`

```{code-cell} ipython3
from typing import Final

# cette variable est constante et désigne un tuple de deux entiers

SCREEN_SIZE: Final[tuple[int, int]] = 100, 100
```

#### alias

+++

On peut facilement se définir des alias ; lorsque vous avez implémenté un système d'identifiants basé sur le type `int`, il est préférable de faire :

```{code-cell} ipython3
# depuis la 3.12

type Vector = tuple[float, float]

v : Vector = 1., 1.
```

#### unions

on peut construire un type "A ou B" avec l'opérateur `|`

```{code-cell} ipython3
type ListOrTuple = list[int] | tuple[int]

l : ListOrTuple = [1, 2]
t : ListOrTuple = 1, 2
```

#### valeurs optionnelles

```{code-cell} ipython3
# soit un entier, soit None

from typing import Optional

type MaybeInteger = Optional[int]

i: MaybeInteger = 1
n: MaybeInteger = None
```

#### plus d'exemples

+++

Pour un aperçu plus complet, je vous invite à parcourir ce document <https://typing.python.org/en/latest/guides/libraries.html#best-practices-for-inlined-types>

+++

### Pour en savoir plus
* la documentation officielle sur [le module typing](https://docs.python.org/3/library/typing.html) ;
* le [mypy cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html), référence pratique sur la syntaxe ;
* la documentation communautaire [typing.readthedocs.io](https://typing.readthedocs.io/) ;
* le [PEP-484](https://peps.python.org/pep-0484/) sur le typage des paramètres et retours de fonctions, implémenté dans Python 3.5 ;
* le [PEP-526](https://peps.python.org/pep-0526/) sur le typage des variables, implémenté dans Python 3.6.
