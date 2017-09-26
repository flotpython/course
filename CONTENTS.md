Plan du MOOC sur Python 3
=================================

## Semaine 1
### Thème: Introduction au MOOC et aux outils Python
### Niveau: BASIC

* w1-s1: Organisation du MOOC
* w1-s2: Pourquoi Python ?
* w1-s3: Interpréteur et IDLE
* w1-s4: Les notebooks
* w1-s5: Notions de variables, objets et typage dynamique
* w1-s6: Les types numériques 


## Semaine 2 
### Thème: Notions de base pour écrire son premier programme en Python
### Niveau: BASIC

* w2-s1: Codage, jeux de caractères et Unicode
* w2-s2: Les chaînes de caractères
* w2-s3: Les séquences
* w2-s4: Les listes
* w2-s5: Introduction aux tests if et à la syntaxe
* w2-s6: Introduction aux boucles for et aux fonctions
* w2-s7: Introduction aux compréhensions de listes
* w2-s8: Introduction aux modules


## Semaine 3 
### Thème: Renforcement des notions de base, références partagées
### Niveau: BASIC, sauf w3-s8 INTERMÉDIAIRE

* w3-s1: Les fichiers
* w3-s2: Les tuples
* w3-s3: Tables de hash
* w3-s4: Les dictionnaires
* w3-s5: Les ensembles
* w3-s6: Les exceptions
* w3-s7: Les références partagées
* w3-s8: Introduction aux classes


## Semaine 4 
### Thème: Fonctions et portée des variables
### Niveau: BASIC

* w4-s1: Fonctions
* w4-s2: Tests if/elif/else et opérateurs booléens
* w4-s3: Boucles while
* w4-s4: Portée des variables dans les fonctions: règle LEGB
* w4-s5: Modification de la portée avec global et nonlocal
* w4-s6: Passage d'arguments et appel de fonctions


## Semaine 5 
### Thème: Itération, importation et espace de nommage
### Niveau: BASIC

* w5-s1: Itérable, itérateur, itération
* w5-s2: Objet fonction, fonction lambda, map et filter
* w5-s3: Compréhension de listes, sets et dictionnaires
* w5-s4: Expressions et fonctions génératrices
* w5-s5: Modules et espaces de nommage
* w5-s6: Processus d'importation des modules
* w5-s7: Importation des modules et espaces de nommage


## Semaine 6 
### Thème: Conception des classes
### Niveau: BASIC, sauf w6-s6, s6-s7, s6-s8 INTERMÉDIAIRE

* w6-s1: Classes, instances et méthodes
* w6-s2: Méthodes spéciales
* w6-s3: Héritage
* w6-s4: Héritage multiple et ordre de résolution des attributs
* w6-s5: Variables et attributs
* w6-s6: Conception d'itérateurs
* w6-s7: Conception d'exceptions personnalisées
* w6-s8: Conception de context manager


## Semaine 7
### Thème: L'écosystème data science Python
### Niveau: BASIC

* status le 22/09

On n'aura pas le temps de tourner toutes
ces vidéos, en tous cas pas cette année,
on a convenu que ce serait
principalement des notebooks

Cela dit MHC me suggère de faire tout de
même une vidéo d'introduction, et je
pense qu'elle a raison et que ça
fluidifiera le tout.


* w7-s1: introduction, survol des différents outils
* w7-s2: numpy
* w7-s3: pandas
* w7-s4: matplotlib


## Semaine 8
### Thème: Programmation asynchrone - asyncio
### Niveau: AVANCÉ

* w8-s1: Programmation asynchrone
* w8-s2: Quelques exemples simples
* w8-s3: asyncio : historique et écosystème
* w8-s4: Extensions asynchrones du langage
* w8-s5: Coroutines et awaitables
* w8-s6: Boucles d'événements
* w8-s7: Tâches et exceptions
* w8-s8: La librairie asyncio
* w8-s9: Bonnes pratiques 


## Semaine 9
### Thème: Sujets avancés
### Niveau: AVANCÉ

* w9-s1: Méthodes statiques et de classe
* w9-s2: Les décorateurs
* w9-s3: property et descripteurs 
* w9-s4: Les métaclasses
* w9-s5: Conclusion du MOOC


## Semaine 10

**Du temps pour les mini-projets ?**

****
****
****

# DROPPED/TODO LATER

* w9-s5: La performance en Python
  * essayer de parler de profilage (%timeit %prun %lineprofiler), ça
    serait bien de parler du décompilateur, mais je connais très mal.


# Compléments

* type hints
  * il faut à mon avis qu'on mentionne ça dans au moins une vidéo - même si c'est pour dire que ce sera traité comme un complément; par exemple W1-S5, quoique c'est sans doute trop tôt..

## librairies utiles 
* pytest
* Date DateTime
* docstrings + tools
* regexp
  * en semaine 2 lorsqu'on parle des string, ça me semble bien dans un complément avancé. 

* un truc qui serait à mon avis pas mal; en semaine 8, ajouter une séquence 'projet type sous github'; sans nécessairement entrer trop dans les détails, on pourrait partir d'un projet déjà existant dans github et montrer:
  * la structure habituelle (setup.py, lalib/, )
  * où sont les tests
  * où est écrite la doc, comment on la génère, et le résultat sur redthedocs.io
  * j'avait un [squelette de projet de ce genre](https://gitlab.com/parmentelat/minisim2) 
  * [AL] C'est une bonne idée, dans un genre similaire, on pourrait faire une review de code et expliquer comment l'améliorer (e.g., http://sametmax.com/revue-de-code-publique/)
  


IDEA TO DISCUSS
===============
au lieu d'introduire le contenu de la semaine dans la premiere vidéo
(ce qui fige la réorganization des vidéo), faire une vidéo 0 en chaque 
début de semaine pour introduire le contenu de la semaine. 


DRAFT
======
Python 3:

introduire tot les notions de différents objets (type buit-in, classe,
module et expliquer le role de chaque type d'objet). 

* faire une classe qui prend un phrase et construit une liste de mots,
implémenter   `str`  , `__len__`, `__contains__`
* couvrir unittest (Thierry: je préconise plutôt `pytest` qui est un surensemble)
* sourire dans les vidéos
* faire des exercices d'application faisant quelque chose d'utile
* corriger des exercices en vidéo
* pour les notions avancées commencer par expliquer à quoi ça sert
(décorateur, métaclasse, descripteurs, etc.)



    
	
	
	
