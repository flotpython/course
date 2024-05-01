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
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
language_info:
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
nbhosting:
  title: Ensembles
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

# Ensembles

+++

## Complément - niveau basique

+++

Ce document résume les opérations courantes disponibles sur le type `set`. On rappelle que le type `set` est un type **mutable**.

+++

### Création en extension

+++

On crée un ensemble avec les accolades, comme les dictionnaires, mais sans utiliser le caractère `:`, et cela donne par exemple :

```{code-cell} ipython3
heteroclite = {'marc', 12, 'pierre', (1, 2, 3), 'pierre'}
print(heteroclite)
```

### Création - la fonction `set`

+++

Il devrait être clair à ce stade que, le nom du type étant `set`, la fonction `set` est un constructeur d'ensemble. On aurait donc aussi bien pu faire :

```{code-cell} ipython3
heteroclite2 = set(['marc', 12, 'pierre', (1, 2, 3), 'pierre'])
print(heteroclite2)
```

### Créer un ensemble vide

+++

Il faut remarquer que l'on ne peut pas créer un ensemble vide en extension. En effet :

```{code-cell} ipython3
type({})
```

Ceci est lié à des raisons historiques, les ensembles n'ayant fait leur apparition que tardivement dans le langage en tant que <em>citoyen de première classe</em>.

+++

Pour créer un ensemble vide, la pratique la plus courante est celle-ci :

```{code-cell} ipython3
ensemble_vide = set()
print(type(ensemble_vide))
```

Ou également, moins élégant mais que l'on trouve parfois dans du vieux code :

```{code-cell} ipython3
autre_ensemble_vide = set([])
print(type(autre_ensemble_vide))
```

### Un élément dans un ensemble doit être globalement immuable

+++

On a vu précédemment que les clés dans un dictionnaire doivent être globalement immuables. Pour exactement les mêmes raisons, les éléments d'un ensemble doivent aussi être globalement immuables :

+++

```python
# on ne peut pas insérer un tuple qui contient une liste
>>> ensemble = {(1, 2, [3, 4])}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

+++

Le type `set` étant lui-même mutable, on ne peut pas créer un ensemble d'ensembles :

+++

```python
>>> ensemble = {{1, 2}}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'set'
```

+++

Et c'est une des raisons d'être du type `frozenset`.

+++

### Création - la fonction `frozenset`

+++

Un `frozenset` est un ensemble qu'on ne peut pas modifier, et qui donc peut servir de clé dans un dictionnaire, ou être inclus dans un autre ensemble (mutable ou pas).

+++

Il n'existe pas de raccourci syntaxique comme les `{}` pour créer un ensemble immuable, qui doit être créé avec la fonction `frozenset`. Toutes les opérations documentées dans ce notebook, et qui n'ont pas besoin de modifier l'ensemble, sont disponibles sur un `frozenset`.

Parmi les fonctions exclues sur un `frozenset`, on peut citer :  `update`, `pop`, `clear`, `remove` ou `discard`.

+++

### Opérations simples

```{code-cell} ipython3
# pour rappel
heteroclite
```

##### Test d'appartenance

```{code-cell} ipython3
(1, 2, 3) in heteroclite
```

##### Cardinal

```{code-cell} ipython3
len(heteroclite)
```

##### Manipulations

```{code-cell} ipython3
ensemble = {1, 2, 1}
ensemble
```

```{code-cell} ipython3
# pour nettoyer
ensemble.clear()
ensemble
```

```{code-cell} ipython3
# ajouter un element
ensemble.add(1)
ensemble
```

```{code-cell} ipython3
# ajouter tous les elements d'un autre *ensemble*
ensemble.update({2, (1, 2, 3), (1, 3, 5)})
ensemble
```

```{code-cell} ipython3
# enlever un element avec discard
ensemble.discard((1, 3, 5))
ensemble
```

```{code-cell} ipython3
# discard fonctionne même si l'élément n'est pas présent
ensemble.discard('foo')
ensemble
```

```{code-cell} ipython3
# enlever un élément avec remove
ensemble.remove((1, 2, 3))
ensemble
```

```{code-cell} ipython3
# contrairement à discard, l'élément doit être présent,
# sinon il y a une exception
try:
    ensemble.remove('foo')
except KeyError as e:
    print("remove a levé l'exception", e)
```

La capture d'exception avec `try` et `except`  sert à capturer une erreur d'exécution du programme (que l'on appelle exception) pour continuer le programme. Le but de cet exemple est simplement de montrer (d'une manière plus élégante que de voir simplement le programme planter avec une exception non capturée) que l'expression `ensemble.remove('foo')` génère une exception. Si ce concept vous paraît obscur, pas d'inquiétude, nous l'aborderons cette semaine et nous y reviendrons en détail en semaine 6.

```{code-cell} ipython3
# pop() ressemble à la méthode éponyme sur les listes
# sauf qu'il n'y a pas d'ordre dans un ensemble
while ensemble:
    element = ensemble.pop()
    print("element", element)
print("et bien sûr maintenant l'ensemble est vide", ensemble)
```

### Opérations classiques sur les ensembles

+++

Donnons-nous deux ensembles simples :

```{code-cell} ipython3
A2 = set([0, 2, 4, 6])
print('A2', A2)
A3 = set([0, 6, 3])
print('A3', A3)
```

N'oubliez pas que les ensembles ne sont **pas ordonnés** (contrairement aux dictionnaires que, depuis Python-3.7, l'on parcourt dans l'ordre de création des clés)

+++

**Remarques** :

* les notations des opérateurs sur les ensembles rappellent les opérateurs "bit-à-bit" sur les entiers ;
* ces opérateurs sont également disponibles sous la forme de méthodes.

+++

##### Union

```{code-cell} ipython3
A2 | A3
```

##### Intersection

```{code-cell} ipython3
A2 & A3
```

##### Différence

```{code-cell} ipython3
A2 - A3
```

```{code-cell} ipython3
A3 - A2
```

##### Différence symétrique

+++

On rappelle que $A \Delta B = (A - B) \cup (B - A)$

```{code-cell} ipython3
A2 ^ A3
```

### Comparaisons

+++

Ici encore on se donne deux ensembles :

```{code-cell} ipython3
superset = {0, 1, 2, 3}
print('superset', superset)
subset =  {1, 3}
print('subset', subset)
```

##### Égalité

```{code-cell} ipython3
heteroclite == heteroclite2
```

##### Inclusion

```{code-cell} ipython3
subset <= superset
```

```{code-cell} ipython3
subset < superset
```

```{code-cell} ipython3
heteroclite < heteroclite2
```

##### Ensembles disjoints

```{code-cell} ipython3
heteroclite.isdisjoint(A3)
```

### Pour en savoir plus

+++

Reportez vous à [la section sur les ensembles](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset) dans la documentation Python.
