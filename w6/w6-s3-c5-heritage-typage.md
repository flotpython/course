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
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Héritage, typage

+++

## Complément - niveau avancé

+++

Dans ce complément, nous allons revenir sur la notion de *duck typing*, et attirer votre attention sur cette différence assez essentielle entre python et les langages statiquement typés. On s'adresse ici principalement à ceux d'entre vous qui sont habitués à C++ et/ou Java.

+++

### Type concret et type abstrait

+++

Revenons sur la notion de type et remarquons que les types peuvent jouer plusieurs rôles, comme on l'a évoqué rapidement en première semaine ; et pour reprendre des notions standard en langages de programmation nous allons distinguer deux types.

1. **type concret :** d'une part, la notion de type a bien entendu à voir avec l'implémentation ; par exemple, un compilateur C a besoin de savoir très précisément quel espace allouer à une variable, et l'interpréteur python sous-traite à la classe le soin d'initialiser un objet ;
1. **type abstrait :** d'autre part, les types sont cruciaux dans les systèmes de vérification statique, au sens large, dont le but est de trouver un maximum de défauts à la seule lecture du code (par opposition aux techniques qui nécessitent de le faire tourner).

+++

### *Duck typing*

+++

En python, ces deux aspects du typage sont relativement décorrélés.

+++

Pour la seconde dimension du typage, le système de types abstraits de python est connu sous le nom de [*duck typing*](http://en.wikipedia.org/wiki/Duck_typing), une appellation qui fait référence à cette phrase :

> When I see a bird that walks like a duck and swims like a duck and quacks like a duck, I call that bird a duck.

+++

### L'exemple des itérables

+++

Pour prendre l'exemple sans doute le plus représentatif, la notion d'*itérable* est un type abstrait, en ce sens que, pour que le fragment :

```python
for item in container:
    do_something(item)
```

ait un sens, il faut et il suffit que `container` soit un itérable. Et vous connaissez maintenant plein d'exemples très différents d'objets itérables, a minima parmi les *built-in* `str`, `list`, `tuple`, `range`...

+++

Dans un langage typé statiquement, pour pouvoir donner un type à cette construction, on serait **obligé** de définir un type - qu'on appellerait logiquement une classe abstraite - dont ces trois types seraient des descendants.

+++

En python, et c'est le point que nous voulons souligner dans ce complément, il n'existe pas dans le système python d'objet de type `type` qui matérialise l'ensemble des `iterable`s. Si on regarde les superclasses de nos types concrets itérables, on voit que leur seul ancêtre commun est la classe  `object` :

```{code-cell}
:cell_style: split

str.__bases__
```

```{code-cell}
:cell_style: split

list.__bases__
```

```{code-cell}
:cell_style: split

tuple.__bases__
```

```{code-cell}
:cell_style: split

range.__bases__
```

### Un autre exemple

+++

Pour prendre un exemple plus simple, si je considère :

```python
def foo(graphic):
    ...
    graphic.draw()
```

pour que l'expression `graphic.draw()` ait un sens, il faut et il suffit que l'objet `graphic` ait une méthode `draw`.

+++

À nouveau, dans un langage typé statiquement, on serait amené à définir une classe abstraite `Graphic`. En python ce n'est **pas requis** ; vous pouvez utiliser ce code tel quel avec deux classes `Rectangle` et `Texte` qui n'ont pas de rapport entre elles - autres que, à nouveau, d'avoir `object` comme ancêtre commun - pourvu qu'elles aient toutes les deux une méthode `draw`.

+++

### Héritage et type abstrait

+++

Pour résumer, en python comme dans les langages typés statiquement, on a bien entendu la bonne propriété que si, par exemple, la classe `Spam` est itérable, alors la classe `Eggs` qui hérite de `Spam` est itérable. 

Mais dans l'autre sens, si `Foo` et `Bar` sont itérables, il n'y a pas forcément une superclasse commune qui représente l'ensemble des objets itérables.

+++

### `isinstance` sur stéroïdes

+++

D'un autre côté, c'est très utile d'exposer au programmeur un moyen de vérifier si un objet a un *type* donné - dans un sens volontairement vague ici.

On a déjà parlé en Semaine 4 de l'intérêt qu'il peut y avoir à tester le type d'un argument avec `isinstance` dans une fonction, pour parvenir à faire l'équivalent de la surcharge en C++ (la surcharge en C++, c'est quand vous définissez plusieurs fonctions qui ont le même nom mais des types d'arguments différents). 

C'est pourquoi, quand on a cherché à exposer au programmeur des propriétés comme "cet objet est-il iterable ?", on a choisi d'étendre *isinstance* au travers de [cette initiative](http://legacy.python.org/dev/peps/pep-3119/). C'est ainsi qu'on peut faire par exemple :

```{code-cell}
from collections.abc import Iterable
```

```{code-cell}
:cell_style: split

isinstance('ab', Iterable)
```

```{code-cell}
:cell_style: split

isinstance([1, 2], Iterable)
```

```{code-cell}
:cell_style: split

# comme on l'a vu, un objet qui a des méthodes
# __iter__() et __next__() 
# est considéré comme un itérable
class Foo:
    def __iter__(self):
        return self
    def __next__(self):
        # ceci naturellement est bidon
        return 
```

```{code-cell}
:cell_style: split

foo = Foo()
isinstance(foo, Iterable)
```

L'implémentation du module `abc` donne l'**illusion** que `Iterable` est un objet dans la hiérarchie de classes, et que tous ces *classes* `str`, `list`, et `Foo` lui sont asujetties, mais ce n'est pas le cas en réalité ; comme on l'a vu plus tôt, ces trois types ne sont pas comparables dans la hiérarchie de classes, ils n'ont pas de plus petit (ou plus grand) élément à part `object`.

+++

Je signale pour finir, à propos de `isinstance` et du module `collections`, que la définition du symbole `Hashable` est à mon avis beaucoup moins convaincante que `Iterable` ; si vous vous souvenez qu'en Semaine 3, Séquence "les dictionnaires", on avait vu que les clés doivent être globalement immuables. C'est une caractéristique qui est assez difficile à écrire, et en tous cas ceci de mon point de vue ne remplit pas la fonction :

```{code-cell}
from collections.abc import Hashable
```

```{code-cell}
# un tuple qui contient une liste ne convient 
# pas comme clé dans un dictionnaire
# et pourtant
isinstance (([1], [2]), Hashable)
```

### python et les classes abstraites

+++

Les points à retenir de ce complément un peu digressif sont :

* en python, on hérite des **implémentations** et pas des **spécifications** ; 
* et le langage n'est pas taillé pour tirer profit de **classes abstraites** - même si rien ne vous interdit d'écrire, pour des raisons documentaires, une classe qui résume l'interface qui est attendue par tel ou tel système de plugin.

+++

Venant de C++ ou de Java, cela peut prendre du temps d'arriver à se débarrasser de l'espèce de réflexe qui fait qu'on pense d'abord classe abstraite, puis implémentations.

+++

### Pour aller plus loin

+++

La [documentation du module `collections.abc`](https://docs.python.org/3/library/collections.abc.html) contient la liste de tous les symboles exposés par ce module, dont par exemple en vrac :

* `Iterable`
* `Iterator`
* `Hashable`
* `Generator`
* `Coroutine` (rendez-vous semaine 8)

et de nombreux autres.

+++

### Avertissement

+++

Prenez garde enfin que ces symboles n'ont - à ce stade du moins - pas de relation forte avec ceux [du module `typing`](https://docs.python.org/3/library/typing.html) dont on a parlé lorsqu'on a vu les *type hints*.
