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
  display_name: Python 3
  language: python
  name: python3
language_info:
  name: python
  pygments_lexer: ipython3
nbhosting:
  title: docstring
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

# Rappels sur *docstring*

+++

## Complément - niveau basique

+++

### Comment documenter une fonction

+++

Pour rappel, il est recommandé de toujours documenter les fonctions en ajoutant une chaîne comme première instruction.

```{code-cell} ipython3
def flatten(containers):
    "returns a list of the elements of the elements in containers"
    return [element for container in containers for element in container]
```

Cette information peut être consultée, soit interactivement :

```{code-cell} ipython3
help(flatten)
```

Soit programmativement :

```{code-cell} ipython3
flatten.__doc__
```

### Sous quel format ?

+++

L'usage est d'utiliser une chaîne simple (délimitée par « `"` » ou « `'` ») lorsque le *docstring* tient sur une seule ligne, comme ci-dessus.

+++

Lorsque ce n'est pas le cas - et pour du vrai code, c'est rarement le cas - on utilise des chaînes multi-lignes (délimitées par « `"""` » ou « `'''` »). Dans ce cas le format est très flexible, car le *docstring* est normalisé, comme on le voit sur ces deux exemples, où le rendu final est identique :

```{code-cell} ipython3
# un style de docstring multi-lignes
def flatten(containers):
    """
provided that containers is a list (or more generally an iterable)
of elements that are themselves iterables, this function
returns a list of the items in these elements
    """
    return [element for container in containers for element in container]

help(flatten)
```

```{code-cell} ipython3
# un autre style, qui donne le même résultat
def flatten(containers):
    """
    provided that containers is a list (or more generally an iterable)
    of elements that are themselves iterables, this function
    returns a list of the items in these elements
    """
    return [element for container in containers for element in container]

help(flatten)
```

### Quelle information ?

+++

On remarquera que dans ces exemples, le *docstring* ne répète pas le nom de la fonction ou des arguments (en mots savants, sa *signature*), et que ça n'empêche pas `help` de nous afficher cette information.

Le [PEP 257](http://legacy.python.org/dev/peps/pep-0257/) qui donne les conventions autour du *docstring* précise bien ceci :

+++

>  The one-line docstring should NOT be a "signature" reiterating the function/method parameters (which can be obtained by introspection). Don't do:

  ```python
  def function(a, b):
      """function(a, b) -> list"""
  ```

>    <...>

>    The preferred form for such a docstring would be something like:

  ```python
  def function(a, b):
      """Do X and return a list."""
  ```

>    (Of course "Do X" should be replaced by a useful description!)

+++

### Pour en savoir plus

+++

Vous trouverez tous les détails sur *docstring* dans le [PEP 257](http://legacy.python.org/dev/peps/pep-0257/).
