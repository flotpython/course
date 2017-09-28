## Vidéo 1 (Fonctions)
### NIVEAU: BASIC

### Compléments Vidéo 1

* xxx todo: montrer sous pythontutor l'exemple de la vidéo

```
L = []
def add_1(a):
    a.append(1)
add_1(L)
# et la version avec copie
def add_1(a):
    a = a[:]
    a.append(1)
    return a
L = add_1(L)
```

* xxx **TODO**, un complément sur les type hints (ou w4-s6 ?)

Pour mémoire, notebook du précédent MOOC sur Python 2

* `Complement-docstring.ipynb`
* `Complement-fonction-isinstance.ipynb`
* `W4-S5-C1-arg-reference.ipynb`

### Quizz Vidéo 1

Pour mémoire, quizz du précédent MOOC sur Python 2

* `W4-S5-E1-functions.quiz`

* xxx idée d'Arnaud : poser une question sur le glitch dans la vidéo (f(1) ne retourne rien)

### Exercices Vidéo 1

Pour mémoire, exercices du précédent MOOC sur Python 2

* NICETOHAVE leur faire faire un exo des fonction polymorphe qui
  prenne en argument un entier ou un nom - par exemple avec les
  bateaux de marine..
* BOF aplatir un arbre - pour isinstance() le faire en deux
  versions, copie ou modif inline (essayer d'abord)


## Vidéo 2 (Tests `if`/`elif`/`else` et opérateurs booléens)
### NIVEAU: BASIC

### Compléments Vidéo 2

* `Complement-evaluation-conditions.ipynb`: évaluation paresseuse (repris et aménagé de W2-S6)
* `Complement-conditions-2.ipynb`:  recap expressions dans un if

### Quizz Vidéo 2

### Exercices Vidéo 2

Pour mémoire, exercices du précédent MOOC sur Python 2

* `Exercice-if.ipynb`: des exercices sur des ifs un peu torturés
* NICETOHAVE : c'est un peu léger dans l'état


## Vidéo 3 (Boucles `while`)
### NIVEAU: BASIC

### Compléments Vidéo 3

Pour mémoire, notebook du précédent MOOC sur Python 2

* `Complement-boucle-while.ipynb`

### Quizz Vidéo 3

### Exercices Vidéo 3

Pour mémoire, exercices du précédent MOOC sur Python 2

* `Exercice-pgcd.ipynb`


## Vidéo 4 (Portée des variables - règle LEGB)
### NIVEAU: BASIC
### Compléments Vidéo 4

* xxx todo ? insister sur le fait qu'une affectation c'est une définition ? il se peut que on en parle mieux dans une vidéo à venir

Pour mémoire, notebook du précédent MOOC sur Python 2

* `S6-C1-scopebuiltin.ipynb` xxx relation avec mots-clés ?
* `Complement-exception-unboundlocalerror.ipynb`

### Quizz Vidéo 4

Pour mémoire, quizz du précédent MOOC sur Python 2

* `W4-S6-E1.quiz`

### Exercices Vidéo 4


## Vidéo 5 (Modification de la portée  avec `global` et `nonlocal`)
NIVEAU: BASIC

### Compléments Vidéo 5

* complément global et nonlocal. Expliquer que global peut créer
  une variable global si elle n'exite pas. Par contre nonlocal ne
  peut pas créer une variable dans une fonction englobante (comme
  il peut y avoir plusieur niveau il y aurait ambiguité) et
  nonlocal ne peut pas accéder aux variable globale. Une variable
  dans l'entête d'une fonction ne peut pas être déclarée nonlocal

* Ajouter des compléments avec Pythontutor pour pratiquer global,
  nonlocal et modification d'objet mutable. **Je n'en parle plus
  dans les vidéos**. C'est important de faire un point sur les
  connaissances à ce niveau. L'idée est de bien voir le variable
  local disparaitre au retour de la fonction, le objet mutable
  modifié par effet de bord alors qu'on ne change pas la référence
  de la variable, etc. Par exemple (sans doute faire mieux):

```
    >>> L = [1,2]
    >>> def f(L):
           L.append(3)
	   L = [4, 5, 6]
    >>> f(L)
    >>> print L
    [1, 2, 3]
```

Pour mémoire, notebook du précédent MOOC sur Python 2

* DROPPED pas de complément ici- la vidéo est déjà très copieuse et
  détaillée montrer que global crée une variable global si elle
  n'existe pas encore. Je trouve qu'on en a déjà beaucoup trop dit sur
  `global`

### Quizz Vidéo 5

Pour mémoire, quizz du précédent MOOC sur Python 2
* `W4-S7-E1.quiz`

### Exercices Vidéo 5

Pour mémoire, exercices du précédent MOOC sur Python 2
*


## Vidéo 6 (Passage d'arguments et appel de fonctions)
NIVEAU: BASIC

### Compléments Vidéo 6

* Parler de https://www.python.org/dev/peps/pep-3102/ pour mettre
des arguments nommés après le *varargs et qu'ils deviennent alors
des arguments qu'on *doit* nommer lors de l'appel
* parler des ordres des arguments et des ordres des paramètres

Pour mémoire, notebook du précédent MOOC sur Python 2

* `Complement-passage-arguments.ipynb`
* `Complement-pas-de-valeur-par-defaut-mutable.ipynb`
* TODO je sais pas trop où mettre argparse, je trouve qu'ici c'est déjà bien chargé...
  * introduire sys.argv en remarquant que c'est une forme *Targs
    et introduire le module argparse.


### Quizz Vidéo 6

Pour mémoire, quizz du précédent MOOC sur Python 2
* `W4-S8-E1.quiz`

### Exercices Vidéo 6

Pour mémoire, exercices du précédent MOOC sur Python 2
* `Exercice-passage-arguments.ipynb`
