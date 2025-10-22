---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
language_info:
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
nbhosting:
  title: Series
---

# `Series` de `pandas`

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Complément - niveau intermédiaire

+++

### Création d'une `Series`

+++

Un objet de type `Series` est un tableau `numpy` à une dimension avec un index, par conséquent, une `Series` a une certaine similarité avec un dictionnaire, et peut d'ailleurs être directement construite à partir de ce dictionnaire. Notons que, comme pour un dictionnaire, l'accès ou la modification est en $O(1)$, c'est-à-dire à temps constant indépendamment du nombre d'éléments dans la `Series`.

```{code-cell} ipython3
# Regardons la construction d'une Series
import numpy as np
import pandas as pd

# à partir d'un itérable
s = pd.Series([x**2 for x in range(10)])
print(s)
```

```{code-cell} ipython3
# en contrôlant maintenant le type
s = pd.Series([x**2 for x in range(10)], dtype='int8')
print(s)
```

```{code-cell} ipython3
# en définissant un index, par défaut l'index est un rang démarrant à 0
s = pd.Series([x**2 for x in range(10)],
              index=[x for x in 'abcdefghij'],
              dtype='int8',
             )
print(s)
```

```{code-cell} ipython3
# et directement à partir d'un dictionnaire,
# les clefs forment l'index
d = {k:v**2 for k, v in zip('abcdefghij', range(10))}
print(d)
```

```{code-cell} ipython3
s = pd.Series(d, dtype='int8')
print(s)
```

Évidemment, l'intérêt d'un index est de pouvoir accéder à un élément par son index, comme nous aurons l'occasion de le revoir :

```{code-cell} ipython3
print(s['f'])
```

### Index

+++

L'index d'une `Series` est un objet implémenté sous la forme d'un `ndarray` de `numpy`, mais qui ne peut contenir que des objets hashables (pour garantir la performance de l'accès).

```{code-cell} ipython3
# pour accéder à l'index d'un objet Series
# attention, index est un attribut, pas une fonction
print(s.index)
```

L'index va également supporter un certain nombre de méthodes qui vont faciliter son utilisation. Pour plus de détails, voyez [la documentation de l'objet Index](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Index.html#pandas.Index) et de ses sous-classes.

+++

L'autre moitié de l'objet `Series` est accessible via l'attribut `values`. **ATTENTION** à nouveau ici, c'est un **attribut** de l'objet et non pas une méthode, ce qui est très troublant par rapport à l'interface d'un dictionnaire.

```{code-cell} ipython3
# regardons les valeurs de ma Series
# ATTENTION !! values est un attribut, pas une fonction
print(s.values)
```

Mais une `Series` a également une interface de dictionnaire à laquelle on accède de la manière suivante :

```{code-cell} ipython3
# les clefs correspondent à l'index
k = s.keys() # attention ici c'est un appel de fonction !
print(f"Les clefs: {k}")
```

```{code-cell} ipython3
# et les couples (clefs, valeurs) sous forme d'un objet zip
for k,v in s.items(): # attention ici aussi c'est un appel de fonction !
    print(k, v)
```

```{code-cell} ipython3
# pour finir remarquons que le test d'appartenance est possible sur les index
print(f"Est-ce que a est dans s ? {'a' in s}")
print(f"Est-ce que z est dans s ? {'z' in s}")
```

Vous remarquez ici qu'alors que `values` et `index` sont des attributs de la `Series`, `keys()` et `items()` sont des méthodes. Voici un exemple des nombreuses petites incohérences de `pandas` avec lesquelles il faut vivre.

+++

### Pièges à éviter

+++

Avant d'aller plus loin, il faut faire attention à la gestion du type des objets contenus dans notre `Series` (on aura le même problème avec les `DataFrame`). Alors qu'un `ndarray` de `numpy` a un type qui ne change pas, une `Series` peut implicitement changer le type de ses valeurs lors d'opérations d'affectations.

```{code-cell} ipython3
# créons une Series et regardons le type de ses valeurs
s = pd.Series({k:v**2 for k, v in zip('abcdefghij', range(10))})
print(s.values.dtype)
```

```{code-cell} ipython3
# On a déjà vu que l'on ne pouvait pas modifier lors d'une affectation le
# type d'un ndarray numpy

try:
    s.values[2] = 'spam'
except ValueError as e:
    print(f"On ne peut pas affecter une str à un ndarray de int64:\n{e}")
```

```{code-cell} ipython3
# Par contre, on peut le faire sur une Series
s['c'] = 'spam'

# et maintenant le type des valeurs de la Series a changé
print(s.values.dtype)
```

C'est un point extrêment important puisque toutes les opérations vectorisées vont avoir leur performance impactée et le résultat obtenu peut même être faux. Regardons cela :

```{code-cell} ipython3
s = pd.Series(range(10_000))
print(s.values.dtype)
```

```{code-cell} ipython3
# combien de temps prend le calcul du carré des valeurs
%timeit s**2
```

```{code-cell} ipython3
# ajoutons 'spam' à la fin de la Series
s[10_000] = 'spam'

# oups, je me suis trompé, enlevons cet élément
del s[10_000]

# calculons de nouveau le temps de calcul pour obtenir le carré des valeurs
%timeit s**2
```

```{code-cell} ipython3
# que se passe-t-il, pourquoi le calcul est maintenant plus long
s.values.dtype
```

Maintenant, les opérations vectorisées le sont sur des objets Python et non plus sur des int64, il y a donc un impact sur la performance.

Et on peut même obtenir un résultat carrément faux. Regardons cela :

```{code-cell} ipython3
# créons une series de trois entiers
s = pd.Series([1, 2, 3])
print(s)
```

```{code-cell} ipython3
# puis ajoutons un nouvel élément, mais ici je me trompe, c'est une str
# au lieu d'un entier
s[3] = '4'

# à part le type qui pourrait attirer mon attention, rien dans l'affichage
# ne distingue les entiers de la str, à part le dtype
print(s)
```

```{code-cell} ipython3
# seulement si j'additionne, les entiers sont additionnés,
# mais les chaînes de caractères concaténées.
print(s+s)
```

### Alignement d'index

+++

Un intérêt majeur de `pandas` est de faire de l'alignement d'index sur les objets que l'on manipule. Regardons un exemple :

```{code-cell} ipython3
argent_poche_janvier = pd.Series([30, 35, 20],
                                 index=['alice', 'bob', 'julie'])
argent_poche_février = pd.Series([30, 35, 20],
                                 index=['alice', 'julie', 'sonia'])
argent_poche_janvier + argent_poche_février
```

On voit que les deux `Series` ont bien été alignées, mais on a un problème. Lorsqu'une valeur n'est pas définie, elle vaut `NaN` et si on ajoute `NaN` à une autre valeur, le résultat est `NaN`. On peut corriger ce problème avec un appel explicite de la fonction add qui accepte un argument `fill_value` qui sera la valeur par défaut en cas d'absence d'une valeur lors de l'opération.

```{code-cell} ipython3
argent_poche_janvier.add(argent_poche_février, fill_value=0)
```

### Accés aux éléments d'une `Series`

+++

Comme les `Series` sont basées sur des `ndarray` de `numpy`, elles supportent les opérations d'accès aux éléments des `ndarray`, notamment la notion de masque et les broadcasts, tout ça en conservant évidemment les index.

```{code-cell} ipython3
s = pd.Series([30, 35, 20], index=['alice', 'bob', 'julie'])

# qui a plus de 25 ans
print(s[s>25])
```

```{code-cell} ipython3
# regardons uniquement 'alice' et 'julie'
print(s[['alice', 'julie']])
```

```{code-cell} ipython3
# et affectons sur un masque
s[s<=25] = np.nan
print(s)
```

```{code-cell} ipython3
# notons également, que naturellement les opérations de broadcast
# sont supportées
s = s + 10
print(s)
```

### Slicing sur les `Series`

+++

L'opération de slicing sur les `Series` est une source fréquente d'erreur qui peut passer inaperçue pour les raisons suivantes :

* on peut slicer sur les labels des index, mais aussi sur la position (l'indice) d'un élément dans la `Series` ;
* les opérations de slices sur les positions et les labels se comportent différemment, [un slice sur les positions exclut la borne de droite (comme tous les slices en Python), mais un slice sur un label inclut la borne de droite](http://pandas.pydata.org/pandas-docs/stable/gotchas.html#endpoints-are-inclusive) ;
* il peut y avoir ambiguïté entre un label et la position d'un élément lorsque le label est un entier.

Nous allons détailler chacun de ces cas, mais sachez qu'il existe une solution qui évite toute ambiguïté, c'est d'utiliser les interfaces `loc` et `iloc` que nous verrons un peu plus loin.

Regardons maintenant ces différents problèmes :

```{code-cell} ipython3
s = pd.Series([30, 35, 20, 28], index=['alice', 'bob', 'julie', 'sonia'])
print(s)
```

```{code-cell} ipython3
# on peut accéder directement à la valeur correspondant à alice
print(s['alice'])

# mais aussi par la position d'alice dans l'index
print(s[0])
```

```{code-cell} ipython3
# On peut faire un slice sur les labels, dans ce cas la borne
# de droite est incluse
s['alice':'julie']
```

```{code-cell} ipython3
# et on peut faire un slice sur les positions, mais dans ce cas
# la borne de droite est exclue, comme un slice normal en Python
s[0:2]
```

Ce comportement mérite quelques explications. On voit bien qu'exclure la borne de droite peut se comprendre sur une position (si on exclut `i` on prend `i-1`), par contre, c'est mal défini pour un label.

En effet, l'ordre d'un index est défini au moment de sa création et le label venant juste avant un autre label `L` ne peut pas être trouvé uniquement avec la connaissance de `L`.

C'est pour cette raison que les concepteurs de `pandas` ont préféré inclure la borne de droite.

Regardons maintenant plus en détail cette notion d'ordre sur les index.

```{code-cell} ipython3
# Regardons le slice sur un index avec un ordre particulier
s = pd.Series([30, 35, 20, 28], index=['alice', 'bob', 'julie', 'sonia'])
print(s['alice':'julie'])
```

```{code-cell} ipython3
# Si on change l'ordre de l'index, ça change la signification du slice
s = pd.Series([30, 35, 20, 28], index=['alice', 'bob', 'sonia', 'julie'])
print(s['alice':'julie'])
```

Vous devez peut-être vous demander si un slice sur l'index est toujours défini. La réponse est non ! Pour qu'un slice soit défini sur un index, il faut que [l'index ait une croissance monotone ou qu'il n'y ait pas de label dans l'index qui soit dupliqué.](https://pandas.pydata.org/pandas-docs/stable/advanced.html#non-monotonic-indexes-require-exact-matches)

Donc la croissance monotonique n'est pas nécessaire tant qu'il n'y a pas de duplication de labels. Regardons cela.

```{code-cell} ipython3
# mon index a des labels dupliqués, mais a une croissance monotonique
s = pd.Series([30, 35, 20, 12], index=['a', 'a', 'b', 'c'])
# le slice est défini
s['a': 'b']
```

```{code-cell} ipython3
# mon index a des labels dupliqués et n'a pas de croissance monotonique
s = pd.Series([30, 35, 20, 12], index=['a', 'b', 'c', 'a'])
# le slice n'est plus défini
try:
    s['a': 'b']
except KeyError as e:
    print(f"Je n'arrive pas à extraire un slice :\n{e}")
```

Pour finir sur les problèmes que l'on peut rencontrer avec les slices, que se passe-t-il si on a un index qui a pour label des entiers ?

Lorsque l'on va faire un slice, il va y avoir ambiguïté entre la position du label et le label lui-même. Dans ce cas, `pandas` donne la priorité à la position, mais ce qui est troublant, c'est que lorsqu'on accède à un seul élément en dehors d'un slice, `pandas` donne la priorité à l'index.

Encore une petite incohérence :

```{code-cell} ipython3
s = pd.Series(['a', 'b', 'c'], index=[2, 0, 1])
print(f"Si on accède directement à un élément, priorité au label : {s[0]}")
print(f"Si on calcule un slice, priorité à la position : {s[0:1]}")
```

### `loc` et `iloc`

+++

La solution à tous ces problèmes est de dire explicitement ce que l'on veut faire. On peut en effet dire explicitement si l'on veut utiliser les labels ou les positions, c'est ce qu'on vous recommande de faire pour éviter les comportements implicites.

Pour utiliser les labels il faut utiliser `s.loc[]` et pour utiliser les positions if faut utiliser `s.iloc[]` (le `i` est pour localisation implicite, c'est-à-dire la position). Regardons cela :

```{code-cell} ipython3
# prenons un cas plus usuel, où les labels sont plutôt des chaines
# notez que la logique est la même quel que soit le type de l'index

s = pd.Series([1000, 2000, 3000, 4000], index=['deux', 'zero', 'un', 'quatre'])
print(s)
```

```{code-cell} ipython3
# accès au label
print(s.loc['zero'])
```

```{code-cell} ipython3
# accès à la position
print(s.iloc[0])
```

```{code-cell} ipython3
# slice sur les labels, ATTENTION, il inclut la borne de droite
print(s.loc['deux':'zero'])
```

```{code-cell} ipython3
# slice sur les positions, ATTENTION, il exclut la borne de droite
print(s.iloc[1:3])
```

Pour allez plus loin, vous pouvez lire la documentation officielle :

<http://pandas.pydata.org/pandas-docs/stable/indexing.html>

+++

### Conclusion

+++

Nous avons vu que les `Series` forment une extension des ndarray de dimension 1, en leur ajoutant un index qui permet une plus grande expressivité pour accéder aux éléments. Seulement cette expressivité vient au prix de quelques subtilités (conversions implicites de type, accès aux labels ou aux positions) qu'il faut maîtriser.

Nous verrons dans le prochain complément la notion de `DataFrame` qui est sans doute la plus utile et la plus puissante structure de données de `pandas`. Tous les pièges que nous avons vus pour les `Series` sont valables pour les `DataFrames`.
