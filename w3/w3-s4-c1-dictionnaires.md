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
  title: Dictionnaires
---

# Dictionnaires

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Complément - niveau basique

+++

Ce document résume les opérations courantes disponibles sur le type `dict`. On rappelle que le type `dict` est un type **mutable**.

+++

### Création en extension

+++

On l'a vu, la méthode la plus directe pour créer un dictionnaire est en extension comme ceci :

```{code-cell} ipython3
annuaire = {'marc': 35, 'alice': 30, 'eric': 38}
print(annuaire)
```

### Création - la fonction dict

+++

Comme pour les fonctions `int` ou `list`, la fonction `dict` est une fonction de construction de dictionnaire - on dit un constructeur. On a vu aussi dans la vidéo qu'on peut utiliser ce constructeur à base d'une liste de tuples (`clé`, `valeur`)

```{code-cell} ipython3
# le paramètre de la fonction dict est
# une liste de couples (clé, valeur)
annuaire = dict([('marc', 35), ('alice', 30), ('eric', 38)])
print(annuaire)
```

Remarquons qu'on peut aussi utiliser cette autre forme d'appel à `dict` pour un résultat équivalent :

```{code-cell} ipython3
annuaire = dict(marc=35, alice=30, eric=38)
print(annuaire)
```

Remarquez ci-dessus l'absence de quotes autour des clés comme `marc`. Il s'agit d'un cas particulier de passage d'arguments que nous expliciterons plus longuement en fin de semaine 4.

+++

### Accès atomique

+++

Pour accéder à la valeur associée à une clé, on utilise la notation à base de crochets `[]` :

```{code-cell} ipython3
print('la valeur pour marc est', annuaire['marc'])
```

Cette forme d'accès ne fonctionne que si la clé est effectivement présente dans le dictionnaire. Dans le cas contraire, une exception `KeyError` est levée. Aussi si vous n'êtes pas sûr que la clé soit présente, vous pouvez utiliser la méthode `get` qui accepte une valeur par défaut :

```{code-cell} ipython3
print('valeur pour marc', annuaire.get('marc', 0))
print('valeur pour inconnu', annuaire.get('inconnu', 0))
```

Le dictionnaire est un type **mutable**, et donc on peut **modifier la valeur** associée à une clé :

```{code-cell} ipython3
annuaire['eric'] = 39
print(annuaire)
```

Ou encore, exactement de la même façon, **ajouter une entrée** :

```{code-cell} ipython3
annuaire['bob'] = 42
print(annuaire)
```

Enfin pour **détruire une entrée**, on peut utiliser l'instruction `del` comme ceci :

```{code-cell} ipython3
# pour supprimer la clé 'marc' et donc sa valeur aussi
del annuaire['marc']
print(annuaire)
```

Pour savoir si une clé est présente ou non, il est conseillé d'utiliser l'opérateur d'appartenance `in` comme ceci :

```{code-cell} ipython3
# forme recommandée
print('john' in annuaire)
```

### Parcourir toutes les entrées

+++

La méthode la plus fréquente pour parcourir tout un dictionnaire est à base de la méthode `items` ; voici par exemple comment on pourrait afficher le contenu :

```{code-cell} ipython3
for nom, age in annuaire.items():
    print(f"{nom}, age {age}")
```

On remarque d'abord que les entrées sont listées dans le désordre, plus précisément, il n'y a pas de notion d'ordre dans un dictionnaire ; ceci est dû à l'action de la fonction de hachage, que nous avons vue dans la vidéo précédente.

+++

On peut obtenir séparément la liste des clés et des valeurs avec :

```{code-cell} ipython3
for cle in annuaire.keys():
    print(cle)
```

```{code-cell} ipython3
for valeur in annuaire.values():
    print(valeur)
```

### La fonction `len`

+++

On peut comme d'habitude obtenir la taille d'un dictionnaire avec la fonction `len` :

```{code-cell} ipython3
print(f"{len(annuaire)} entrées dans annuaire")
```

### Pour en savoir plus sur le type `dict`

+++

Pour une liste exhaustive reportez-vous à la page de la documentation Python ici :

<https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>

+++

**********

+++

## Complément - niveau intermédiaire

+++

### La méthode `update`

+++

On peut également modifier un dictionnaire avec le contenu d'un autre dictionnaire avec la méthode `update` :

```{code-cell} ipython3
print(f"avant: {list(annuaire.items())}")
```

```{code-cell} ipython3
annuaire.update({'jean':25, 'eric':70})
list(annuaire.items())
```

### dictionnaire et ordre d'insertion

+++

**Attention** : ce qui suit est valable ***pour les versions de Python-3.7 et supérieures***

depuis cette version un dictionnaire est **ordonné**; cela signifie qu'il se souvient de l'ordre dans lequel les éléments ont été insérés, et c'est dans cet ordre que l'on itère sur le dictionnaire.

```{code-cell} ipython3
# quand on itère sur un dictionnaire, 
# les clés sont parcourues dans l'ordre d'insertion
d = {'a' : 1, 'b' : 2, 'c' : 3}
d['d'] = 4
for k, v in d.items():
    print(k, v)
```

Je vous signale à toutes fins utiles, dans [le module `collections`](https://docs.python.org/3/library/collections.html) la classe [`OrderedDict`](https://docs.python.org/3/library/collections.html#collections.OrderedDict), qui est une personnalisation (une sous-classe) du type `dict`, date de l'époque (jusque 3.7 donc) où le dictionnaire natif n'avait pas cette bonne propriété, et qui reste disponible pour des raisons de compatibilité ascendante.

+++

### `collections.defaultdict` : initialisation automatique

+++

Imaginons que vous devez gérer un dictionnaire dont les valeurs sont des listes, et que votre programme ajoute des valeurs au fur et à mesure dans ces listes.

Avec un dictionnaire de base, cela peut vous amener à écrire un code qui ressemble à ceci :

```{code-cell} ipython3
# imaginons qu'on a lu dans un fichier des couples (x, y)
tuples = [
    (1, 2),
    (2, 1),
    (1, 3),
    (2, 4),
]
```

```{code-cell} ipython3
# et on veut construire un dictionnaire
# x -> [liste de tous les y connectés à x]
resultat = {}

for x, y in tuples:
    if x not in resultat:
        resultat[x] = []
    resultat[x].append(y)

for key, value in resultat.items():
    print(key, value)
```

Cela fonctionne, mais n'est pas très élégant. Pour simplifier ce type de traitement, vous pouvez utiliser `defaultdict`, une sous-classe de `dict` dans le module `collections` :

```{code-cell} ipython3
from collections import defaultdict

# on indique que les valeurs doivent être créées à la volée
# en utilisant la fonction list
resultat = defaultdict(list)

# du coup plus besoin de vérifier la présence de la clé
for x, y in tuples:
    resultat[x].append(y)

for key, value in resultat.items():
    print(key, value)
```

Cela fonctionne aussi avec le type `int`, lorsque vous voulez par exemple compter des occurrences :

```{code-cell} ipython3
compteurs = defaultdict(int)

phrase = "une phrase dans laquelle on veut compter les caractères"

for c in phrase:
    compteurs[c] += 1

sorted(compteurs.items())
```

Signalons enfin une fonctionnalité un peu analogue, quoiqu'un peu moins élégante à mon humble avis, mais qui est présente avec les dictionnaires `dict` standard. Il s'agit de [la méthode `setdefault`](https://docs.python.org/3/library/stdtypes.html#dict.setdefault) qui permet, en un seul appel, de retourner la valeur associée à une clé et de créer cette clé au besoin, c'est-à-dire si elle n'est pas encore présente :

```{code-cell} ipython3
# avant
annuaire
```

```{code-cell} ipython3
# ceci sera sans effet car eric est déjà présent
annuaire.setdefault('eric', 50)
```

```{code-cell} ipython3
# par contre ceci va insérer une entrée dans le dictionnaire
annuaire.setdefault('inconnu', 50)
```

```{code-cell} ipython3
# comme on le voit
annuaire
```

Notez bien que `setdefault` peut éventuellement créer une entrée mais ne **modifie jamais** la valeur associée à une clé déjà présente dans le dictionnaire, comme le nom le suggère d'ailleurs.

+++

## Complément - niveau avancé

+++

Pour bien appréhender les dictionnaires, il nous faut souligner certaines particularités, à propos de la valeur de retour des méthodes comme `items()`, `keys()` et `values()`.

+++

### Ce sont des objets itérables

+++

Les méthodes `items()`, `keys()` et `values()` ne retournent pas des listes (comme c'était le cas en Python 2), mais des **objets itérables** :

```{code-cell} ipython3
d = {'a' : 1, 'b' : 2}
keys = d.keys()
keys
```

Comme ce sont des itérables, on peut naturellement faire un `for` avec, on l'a vu :

```{code-cell} ipython3
for key in keys:
    print(key)
```

Et un test d'appartenance avec `in` :

```{code-cell} ipython3
print('a' in keys)
```

```{code-cell} ipython3
print('x' in keys)
```

### Mais **ce ne sont pas des listes**

```{code-cell} ipython3
isinstance(keys, list)
```

Ce qui signifie qu'on n'a **pas alloué de mémoire** pour stocker toutes les clés, mais seulement un objet qui ne prend pas de place, ni de temps à construire :

```{code-cell} ipython3
# construisons un dictionnaire
# pour anticiper un peu sur la compréhension de dictionnaire

big_dict = {k : k**2 for k in range(1_000_000)}
```

```{code-cell} ipython3
%%timeit -n 10000
# créer un objet vue est très rapide
big_keys = big_dict.keys()
```

```{code-cell} ipython3
# on répète ici car timeit travaille dans un espace qui lui est propre
# et donc on n'a pas défini big_keys pour notre interpréteur
big_keys = big_dict.keys()
```

```{code-cell} ipython3
%%timeit -n 20
# si on devait vraiment construire la liste ce serait beaucoup plus long
big_lkeys = list(big_keys)
```

### En fait ce sont des *vues*

+++

Une autre propriété un peu inattendue de ces objets, c'est que **ce sont des vues** ; ce qu'on veut dire par là (pour ceux qui connaissent, cela fait fait référence à la notion de vue dans les bases de données) c'est que la vue *voit* les changements fait sur l'objet dictionnaire *même après sa création* :

```{code-cell} ipython3
d = {'a' : 1, 'b' : 2}
keys = d.keys()
```

```{code-cell} ipython3
# sans surprise, il y a deux clés dans keys
for k in keys:
    print(k)
```

```{code-cell} ipython3
# mais si maintenant j'ajoute un objet au dictionnaire
d['c'] = 3
# alors on va 'voir' cette nouvelle clé à partir
# de l'objet keys qui pourtant est inchangé
for k in keys:
    print(k)
```

Reportez vous à [la section sur les vues de dictionnaires](https://docs.python.org/3/library/stdtypes.html#dictionary-view-objects) pour plus de détails.
