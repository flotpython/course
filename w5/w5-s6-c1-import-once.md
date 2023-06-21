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
  title: "Pr\xE9cisions sur l'importation"
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Précisions sur l'importation

+++

## Complément - niveau basique

+++

### Importations multiples - rechargement

+++

##### Un module n'est chargé qu'une fois

+++

De manière générale, à l'intérieur d'un interpréteur python, un module donné n'est chargé qu'une seule fois. L'idée est naturellement que si plusieurs modules différents importent le même module, (ou si un même module en importe un autre plusieurs fois) on ne paie le prix du chargement du module qu'une seule fois.

Voyons cela sur un exemple simpliste, importons un module pour la première fois :

```{code-cell} ipython3
import multiple_import
```

Ce module est très simple, comme vous pouvez le voir

```{code-cell} ipython3
from modtools import show_module
show_module(multiple_import)
```

Si on le charge une deuxième fois (peu importe où, dans le même module, un autre module, une fonction..), vous remarquez qu'il ne produit aucune impression

```{code-cell} ipython3
import multiple_import 
```

Ce qui confirme que le module a déjà été chargé, donc cette instruction `import` n'a aucun effet autre qu'affecter la variable `multiple_import` de nouveau à l'objet module déjà chargé. En résumé, l'instruction `import` fait l'opération d'affectation autant de fois qu'on appelle `import`, mais elle ne charge le module qu'une seule fois à la première importation.

+++

Une autre façon d'illustrer ce trait est d'importer plusieurs fois le module `this`

```{code-cell} ipython3
# la première fois le chargement a vraiment lieu
import this
```

```{code-cell} ipython3
# la deuxième fois il ne se passe plus rien
import this
```

##### Les raisons de ce choix

+++

Le choix de ne charger le module qu'une seule fois est motivé par plusieurs considérations.

+++

* D'une part, cela permet à deux modules de dépendre l'un de l'autre (ou plus généralement à avoir des cycles de dépendances), sans avoir à prendre de précaution particulière.

+++

* D'autre part, naturellement, cette stratégie améliore considérablement les performances.

+++

* Marginalement, `import` est une instruction comme une autre, et vous trouverez occasionnellement un avantage à l'utiliser à l'intérieur d'une fonction, **sans aucun surcoût** puisque vous ne payez le prix de l'import qu'au premier appel et non à chaque appel de la fonction.

```python
def ma_fonction():
    import un_module_improbable
    ....
```

Cet usage n'est pas recommandé en général, mais de temps en temps peut s'avérer très pratique pour alléger les dépendances entre modules dans des contextes particuliers, comme du code multi-plateformes.

+++

##### Les inconvénients de ce choix - la fonction `reload`

+++

L'inconvénient majeur de cette stratégie de chargement unique est perceptible dans l'interpréteur interactif pendant le développement. Nous avons vu comment IDLE traite le problème en remettant l'interpréteur dans un état vierge lorsqu'on utilise la touche F5. Mais dans l'interpréteur "de base", on n'a pas cette possibilité.

+++

Pour cette raison, python fournit dans le module `importlib` une fonction `reload`, qui permet comme son nom l'indique de forcer le rechargement d'un module, comme ceci :

```{code-cell} ipython3
from importlib import reload
reload(multiple_import)
```

Remarquez bien que `importlib.reload` est une fonction et non une instruction comme `import` - d'où la syntaxe avec les parenthèses qui n'est pas celle de `import`.

Notez également que la fonction `importlib.reload` a été introduite en python3.4, avant, il fallait utiliser la fonction `imp.reload` qui est dépréciée depuis python3.4 mais qui existe toujours. Évidemment, vous devez maintenant exlusivement utiliser la fonction `importlib.reload`.

+++

*****

+++

**NOTE** spécifique à l'environnement des **notebooks** (en fait, à l'utilisation de ipython) :

À l'intérieur d'un notebook, vous [pouvez faire comme ceci](https://ipython.org/ipython-doc/3/config/extensions/autoreload.html) pour recharger le code importé automatiquement :

```{code-cell} ipython3
# charger le magic 'autoreload'
%load_ext autoreload
```

```{code-cell} ipython3
# activer autoreload
%autoreload 2
```

À partir de cet instant, et si le code d'un module importé est modifié par ailleurs (ce qui est difficile à simuler dans notre environnement), alors le module en question sera effectivement rechargé lors du prochain import. Voyez le lien ci-dessus pour plus de détails.

+++

## Complément - niveau avancé

+++

Revenons à python standard. Pour ceux qui sont intéressés par les détails, signalons enfin les deux variables suivantes.

+++

### `sys.modules`

+++

L'interpréteur utilise cette variable pour conserver la trace des modules actuellement chargés.

```{code-cell} ipython3
import sys
'csv' in sys.modules
```

```{code-cell} ipython3
import csv
'csv' in sys.modules
```

```{code-cell} ipython3
csv is sys.modules['csv']
```

La [documentation sur `sys.modules`](https://docs.python.org/3/library/sys.html#sys.modules) indique qu'il est possible de forcer le rechargement d'un module en l'enlevant de cette variable `sys.modules`.

```{code-cell} ipython3
del sys.modules['multiple_import']
import multiple_import
```

### `sys.builtin_module_names`

+++

Signalons enfin [la variable `sys.builtin_module_names`](https://docs.python.org/3/library/sys.html#sys.builtin_module_names) qui contient le nom des modules, comme par exemple le garbage collector `gc`, qui sont implémentés en C et font partie intégrante de l'interpréteur.

```{code-cell} ipython3
'gc' in sys.builtin_module_names
```

### Pour en savoir plus

+++

Pour aller plus loin, vous pouvez lire [la documentation sur l'instruction `import`](https://docs.python.org/3/reference/simple_stmts.html#the-import-statement)
