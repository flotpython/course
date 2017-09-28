## Vidéo 1 (Codage, jeux de caractères et unicode)
### NIVEAU: BASIC
### Compléments Vidéo 1

* xxx s'assurer qu'on explique %timeit la première fois qu'on s'en sert
* parler d'UTF-8, UTF-16, UTF-32
* faire un peu d'historique avec ASCII et les pages de code
* donner des exemples de problème d'encodage aujoud'hui

### Quizz Vidéo 1
### Exercices Vidéo 1


## Vidéo 2 (Les chaînes de caractères)
### NIVEAU: BASIC
### Compléments Vidéo 2
* parler des doctring (triple guillemet ou apostrophe)
* parler des différences entre `isdigit`, `isnumeric`, `isdecimal`
* parler de `bytearray`
* citer https://docs.python.org/3.5/howto/unicode.html
* citer http://nedbatchelder.com/text/unipain.html (PyCon 2012)
* parler dans format du nouveau séparateur, pour les nombre qui
  permet de formatter automatiquement comme ça : 100,133,589
* faire un complément sur print et montrer la différence en print
  et la représentation interne
* complément unicode en Python (str, bytes, \u, chr, ord, hex,
* etc.) et parler de librairie chardet et unidecode
* parler du module logging

Pour mémoire, notebook du précédent MOOC sur Python 2

* xxx `raw-strings.ipynb` - backslashes - \n \t
   il FAUT le garder pour les vidéos w3-s1 notamment
* montrer encodage / décodage sous forme de figure
  en profiter pour introduire le type bytes - on y fait référence dans w3-s1 pour les fichiers binaires

* `Complement-formatage-de-chaines.ipynb` : format et % - je laisse
  tomber rjust/ljust/center pour le moment
* `Complement-outils-sur-chaines.ipynb` : # `help(str)`  #split join
  #replace strip #index find rfind count startswith endswith upper
  lower swapcase capitalize title  renvoi sur la doc
  * AL: déplacer la discution sur join et split en vidéo 4
    	lorsque je parle des listes
* `Complement-la-fonction-input.ipynb`

### Quizz Vidéo 2
Pour mémoire, quizz du précédent MOOC sur Python 2

* `W2-S8-E1-strings.quiz` - le quiz se prete bien surement aux basiques des strings


### Exercices Vidéo 2

Pour mémoire, quizz du précédent MOOC sur Python 2

* `Exercice-chaines.ipynb` - split, replace, format...


## Vidéo 3 (Les séquences)
### NIVEAU: BASIC
### Compléments Vidéo 3
Pour mémoire, notebook du précédent MOOC sur Python 2

* `Complement-slices.ipynb` : reprend le slicing

### Quizz Vidéo 3
Pour mémoire, quizz du précédent MOOC sur Python 2

* `W2-S3-E1-generic-slicing.quiz` : opérations génériques sur les
  séquences en prenant une str comme exemple

### Exercices Vidéo 3
Pour mémoire, quizz du précédent MOOC sur Python 2

* `Exercice-slicing.ipynb`: un peu de slicing, et des indices
  négatifs, le slicing avec pas, utilisation de la longueur


## Vidéo 4 (Les listes)
### NIVEAU: BASIC

### Compléments Vidéo 4

* TODO faire un complément sur range()
* TODO un complément sur les mutables avec pythontutor

Pour mémoire, notebook du précédent MOOC sur Python 2

* `Complement-listes.ipynb`: un complément sur les méthodes des listes
* `Complement-tris-de-listes-1.ipynb` : sort avec les paramètres reverse, et sur des strings

### Quizz Vidéo 4
Pour mémoire, quizz du précédent MOOC sur Python 2

* `W2-S4-E1-listes.quiz` : pop append extend del sort sorted (j'utilise aussi += a un moment)

### Exercices Vidéo 4
Pour mémoire, quizz du précédent MOOC sur Python 2


## Vidéo 5 (Introduction aux tests `if` et à la syntaxe)
### NIVEAU: BASIC
### Compléments Vidéo 5
* faire un complément sur des list, tuple, dict, fonction sur
  plusieurs lignes. Dire que c'est pas une bonne idée de coupée une
  chaine de caractère avec \ en fin de ligne, il vaut mieux faire
  une concaténation.

[[xxx TP: mais mais on n'a pas encore prononcé le mot de tuple ni dict à ce stade ?!?]]

Pour mémoire, notebook du précédent MOOC sur Python 2

* `Complement-conditions-1.ipynb` : introduire les opérateurs logiques
  - expliquer <> pour !=, obsolète mais dans du code ancien
* `Complement-indentations.ipynb` : imbrications, espaces vs
  tabulations, utilisez des indentations de 4 espaces
* `Complement-if-comme-expression.ipynb`: return 0 if n<=1 else
  n*factoriel (n-1)
*  `Complement-presentation.ipynb`
*  `Complement-instruction-pass.ipynb`
* présenter pass qui est utilisé pour rendre syntaxiquement correct un bloc
  de code que l'on n'a pas encore écrit (voir pour les fonctions, for, if)

### Quizz Vidéo 5
Pour mémoire, quizz du précédent MOOC sur Python 2

### Exercices Vidéo 5
Pour mémoire, quizz du précédent MOOC sur Python 2


## Vidéo 6 (Introduction aux boucles `for` et aux fonctions)
### NIVEAU: BASIC
### Compléments Vidéo 6
Pour mémoire, notebook du précédent MOOC sur Python 2

* xxx montrer range() (les slices ont déjà été vues)

* `Complement-for-sur-plusieurs-variables.ipynb`: affectation a,b dans
  un for, la fonction zip
* `Complement-comprehension-de-liste.ipynb`: [ exp(x) for x in .... if
  ] - XXX reduce ?
* `Complement-tris-de-listes-2.ipynb` : suite de listes-sort: sort
  avec le paramètre key (une fonction), et sorted
* `Complement-valeur-de-retour.ipynb` : il nous faut 'return' pour les
  exe rcices please
* Arnaud : ajouter sur les conventions de style: un espace après les
  virgules, en espace avant et après les opérateurs
  (a = f(1, 2) + g(3, 4)), un saut
  de ligne pour séparer les bloc d'instructions et les fonctions.


### Quizz Vidéo 6

   Pour mémoire, quizz du précédent MOOC sur Python 2

### Exercices Vidéo 6
Pour mémoire, quizz du précédent MOOC sur Python 2

* `Exercice-if-et-def.ipynb` : une petite fonction qui calcule si
  deux entiers sont divisibles ou pas
* `Exercice-boucle-for.ipynb` : trier toutes les listes dans une
  liste; idem avec une direction
* Arnaud: montrer une boucle for sur une chaine de caractères.


## Vidéo 7 (Introduction aux compréhensions de listes)
### NIVEAU: BASIC
### Compléments Vidéo 7
Pour mémoire, notebook du précédent MOOC sur Python 2

### Quizz Vidéo 7
Pour mémoire, quizz du précédent MOOC sur Python 2

### Exercices Vidéo 7
Pour mémoire, quizz du précédent MOOC sur Python 2


## Vidéo 8 (Introduction aux modules)
### NIVEAU: BASIC
### Compléments Vidéo 8
Pour mémoire, notebook du précédent MOOC sur Python 2

* `Complement-packages.ipynb`
* `Complement-modules-et-chemins.ipynb`
* `Complement-recapitulatif-import.ipynb` : pourquoi il ne faut pas
  utiliser import *
* `Complement-module-collections.ipynb`: des variantes utiles aux
  types de base

### Quizz Vidéo 8
Pour mémoire, quizz du précédent MOOC sur Python 2

### Exercices Vidéo 8
Pour mémoire, quizz du précédent MOOC sur Python 2

* `Exercice-decode-zen.ipynb` : décoder le zen de python à partir de this (de import this)
