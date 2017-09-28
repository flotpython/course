## Vidéo 0 (Présentation de la sixième semaine)


## Vidéo 1 (Classes, instances et méthodes)
### NIVEAU: BASIC
### Compléments Vidéo 1

* introduire les properties et notamment qu'on n'a pas besoin de
  setter et getter tout le temps.

* références importantes sur les espaces de nommage
  https://docs.python.org/3.6/tutorial/classes.html#python-scopes-and-namespaces
  https://docs.python.org/2.6/reference/executionmodel.html

Pour mémoire, notebook du précédent MOOC sur Python 2

* s4-c1-introduction-classes.ipynb
* s4-c2-module-datetime.ipynb mentionner datetime
  vs time()
* s4-c3-record-et-classe.ipynb
* s4-c4-attributs-classe-instance.ipynb

intermédiaire montrer les attributs de classe et les attributs
d'instance sur un exemple par exemple Matrix2.template pour une mise
en forme..  ou trouver mieux monter qu'on peut faire self.template
aussi bien que Matrix2.template

### Quizz Vidéo 1

Pour mémoire, quizz du précédent MOOC sur Python 2
* w5-s4-e1.quiz

### Exercices Vidéo 1


## Vidéo 2 (Méthodes spéciales)
### NIVEAU: BASIC
### Compléments Vidéo 2

Pour mémoire, notebook du précédent MOOC sur Python 2
* s6-c1-surcharge-operateurs-1.ipynb

* parler des fallback
 * Itération : __iter__ puis __getitem__
 * in :  __contains__ puis __iter__ puis __getitem__
 *     Test vrai/faux : __nonzero__ puis __len__ (faux si __len__ retourne 0)
 * print : __str__ puis __repr__

* parler des optimisations de CPython sur les opérateurs
     Plus rapide d'utiliser un opérateur que l'appel direct sur le méthode
     >>> timeit.timeit(setup = "L = range(1000)", number = 100000000, stmt = "0 in L")
     3.1706046182752914
     >>> timeit.timeit(setup = "L = range(1000)", number = 100000000, stmt = "L.__contains__(0)")
     11.681099249275206

### Quizz Vidéo 2
### Exercices Vidéo 2

Pour mémoire, exercices du précédent MOOC sur Python 2

   * s6-e1-classes.ipynb


## Vidéo 3 (Héritage)
### NIVEAU: BASIC
### Compléments Vidéo 3

* Parler de l'héritage des built-ins et en particulier les immuables
   (  new  )

Pour mémoire, notebook du précédent MOOC sur Python 2

* s5-c1-heritage.ipynb
* s5-c2-classes-new-style.ipynb
* s5-c3-heritage-multiple.ipynb
* s5-c4-heritage-typage.ipynb

### Quizz Vidéo 3
Pour mémoire, quizz du précédent MOOC sur Python 2

* w5-s5-e1.quiz

### Exercices Vidéo 3


## Vidéo 4 (Héritage multiple et ordre de résolution des attributs)
### NIVEAU: BASIC
### Compléments Vidéo 4

* Parler de la MRO
* Parler de super()

### Quizz Vidéo 4
### Exercices Vidéo 4


## Vidéo 5 (Variables et attributs)
### NIVEAU: BASIC
### Compléments Vidéo 5
### Quizz Vidéo 5
### Exercices Vidéo 5

Pour mémoire, exercices du précédent MOOC sur Python 2

* proposer quelques exercices un peu vicieux (avec des imports, des
     classes, des fonctions englobantes, etc.)


## Vidéo 6 (Conception d'itérateurs)
### NIVEAU: INTERMEDIAIRE
### Compléments Vidéo 6

### Quizz Vidéo 6
### Exercices Vidéo 6


## Vidéo 7 (Conception d'exceptions personnalisées)
### NIVEAU: INTERMEDIAIRE
### Compléments Vidéo 7
### Quizz Vidéo 7
### Exercices Vidéo 7


## Vidéo 8 (Conception de context manager)
### NIVEAU: INTERMEDIAIRE
### Compléments Vidéo 8

   * parler de
     https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager
     pour faire une contexte manager avec un décorateur et une
     fonction génératrice

   * parler de
     https://docs.python.org/3/library/contextlib.html#contextlib.ContextDecorator
     peut-être n'en parler que lorsque nous parlerons des décorateurs.


   * PEP 343 contains a lot of very nice exemples of context manager,
     we might build on it for exercices
     https://www.python.org/dev/peps/pep-0343/

   Pour mémoire, notebook du précédent MOOC sur Python 2

   * en complément introduire le module logging (ça va bien ici, mais
     si ça fait trop de compléments, on peut le bouger en semaine 6 ou
     7) avec les références
     https://docs.python.org/2/library/logging.html et
     https://docs.python.org/2/howto/logging.html#logging-basic-tutorial

### Quizz Vidéo 8
### Exercices Vidéo 8
