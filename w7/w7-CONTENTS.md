## Vidéo 1 (Data science en Python) 
### NIVEAU: BASIC
### Compléments Vidéo 1

### Quizz Vidéo 1

### Exercices Vidéo 1



## Vidéo 2 (Les bases de numpy) 
### NIVEAU: BASIC
### Compléments Vidéo 2

- créer des tableaux d'objects
- créer des tableaux de numpy.void (taille constante, type quelconque)
- créer des dtype custom
- montrer les notation U4, <i2, etc. au lieux de ('str', 4), np.int16
- concaténation, split

### Quizz Vidéo 2

### Exercices Vidéo 2


## Vidéo 3 (Slicing, reshaping et indexation avancée) 
### NIVEAU: BASIC
### Compléments Vidéo 3

- montrer ce cas d'indexation avancée
a = np.arange(1, 11).reshape(2,5)
L = [[0,1], [2,4]]
a[L]
-parler de sort
-parler de partition
- parler du tuple comme indice d'un tableau
a = np.random.randint(1, 10, size=(3, 3))
print(a)
t = (1, 1)
L = [1, 1]
print(a[1, 1])
print(a[t]) # me retourne l'élément de coordonnées (1, 1)
print(a[L]) # me retourne deux fois la ligne 1

### Quizz Vidéo 3

### Exercices Vidéo 3


## Vidéo 4 (vectorisation) 
### NIVEAU: BASIC
### Compléments Vidéo 4

-introduire numba et cython
- donner le lien de toutes les fonctions vectorisées numpy
https://docs.scipy.org/doc/numpy/reference/ufuncs.html
-parler de 
ufunc.nin 	The number of inputs.
ufunc.nout 	The number of outputs.
ufunc.nargs 	The number of arguments.
ufunc.ntypes 	The number of types.
ufunc.types 	Returns a list with types grouped input->output.
ufunc.identity 	The identity value.
ufunc.signature 	Definition of the core elements a generalized ufunc operates on.

-parler de scipy.special
-parler de reduce, accumulate, outer

### Quizz Vidéo 4

### Exercices Vidéo 4


## Vidéo 5 (broadcasting) 
### NIVEAU: BASIC
### Compléments Vidéo 5
-citer http://scipy.github.io/old-wiki/pages/EricsBroadcastingDoc
notamment sur le problème de performance en broadcasting

### Quizz Vidéo 5

### Exercices Vidéo 5


## Vidéo 6 (Introduction aux Series et aux indexes en pandas) 
### NIVEAU: BASIC
### Compléments Vidéo 6

### Quizz Vidéo 6

### Exercices Vidéo 6


## Vidéo 7 (Les DataFrames en pandas) 
### NIVEAU: BASIC
### Compléments Vidéo 7

### Quizz Vidéo 7

### Exercices Vidéo 7


## Vidéo 1 () 
### NIVEAU: BASIC
### Compléments Vidéo 1

### Quizz Vidéo 1

### Exercices Vidéo 1


## Vidéo 1 () 
### NIVEAU: BASIC
### Compléments Vidéo 1

### Quizz Vidéo 1

### Exercices Vidéo 1


## Vidéo 1 () 
### NIVEAU: BASIC
### Compléments Vidéo 1

### Quizz Vidéo 1

### Exercices Vidéo 1



# Old content

## Vidéo 1 (Introduction, survol des différents outils)

### compléments w7-s1

* **c1** installation (partant de python pur, ou avec conda)


## Séquence 2 (`numpy`) - pas de vidéo
### NIVEAU: basique
### compléments w7-s2

* **c1** programmation vectorielle à 1 dimension

* **c2** type d'un tableau numpy -- attribut `dtype`

* **c3** plusieurs dimensions & reshaping

* **c4** initialisations de tableaux (empty, zeros, ones, arange, linspace, gridmesh, ...)

* **c5** broadcasting

* **x1** première tranche d'exercices - pour montrer qu'on
  peut faire **plein** de trucs sans indexation
  * distributions normale et uniforme (introduire np.random)

* **c6** indexing & slicing

* **c7** opérations logiques

* **c8** algèbre linéaire

* **c9** indexation - revisitée
  * indexations évoluées (booléens, listes et tableaux)

* **c10** divers
  * mémoire / copies / views / l'option out=
  * structured arrays
  * stacking & tiling

* **x2**

  * ACP
  * modeliser D4 avec des structured arrays
  * mandelbrot (avancé)


## Séquence 3 (`pandas`) - pas de vidéo
### compléments w7-s3

* ...


## Séquence 4 (`matplotlib`) - pas de vidéo
### compléments w7-s4

* **c01** matplotlib: juste mentionner les deux tutos
  * 2D: on peut sans doute s'inspirer de https://matplotlib.org/2.0.2/users/pyplot_tutorial.html
  * 3D : s'inspirer de https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html

* **c02** autres librairies ?
  * bokeh - notamment https://bokeh.pydata.org/en/latest/docs/user_guide/notebook.html#inline-plots
  * plotly https://plot.ly/python/offline/
  * seaborn

* **cxx** : notebooks interactifs : `interact` et `ipywidgets`
