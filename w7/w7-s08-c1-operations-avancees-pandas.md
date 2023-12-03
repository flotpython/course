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
  title: "Op\xE9rations avanc\xE9es"
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Opération avancées en `pandas`

+++

## Complément - niveau intermédiaire

+++

### Introduction

+++

`pandas` supporte des opérations de manipulation des `Series` et `DataFrame` qui sont similaires dans l'esprit à ce que l'on peut faire avec une base de données et le langage SQL, mais de manière plus intuitive et expressive et beaucoup plus efficacement puisque les opérations se déroulent toutes en mémoire.

Vous pouvez concaténer (`concat`) des `DataFrame`, faire des jointures (`merge`), faire des regroupements (`groupby`) ou réorganiser les index (`pivot`).

Nous allons dans la suite développer ces différentes techniques.

```{code-cell} ipython3
import numpy as np
import pandas as pd
```

### Concaténations avec `concat`

+++

`concat` est utilisé pour concaténer des `Series` ou des `DataFrame`. Regardons un exemple.

```{code-cell} ipython3
s1 = pd.Series([30, 35], index=['alice', 'bob'])
s2 = pd.Series([32, 22, 29], index=['bill', 'alice', 'jo'])
```

```{code-cell} ipython3
:cell_style: split

s1
```

```{code-cell} ipython3
:cell_style: split

s2
```

```{code-cell} ipython3
pd.concat([s1, s2])
```

On remarque, cependant, que par défaut il n'y a pas de contrôle sur les labels d'index dupliqués. On peut corriger cela avec l'argument `verify_integrity`, qui va produire une exception s'il y a des labels d'index communs. Évidemment, cela a un coût de calcul supplémentaire, ça n'est donc à utiliser que si c'est nécessaire.

```{code-cell} ipython3
try:
    pd.concat([s1, s2], verify_integrity=True)
except ValueError as e:
    print(f"erreur de concaténation:\n{e}")
```

```{code-cell} ipython3
# créons deux Series avec les index sans recouvrement
s1 = pd.Series(range(1000), index=[chr(x) for x in range(1000)])
s2 = pd.Series(range(1000), index=[chr(x+2000) for x in range(1000)])
```

```{code-cell} ipython3
# temps de concaténation avec vérification des recouvrements
%timeit pd.concat([s1, s2], verify_integrity=True)
```

```{code-cell} ipython3
# temps de concaténation sans vérification des recouvrements
%timeit pd.concat([s1, s2])
```

Par défaut, `concat` concatène les lignes, c'est-à-dire que `s2` sera sous `s1`, mais on peut changer ce comportement en utilisant l'argument `axis` :

```{code-cell} ipython3
p1 = pd.DataFrame(np.random.randint(1, 10, size=(2,2)),
                  columns=list('ab'), index=list('xy'))
p2 = pd.DataFrame(np.random.randint(1, 10, size=(2,2)),
                  columns=list('ab'), index=list('zt'))
```

```{code-cell} ipython3
:cell_style: split

p1
```

```{code-cell} ipython3
:cell_style: split

p2
```

```{code-cell} ipython3
# équivalent à pd.concat([p1, p2], axis=0)
# concaténation des lignes
pd.concat([p1, p2])
```

```{code-cell} ipython3
p1 = pd.DataFrame(np.random.randint(1, 10, size=(2,2)),
                  columns=list('ab'), index=list('xy'))
p2 = pd.DataFrame(np.random.randint(1, 10, size=(2,2)),
                  columns=list('cd'), index=list('xy'))
```

```{code-cell} ipython3
:cell_style: split

p1
```

```{code-cell} ipython3
:cell_style: split

p2
```

```{code-cell} ipython3
# concaténation des colonnes
pd.concat([p1, p2], axis=1)
```

Regardons maintenant ce cas :

```{code-cell} ipython3
pd.concat([p1, p2])
```

Vous remarquez que lors de la concaténation, on prend l'union des tous les labels des index de `p1` et `p2`, il y a donc des valeurs absentes qui sont mises à `NaN`. On peut contrôler ce comportement de plusieurs manières comme nous allons le voir ci-dessous.

+++

Par défaut (ce que l'on a fait ci-dessus), join utilise la stratégie dite `outer`, c'est-à-dire qu'on prend l'union des labels.

```{code-cell} ipython3
# on concatène les lignes, l'argument join décide quels labels on garde
# sur l'autre axe  (ici sur les colonnes).

# si on spécifie 'inner' on prend l'intersection des labels
# du coup il ne reste rien ..
pd.concat([p1, p2], join='inner')
```

Avec `reindex`, on peut spécifier les labels qu'on veut garder dans l'index des lignes (`axis=0`, c'est la valeur par défaut) ou des colonnes (`axis=1`) :

```{code-cell} ipython3
# on peut passer à reindex une liste de labels...
pd.concat([p1, p2], axis=1).reindex(['x'])
```

```{code-cell} ipython3
# ou un objet Index 
# Pour les colonnes je spécifie un reindex avec axis=1
pd.concat([p1, p2], axis=1).reindex(p2.columns, axis=1)
```

```{code-cell} ipython3
pd.concat([p1, p2], axis=1).reindex(['a', 'b'], axis=1)
```

Notons que les `Series` et `DataFrame` ont une méthode `append` qui est un raccourci vers `concat`, mais avec moins d'options.

Pour aller plus loin, voici la documentation officielle :

<http://pandas.pydata.org/pandas-docs/stable/merging.html#concatenating-objects>

+++

### Jointures avec `merge`

+++

`merge` est dans l'esprit similaire au `JOIN` en SQL. L'idée est de combiner deux `DataFrame` en fonction d'un critère d'égalité sur des colonnes. Regardons un exemple :

```{code-cell} ipython3
df1 = pd.DataFrame({'employee': ['Bob', 'Lisa', 'Sue'],
                    'group': ['Accounting', 'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Sue'],
                    'hire_date': [2004, 2008, 2014]})
```

```{code-cell} ipython3
:cell_style: split

df1
```

```{code-cell} ipython3
:cell_style: split

df2
```

On souhaite ici combiner `df1` et `df2` de manière à ce que les lignes contenant le même _employee_ soient alignées. Notre critère de merge est donc l'égalité des labels sur la colonne _employee_.

```{code-cell} ipython3
pd.merge(df1, df2)
```

Par défaut, `merge` fait un *inner join* (ou jointure interne) en utilisant comme critère de jointure les colonnes de même nom (ici `employee`). *inner join* veut dire que pour joindre deux lignes il faut que le même `employee` apparaisse dans les deux `DataFrame`.

+++

Il existe trois type de merges :

- one-to-one, c'est celui que l'on vient de voir. C'est le merge lorqu'il n'y a pas de labels dupliqués dans les colonnes utilisées comme critère de merge ;

- many-to-one, c'est le merge lorsque l'une des deux colonnes contient des labels dupliqués, dans ce cas, on applique la stratégie one-to-one pour chaque label dupliqué, donc les entrées dupliquées sont préservées ;

- many-to-many, c'est la stratégie lorsqu'il y a des entrées dupliquées dans les deux colonnes. Dans ce cas, on fait un produit cartésien des lignes.

D'une manière générale, gardez en tête que `pandas` fait essentiellement ce à quoi on s'attend. Regardons cela sur des exemples :

```{code-cell} ipython3
df1 = pd.DataFrame({'patient': ['Bob', 'Lisa', 'Sue'],
                    'repas': ['SS', 'SS', 'SSR']})
df2 = pd.DataFrame({'repas': ['SS', 'SSR'],
                    'explication': ['sans sel', 'sans sucre']})
```

```{code-cell} ipython3
:cell_style: split

df1
```

```{code-cell} ipython3
:cell_style: split

df2
```

```{code-cell} ipython3
# la colonne commune pour le merge est 'repas' et dans une des colonnes
# (sur df1), il y a des labels dupliqués, on applique la stratégie many-to-one
pd.merge(df1, df2)
```

```{code-cell} ipython3
df1 = pd.DataFrame({'patient': ['Bob', 'Lisa', 'Sue'],
                    'repas': ['SS', 'SS', 'SSR']})
df2 = pd.DataFrame({'repas': ['SS', 'SS', 'SSR'],
                    'explication': ['sans sel', 'légumes', 'sans sucre']})
```

```{code-cell} ipython3
:cell_style: split

df1
```

```{code-cell} ipython3
:cell_style: split

df2
```

```{code-cell} ipython3
# la colonne commune pour le merge est 'repas' et dans les deux colonnes
# il y a des labels dupliqués, on applique la stratégie many-to-many
pd.merge(df1,df2)
```

Dans un merge, on peut contrôler les colonnes à utiliser comme critère de merge. Regardons ces différents cas sur des exemples :

```{code-cell} ipython3
df1 = pd.DataFrame({'employee': ['Bob', 'Lisa', 'Sue'],
                    'group': ['Accounting', 'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Sue'],
                    'hire_date': [2004, 2008, 2014]})
```

```{code-cell} ipython3
:cell_style: split

df1
```

```{code-cell} ipython3
:cell_style: split

df2
```

```{code-cell} ipython3
# on décide d'utiliser la colonne 'employee' comme critère de merge
pd.merge(df1, df2, on='employee')
```

```{code-cell} ipython3
df1 = pd.DataFrame({'employee': ['Bob', 'Lisa', 'Sue'],
                    'group': ['Accounting', 'Engineering', 'HR']})
df2 = pd.DataFrame({'name': ['Lisa', 'Bob', 'Sue'],
                    'hire_date': [2004, 2008, 2014]})
```

```{code-cell} ipython3
:cell_style: split

df1
```

```{code-cell} ipython3
:cell_style: split

df2
```

```{code-cell} ipython3
# mais on peut également définir un nom de colonne différent
# à gauche et à droite
m = pd.merge(df1,df2, left_on='employee', right_on='name')
m
```

```{code-cell} ipython3
# dans ce cas, comme on garde les colonnes utilisées comme critère dans
# le résultat du merge, on peut effacer la colonne inutile ainsi
m.drop('name', axis=1)
```

`merge` permet également de contrôler la stratégie à appliquer lorsqu'il y a des valeurs dans une colonne utilisée comme critère de merge qui sont absentes dans l'autre colonne. C'est ce que l'on appelle jointure à gauche, jointure à droite, jointure interne (comportement par défaut) et jointure externe. Pour ceux qui ne sont pas familiers avec ces notions, regardons des exemples :

```{code-cell} ipython3
df1 = pd.DataFrame({'name': ['Bob', 'Lisa', 'Sue'],
                    'pulse': [70, 63, 81]})
df2 = pd.DataFrame({'name': ['Eric', 'Bob', 'Marc'],
                    'weight': [60, 100, 70]})
```

```{code-cell} ipython3
:cell_style: split

df1
```

```{code-cell} ipython3
:cell_style: split

df2
```

```{code-cell} ipython3
# la colonne 'name' est le critère de merge dans les deux DataFrame.
# Seul Bob existe dans les deux colonnes. Dans un inner join
# (le cas par défaut) on ne garde que les lignes pour lesquelles il y a une
# même valeur présente à gauche et à droite
pd.merge(df1, df2) # équivalent à pd.merge(df1, df2, how='inner')
```

```{code-cell} ipython3
# le outer join va au contraire faire une union des lignes et compléter ce
# qui manque avec NaN
pd.merge(df1, df2, how='outer')
```

```{code-cell} ipython3
# le left join ne garde que les valeurs de la colonne de gauche
pd.merge(df1, df2, how='left')
```

```{code-cell} ipython3
# et le right join ne garde que les valeurs de la colonne de droite
pd.merge(df1, df2, how='right')
```

Pour aller plus loin, vous pouvez lire la documentation. Vous verrez notamment que vous pouvez merger sur les index (au lieu des colonnes) ou le cas où vous avez des colonnes de même nom qui ne font pas partie du critère de merge :

<http://pandas.pydata.org/pandas-docs/stable/merging.html#database-style-dataframe-joining-merging>

+++

### Regroupement avec `groupby`

+++

Regardons maintenant cette notion de groupement. Il s'agit d'une notion très puissante avec de nombreuses options que nous ne couvrirons que partiellement.
La logique derrière `groupby` est de créer des groupes dans une `DataFrame` en fonction des valeurs d'une (ou plusieurs) colonne(s), toutes les lignes contenant la même valeur sont dans le même groupe. On peut ensuite appliquer à chaque groupe des opérations qui sont :

- soit des calculs sur chaque groupe ;
- soit un filtre sur chaque groupe qui peut garder ou supprimer un groupe ;
- soit une transformation qui va modifier tout le groupe (par exemple, pour centrer les valeurs sur la moyenne du groupe).

Regardons quelques exemples :

```{code-cell} ipython3
d = pd.DataFrame({'key': list('ABCABC'), 'val': range(6)})
d
```

```{code-cell} ipython3
# utilisons comme colonne de groupement 'key'
g = d.groupby('key')
g
```

`groupby` produit un nouvel objet, mais ne fait aucun calcul. Les calculs seront effectués lors de l'appel d'une fonction sur ce nouvel objet. Par exemple, calculons la somme pour chaque groupe.

```{code-cell} ipython3
g.sum()
```

`groupby` peut utiliser comme critère de groupement une colonne, une liste de colonnes, ou un index (c'est notamment utile pour les `Series`).

Une particularité de `groupby` est que le critère de groupement devient un index dans le nouvel objet généré. L'avantage est que l'on a maintenant un accès optimisé sur ce critère, mais l'inconvénient est que sur certaines opérations qui détruisent l'index on peut perdre ce critère. On peut contrôler ce comportement avec `as_index`.

```{code-cell} ipython3
g = d.groupby('key', as_index=False)
g.sum()
```

L'objet produit par `groupby` pemet de manipuler les groupes, regardons cela :

```{code-cell} ipython3
d = pd.DataFrame({'key': list('ABCABC'),
                  'val1': range(6),
                  'val2' : range(100, 106)})
d
```

```{code-cell} ipython3
g = d.groupby('key')

# g.groups donne accès au dictionnaire des groupes,
# les clefs sont le nom du groupe
# et les valeurs les index des lignes
# appartenant au groupe
g.groups
```

```{code-cell} ipython3
# pour accéder directement au groupe, on peut utiliser get_group
g.get_group('A')
```

```{code-cell} ipython3
# on peut également filtrer un groupe par colonne
# lors d'une opération
g.sum()['val2']
```

```{code-cell} ipython3
# ou directement sur l'objet produit par groupby
g['val2'].sum()
```

On peut également itérer sur les groupes avec un boucle `for` classique :

```{code-cell} ipython3
import seaborn as sns
# on charge le fichier de données des pourboires
tips = sns.load_dataset('tips')

# pour rappel
tips.head()
```

```{code-cell} ipython3
# on groupe le DataFrame par jours
g = tips.groupby('day')

# on calcule la moyenne du pourboire par jour
for (group, index) in g:
    print(f"On {group} the mean tip is {index['tip'].mean():.3}")
```

L'objet produit par `groupby` supporte ce que l'on appelle le _dispatch_ de méthodes. Si une méthode n'est pas directement définie sur l'objet produit par `groupby`, elle est appelée sur chaque groupe (il faut donc qu'elle soit définie sur les `DataFrame` ou les `Series`). Regardons cela :

```{code-cell} ipython3
# on groupe par jour et on extrait uniquement la colonne 'total_bill'
# pour chaque groupe
g = tips.groupby('day')['total_bill']

# on demande à pandas d'afficher les float avec seulement deux chiffres
# après la virgule
pd.set_option('display.float_format', '{:.2f}'.format)

# on appelle describe() sur g, mais elle n'est pas définie sur cet objet,
# elle va donc être appelée (dispatch) sur chaque groupe
g.describe()
```

```{code-cell} ipython3
# Mais, il y a tout de même un grand nombre de méthodes
# définies directement sur l'objet produit par le groupby

methods = [x for x in dir(g) if not x.startswith('_')]
f"Le type {type(g).__name__} expose {len(methods)} méthodes."
```

```{code-cell} ipython3
# profitons de la mise en page des dataframes
# pour afficher ces méthodes sur plusieurs colonnes
# on fait un peu de gymnastique
# il y a d'ailleurs sûrement plus simple..
columns = 7
nb_methods = len(methods)
nb_pad = (columns - nb_methods % columns) % columns

array = np.array(methods + nb_pad * ['']).reshape((columns, -1))
```

```{code-cell} ipython3
pd.DataFrame(data=array.transpose())
```

Nous allons regarder la méthode `aggregate` (dont l'alias est `agg`). Cette méthode permet d'appliquer une fonction (ou liste de fonctions) à chaque groupe avec la possibilité d'appliquer une fonction à une colonne spécifique du groupe.

Une subtilité de `aggregate` est que l'on peut passer soit un objet fonction, soit un nom de fonction sous forme d'une `str`. Pour que l'utilisation du nom de la fonction marche, il faut que la fonction soit définie sur l'objet produit par le `groupby` ou qu'elle soit définie sur les groupes (donc avec dispatching).

```{code-cell} ipython3
# calculons la moyenne et la variance pour chaque groupe
# et chaque colonne numérique
numeric_columns = tips.describe().columns

tips.groupby('day')[numeric_columns].agg(['mean', 'std'])
```

```{code-cell} ipython3
# de manière équivalente avec les objets fonctions
tips.groupby('day')[numeric_columns].agg([np.mean, np.std])
```

```{code-cell} ipython3
# en appliquant une fonction différente pour chaque colonne,
# on passe alors un dictionnaire qui a pour clef le nom de la
# colonne et pour valeur la fonction à appliquer à cette colonne
tips.groupby('day').agg({'tip': np.mean, 'total_bill': np.std})
```

La méthode `filter` a pour but de filtrer les groupes en fonction d'un critère. Mais attention, `filter` retourne **un sous ensemble des données originales** dans lesquelles les éléments appartenant aux groupes filtrés ont été enlevés.

```{code-cell} ipython3
d = pd.DataFrame({'key': list('ABCABC'), 
                  'val1': range(6),
                  'val2' : range(100, 106)})
d
```

```{code-cell} ipython3
# regardons la somme par groupe
d.groupby('key').sum()
```

```{code-cell} ipython3
# maintenant gardons dans les données originales toutes les lignes
# pour lesquelles la somme de leur groupe est supérieure à 3
# (ici les groupes B et C)
d.groupby('key').filter(lambda x: x['val1'].sum() > 3)
```

La méthode `transform` a pour but de retourner **un sous ensemble des données originales** dans lesquelles une fonction a été appliquée par groupe. Un usage classique est de centrer des valeurs par groupe, ou de remplacer les `NaN` d'un groupe par la valeur moyenne du groupe.

Attention, `transform` ne doit pas faire de modifications en place, sinon le résultat peut être faux. Faites donc bien attention de ne pas appliquer des fonctions qui font des modications en place.

```{code-cell} ipython3
r = np.random.normal(0.5, 2, 4)
d = pd.DataFrame({'key': list('ab'*2), 'data': r,'data2': r*2})
d
```

```{code-cell} ipython3
# je groupe sur la colonne 'key'
g = d.groupby('key')
```

```{code-cell} ipython3
# maintenant je centre chaque groupe par rapport à sa moyenne
g.transform(lambda x: x - x.mean())
```

Notez que la colonne `key` a disparu, ce comportement est expliqué ici :

<http://pandas.pydata.org/pandas-docs/stable/groupby.html#automatic-exclusion-of-nuisance-columns>

Pour aller plus loin sur `groupby` vous pouvez lire la documentation :

<http://pandas.pydata.org/pandas-docs/stable/groupby.html>

+++

### Réorganisation des indexes avec `pivot`

+++

Un manière de voir la notion de pivot est de considérer qu'il s'agit d'une extension de `groupy` à deux dimensions. Pour illustrer cela, prenons un exemple en utilisant le jeu de données seaborn sur les passagers du Titanic.

```{code-cell} ipython3
titanic = sns.load_dataset('titanic')
```

```{code-cell} ipython3
# regardons le format de ce jeu de données
titanic.head()
```

```{code-cell} ipython3
# regardons maintenant le taux de survie par classe et par sex
titanic.pivot_table('survived', index='class', columns='sex')
```

Je ne vais pas entrer plus dans le détail, mais vous voyez qu'il s'agit d'un outil très puissant.

Pour aller plus loin, vous pouvez regarder la documentation officielle :

<http://pandas.pydata.org/pandas-docs/stable/reshaping.html>

mais vous aurez des exemples beaucoup plus parlants en regardant ici :

<https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/03.09-Pivot-Tables.ipynb>
