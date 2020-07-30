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
notebookname: DataFrame
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# `DataFrame` de `pandas`

+++

## Complément - niveau intermédiaire

+++

### Création d'une `DataFrame`

+++

Une `DataFrame` est un tableau `numpy` à deux dimensions avec un index pour les lignes et un index pour les colonnes. Il y a de nombreuses manières de construire une `DataFrame`.

```{code-cell}
# Regardons la construction d'une DataFrame
import numpy as np
import pandas as pd

# Créons une Series pour définir des âges
age = pd.Series([30, 20, 50], index=['alice', 'bob', 'julie'])

# et une Series pour définir des tailles
height = pd.Series([150, 170, 168], index=['alice', 'marc', 'julie'])

# On peut maintenant combiner ces deux Series en DataFrame,
# chaque Series définissant une colonne, une manière de le faire est
# de définir un dictionnaire qui contient pour clef le nom de la colonne
# et pour valeur la Series correspondante
stat = pd.DataFrame({'age': age, 'height': height})
print(stat)
```

On remarque que `pandas` fait automatiquement l'alignement des index, lorsqu'une valeur n'est pas présente, elle est automatiquement remplacée par `NaN`. `Panda` va également broadcaster une valeur unique définissant une colonne sur toutes les lignes. Regardons cela :

```{code-cell}
stat = pd.DataFrame({'age': age, 'height': height, 'city': 'Nice'})
print(stat)
```

```{code-cell}
# On peut maintenant accéder aux index des lignes et des colonnes

# l'index des lignes
print(stat.index)
```

```{code-cell}
# l'index des colonnes
print(stat.columns)
```

Il y a de nombreuses manières d'accéder aux éléments de la `DataFrame`, certaines sont bonnes et d'autres à proscrire, commençons par prendre de bonnes habitudes. Comme il s'agit d'une structure à deux dimensions, il faut donner un indice de ligne et de colonne :

```{code-cell}
:cell_style: split

# Quel est l'âge de alice
a = stat.loc['alice', 'age']
```

```{code-cell}
:cell_style: split

# a est un flottant
type(a), a
```

```{code-cell}
:cell_style: split

# Quel est la moyenne de tous les âges
c = stat.loc[:, 'age']
m = c.mean()
print(f"L'âge moyen est de {m:.1f} ans.")
```

```{code-cell}
:cell_style: split

# c est une Series
type(c)
```

```{code-cell}
:cell_style: split

# et m est un flottant
type(m)
```

On peut déjà noter plusieurs choses intéressantes :

- On peut utiliser `.loc[]` et `.iloc` comme pour les `Series`. Pour les `DataFrame` c'est encore plus important parce qu'il y a plus de risques d'ambiguïtés (notamment entre les lignes et les colonnes, on y reviendra) ;

- la méthode `mean` calcule la moyenne, ça n'est pas surprenant, mais ignore les `NaN`. C'est en général ce que l'on veut. Si vous vous demandez comment savoir si la méthode que vous utilisez ignore ou pas les `NaN`, le mieux est de regarder l'aide de cette méthode. Il existe pour un certain nombre de méthodes deux versions : une qui ignore les `NaN` et une autre qui les prend en compte ; on en reparlera.

+++

Une autre manière de construire une `DataFrame` est de partir d'un `array` de `numpy`, et de spécifier les index pour les lignes et les colonnes avec les arguments `index` et `columns` :

```{code-cell}
a = np.random.randint(1, 20, 9).reshape(3, 3)
p = pd.DataFrame(a, index=['a', 'b', 'c'], columns=['x', 'y', 'z'])
print(p)
```

### Importation et exportation de données

+++

En pratique, il est très fréquent que les données qu'on manipule soient stockées dans un fichier ou une base de données. Il existe en `pandas` de nombreux utilitaires pour importer et exporter des données et les convertir automatiquement en `DataFrame`. Vous pouvez importer ou exporter du CSV, JSON, HTML, Excel, HDF5, SQL, Python pickle, etc.

+++

À titre d'illustration écrivons la `DataFrame` `p` dans différents formats.

```{code-cell}
# écrivons notre DataFrame dans un fichier CSV
p.to_csv('my_data.csv')
!cat my_data.csv
```

```{code-cell}
# et dans un fichier JSON
p.to_json('my_data.json')
!cat my_data.json
```

```{code-cell}
# on peut maintenant recharger notre fichier
# la conversion en DataFrame est automatique
new_p = pd.read_json('my_data.json')
print(new_p)
```

Pour la gestion des autres formats, comme il s'agit de quelque chose de très spécifique et sans difficulté particulière, je vous renvoie simplement à la documentation :

<http://pandas.pydata.org/pandas-docs/stable/io.html>

+++

### Manipulation d'une `DataFrame`

```{code-cell}
# construisons maintenant une DataFrame jouet

# voici une liste de prénoms
names = ['alice', 'bob', 'marc', 'bill', 'sonia']

# créons trois Series qui formeront les trois colonnes
age = pd.Series([12, 13, 16, 11, 16], index=names)
height = pd.Series([130, 140, 176, 120, 165], index=names)
sex = pd.Series(list('fmmmf'), index=names)

# créons maintenant la DataFrame
p = pd.DataFrame({'age': age, 'height': height, 'sex': sex})
print(p)
```

```{code-cell}
# et chargeons le jeux de données sur les pourboires de seaborn
import seaborn as sns
tips = sns.load_dataset('tips')
```

`pandas` offre de nombreuses possibilités d'explorer les données. Attention, dans mes exemples je vais alterner entre le `DataFrame` `p` et le `DataFrame` `tips` suivant les besoins de l'explication.

```{code-cell}
# afficher les premières lignes
tips.head()
```

```{code-cell}
# et les dernière lignes
tips.tail()
```

```{code-cell}
# l'index des lignes
p.index
```

```{code-cell}
# et l'index des colonnes
p.columns
```

```{code-cell}
# et afficher uniquement les valeurs
p.values
```

```{code-cell}
:cell_style: center

# échanger lignes et colonnes
# cf. la transposition de matrices
p.T
```

Pour finir, il y a la méthodes `describe` qui permet d'obtenir des premières statistiques sur un `DataFrame`. `describe` permet de calculer des statistiques sur des type numériques, mais aussi sur des types chaînes de caractères.

```{code-cell}
# par défaut describe ne prend en compte que les colonnes numériques
p.describe()
```

```{code-cell}
# mais on peut le forcer à prendre en compte toutes les colonnes
p.describe(include='all')
```

### Requêtes sur une `DataFrame`

+++

On peut maintenant commencer à faire des requêtes sur les `DataFrames`. Les `DataFrame` supportent la notion de masque que l'on a vue pour les `ndarray` de `numpy` et pour les `Series`.

```{code-cell}
# p.loc prend soit un label de ligne
print(p.loc['sonia'])
```

```{code-cell}
# ou alors un label de ligne ET de colonne
print(p.loc['sonia', 'age'])
```

On peut mettre à la place d'une label :

- une liste de labels ;
- un slice sur les labels ;
- un masque (c'est-à-dire un tableau de booléens) ;
- un callable qui retourne une des trois premières possibilités.

Noter que l'on peut également utiliser la notation `.iloc[]` avec les mêmes règles, mais elle est moins utile.

Je recommande de toujours utiliser la notation `.loc[lignes, colonnes]` pour éviter toute ambiguïté. Nous verrons que les notations `.loc[lignes]` ou pire seulement `[label]` sont sources d'erreurs.

Regardons maintenant d'autres exemples plus sophistiqués :

```{code-cell}
:cell_style: split

# un masque sur les femmes
p.loc[:, 'sex'] == 'f'
```

```{code-cell}
:cell_style: split

# si bien que pour construire un tableau
# avec uniquement les femmes
p.loc[p.loc[:, 'sex'] == 'f', :]
```

```{code-cell}
# si on veut ne garder uniquement
# que les femmes de plus de 14 ans
p.loc[(p.loc[:, 'sex'] == 'f') & (p.loc[:, 'age'] > 14), :]
```

```{code-cell}
# quelle est la moyenne de 'total_bill' pour les femmes
addition_f = tips.loc[tips.loc[:, 'sex'] == 'Female', 'total_bill'].mean()
print(f"addition moyenne des femmes : {addition_f:.2f}")
```

```{code-cell}
# quelle est la note moyenne des hommes
addition_h = tips.loc[tips.loc[:, 'sex'] == 'Male', 'total_bill'].mean()
print(f"addition moyenne des hommes : {addition_h:.2f}")
```

```{code-cell}
# qui laisse le plus grand pourcentage de pourboire :
# les hommes ou les femmes ?

pourboire_f = tips.loc[tips.loc[:, 'sex'] == 'Female', 'tip'].mean()
pourboire_h = tips.loc[tips.loc[:, 'sex'] == 'Male', 'tip'].mean()

print(f"Les femmes laissent {pourboire_f/addition_f:.2%} de pourboire")
print(f"Les hommes laissent {pourboire_h/addition_h:.2%} de pourboire")
```

### Erreurs fréquentes et ambiguïtés sur les requêtes

+++

Nous avons vu une manière simple et non ambiguë de faire des requêtes sur les `DataFrame`. Nous allons voir qu'il existe d'autres manières qui ont pour seul avantage d'être plus concises, mais sources de nombreuses erreurs.

**Souvenez-vous, utilisez toujours la notation `.loc[lignes, colonnes]` sinon, soyez sûr de savoir ce qui est réellement calculé**.

```{code-cell}
# commençons par la notation la plus classique
p['sex']  # prend forcément un label de colonne
```

```{code-cell}
# mais par contre, si on passe un slice, c'est forcément des lignes,
# assez perturbant et source de confusion.
p['alice': 'marc']
```

```{code-cell}
# on peut même directement accéder à une colonne par son nom
p.age
```

Mais c'est **fortement déconseillé** parce que si un attribut de même nom existe sur une `DataFrame`, alors la priorité est donnée à l'attribut, et non à la colonne :

```{code-cell}
# ajoutons une colonne qui a pour nom une méthode qui existe sur
# les DataFrame
p['mean'] = 1
print(p)
```

```{code-cell}
:cell_style: split

# je peux bien accéder
# à la colonne sex
p.sex
```

```{code-cell}
:cell_style: split

# mais pas à la colonne mean
p.mean
```

```{code-cell}
# à nouveau, la seule méthode non ambiguë est d'utiliser .loc
p.loc[:, 'mean']
```

```{code-cell}
# supprimons maintenant la colonne mean *en place* (par défaut,
# drop retourne une nouvelle DataFrame)
p.drop(columns='mean', inplace=True)
print(p)
```

Pour aller plus loin, vous pouvez lire la documentation officielle :

<http://pandas.pydata.org/pandas-docs/stable/indexing.html>

+++

### *Universal functions* et `pandas`

+++

Ça n'est pas une surprise, les `Series` et `DataFrame` de `pandas` supportent les `ufunc` de `numpy`. Mais il y a une subtilité. Il est parfaitement légitime et correct d'appliquer une `ufunc` de `numpy` sur les éléments d'une `DataFrame` :

```{code-cell}
d = pd.DataFrame(np.random.randint(
    1, 10, 9).reshape(3, 3), columns=list('abc'))
print(d)
```

```{code-cell}
np.log(d)
```

Nous remarquons que comme on s'y attend, la `ufunc` a été appliquée à chaque élément de la `DataFrame` et que les labels des lignes et colonnes ont été préservés.

+++

Par contre, si l'on a besoin d'alignement de labels, c'est le cas avec toutes les opérations qui s'appliquent sur deux objets comme une addition, alors les `ufunc` de `numpy` ne **vont pas faire** ce à quoi on s'attend. Elles vont faire les opérations sur les tableaux `numpy` sans prendre en compte les labels.

Pour avoir un alignement des labels, il faut utiliser les `ufunc` de `pandas`.

```{code-cell}
:cell_style: split

# prenons deux Series
s1 = pd.Series([10, 20, 30],
               index=list('abc'))
print(s1)
```

```{code-cell}
:cell_style: split

#
s2 = pd.Series([12, 22, 32],
               index=list('acd'))
print(s2)
```

```{code-cell}
:cell_style: split

# la ufunc numpy fait la somme
# des arrays sans prendre en compte
# les labels, donc sans alignement
np.add(s1, s2)
```

```{code-cell}
:cell_style: split

# la ufunc pandas va faire
# un alignement des labels
# cet appel est équivalent à s1 + s2
s1.add(s2)
```

```{code-cell}
# comme on l'a vu sur le complément précédent, les valeurs absentes sont
# remplacées par NaN, mais on peut changer ce comportement lors de
# l'appel de .add
s1.add(s2, fill_value=0)
```

```{code-cell}
# regardons un autre exemple sur des DataFrame
# on affiche tout ça dans les cellules suivantes
names = ['alice', 'bob', 'charle']

bananas = pd.Series([10, 3, 9], index=names)
oranges = pd.Series([3, 11, 6], index=names)
fruits_jan = pd.DataFrame({'bananas': bananas, 'orange': oranges})

bananas = pd.Series([6, 1], index=names[:-1])
apples = pd.Series([8, 5], index=names[1:])
fruits_feb = pd.DataFrame({'bananas': bananas, 'apples': apples})
```

```{code-cell}
:cell_style: split

# ce qui donne
fruits_jan
```

```{code-cell}
:cell_style: split

# et
fruits_feb
```

```{code-cell}
# regardons maintenant la somme des fruits mangés
eaten_fruits = fruits_jan + fruits_feb
print(eaten_fruits)
```

```{code-cell}
# On a bien un alignement des labels, mais il y a beaucoup de valeurs
# manquantes. Corrigeons cela on remplaçant les valeurs manquantes par 0
eaten_fruits = fruits_jan.add(fruits_feb, fill_value=0)
print(eaten_fruits)
```

Notons que lorsqu'une valeur est absente dans toutes les `DataFrame`, `NaN` est conservé.

+++

Un dernière subtilité à connaître lors de l'alignement des labels intervient lorsque vous faites une opération sur une `DataFrame` et une `Series`. `pandas` va considérer la `Series` comme une ligne et va la broadcaster sur les autres lignes. Par conséquent, l'index de la `Series` va être considéré comme des colonnes et aligné avec les colonnes de la `DataFrame`.

```{code-cell}
dataframe = pd.DataFrame(
    np.random.randint(1, 10, size=(3, 3)),
    columns=list('abc'), index=list('xyz'))
dataframe
```

```{code-cell}
:cell_style: split

series_row = pd.Series(
    [100, 200, 300],
    index=list('abc'))
series_row
```

```{code-cell}
:cell_style: split

series_col = pd.Series(
    [400, 500, 600],
    index=list('xyz'))
series_col
```

```{code-cell}
# la Series est considérée comme une ligne et son index
# s'aligne sur les colonnes de la DataFrame
# la Series va être broadcastée
# sur les autres lignes de la DataFrame

dataframe + series_row
```

```{code-cell}
# du coup si les labels ne correspondent pas,
# le résultat sera le suivant

dataframe + series_col
```

```{code-cell}
# on peut dans ce cas, changer le comportement par défaut en forçant
# l'alignement de la Series suivant un autre axe avec l'argument axis

dataframe.add(series_col, axis=0)
```

Ici, `axis=0` signifie que la `Series` est considérée comme une colonne est qu'elle va être broadcastée sur les autres colonnes (le long de l'axe de ligne).

+++

### Opérations sur les chaînes de caractères

+++

Nous allons maintenant parler de la vectorisation des opérations sur les chaînes de caractères. Il y a plusieurs choses importantes à savoir :

* les méthodes sur les chaînes de caractères ne sont disponibles que pour les `Series` et les `Index`, mais pas pour les `DataFrame` ;
* ces méthodes ignorent les `NaN` et remplacent les valeurs qui ne sont pas des chaînes de caractères par `NaN` ;
* ces méthodes retournent une copie de l'objet (`Series` ou `Index`), il n'y a pas de modification en place ;
* la plupart des méthodes Python sur le type `str` existe sous forme vectorisée ;
* on accède à ces méthodes avec la syntaxe :
  * `Series.str.<vectorized method name>`
  * `Index.str.<vectorized method name>`

Regardons quelques exemples :

```{code-cell}
# Créons une Series avec des noms ayant une capitalisation inconsistante
# et une mauvaise gestion des espaces
names = ['alice ', '  bOB', 'Marc', 'bill', 3, ' JULIE ', np.NaN]
age = pd.Series(names)
```

```{code-cell}
# nettoyons maintenant ces données

# on met en minuscule
a = age.str.lower()

# on enlève les espaces
a = a.str.strip()
a
```

```{code-cell}
# comme les méthodes vectorisées retournent un objet de même type, on
# peut les chaîner comme ceci

[x for x in age.str.lower().str.strip()]
```

+++ {"cell_style": "split"}

On peut également utiliser l'indexation des `str` de manière vectorisée :

```{code-cell}
:cell_style: split

print(a)
```

```{code-cell}
:cell_style: split

print(a.str[-1])
```

Pour aller plus loin vous pouvez lire la documentation officielle :

<http://pandas.pydata.org/pandas-docs/stable/text.html>

+++

### Gestion des valeurs manquantes

+++

Nous avons vu que des opérations sur les `DataFrame` pouvaient générer des valeurs `NaN` lors de l'alignement. Il est également possible d'avoir de telles valeurs _manquantes_ dans votre jeu de données original. `pandas` offre plusieurs possibilités pour gérer correctement ces valeurs manquantes.

+++

Avant de voir ces différentes possibilités, définissons cette notion de valeur manquante.

Une valeur manquante peut-être représentée avec `pandas` soit par `np.NaN` soit par l'objet Python `None`.

- `np.NaN` est un objet de type `float`, par conséquent il ne peut apparaître que dans un array de `float` ou un array d'`object`. Notons que `np.NaN` apparaît avec `pandas` comme simplement `NaN` et que dans la suite on utilise de manière indifférente les deux notations, par contre, dans du code, il faut obligatoirement utiliser `np.NaN` ;
  - si on ajoute un `NaN` dans un array d'entier, ils seront convertis en `float64` ;
  - si on ajoute un `NaN` dans un array de booléens, ils seront convertis en `object` ;
- `NaN` est contaminant, toute opération avec un `NaN` a pour résultat `NaN` ;
- lorsque l'on utilise `None`, il est automatiquement converti en `NaN` lorsque le type de l'array est numérique.

Illustrons ces propriétés :

```{code-cell}
# une Series d'entiers
s = pd.Series([1, 2])
s
```

```{code-cell}
# on insère un NaN, la Series est alors convertie en float64
s[0] = np.NaN
s
```

```{code-cell}
# on réinitialise
s = pd.Series([1, 2])
s
```

```{code-cell}
# et on insère None
s[0] = None

# Le résultat est le même
# None est converti en NaN
s
```

Regardons maintenant, les méthodes de `pandas` pour gérer les valeurs manquantes (donc `NaN` ou `None`) :

- `isna()` retourne un masque mettant à `True` les valeurs manquantes (il y a un alias `isnull()`) ;
- `notna()` retourne un masque mettant à `False` les valeurs manquantes (il y a un alias `notnull()`) ;
- `dropna()` retourne un nouvel objet sans les valeurs manquantes ;
- `fillna()` retourne un nouvel objet avec les valeurs manquantes remplacées.

On remarque que l'ajout d'alias pour les méthodes est de nouveau une source de confusion avec laquelle il faut vivre.

On remarque également qu'alors que `isnull()` et `notnull()` sont des méthodes simples, `dropna()` et `fillna()` impliquent l'utilisation de stratégies. Regardons cela :

```{code-cell}
# créons une DataFrame avec quelques valeurs manquantes
names = ['alice', 'bob', 'charles']
bananas = pd.Series([6, 1], index=names[:-1])
apples = pd.Series([8, 5], index=names[1:])
fruits_feb = pd.DataFrame({'bananas': bananas, 'apples': apples})
print(fruits_feb)
```

```{code-cell}
fruits_feb.isna()
```

```{code-cell}
fruits_feb.notna()
```

Par défaut, `dropna()` va enlever toutes les lignes qui contiennent au moins une valeur manquante. Mais on peut changer ce comportement avec des arguments :

```{code-cell}
p = pd.DataFrame([[1, 2, np.NaN], [3, np.NaN, np.NaN], [7, 5, np.NaN]])
print(p)
```

```{code-cell}
# comportement par défaut, j'enlève toutes les lignes avec au moins
# une valeur manquante; il ne reste rien !
p.dropna()
```

```{code-cell}
# maintenant, je fais l'opération par colonne
p.dropna(axis=1)
```

```{code-cell}
# je fais l'opération par colonne si toute la colonne est manquante
p.dropna(axis=1, how='all')
```

```{code-cell}
# je fais l'opération par ligne si au moins 2 valeurs sont manquantes
p.dropna(thresh=2)
```

Par défaut, `fillna()` remplace les valeurs manquantes avec un argument pas défaut. Mais on peut ici aussi changer ce comportement. Regardons cela :

```{code-cell}
print(p)
```

```{code-cell}
# je remplace les valeurs manquantes par -1
p.fillna(-1)
```

```{code-cell}
# je remplace les valeurs manquantes avec la valeur suivante sur la colonne
# bfill est pour back fill, c'est-à-dire remplace en arrière à partir des
# valeurs existantes
p.fillna(method='bfill')
```

```{code-cell}
# je remplace les valeurs manquantes avec la valeur précédente sur la ligne
# ffill est pour forward fill, remplace en avant à partir des valeurs
# existantes
p.fillna(method='ffill', axis=1)
```

Regardez l'aide de ces méthodes pour aller plus loin.

```{code-cell}
p.dropna?
```

```{code-cell}
p.fillna?
```

### Analyse statistique des données

+++

Nous n'avons pas le temps de couvrir les possibilités d'analyse statistique de la suite data science de Python. `pandas` offre quelques possibilités basiques avec des calculs de moyennes, d'écarts types ou de covariances que l'on peut éventuellement appliquer par fenêtres à un jeux de données. Pour avoir plus de détails dessus vous pouvez consulter cette documentation :

<http://pandas.pydata.org/pandas-docs/stable/computation.html>

Dans la suite data science de Python, il a aussi des modules spécialisés dans l'analyse statistique comme :

- [StatsModels](http://www.statsmodels.org/stable/index.html)
- [ScikitLearn](http://scikit-learn.org/stable/)

ou des outils de calculs scientifiques plus génériques comme [SciPy](https://www.scipy.org/).

De nouveau, il s'agit d'outils appliqués à des domaines spécifiques et ils se basent tous sur le couple `numpy`/`pandas`.

+++

## Complément - niveau avancé

+++

### Les MultiIndex

+++

`pandas` avait historiquement d'autres structures de données en plus des `Series` et des `DataFrame` permettant d'exprimer des dimensionnalités supérieures à 2, comme par exemple les `Panel`. Mais pour des raisons de maintenance du code et d'optimisation, les développeurs ont décidé de ne garder que les `Series` et les `DataFrame`. Alors, comment exprimer des données avec plus de deux dimensions ?

On utilise pour cela des `MultiIndex`. Un `MultiIndex` est un index qui peut être utilisé partout où l'on utilise un index (dans une `Series`, ou comme ligne ou colonne d'une `DataFrame`) et qui a pour caractéristique d'avoir plusieurs niveaux.

Comme tous types d'index, et parce qu'un `MultiIndex` est une sous classe d'`Index`, `pandas` va correctement aligner les `Series` et les `DataFrame` avec des `MultiIndex`.

Regardons tout de suite un exemple :

```{code-cell}
# construisons une DataFrame jouet

# voici une liste de prénoms
names = ['alice', 'bob', 'sonia']

# créons trois Series qui formeront trois colonnes
age = pd.Series([12, 13, 16], index=names)
height = pd.Series([130, 140, 165], index=names)
sex = pd.Series(list('fmf'), index=names)

# créons maintenant la DataFrame
p = pd.DataFrame({'age': age, 'height': height, 'sex': sex})
print(p)
```

```{code-cell}
# unstack, en première approximation, permet de passer d'une DataFrame à
# une Series avec un MultiIndex
s = p.unstack()
print(s)
```

```{code-cell}
# et voici donc l'index de cette Series
s.index
```

Il existe évidemment des moyens de créer directement un `MultiIndex` et ensuite de le définir comme index d'une `Series` ou comme index de ligne ou colonne d'une `DataFrame` :

```{code-cell}
# on peut créer un MultiIndex à partir d'une liste de liste
names = ['alice', 'alice', 'alice', 'bob', 'bob', 'bob']
age = [2014, 2015, 2016, 2014, 2015, 2016]
s_list = pd.Series([40, 42, 45, 38, 40, 40], index=[names, age])
print(s_list)
```

```{code-cell}
# ou à partir d'un dictionnaire de tuples
s_tuple = pd.Series({('alice', 2014): 40,
                     ('alice', 2015): 42,
                     ('alice', 2016): 45,
                     ('bob', 2014): 38,
                     ('bob', 2015): 40,
                     ('bob', 2016): 40})

print(s_tuple)
```

```{code-cell}
# ou avec la méthode from_product()
name = ['alice', 'bob']
year = [2014, 2015, 2016]
i = pd.MultiIndex.from_product([name, year])
s = pd.Series([40, 42, 45, 38, 40, 40], index=i)
print(s)
```

On peut même nommer les niveaux d'un `MultiIndex`.

```{code-cell}
name = ['alice', 'bob']
year = [2014, 2015, 2016]
i = pd.MultiIndex.from_product([name, year], names=['name', 'year'])
s = pd.Series([40, 42, 45, 38, 40, 40], index=i)
print(s)
```

```{code-cell}
# on peut changer le nom des niveaux du MultiIndex
s.index.names = ['NAMES', 'YEARS']
print(s)
```

Créons maintenant une `DataFrame` jouet avec des `MultiIndex` pour étudier comment accéder aux éléments de la `DataFrame`.

```{code-cell}
index = pd.MultiIndex.from_product([[2013, 2014],
                                    [1, 2, 3]],
                                   names=['year',
                                          'visit'])

columns = pd.MultiIndex.from_product([['Bob', 'Sue'],
                                      ['avant', 'arrière']],
                                     names=['client',
                                            'pression'])

# on crée des pressions de pneus factices
data = 2 + np.random.rand(6, 4)

# on crée la DataFrame
mecanics_data = pd.DataFrame(data, index=index, columns=columns)
print(mecanics_data)
```

Il y a plusieurs manières d'accéder aux éléments, mais une seule que l'on recommande :

**utilisez la notation `.loc[ligne, colonne], .iloc[ligne, colonne]`**.

```{code-cell}
# pression en 2013 pour Bob
mecanics_data.loc[2013, 'Bob']
```

```{code-cell}
# pour accéder aux sous niveaux du MultiIndex, on utilise des tuples
mecanics_data.loc[(2013, 2), ('Bob', 'avant')]
```

Le slice sur le `MultiIndex` est un peu délicat. On peut utiliser la notation `:` si on veut slicer sur tous les éléments d'un `MultiIndex`, sans prendre en compte un niveau. Si on spécifie les niveaux, il faut utiliser un objet `slice` ou `pd.IndexSlice` :

```{code-cell}
# slice(None) signifie tous les éléments du niveau
print(mecanics_data.loc[slice((2013, 2), (2014, 1)), ('Sue', slice(None))])
```

```{code-cell}
# on peut utiliser la notation : si on ne distingue par les niveaux
print(mecanics_data.loc[(slice(None), slice(1, 2)), :])
```

```{code-cell}
# on peut aussi utiliser pd.IndexSlice pour slicer avec une notation
# un peu plus concise
idx = pd.IndexSlice
print(mecanics_data.loc[idx[:, 1:2], idx['Sue', :]])
```

Pour aller plus loin, regardez la documentation des `MultiIndex` :

<http://pandas.pydata.org/pandas-docs/stable/advanced.html>

+++

## Conclusion

+++

La `DataFrame` est la structure de données la plus souple et la plus puissante de `pandas`. Nous avons vu comment créer des `DataFrame` et comment accéder aux éléments. Nous verrons dans le prochain complément les techniques permettant de faire des opérations complexes (et proches dans l'esprit de ce que l'on peut faire avec une base de données) comme les opérations de `merge` ou de `groupby`.
