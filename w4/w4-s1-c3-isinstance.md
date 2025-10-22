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
  title: isinstance
---

# `isinstance`

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Complément - niveau basique

+++

### Typage dynamique

+++

En première semaine, nous avons rapidement mentionné les concepts de typage statique et dynamique.

Avec la fonction prédéfinie `isinstance` - qui peut être par ailleurs utile dans d'autres contextes - vous pouvez facilement :

 * vérifier qu'un argument d'une fonction a bien le type attendu,
 * et traiter différemment les entrées selon leur type.

+++

Voyons tout de suite sur un exemple simple comment on pourrait définir une fonction qui travaille sur un entier, mais qui par commodité peut aussi accepter un entier passé comme une chaîne de caractères, ou même une liste d'entiers (auquel cas on renvoie la liste des factorielles) :

```{code-cell} ipython3
def factoriel(argument):
    # si on reçoit un entier
    if isinstance(argument, int):              # (*)
        return 1 if argument <= 1 else argument * factoriel(argument - 1)
    # convertir en entier si on reçoit une chaîne
    elif isinstance(argument, str):
        return factoriel(int(argument))
    # la liste des résultats si on reçoit un tuple ou une liste 
    elif isinstance(argument, (tuple, list)):  # (**)
        return [factoriel(i) for i in argument]
    # sinon on lève une exception
    else:
        raise TypeError(argument)
```

```{code-cell} ipython3
print("entier", factoriel(4))
print("chaine", factoriel("8"))
print("tuple", factoriel((4, 8)))
```

Remarquez que la fonction `isinstance` **possède elle-même** une logique de ce genre, puisqu'en ligne 3 `(*)` nous lui avons passé en deuxième argument un type (`int`), alors qu'en ligne 11  `(**)` on lui a passé un tuple de deux types. Dans ce second cas naturellement, elle vérifie si l'objet (le premier argument) est **de l'un des types** mentionnés dans le tuple.

+++

## Complément - niveau intermédiaire

+++

### Le module `types`

+++

Le module `types` définit un certain nombre de constantes qui peuvent être utiles dans ce contexte - vous trouverez une liste exhaustive à la fin de ce notebook. Par exemple :

```{code-cell} ipython3
from types import FunctionType
isinstance(factoriel, FunctionType)
```

Mais méfiez-vous toutefois des fonctions *built-in*, qui sont de type `BuiltinFunctionType`

```{code-cell} ipython3
from types import BuiltinFunctionType
isinstance(len, BuiltinFunctionType)
```

```{code-cell} ipython3
# alors qu'on pourrait penser que
isinstance(len, FunctionType)
```

### `isinstance` *vs* `type`

+++

Il est recommandé d'utiliser `isinstance` par rapport à la fonction `type`. Tout d'abord, cela permet, on vient de le voir, de prendre en compte plusieurs types. 

Mais aussi et surtout `isinstance` supporte la notion d'héritage qui est centrale dans le cadre de la programmation orientée objet, sur laquelle nous allons anticiper un tout petit peu par rapport aux présentations de la semaine prochaine. 

Avec la programmation objet, vous pouvez définir vos propres types. On peut par exemple définir une classe `Animal` qui convient pour tous les animaux, puis définir une sous-classe `Mammifere`. On dit que la classe `Mammifere` *hérite* de la classe `Animal`, et on l'appelle sous-classe parce qu'elle représente une partie des animaux ; et donc tout ce qu'on peut faire sur les animaux peut être fait sur les mammifères.

En voici une implémentation très rudimentaire, uniquement pour illustrer le principe de l'héritage. Si ce qui suit vous semble difficile à comprendre, pas d'inquiétude, nous reviendrons sur ce sujet lorsque nous parlerons des classes.

```{code-cell} ipython3
class Animal:
    def __init__(self, name):
        self.name = name

class Mammifere(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
```

Ce qui nous intéresse dans l'immédiat c'est que `isinstance` permet dans ce contexte de faire des choses qu'on ne peut pas faire directement avec la fonction `type`, comme ceci :

```{code-cell} ipython3
# pour créer un objet de type `Animal` (méthode __init__)
requin = Animal('requin')
# idem pour un Mammifere
baleine = Mammifere('baleine')

# bien sûr ici la réponse est 'True'
print("l'objet baleine est-il un mammifère ?", isinstance(baleine, Mammifere))
```

```{code-cell} ipython3
# ici c'est moins évident, mais la réponse est 'True' aussi
print("l'objet baleine est-il un animal ?", isinstance(baleine, Animal))
```

Vous voyez qu'ici, bien que l'objet baleine soit de type `Mammifere`, on peut le considérer comme étant **aussi** de type `Animal`. 

Ceci est motivé de la façon suivante : comme on l'a dit plus haut, tout ce qu'on peut faire (en matière notamment d'envoi de méthodes) sur un objet de type `Animal`, on peut le faire sur un objet de type `Mammifere`. Dit en termes ensemblistes, l'ensemble des mammifères est inclus dans l'ensemble des animaux.

+++

### Annexe - Les symboles du module `types`

+++

Vous pouvez consulter [la documentation du module `types`](https://docs.python.org/3/library/types.html).

```{code-cell} ipython3
# voici par ailleurs la liste de ses attributs
import types 
dir(types)
```
