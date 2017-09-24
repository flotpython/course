Pas de quiz cette semaine

## Vidéo 0 (Présentation de la neuvième semaine)


## Vidéo 1 Introduction à la programmation asynchrone
### NIVEAU: avancé

* distinction CPU-intensif / IO-intensif;
* exhiber un exemple simple (aller chercher plusieurs pages web) et montrer comment est utilisé le CPU
* écarter rapidement le mode multi-CPUs (qui s'adresse aux applis CPU-intensifs)
* mono CPU / multi-threads: pas de contrôle sur le context switching; sections critiques, dur à débugger...
* callbacks: exhiber saucissonnage délirant https://cdn-images-1.medium.com/max/1600/1*cS467MRjN5awIWqFeD27XQ.jpeg
* utilité de définir un modèle qui permette
 * la concurrence
 * single-thread
 * avec contrôle sur les changements de contexte

### Compléments Vidéo 1 
### Exercices Vidéo 1 


## Vidéo 2 Quelques exemples simples
### NIVEAU: avancé

* plus petit exemple complet (une boucle, deux tâches qui font sleep())
* conclure
  * (async def / await) pour définir les coroutines,
  * librairie asyncio pour la gestion des boucles d'événements (signaler par exemple curio)

* coroutine functions vs coroutine
* montrer ce qui se passe si on appelle une coroutine sans await
* un message d'erreur quand on oublie le await 

### Compléments Vidéo 2
### Exercices Vidéo 2


## Vidéo 3 écosystème asyncio
### NIVEAU: avancé
### Compléments Vidéo 3
### Exercices Vidéo 3


## Vidéo 4 Extensions asynchrones du langage
### NIVEAU: avancé
### Compléments Vidéo 4

* à faire: itérations asynchrones
  async for; compréhension asynchrone;
  [await foo(x) for x in iterator]
  [await foo(x) async for x in async_iterator]
  montrer que c'est différent d'un gather()
  et a creuser
  expressions generatrices asynchrones ?
  generateurs asynchrones ?
  montrer qu'un objet *peut* être context manager synchrone et asynchrone
  dire qu'il manque juste les lambda asynchrones dans 3.6

### Exercices Vidéo 4
### NIVEAU: avancé


## Vidéo 4b coroutines et awaitables

* Le protocole awaitable, send(), la pile, await et yield

## Compléments 4b

* montrer que send() et yield permettent de causer dans les deux sens entre la boucle et les awaitables


## Vidéo 5 La boucle d'événements
### NIVEAU: avancé

* ensure_future & run_forever() - Queue()
* ensure_future pour ajouter une tâche au milieu d'un scénario
* parler de get_event_loop()

### Compléments Vidéo 5

* montrer l'importance de get-event_loop pour accéder à la boucle
  courante depuis le code asynchrone (trouver un exemple ou le code
  asynchrone a besoin d'accéder à la boucle..)

* un complément sur stop() et close() et ces choses-là ce serait
  vraiment bien, est-ce facile à faire ? il faudra sans doute que les
  apprenants interrompent le kernel, ça peut être tricky, mais pas
  sûr...

* un complément sur la notion de Tâche
  voir dans tutorial.ipynb la section avec monitor_tasks()
  qu'il faudra sans doute simplifier un peu

* un complément sur wait() - cf. asynciojobs
  https://docs.python.org/3/library/asyncio-task.html#asyncio.wait

### Exercices Vidéo 5


## Vidéo 6 Tâches et exceptions
### NIVEAU: avancé

* animation de la boucle, les piles, et comment sont gérées les exceptions

### Compléments Vidéo 6

* des exemples de tâches qu'on cancelle, de boucle qu'on arrête, ce
  genre de trucs

* peut-être le bon endroit pour parler de wait() ?

### Compléments Vidéo 6

* s'inspirer de raise2.py qui montre comment monitorer les tâches
  d'une boucle, regarder les résultats et les exceptions..


## Vidéo 7 La librairie asyncio 
### NIVEAU: avancé

* Queue 

* ~~Subprocess~~ je crois que finalement subprocess j'ai pas le temps
  d'en parler

* transition: insister sur le fait que la boucle d'évenements sait dialoguer avec
  l'OS pour faire son job de manière efficace

* mentionner Transport/Protocol + Stream
  -> compléments / utiliser des lib. de haut niveau
     comme aiohttp asyncssh

### Compléments Vidéo 7

* a minima un exemple avec Lock
  parler de connection partagée (e.g. ssh) par plusieurs sessions ->
  tout de même besoin de gérer les accès parallèles
* un protocole de bas niveau avec connection_made() connection_lost() 
* montrer un serveur TCP encore + basique tel que dans 
  https://www.python.org/dev/peps/pep-0492/#types-coroutine
  se méfier tout de même, on risque d'être limité par l'infra de
  notebooks, qui utilise localhost...

### Exercices Vidéo 7


## Vidéo 8 bonnes pratiques
### NIVEAU: avancé

* quels appels entre monde synchrone et monde asynchrone sont légaux ou pas
* bien penser à ne pas bloquer pendant trop longtemps
* lire les exceptions des tâches

NOTES

* le seul truc qui reste nouveau c'est la digression sur les
awaitables
* qu'on pourrait bouger dans w8-s4 (extensions asynchrones du langage)

* sinon à ce stade tout ce qui est là dedans ce sont des redites, je me
demande si ça vaut le coup de tourner ça ou pas; on pourrait
transformer le notebook en compléments, car ça vaut qd même le coup de
bien insister sur ces deux points.

### Compléments Vidéo 8
### Exercices Vidéo 8

*****

# Idées

* pour les complements, ajouter un lien vers
  https://www.youtube.com/watch?v=2ZFFv-wZ8_g
  le talk de Yuri Selivanov - etat de asyncio pour PyCon'17

* contagion: exemple d'un parser; un parser travaille sur un fichier
  complet et pas à priori de manière incrémentale

* trade-off entre une approche 'monkey-patch' à la gevent, vs une
  approche explicite avec async/await

* très intéressant - pour un complément:
  https://mdk.fr/blog/python-coroutines-with-async-and-await.html
  pour implémenter sa propre mini-loop et bien comprendre send et yield et StopIteration et tout ça
