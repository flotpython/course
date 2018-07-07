# Un index est un objet immuable qui est à la frontières d'un set 
# et d'une liste. En effet, un index est un ensemble de
# labels hashables (comme pour les éléments d'un set), mais
# ordonnées et sliceable (comme les éléments d'une liste). En
# particulier, je peux avoir des éléments dupliqués dans un index. 

# Un index offre donc à la fois un comportement de liste et 
# un comportement de set. 

# En pratique, on crée jamais directement un objet index. Il 
# va être automatiquement créé au moment de l'importation
# de nos données. Pandas supporte l'importation et l'exporation 
# d'un grand nombre de format : CSV, JSON, HTML, Excel, SQL,
# pickle, etc. C'est un sujet qui ne présente pas de difficulté particulière
# et que vous verrons dans un complément. 
 
 #55s
 
# Regardons maintenant un exemple de Series

import pandas as pd
s = pd.Series([20, 30, 40, 50], index=['eve', 'bill', 'liz','bob' ])
print(s)

# regardons maintenant les différents composants de cette Series
s.values

# représente le tableau numpy contenant les données, il s'agit
# d'un tableau numpy tout à fait standard. 

s.index

# représente l'object index. 

#2m10s

# Il existe plusieurs manières d'accéder à un élément dans une
# Series, mais une seule manière de le faire sans risque d'ambiguité
# et sans effets de bords. 

# Pour accéder aux éléments d'une Series par leur label on utilise
# l'attribut loc

s.loc['eve']

# on peut slicer sur les label de la manière suivante

s.loc['eve':'liz']

# avec une différence notoire avec le slice classique : la borne
# de droite est incluse, dans notre exemple, on va donc de 'eve' à 
# 'liz' inclue.

# comme on peut faire un slice sur des labels, vous vous demandez
# sans doute quelle est la relation d'ordre sur les label dans un index.
# L'ordre est déterminé à la création de l'index par l'ordre dans 
# lequel on range les labels, de la même manière que pour une 
#séquence. Modifions l'ordre de création de l'index

s = pd.Series([20, 30, 40, 50], index=['eve',  'liz', 'bill','bob' ])
print(s)
s.loc['eve':'liz']

# 4m00

# Cependant, il y a un cas pour lequel le slicing ne marche. C'est
# s'il y a des labels dupliqués ET que l'index n'est pas trié. Dis 
# autrement, s'il n'y a pas de boublons dans l'index, le slicing 
# fonctionne toujours, si l'index est trié, le slicing fonctionne 
# toujours. C'est par conséquent, une bonne pratique de 
# toujours trier l'index avant de commencer à travailler
# sur la Series, d'autant plus que cela peut augmenter de manière
# trés significative la performance de l'index. Prenons la série
# d'animaux que possèdent des personnes
animaux = ['chien','chat', 'chat', 'chien', 'poisson']
proprio = ['eve', 'bob', 'eve', 'bill', 'liz']
s = pd.Series(animaux, index=proprio)
print(s)
s.loc['eve':'liz']

# trions maintenant l'index, attention, la méthode sort_index()
# ne fait pas de trie en place, mais retourne par défaut une 
# nouvelle Series avec l'index trié

s = s.sort_index()
s.loc['eve':'liz']

# 6m50

# Il existe également un attribut iloc qui permet d'accéder aux 
# élément d'une Serie par leur rang dans la Series et non plus 
# par leur label. Regardons un exemple

print(s)
s.iloc[0]
s.iloc[4]

# on peut également faire des slices sur l'attribut iloc, 
# avec la même sémantique que pour les listes, on va de
# i à j-1 par pas de k. Attention donc que pour iloc la borne
# de droite est bien exclue

s.iloc[1:3]

#7m40

# Les Series acceptent également la notion d'indexation avancée
# comme les tableaux numpy. On peut donc faire les opérations 
# suivantes
s.loc[s=='chien']

s.loc[(s=='chat') | (s=='poisson')]

# et on peut faire de l'affectation comme pour les tableaux numpy
s.loc[(s=='chat') | (s=='poisson')] = 'autre'

#8m40

# Il faut bien comprendre que certaines opérations sur les Series
# sont faites
# sur les valeurs de la Series, c'est le cas de la création des tableaux
# de booléens que l'on vient d'utiliser pour l'indexation avancée, 

s == 'chien'

# et certains opérations sont faites sur les clefs, c'est le cas, 
# par exemple, du test d'appartenance

'eve' in s

# Le moyen mnémotechnique vous s'en souvenir est que les 
# opérations que l'on fait habituellement sur les tableaux numpy 
# s'applique aux valeurs de la Series, et les opérations que l'on 
# fait habituellement sur  des dictionnaires s'appliques à l'index 
# de la Series.

# 9m30

### Alignement des labels

# J'aimerais introduire la notion d'alignement des labels
# qui est une notion clef en pandas. Regardons un exemple

s1 = pd.Series([1, 2, 3], index=list('abc'))
s2 = pd.Series([5, 6, 7], index=list('acd'))

# maintenant additionnons ces deux DataFrame
s1 + s2

# On voit qu'il y a eu alignement automatique. 
# Les opérations sont faites pour les valeurs correspondant au même
# label. À chaque fois que l'on fait une opération sur deux Series,
# il y a toujours alignement des index. 
# On voit par contre que si un label manque dans l'un des deux index, 
# le résultat de l'opération est automatiquement NaN.

#11m20

# Vous vous en souvenez, dans un tableau numpy, seul les types
# float supportent le NaN, par conséquent le résultat sera 
# obligatoirement de type float

# On peut controller ce comportement en utilisant la fonction 
# pandas correspondante. Comme pour numpy, en pandas chaque
# opérateur à une méthode pandas correspondante
s1.add(s2) 

# cette méthode accepte un argument fill_value qui permet de 
# remplacer la valeur manquant par une valeur par défaut
s1.add(s2, fill_value=18)

# Vous noterez cependant que le résultat sera tout de même 
# du type float, c'est une limitation de fill_value.

#12m10
