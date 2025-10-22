---
jupytext:
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

Maintenant que nous en avons bien vu la finalité, voyons un très bref aperçu des possibilités offertes pour la construction des types dans ce contexte de *type hints*. N'hésitez pas à vous reporter à la documentation officielle [du module `typing`](https://docs.python.org/3/library/typing.html) pour un exposé plus exhaustif.

+++

##### le module `typing`

+++

L'ensemble des symboles que nous allons utiliser dans la suite de ce complément provient du module `typing`

+++

##### exemples simples

```{code-cell} ipython3
from typing import List
```

```{code-cell} ipython3
# une fonction qui 
# attend un paramètre qui soit une liste d'entiers,
# et qui retourne une liste de chaînes
def foo(x: List[int]) -> List[str]:
    pass    
```

##### avertissement : `list` vs `List`

+++

Remarquez bien dans l'exemple ci-dessus que nous avons utilisé `typing.List` plutôt que le type *built-in* `list`, alors que l'on a pu par contre utiliser `int` et `str`.

Les raisons pour cela sont de deux ordres :

* tout d'abord, si je devais utiliser `list` pour construire un type comme *liste d'entiers*, il me faudrait écrire quelque chose comme `list(int)` ou encore `list[int]`, et cela serait source de confusion car ceci a déjà une signification dans le langage ;

* de manière plus profonde, il faut distinguer entre `list` qui est un type concret (un objet qui sert à construire des instances), de `List` qui dans ce contexte doit plus être vu comme un type abstrait.

+++

Pour bien voir cela, considérez l'exemple suivant :

```{code-cell} ipython3
from typing import Iterable
```

```{code-cell} ipython3
def lower_split(sep: str, inputs : Iterable[str]) -> str:
    return sep.join([x.lower() for x in inputs])
```

```{code-cell} ipython3
lower_split('--', ('AB', 'CD', 'EF'))
```

On voit bien dans cet exemple que `Iterable` ne correspond pas à un type concret particulier, c'est un type abstrait dans le sens du *duck typing*.

+++

##### un exemple plus complet

+++

Voici un exemple tiré de la documentation du module `typing` qui illustre davantage de types construits à partir des types *builtin* du langage :

```{code-cell} ipython3
from typing import Dict, Tuple, List

ConnectionOptions = Dict[str, str]
Address = Tuple[str, int]
Server = Tuple[Address, ConnectionOptions]

def broadcast_message(message: str, servers: List[Server]) -> None:
    ...

# The static type checker will treat the previous type signature as
# being exactly equivalent to this one.
def broadcast_message(
        message: str,
        servers: List[Tuple[Tuple[str, int], Dict[str, str]]]) -> None:
    ...
```

J'en profite d'ailleurs (ça n'a rien a voir, mais...) pour vous signaler un objet python assez étrange :

```{code-cell} ipython3
# L'objet ... existe bel et bien en Python
el = ...
el
```

qui sert principalement pour le slicing multidimensionnel de numpy. Mais ne nous égarons pas...

+++

##### typage partiel

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

##### alias

+++

On peut facilement se définir des alias ; lorsque vous avez implémenté un système d'identifiants basé sur le type `int`, il est préférable de faire :

```{code-cell} ipython3
from typing import NewType

UserId = NewType('UserId', int)

user1_id : UserId = 0
```

plutôt que ceci, qui est beaucoup moins parlant :

```{code-cell} ipython3
user1_id : int = 0
```

## Complément - niveau avancé

+++

##### `Generic`

+++

Pour ceux qui connaissent déjà la notion de classe (les autres peuvent ignorer la fin de ce complément) :

+++

Grâce aux constructions `TypeVar` et `Generic`, il est possible de manipuler une notion de *variable de type*, que je vous montre sur un exemple tiré à nouveau de la documentation du module `typing` :

```{code-cell} ipython3
from typing import TypeVar, Generic
from logging import Logger

T = TypeVar('T')

class LoggedVar(Generic[T]):
    def __init__(self, value: T, name: str, logger: Logger) -> None:
        self.name = name
        self.logger = logger
        self.value = value

    def set(self, new: T) -> None:
        self.log('Set ' + repr(self.value))
        self.value = new

    def get(self) -> T:
        self.log('Get ' + repr(self.value))
        return self.value

    def log(self, message: str) -> None:
        self.logger.info('%s: %s', self.name, message)
```

qui vous donne je l'espère une idée de ce qu'il est possible de faire, et jusqu'où on peut aller avec les *type hints*. Si vous êtes intéressé par cette fonctionnalité, je vous invite [à poursuivre la lecture ici](https://docs.python.org/3/library/typing.html#user-defined-generic-types).

+++

### Pour en savoir plus

* la documentation officielle sur [le module typing](https://docs.python.org/3/library/typing.html) ;
* la page d'accueil [de l'outil mypy](http://mypy-lang.org/).


* le [PEP-525](https://www.python.org/dev/peps/pep-0484/) sur le typage des paramètres et retours de fonctions, implémenté dans python-3.5 ;
* le [PEP-526](https://www.python.org/dev/peps/pep-0526/) sur le typage des variables, implémenté dans 3.6.
