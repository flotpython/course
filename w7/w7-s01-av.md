Bonjour à tous,

cette semaine nous allons voir une
introduction à cette énorme famille
d'outils qui gravitent autour de python
et qui ont à voir de près ou de loin
avec le **calcul scientifique**, ou comme on
dit maintenant le data science.

quand je dis data science, c'est
à prendre au sens très très large, ça
peut être classiquement du traitement
d'images, du traitement du signal, des
statistiques, de l'intelligence
artificielle, bref dès qu'il s'agit de
faire beaucoup de calculs sur des nombres.

je précise tout de suite que, bien
évidemment, c'est un sujet **très très
vaste** qui pourrait sans problème occuper
un mooc de plusieurs semaines

En ce qui nous concerne ici et dans cette édition en tous cas,
nous allons nous contenter d'effleurer trois outils qui sont

* numpy
* pandas
* et matplotlib

notre objectif c'est d'abord que vous
sachiez **que ça existe**, et que vous voyiez
bien comment ça s'articule **par rapport aux
types de base** et autres notions python
qu'on a vus jusqu'ici. Comme ça on
pourra gratter la surface avec quelques
exemples simples, à vous ensuite de
creuser les différentes librairies en
fonction de vos besoins.


========== numpy

la pièce centrale de tout l'édifice,
c'est une librairie qui s'appelle numpy
c'est vraiment un incontournable car
toutes les autres librairies dont on va
parler sont écrites au dessus de numpy

et dans cette vidéo je vais vous
montrer comment elle est conçue et ce
qu'elle apporte

========== tableaux

à la base pour toutes ces applications,
on a besoin de manipuler des nombres,
beaucoup de nombres, le plus souvent
structurés en tableaux, que ce soit pour
des images, des matrices, des séries
temporelles.

et si vous regardez l'ensemble des types
natifs python que l'on a vus jusqu'ici,
on a bien tout de qu'il faut pour les
nombres entiers, réels et même
complexes, mais quand il s'agit de les
organiser en tableaux, eh bien en fait
il y a un gros problème d'efficacité.

========== fragment

Je peux bien sûr représenter une matrice
comme une liste de listes par
exemple.

========== fragment

Ou bien comme un dictionnaire indexé par
des tuples

========== fragment

si je choisis la première option je peux
accéder à un élément de tableau comme
ceci

========== fragment

et si je choisis l'autre option je ferai
comme ceci

et bien sûr on peut imaginer plein
d'autres façons de faire

========== slide langage compilé

avant d'aller plus loin dans l'analyse,
je voudrais vous montrer comment sont
implémentés les tableaux dans un
langage compilé plus traditionnel,
disons en C, mais ça s'applique à plein
d'autres langages tournés vers
l'efficacité.

Dans ces langages-là, comme c'est
compilé le programmeur a fait un travail
en plus par rapport à python, il a déclaré sous
une forme ou sous une autre son tableau,
ça veut dire essentiellement deux choses

========== fragment

d'abord typiquement que le tableau est
homogène, je veux dire que tous les
éléments sont de même type, et pour un
langage compilé ça veut dire qu'ils
ont la même taille en mémoire

========== fragment

et on a déclaré aussi la dimension du tableau

========== accès direct

ce qui fait qu'on peut typiquement
implémenter un tableau comme ceci

========== animation

* je connais la taille du tableau
* je connais la taille de chaque cellule,
  parce que le tableau est homogène
* donc au lieu de mettre mes cellules
  n'importe où
* je vais prendre un espace mémoire
  contigü
* et ranger les éléments du tableau en
  ordre croissant
* space
* et du coup quand je vais vouloir accéder
à un élément à partir de ses indices
ligne et colonnes, je peux appliquer une
formule simple, qui dépend seulement de
la taille du tableau
* space
qui me donne directement accès à la case
qui m'intésse.
* ...
* aussi et surtout, lorsque je vais
vouloir passer sur tout mon tableau
pour, par exemple, appliquer la même
fonction à toutes les cellule, avec
cette implémentation c'est aussi super
rapide, comme je connais la taille de
chaque cellule je passe à la suivante en
faisant juste une addition sur les
adresses.

========== de python à numpy

Avec python de base tel qu'on l'a vu
dans le tronc commun, on ne peut pas arriver à
implémenter quelque chose qui ressemble
à un tableau et qui soit aussi efficace
que ce que je viens de vous montrer.

C'est principalement une conséquence du typage
dynamique: car dans une liste ou un
ensemble je peux par construction
mélanger plusieurs types, et ajouter ou
enlever des éléments.

========== fragment

La valeur ajoutée essentielle de numpy,
c'est de proposer un nouveau type de
données, qui s'appelle ndarray pour
n-dimension array, tableau à n
dimensions, qui vient avec des
restrictions qui sont, justement, que le
container doit être homogène, et disons
pour l'instant de taille fixe, on
précisera ça.

moyennant quoi il va être possible
de gagner beaucoup sur l'optimisation
de tous ces traitements de tableaux


========== slide benchmark1 - liste

on va faire quelques petits benchmark
pour comparer, ça nous donnera l'occasion
de jouer un peu avec numpy.

========== fragment

on va calculer le cosinus de 10.000
nombres

je pars d'entrées qui sont des flottants
car c'est plus représentatif

========== fragment

alors voici comment on construirait un
tableau numpy équivalent.

Vous voyez que j'importe le package
numpy sous le nom raccourci np, c'est la
tradition.

Et donc je crée un objet du type
numpy.ndarray en appelant `np.array` et
en lui passant mes données, puisque je
les ai sous forme de liste.

[[Bien sûr c'est pour les besoins du benchmark, en
pratique on n'a pas besoin de passer par
l'étape de la liste si on utilise pandas
ou autre.]]

========== fragment

maintenant je vais calculer **le cosinus de tous ces nombres**.
j'ai pris cosinus au hasard bien sûr, mais c'est très très fréquent qu'on ait besoin d'appliquer la même fonction à tous les éléments d'un tableau.

je regarde combien de temps
ça prend de calculer tous les
cosinus, et je commence par la version en
python pur avec la liste

========== run cell

Pour comparer des choses comparables je
rassemble les résultats dans une **compréhension**

donc à peu près 1.2ms pour cette version

========== fragment
la version en numpy ça se présente comme
ceci, j'appelle juste la fonction np.cos
sur le tableau, et ça ça veut dire de me
remvoyer un tableau de même dimension
que n avec les cosinus à la place des
entrées

========== run cell

si je l'exécute vous pouvez voir que ça
va environ 10 fois plus vite.


========== slide benchmark 2 - dict / tuple

Voyons rapidement notre deuxième idée de
tout à l'heure, vous vous rappelez on
avait parlé d'implémenter un tableau
comme un dictionnaire indexé par des
tuples d'entiers, voyons ce que ça
donnerait avec cette idée-là.

Du coup cette fois-ci je vais prendre un
tableau à deux dimensions.

dans la version en pur python je crée
donc un dictionnaire d qui est indexé
par des couples, des tuples à deux
éléments; ici je fais un tableau carré
de taille 100. J'ai pris en fait la même
taille qu'à l'instant avec les listes
vous pouvez comparer si vous êtes curieux

========== fragment

pour créer l'objet ndarray c'est comme
tout à l'heure, je passe par une liste
pour me simplifier le travail

========== fragment

si à nouveau je calcule une structure
analogue à l'entrée mais qui contient
les cosinus, avec une compréhension en
python ça me donne ceci en python pur

========== fragment

et ceci en numpy, vous voyez qu'on est
ici encore dans un facteur 10 en gros.


[[AL: je trouve qu'un facteur 10 c'est très en deça de ce qu'on
peut avoir en numpy. Je te donne ci dessous un exemple plus
spectaculaire
In [45]: L = [random.randint(0,10) for i in range(1000000)]

In [46]: %timeit [x**2 for x in L]
1 loop, best of 3: 296 ms per loop

In [47]: a = np.array(L)

In [48]: %timeit np.square(a)
1000 loops, best of 3: 1.85 ms per loop

In [49]: %timeit np.square(a, out=a)
1000 loops, best of 3: 788 µs per loop

]]
========== slide tableau = vue

On a vu donc qu'un tableau numpy est un
container d'objets homogènes, et qu'il
possède une taille.

Je voudrais mettre en évidence un autre
aspect des tableaux numpy, qui n'est pas
totalement évident et peut déstabiliser
un peu les débutants.

Je fais une petite expérience, je crée
un tableau, j'en profite pour vous
montrer qu'on peut choisir son type à la
création du tableau, bon,

==========

si je l'évalue je vois le même tableau
que tout à l'heure avec 3 lignes de 4
colonnes, très bien

==========

maintenant je crée un second tableau b à
partir de a. Bon ici j'utilise la
méthode reshape, c'est parce que c'est
celle qui me permet le plus facilement
de vous montrer cette notion de vue,
je me retrouve donc avec un autre
tableau, qui a le même contenu de toute
évidence mais une autre géométrie.

Très bien maintenant je vais vous
montrer qu'en fait j'ai créé une
référence partagée, un peu comme avec
les listes. Regardons ça,

========== run

il suffit que je touche au contenu de a
pour que b soit modifié aussi.

========== slide - animation

pour bien comprendre ce qui se passe, je
vous ai préparé une animation, je rejoue
exactement le même scénario, alors
lorsque je crée mon tableau en fait je
crée deux choses distinctes,

* d'abord une zone de **mémoire contigüe**, dans laquelle
vont se trouver les données bien sûr,
mais aussi
* un objet tableau qui est en fait une vue
vers ces données; le tableau voit les données
au travers de sa géométrie - et du type.

  et donc lorsque je crée l'objet b

* ce que je fais c'est uniquement de créer
une autre vue sur le même buffer, avec
une autre géométrie.

donc j'insiste bien, on pourrait penser
que c'est spécifique à l'utilisation de
`reshape`, mais non, c'est vraiment une
caractéristique profonde des tableaux
numpy, c'est vraiment important de bien
voir ça avant de commencer, ça évite
bien des confusions.

* ----- a[1, 2]

  et donc ensuite, quand on cherche
a[1, 2] on utilise la géométrie de a pour
calculer un indice, donc comme tout à
l'heure l'indice 1,2 se traduit en 6

* ----- = 600

  et donc j'écris la valeur 600

* à cet endroit du buffer

  si bien qu'ensuite

* ---- b[3, 0]

  b voit le buffer modifié, ça fait un
effet de bord exactement comme avec les
références partagées de liste ou de
dictionnaires.

----- close animation

Je n'en dis pas plus ici à propos de numpy, je vous donne rendez-vous dans la deuxième séquence pour approfondir le sujet sous forme de notebooks.


---------- `pandas`

Ensuite nous regarderons la librairie pandas, qui est également un outil extêmement utilisé. Le type central de pandas s'appelle le dataframe, vous pouvez le voir un peu comme un tableau excel sur stéroïdes, car il permet de faire d e manière très efficace, le chargement de données, l'indexation dans tous les sens de lignes et de colonnes, et même des opérations qui se rapprochent des bases de données comme des join ou des group-by.

Je vous invite donc à lire les notebooks de la troisième séquence de cette semaine.

========== `matplotlib`

Enfin, en complément de numpy, nous verrons aussi matplotlib, je vous montre très rapidement deux figures obtenues avec matplotlib, c'est un outil très puissant, on en verra quelques exemples dans les notebooks de la quatrième et dernière séquence.


========== slide conclusion

bon voila je vais en rester la, ce sera la seule vidéo de cette semaine, j'espère vous avoir fait
bien sentir les motivations qui sont
derrière les tableaux numpy, qui sont je
le répète omniprésents dans toutes les
librairies scientifiques au sens large.

Motivations qui sont d'améliorer très
sensiblement les performances, notamment
par une meilleure utilisation de la
mémoire, au prix d'une petite limitation - si on compare aux type de base de python - tout à fait inoffensive dans ce contexte.

========== fragment

Ce sera la seule vidéo de la semaine, je vous invite à nous retrouver dans les notebooks des trois séquences consacrées aux trois outils que je viens d'évoquer - sachant que dans ce domaine pratiquement toutes les publications se font maintenant sous forme de notebook.

à bientôt
