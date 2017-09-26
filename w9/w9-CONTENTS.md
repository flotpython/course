# -*- coding: utf-8 -*-
# -*- eval: (auto-fill-mode 0) -*-

## Vidéo 0 (Présentation de la neuvième semaine)

## Vidéo 1 (Méthodes statiques et de classe)
### NIVEAU: AVANCÉ
### Compléments Vidéo 1
### Quizz Vidéo 1
### Exercices Vidéo 1


## Vidéo 2 (Les décorateurs)
### NIVEAU: AVANCÉ
### Compléments Vidéo 2

* **parler de cloture** et de décoration avec une méthode (cloture,
  nonlocal, attribut de méthode).
* parler de functools.wraps pour garder les métadonnées de la
  fonction décorée
* comment passer des arguments à un décorateur
* comment avoir plusieurs décorateurs sur une même fonction
* décoration de méthodes
* parler des décorateurs de classe

Pour mémoire, notebook du précédent MOOC sur Python 2

* OK (S2-C1-)Complement-decorateurs.ipynb
* les exemples pratiques que tu as déjà faits. 
* (initialement avec les context managers) : montrer cet exemple et
  le comparer avec les décorateur

```
import time
class Timer():    
    def __enter__(self):
        self.start = time.clock()
        return self
    def __exit__(self, *args):
        self.end = time.clock()
        print "duree d'execution : " + \
              str(self.end - self.start)
        return False

with Timer() as t:
    [x ** 3 for x in xrange(1000000)]
    print 1/0
```

### Quizz Vidéo 2
### Exercices Vidéo 2


## Vidéo 3 (La gestion avancée des attributs)
### NIVEAU: AVANCÉ
### Compléments Vidéo 3

   * complément property (get, set, del, doc)
   * notation de décorateur pour les property
   * give a reference to
     https://docs.python.org/3/howto/descriptor.html
   * parler de data et non-data descripteur
   * expliquer comment rendre un descripteur read-only
     (AttributeError) dans la méthode __set__
   
### Quizz Vidéo 3
### Exercices Vidéo 3

## Vidéo 4 (Les métaclasses)
### NIVEAU: AVANCÉ
### Compléments Vidéo 4
Pour mémoire, notebook du précédent MOOC sur Python 2

* lien vers
     https://www.python.org/download/releases/2.2.3/descrintro#metaclasses

### Quizz Vidéo 4
### Exercices Vidéo 4


## Vidéo 5 (Conclusion du MOOC)
### NIVEAU: INTERMEDIAIRE
### Compléments Vidéo 5
### Quizz Vidéo 5
### Exercices Vidéo 5


