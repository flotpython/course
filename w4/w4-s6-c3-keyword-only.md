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

# Arguments *keyword-only*

+++

## Complément - niveau intermédiaire

+++

### Rappel

+++

Nous avons vu dans un précédent complément les 4 familles de paramètres qu'on peut déclarer dans une fonction :

1. paramètres positionnels (usuels)
1. paramètres nommés (forme *name=default*)
1. paramètres **args* qui attrape dans un tuple le reliquat des arguments positionnels 
1. paramètres ***kwds* qui attrape dans un dictionnaire le reliquat des arguments nommés

Pour rappel :

```{code-cell}
# une fonction qui combine les différents 
# types de paramètres
def foo(a, b=100, *args, **kwds):
    print(f"a={a}, b={b}, args={args}, kwds={kwds}")
```

```{code-cell}
:cell_style: center

foo(1)
```

```{code-cell}
:cell_style: center

foo(1, 2)
```

```{code-cell}
:cell_style: center

foo(1, 2, 3)
```

```{code-cell}
:cell_style: center

foo(1, 2, 3, bar=1000)
```

### Un seul paramètre attrape-tout

+++

Notez également que, de bon sens, on ne peut déclarer qu'un seul paramètre de chacune des formes d'attrape-tout ; on ne peut pas par exemple déclarer

```python
# c'est illégal de faire ceci
def foo(*args1, *args2):
    pass
```

car évidemment on ne saurait pas décider de ce qui va dans `args1` et ce qui va dans `args2`.

+++

### Ordre des déclarations

+++

L'ordre dans lequel sont déclarés les  différents types de paramètres d'une fonction est imposé par le langage. Ce que vous avez peut-être en tête si vous avez appris **Python 2**, c'est qu'à l'époque on devait impérativement les déclarer dans cet ordre :

> positionnels, nommés, forme `*`, forme `**`

comme dans notre fonction `foo`.

+++

Ça reste une bonne approximation, mais depuis Python-3, les choses ont un petit peu changé suite à [l'adoption du PEP 3102](https://www.python.org/dev/peps/pep-3102/), qui vise à introduire la notion de paramètre qu'il faut impérativement nommer lors de l'appel (en anglais : *keyword-only* argument)

+++

Pour résumer, il est maintenant possible de déclarer des **paramètres nommés après la forme `*`**

Voyons cela sur un exemple

```{code-cell}
# on peut déclarer un paramètre nommé **après** l'attrape-tout *args
def bar(a, *args, b=100, **kwds):
        print(f"a={a}, b={b}, args={args}, kwds={kwds}")
```

L'effet de cette déclaration est que, si je veux passer un argument au paramètre `b`, **je dois le nommer**

```{code-cell}
:cell_style: center

# je peux toujours faire ceci
bar(1)
```

```{code-cell}
:cell_style: center

# mais si je fais ceci l'argument 2 va aller dans args
bar(1, 2)
```

```{code-cell}
# pour passer b=2, je **dois** nommer mon argument
bar(1, b=2)
```

Ce trait n'est objectivement pas utilisé massivement en Python, mais cela peut être utile de le savoir :

* en tant qu'utilisateur d'une bibliothèque, car cela vous impose une certaine façon d'appeler une fonction ;
* en tant que concepteur d'une fonction, car cela vous permet de manifester qu'un paramètre optionnel joue un rôle particulier.
