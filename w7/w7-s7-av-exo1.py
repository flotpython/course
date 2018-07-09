##### Initialiser le notebook avec le code ci-dessous
##### BEGIN

import numpy as np
import pandas as pd

# liste des noms
prenoms = ['liz', 'bob', 'bill', 'eve']

# création des trois colonnes
age = pd.Series([25, 30, 35, 40], index=prenoms)
taille = pd.Series([160, 175, 170, 180], index=prenoms)
sexe = pd.Series(list('fhhf'), index=prenoms)

# création de la DataFrame
df = pd.DataFrame({'age': age, 'taille': taille, 'sexe': sexe})
##### END

# Regardons ce code pour créer une DataFrame. N'hésitez
# pas à mettre la vidéo en pause pour avoir le temps de taper
# ce code.
df

#1m00

# on peut maintenant accéder à l'index des lignes
df.index

# à l'index de colonnes
df.columns

# au tableau des valeurs
df.values

# lorsqu'on a une grande DataFrame, on peut explorer les premières
# lignes avec
df.head(2)

# les dernières lignes avec
df.tail(2)

# et une première description statistique avec
df.describe()

# 2m11

# Regardons maintenant l'indexation.
# Comme pour les Series, je vous recommande de toujours
# utiliser les attributs loc et iloc. Loc est pour l'indexation sur les
# label et iloc sur les rangs des labels dans les index

# Lorsque vous ne spécifiez qu'un seul argument à loc, cet argument
# sera recherché dans l'index de lignes.

df.loc['liz']

# si vous donner deux arguments, le premier sera pour
# l'index des lignes et le deuxième pour l'index des colonnes
df.loc['liz', 'age']

# On peut faire du slicing sur les lignes et le colonnes
df.loc[:, 'taille']

# on peut évidemment faire de l'indexation avancée

df.loc[df.loc[:,'age']< 32]

# Il est courant avec une DataFrame de transformer un index
# en colonne et une colonne en index. Regardons cela

df = df.reset_index()
print(df)
# j'aimerais maintenant renomer ma colonne index en nom

df = df.rename(columns={'index':'prenom'})
print(df)
# en ensuite je vais utiliser la colonne age comme index

 df = df.set_index('age')
 print(df)
 # Les méthodes sur les DataFrame retournent en général une
 # nouvelle DataFrame, il est par conséquent courant chainer
 # les appelles de méthodes de la manière suivante

noms = ['liz', 'bob', 'bill', 'eve']
age = pd.Series([25, 30, 35, 40], index=noms)
taille = pd.Series([160, 175, 170, 180], index=noms)
sexe = pd.Series(list('fhhf'), index=noms)
df = pd.DataFrame({'age': age, 'taille': taille, 'sexe': sexe})

df = (df.reset_index()
    .rename(columns={'index':'nom'})
    .set_index('age'))

#6m30

# regardons maintenant un exemple sur l'alignement des
# index lors des opérations entre DataFrames

df1 = pd.DataFrame(np.ones((2,2)), index=list('ab'), columns=list('xy'))
df2 = pd.DataFrame(np.ones((2,2)), index=list('ac'), columns=list('xz'))

# regardons en premier df1 et df2
df1
df2

df1+df2

# Si j'aditionne les deux DataFrames, les valeurs manquantes
# sont automatiquement replacée par NaN. Je peux controller
# ce comportement en appelant la méthodes correspondant
# à l'opération avec l'argument fill_value

df = df1.add(df2, fill_value=0)
df
# Par contre, si des valeurs sont manquantes dans les deux DataFrame
# le résultat sera tout de même NaN. Je peux cependant,
# remplacer les NaN et effacer les lignes les contenants.

df.fillna(-1) # pour remplacer les NaN par un -1

df.dropna() # pour supprimer les lignes contenant un NaN

# Vous verrez dans les compléments que ces methodes ont
# plusieurs options qui par exemple de remplacer les NaN
# avec une valeurs proches du NaN dans le tableau ou
# de supprimer une contenant uniquement un certains
# nombre de NaN.

#9m30
