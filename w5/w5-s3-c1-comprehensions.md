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
notebookname: "Compr\xE9hension de liste"
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Construction de liste par compréhension

+++

## Révision - niveau basique

+++

Ce mécanisme très pratique permet de construire simplement une liste à partir d'une autre (ou de **tout autre type itérable** en réalité, mais nous y viendrons).

Pour l'introduire en deux mots, disons que la compréhension de liste est à l'instruction `for` ce que l'expression conditionnelle est à l'instruction  `if`, c'est-à-dire qu'il s'agit d'une **expression à part entière**.

+++

### Cas le plus simple

+++

Voyons tout de suite un exemple :

```{code-cell} ipython3
depart = (-5, -3, 0, 3, 5, 10)
arrivee = [x**2 for x in depart]
arrivee
```

Le résultat de cette expression est donc une liste, dont les éléments sont les résultats de l'expression `x**2` pour `x` prenant toutes les valeurs de `depart`.

+++

**Remarque** : si on prend un point de vue un peu plus mathématique, ceci revient donc à appliquer une certaine fonction (ici $x \rightarrow x^2$) à une collection de valeurs, et à retourner la liste des résultats. Dans les langages fonctionnels, cette opération est connue sous le nom de `map`, comme on l'a vu dans la séquence précédente.

+++

##### Digression

```{code-cell} ipython3
# profitons de cette occasion pour voir 
# comment tracer une courbe avec matplotlib
%matplotlib inline
import matplotlib.pyplot as plt
plt.ion()
```

```{code-cell} ipython3
# si on met le départ et l'arrivée 
# en abscisse et en ordonnée, on trace
# une version tronquée de la courbe de f: x -> x**2
plt.plot(depart, arrivee);
```

### Restriction à certains éléments

+++

Il est possible également de ne prendre en compte que certains des éléments de la liste de départ, comme ceci :

```{code-cell} ipython3
[x**2 for x in depart if x%2 == 0]
```

qui cette fois ne contient que les carrés des éléments pairs de `depart`.

+++

**Remarque** : pour prolonger la remarque précédente, cette opération s'appelle fréquemment `filter` dans les langages de programmation.

+++

### Autres types

+++

On peut fabriquer une compréhension à partir de tout objet itérable, pas forcément une liste, mais le résultat est toujours une liste, comme on le voit sur ces quelques exemples :

```{code-cell} ipython3
[ord(x) for x in 'abc']
```

```{code-cell} ipython3
[chr(x) for x in (97, 98, 99)]
```

### Autres types (2)

+++

On peut également construire par compréhension des dictionnaires et des ensembles :

```{code-cell} ipython3
d = {x: ord(x) for x in 'abc'}
d
```

```{code-cell} ipython3
e = {x**2 for x in (97, 98, 99) if x %2 == 0}
e
```

### Pour en savoir plus

+++

Voyez [la section sur les compréhensions de liste](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions) dans la documentation python.
