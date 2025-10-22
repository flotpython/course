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
  title: "Fusionner des donn\xE9es"
---

# Fusionner des données

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Exercices

+++

Cet exercice vient en deux versions, une de niveau basique et une de niveau intermédiaire.

La version basique est une application de la technique d'indexation que l'on a vue dans le complément "Gérer des enregistrements". On peut très bien faire les deux versions dans l'ordre, une fois qu'on a fait la version basique on est en principe un peu plus avancé pour aborder la version intermédiaire.

+++

### Contexte

+++

Nous allons commencer à utiliser des données un peu plus réalistes. Il s'agit de données obtenues auprès de [MarineTraffic](https://www.marinetraffic.com) - et légèrement simplifiées pour les besoins de l'exercice. Ce site expose les coordonnées géographiques de bateaux observées en mer au travers d'un réseau de collecte de type *crowdsourcing*.

+++

De manière à optimiser le volume de données à transférer, l'API de MarineTraffic offre deux modes pour obtenir les données :

* **mode étendu** : chaque mesure (bateau x position x temps) est accompagnée de tous les détails du bateau (`id`, nom, pays de rattachement, etc.) ;
* **mode abrégé** : chaque mesure est uniquement attachée à l'`id` du bateau.

En effet, chaque bateau possède un identifiant unique qui est un entier, que l'on note  `id`.

+++

### Chargement des données

+++

Commençons par charger les données de l'exercice :

```{code-cell} ipython3
from corrections.exo_marine_dict import extended, abbreviated
```

### Format des données

+++

Le format de ces données est relativement simple, il s'agit dans les deux cas d'une liste d'entrées - une par bateau.

Chaque entrée à son tour est une liste qui contient :

    mode étendu: [id, latitude, longitude, date_heure, nom_bateau, code_pays, ...]
    mode abrégé: [id, latitude, longitude, date_heure]

sachant que les entrées après le code pays dans le format étendu ne nous intéressent pas pour cet exercice.

```{code-cell} ipython3
# une entrée étendue est une liste qui ressemble à ceci
sample_extended_entry = extended[3]
print(sample_extended_entry)
```

```{code-cell} ipython3
# une entrée abrégée ressemble à ceci
sample_abbreviated_entry = abbreviated[0]
print(sample_abbreviated_entry)
```

On précise également que les deux listes `extended` et `abbreviated` :

* possèdent exactement **le même nombre** d'entrées ;
* et correspondent **aux mêmes bateaux** ;
* mais naturellement **à des moments différents** ;
* et **pas forcément dans le même ordre**.

+++

*******

+++

### Exercice - niveau basique

```{code-cell} ipython3
# chargement de l'exercice
from corrections.exo_marine_dict import exo_index
```

##### But de l'exercice

+++

On vous demande d'écrire une fonction `index` qui calcule, à partir de la liste des données étendues, un dictionnaire qui est :

* indexé par l'`id` de chaque bateau ;
* et qui a pour valeur la liste qui décrit le bateau correspondant.

+++

De manière plus imagée, si :

```python
extended = [ bateau1, bateau2, ... ]
```

Et si :

```python
bateau1 = [ id1, latitude, ... ]
```

On doit obtenir comme résultat de `index` un dictionnaire :

```python
{
    id1 -> [ id_bateau1, latitude, ... ],
    id2 ...
}
```

Bref, on veut pouvoir retrouver les différents éléments de la liste `extended` par accès direct, en ne faisant qu'une seule recherche dans l'index.

```{code-cell} ipython3
# le résultat attendu
result_index = exo_index.resultat(extended)

# on en profite pour illustrer le module pprint
from pprint import pprint

# à quoi ressemble le résultat pour un bateau au hasard
for key, value in result_index.items():
    print("==== clé")
    pprint(key)
    print("==== valeur")
    pprint(value)
    break
```

Remarquez ci-dessus l'utilisation d'un utilitaire parfois pratique : le [module `pprint` pour pretty-printer](https://docs.python.org/3/library/pprint.html).

+++

##### Votre code

```{code-cell} ipython3
def index(extended):
    "<votre_code>"
```

##### Validation

```{code-cell} ipython3
exo_index.correction(index, abbreviated)
```

Vous remarquerez d'ailleurs que la seule chose que l'on utilise dans cet exercice, c'est que l'id des bateaux arrive en première position (dans la liste qui matérialise le bateau), aussi votre code doit marcher à l'identique avec les bateaux étendus :

```{code-cell} ipython3
exo_index.correction(index, extended)
```

### Exercice - niveau intermédiaire

```{code-cell} ipython3
# chargement de l'exercice
from corrections.exo_marine_dict import exo_merge
```

##### But de l'exercice

+++

On vous demande d'écrire une fonction `merge` qui fasse une consolidation des données, de façon à obtenir en sortie un dictionnaire :

```python
id -> [nom_bateau, code_pays, position_etendu, position_abrege]
```

dans lequel les deux objets `position` sont tous les deux des tuples de la forme :

```python
(latitude, longitude, date_heure)
```

+++

Voici par exemple un couple clé-valeur dans le résultat attendu :

```{code-cell} ipython3
# le résultat attendu
result_merge = exo_merge.resultat(extended, abbreviated)

# à quoi ressemble le résultat pour un bateau au hasard
from pprint import pprint
for key_value in result_merge.items():
    pprint(key_value)
    break
```

##### Votre code

```{code-cell} ipython3
def merge(extended, abbreviated):
    "votre code"
```

##### Validation

```{code-cell} ipython3
exo_merge.correction(merge, extended, abbreviated)
```

### Les fichiers de données complets

+++

Signalons enfin pour ceux qui sont intéressés que les données chargées dans cet exercice sont disponibles au format JSON - qui est précisément celui exposé par marinetraffic.

Nous avons beaucoup simplifié les données d'entrée pour vous permettre une mise au point plus facile. Si vous voulez vous amuser à charger des données un peu plus significatives, sachez que :

* vous avez accès aux fichiers de données plus complets :
  * [data/marine-e1-ext.json](data/marine-e1-ext.json)
  * [data/marine-e1-abb.json](data/marine-e1-abb.json)
* pour charger ces fichiers, qui sont donc au [format JSON](http://en.wikipedia.org/wiki/JSON), la connaissance intime de ce format n'est pas nécessaire, on peut tout simplement utiliser le [module `json`](https://docs.python.org/3/library/json.html). Voici le code utilisé dans l'exercice pour charger ces JSON en mémoire ; il utilise des notions que nous verrons dans les semaines à venir :

```{code-cell} ipython3
# load data from files
import json

with open("data/marine-e1-ext.json", encoding="utf-8") as feed:
    extended_full = json.load(feed)

with open("data/marine-e1-abb.json", encoding="utf-8") as feed:
    abbreviated_full = json.load(feed)
```

Une fois que vous avez un code qui fonctionne vous pouvez le lancer sur ces données plus copieuses en faisant :

```{code-cell} ipython3
exo_merge.correction(merge, extended_full, abbreviated_full)
```
