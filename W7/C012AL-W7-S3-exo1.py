# -*- coding: iso-8859-15 -*-

## commençons avec quelque chose de simple
## la fonction built-in type() retourne
## ce que l'on appelle le type d'un objet
## c'est également équivallent à appeler
## l'argument __class__ sur l'objet.
## Donc le type d'un objet c'est la classe
## qui a instancié cet objet. Notons que
## cette classe est aussi un objet

print type('a')
print 'a'.__class__

## les classes new style ont été introduites
## pour répondre à deux problèmes majeurs
## avec les classes classiques qui étaient les
## seuls à exister.
## 1) il n'est pas possible
## avec les classes classiques d'hériter d'un
## type built-in. C'est très ennuyeux parce
## que l'on peut imaginer beaucoup de cas où l'on
## veut simplement légèrement modifier le comportement
## d'un type built-in. En effet, les types built-in
## sont très puissant et constituent une bonne base
## de départ pour de nouvelles classes.
## 2) le type d'une instance d'un type built-in
## est le type built-in. Mais le type d'une intance
## d'une classe classique, n'est pas la classe,
## mais un objet instance. Donc toutes les instances
## des classes classiques sont du type instance.
## c'est inconsistant avec les types built-in, en effet
## on aurait préféré que le type des instances soit
## la classe qui a créé l'instance.

class C:
    pass

class D:
    pass

c = C()
d = D()
## c et d on le même type instance
print type(c)
print type(d)

i = 1
s = 'a'
## mais le type des types built-in est bien celui
## de la classe qui l'a créé
print type(i)
print type(s)

## les classes new-style corrigent ces deux problèmes
## et introduisent d'autres améliorations comme
## la notion de propriété ou comme un nouvel
## algorithme pour parcourir les arbres d'héritage
## en cas d'héritage multiple.
## Ces classes new-style représentent une modification profonde
## du fonctionnement des classes classiques en Python. Cependant,
## dans les versions actuelles de Python 2, les 
##  classes classiques et new-style cohabitent. La principale
## raison est de ne pas casser la compatibilité avec du code
## ancien. Il faut noter que les classes classiques sont les
## classes par défaut en Python 2.

## Heureusement, les différences entre classes classiques
## et new-style sont sur des applications avancées, donc
## le fait que les classes classiques soient les classes
## par défaut pose rarement un problème. De plus, dès que
## l'on est dans un cas qui à nécessite des classes new-style
## comme l'héritage d'un type built-in ou d'une classe new-style
## la classe sera automatiquement new-style.

## Cependant, c'est une bonne
## habitude de toujours démarrer un nouveau projet avec les
## classes new-style et de ne réserver les classes classiques
## que pour les projets existants utilisant déjà des classes
## classiques. 

## regardons maintenant comment créer une classe new style.
## Il faut soit hériter d'un type built-in, soit d'une classe
## new-style, soit de object. 

class C(object):
    pass

## le type de l'instance est bien la classe C
c = C()
print type(c)
print type (C)

class D(list):
    pass

## le type de l'instance est bien la classe C
d = D()
print type(d)



