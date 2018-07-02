# Commençons par créer une liste de 1000 éléments et un tableau numpy de 1000 éléments. 
# Nous reviendrons largement sur les tableaux numpy, l'objectif ici est de vous montrer le
# la gain de performance

L = list(range(1_000))
a = np.arange(1_000)

# regardons si ces deux objets contiennent la même chose

all(L == a) # va comparer élément pas élément

# maintenant, comparons le temps pour élever au carré chaque élément
%timeit [x**2 for x in L]
%timeit [x**2 for x in a]

# la même compréhension sur un tableau numpy est 30% plus rapide que sur une liste
# Mais en réalité, en numpy on utilise un principe que l'on appelle la vectorization et qui
# n'existe pas sur les builtins Python. C'est avec la vectorization que l'on obtient le vrai
# gain de performance

%timeit a**2  #vectorisation

# sur ce simple exemple, on gagne un facteur 200. 

# Vérifions tout de même que ces deux opérations donnent le même résultat

all(a**2 == [x**2 for x in L])

# Mais alors quel est le prix à payer pour ce gain majeur de performance ?

# Vous noterez que les les tableaux numpy supportent le protocol d'itération. 
# On peut faire des boucles for ou des compréhensions. Mais le vrai gain de 
# performance apparait lorsqu'on utilise un nouveau concept à apprendre 
# et maitriser, la vectorization. Nous verrons que vous aurez à apprendre
# beaucoup de nouveaux concepts.
#
# On autre prix à payer et la perte de souplesse et l'absence d'exception sur 
# certaines opérations douteuses. Regardons cela
 print(a[999])
 
 a[999]**2 == 999**2   # c'est évidemment vrai
 
 # mais regardons maintenant cela
 a[999]**32 == 999**32  # c'est faux. 
 
 type(a[999]) # c'est un entier signé codé sur 32 bits
 a[999]**32
 
 # alors que
 999**32
 
 # Un tableau numpy ne peut contenir que des objets de même type, mais
 # si on fait une opération qui dépasse la précision de cet objet, l'erreur peut
 # passer silencieusement. 
 

