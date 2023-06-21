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
notebookname: "Op\xE9rateur is"
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# L'opérateur `is`

+++

## Complément - niveau basique

```{code-cell} ipython3
%load_ext ipythontutor
```

### Les opérateurs `is` et `==`

+++

* nous avons déjà parlé de l'opérateur `==` qui **compare la valeur** de deux objets ;
* python fournit aussi un opérateur `is` qui permet de savoir si deux valeurs correspondent **au même objet** en mémoire.

Nous allons illustrer la différence entre ces deux opérateurs.

+++

##### Scénario 1

```{code-cell} ipython3
:cell_style: split

# deux listes identiques
a = [1, 2]
b = [1, 2]

# les deux objets se ressemblent
print('==', a == b)
```

```{code-cell} ipython3
:cell_style: split

# mais ce ne sont pas les mêmes objets
print('is', a is b)
```

##### Scénario 2

```{code-cell} ipython3
:cell_style: split

# par contre ici il n'y a qu'une liste
a = [1, 2]

# et les deux variables
# référencent le même objet
b = a

# non seulement les deux expressions se ressemblent
print('==', a == b)
```

```{code-cell} ipython3
:cell_style: split

# mais elles désignent le même objet
print('is', a is b)
```

### La même chose sous pythontutor

+++

##### Scénario 1

```{code-cell} ipython3
%%ipythontutor curInstr=2
a = [1, 2]
b = [1, 2]
```

##### Scénario 2

```{code-cell} ipython3
%%ipythontutor curInstr=1
# équivalent à la forme ci-dessus
# a = [1, 2]
# b = a
a = b = [1, 2]
```

### Utilisez `is` plutôt que `==` lorsque c'est possible

+++

La pratique usuelle est d'utiliser `is` lorsqu'on compare avec un objet qui est un singleton, comme typiquement `None`.

+++ {"cell_style": "split"}

Par exemple on préfèrera écrire :

```{code-cell} ipython3
:cell_style: split

undef = None

if undef is None:
    print('indéfini')
```

+++ {"cell_style": "split"}

Plutôt que :

```{code-cell} ipython3
:cell_style: split

if undef == None:
    print('indéfini')
```

Qui se comporte de la même manière (à nouveau, parce qu'on compare avec `None`), mais est légèrement moins lisible, et franchement moins pythonique. :)

+++

Notez aussi et surtout que `is` est **plus efficace** que `==`. En effet `is` peut être évalué en temps constant, puisqu'il s'agit essentiellement de comparer les deux adresses. Alors que pour `==` il peut s'agir de parcourir toute une structure de données possiblement très complexe.

+++

## Complément - niveau intermédiaire

+++

### La fonction `id`

+++

Pour bien comprendre le fonctionnement de `is` nous allons voir la fonction `id` qui retourne un identificateur unique pour chaque objet ; un modèle mental acceptable est celui d'adresse mémoire.

```{code-cell} ipython3
id(True)
```

Comme vous vous en doutez, l'opérateur `is` peut être décrit formellement à partir de `id` comme ceci :

(`a is b`) $\Longleftrightarrow$ (`id(a) == id(b)`)

+++

### Certains types de base sont des singletons

+++

Un singleton est un objet qui n'existe qu'en un seul exemplaire dans la mémoire. Un usage classique des singletons en Python est de minimiser le nombre d'objets immuables en mémoire. Voyons ce que cela nous donne avec des entiers :

```{code-cell} ipython3
a = 3
b = 3
print('a', id(a), 'b', id(b))
```

Tiens, c'est curieux, nous avons ici deux objets, que l'on pourrait penser différents, mais en fait ce sont les mêmes ; `a` et `b` désignent **le même objet** python, et on a :

```{code-cell} ipython3
a is b
```

Il se trouve que, dans le cas des petits entiers, python réalise une optimisation de l'utilisation de la mémoire. Quel que soit le nombre de variables dont la valeur est `3`, un seul objet correspondant à l'entier `3` est alloué et créé, pour éviter d'engorger la mémoire. On dit que l'entier `3` est implémenté comme un singleton ; nous reverrons ceci en exercice.

+++

On trouve cette optimisation avec quelques autres objets python, comme par exemple :

```{code-cell} ipython3
a = ""
b = ""
a is b
```

Ou encore, plus surprenant :

```{code-cell} ipython3
a = "foo"
b = "foo"
a is b
```

**Conclusion** cette optimisation ne touche aucun type mutable (heureusement) ; pour les types immuables, il n'est pas extrêmement important de savoir en détail quels objets sont implémentés de la sorte.

Ce qui est par contre extrêmement important est de comprendre la différence entre `is` et `==`, et de les utiliser à bon escient au risque d'écrire du code fragile.

+++

### Pour en savoir plus

+++

Aux étudiants de niveau avancé, nous recommandons la lecture de la section "Objects, values and types" dans la documentation Python :

<https://docs.python.org/3/reference/datamodel.html#objects-values-and-types>

qui aborde également la notion de "garbage collection", que nous n'aurons pas le temps d'approfondir dans ce MOOC.
