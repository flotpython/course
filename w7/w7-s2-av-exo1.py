# avant toute opération, on import le module numpy en le nommant np
import numpy as np

# un tableau numpy peut avoir 1, 2 ou plus de dimensions. 
# Pour les méthodes qui permettent de créer un tableau numpy
# comme la méthode ones qui permet de créer un tableau
# contenant des 1, 
# on doit spécifier les dimensions dans l'argument shape, soit
# avec un entier, pour les tableaux à une dimension, soit comme
# un tuple avec les tableaux à plusieurs dimensions. Regardons
# cela. Utilisons la méthode ones pour créer un 
# tableau ne contenant que des 1

np.ones(shape=2)

# Comme shape est le premier argument, je peux me passer
# de le nommer. 

np.ones((2, 2)) # tableau à 2 dimensions

np.ones((2, 2, 2)) # tableau à 3 dimensions

# je peux donner autant de dimensions que nécessaire. 

# Évidemment un tableau numpy est mutable, je peux donc 
# changer la valeur d'un élément en utilisant la notation crochet
a = np.ones((2, 2))
# on spécifie la position dans chaque dimension séparée par des
# virgules, la numérotation commence à zero.
# ici on choisi l'élément à la deuxième ligne et la deuxième colonne
a[1, 1] = 18 
print(a)

# 2m20

# Attention, comme un tableau numpy définie une zone contiguë de 
# mémoire on ne peut faire des opérations de type append() comme
# sur les liste. Le nombre d'éléments reste fixe une fois le tableau créé.
# c'est pourquoi on a des méthodes ones et zeros pour 
# préallouer des tableaux en les remplissant de 0 ou de 1 pour ensuite
# les modifier. 

# 2m50

# dans un tableau numpy, je peux également spécifier le type des objets 
# stocké avec l'argument dtype pour data type. Il s'agit d'un argument
# optionnel, mais on vous recommande fortement de toujours
# spécifier votre data type, sinon, numpy va faire un choix
# pour vous qui risque de ne pas être pertinent. 

# Dans cet argument dtype on doit spécifier soit 
# un objet de type dtype, soit un type scalaire. 
# Ces types définissent toujours une taille fixe. 
# Ainsi un tableau numpy définit une zone de mémoire 
# contiguë contenant des objets qui ont tous le même type 
# et la même taille.

# On utilise en général dans les tableaux numpy les types scalaires.

#3m40

# voici tous les types scalaires que l'on peut mettre dans un tableau
np.sctypes

# nous avons les int et unsigned int codés sur 8 à 64 bits, les float
# codé sur 16 à 64 bits, les complex et d'autres types sur lesquels nous 
# reviendrons dans quelques instants.  

# Créons un tableau numpy avec la méthode array qui sert à 
# convertir une séquence Python en tableau numpy

np.array([1, 100, 110], dtype=np.int8)

# tout fonctionne bien, on a un tableau très compact, contenant
# uniquement des entier codés sur 8 bits, 

# 4m40

# mais regardons le cas  suivant

np.array([1, 4.5, 128], dtype=np.int8)

# on remarque que le float a été tronqué et que le 128 c'est transformé
# en -128. Numpy va automatiquement tronquer les float lorsque le
# type est un int. Et si le int donné dépasse la précision on va boucler, 
# sans signaler d'erreur. Dans notre cas, les int8 vont de -128 à 127, soit 
# 256 valeurs. Si on donne un 128, comme cela dépasse le int8 
#  maximum, on va boucler sur la première valeur, soit -128, Si on avait
# donner 129, on aurait boucler sur la deuxième valeur soit -127, etc.

# 6m00

# Évidemment, je peux spécifier une précision plus grande

np.array([1, 2**32], dtype=np.int64)

# revenons maintenant au type scalaire dans la catégorie autre
np.sctypes['others']

# on pourrait croire en voyant les str et bytes, que l'on
# peut spécifier des chaînes de taille variable. Ça
# n'est pas le cas. On peut effectivement stocker des  
# chaînes de caractères, mais ces chaines  doivent toutes avoir
# la même taille. Regardons cela

np.array(['spam', 'bean'], dtype='str')

# nous voyons que les chaînes sont des chaines unicode codés sur 4 
# caractères

np.array(['spam', 'beans'], dtype='str')

# on a maintenant des chaines codés sur 5 caractères, mais on peut
# spécifier le nombre de caractères que l'on souhaite dans le type

np.array(['spam', 'beans'], dtype=('str', 2))

# et dans ce cas, les caractères au delà du deuxième sont simplement
# tronqués. 
 
 #8m40
 
# pour finir sur les types scalaires, il y a également les types object et 
# numpy.void. Ces deux types sont très particulier. Le type object 
# permet de stocker dans le tableau des références vers des objets 
# Python. Par conséquent, les objets ne sont par directement stockés 
# dans le tableau, on a donc une perte de performance. Dans l'esprit, un
#  tableau d'objet Python se rapproche d'une liste. 

# Le type numpy.void permet de stocker dans un tableau numpy 
# n'importe quel type d'objet d'une taille prédéfinie. Nous n'en 
# parlerons pas plus ici. 

#9m10

# Nous avons vu qu'un tableau numpy pouvait contenir n'importe quel
# type scalaire ou un objet dtype. L'objet dtype permet de 
# composer des types scalaires dans une structure avec des champs
# nommés. C'est une construction que l'on trouve dans les 
# structured arrays qui sont aujourd'hui très avantagement remplacés
# par les DataFrame pandas que nous verrons dans la suite. C'est   
# pourquoi je ne parlerai pas plus des notions de dtypes et de 
# structured array

# 9m50

# Pour finir créons de nouveau un tableau

a = np.zeros((2, 3), dtype=np.int8)

# on a un certain nombre d'attributs qui nous permettent 
# d'explorer les caractéristiques de ce tableau

a.shape # donne la taille du tableau
a.dtype # donne le type des éléments du tableau
a.itemsize # donne la taille en bytes de éléments du tableau
a.nbytes # donne la taille totale du tableau

# 11m00