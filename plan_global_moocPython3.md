Plan général du MOOC sur Python 3
=================================

## Week 1
**Thème de la semaine**: introduction au MOOC et aux outils Python utilisés dans le MOOC

* W1-S1: Organisation du MOOC
* W1-S2: Pourquoi Python 3
* W1-S3: iPython
* W1-S4: Les notebooks
* W1-S5: IDLE
	* dire un mot sur pycharm pour expliquer que IDLE c'est super pour taper des petits exemples dans un environement de dev, les notebooks, c'est super pour faire pleins de petits exemples avec du texte formaté, des figures et voir immédiatement le résultat. Mais pour faire un gros programme (disons à partir d'une centaine de ligne), seul un vrai éditeur avec du refactoring intégré, des suggestions avancés, lint, etc. comme pycharm est utilisable. 
* W1-S6: Introduction aux notions de variables, objets et typage dynamique
* W1-S7: Les types numériques 

## Week 2
**Thème de la semaine**: découverte des types builtins (entiers, listes, chaines de caractères)

* W2-S1: Les chaînes de caractères, explication unicode, print (format, f-string) (2 vidéos probablement)
	* ne pas passer du temps sur des choses peu importante pour ne pas alourdir la vidéo (comme les docstrings)
* W2-S2: Les séquences
* W2-S3: Les listes
* W2-S4: Introduction aux tests if/else et aux expressions conditionnelles + indentation comme syntaxe de base
* W2-S5: Introduction aux boucles for et aux fonctions
* W2-S6: Introduction aux modules
* W2-S7: Les fichiers (introduction aux contexts managers)

## Week 3
**Thème de la semaine**: Fin des types builtins et introduction aux modules et aux classes

* W3-S1: Les tuples
* W3-S2: Tables de hash
* W3-S3: Les dictionnaires
* W3-S4: Les ensembles
* W3-S5: Les exceptions
* W3-S6: Les références partagées
* W3-S7: Les modules pour créer nos objets
* W3-S8: Les classes pour créer nos objets 
	* quoi utiliser pour créer des objets en Python fonction, module ou classe

## Week 4
**Thème de la semaine**: Fontions

* W4-S1: Fonctions
	* une fonction crée une référence partagée
* W4-S2: Les tests if/elif/else et les opérateurs booléens (faire un exemple d'analyseur de syntaxe)
* W4-S3: Boucle while (continuer l'exemple d'analyseur de syntaxe)
* W4-S4: Portée des variables dans les fonctions: règle LEG
		* variable liaison statique, attributs calculés à runtime ?
* W4-S5: Portée des variables dans les fonctions et références partagées
* W4-S6: Passage d'arguments et appel de fonctions
	* exemple pratique de passage d'arguments/unpacking

## Week 5
**Thème de la semaine**: Itération et importation

* W5-S1: Les boucles for et les itérateurs
* W5-S2: Fonction lambda, programmation fonctionnelle
* W5-S3: Compréhension de listes, sets et dictionnaires + expressions génératrices
* W5-S4: Fonctions génératrices
* W5-S5: L'itération en Python
	* expliquer que Python est construit autour de cette notion d'itération, qu'il faut toujours utiliser l'itération, qu'il faut éviter de créer des structures de données si on n'en n'a pas besoin tout de suite (expression génératrice plutôt que compréhension)
	* illustrer le gain de performance entre une boucle for sur des indices (à la Java) et une comrpréhension
* W5-S6: Modules et espaces de nommage
* W5-S7: Processus d'importation des modules
* W5-S8: Importation de modules et espace de nommage


## Week 6
**Thème de la semaine**: Conception des classes

* W6-S1: Classes, instances et méthodes
* W6-S2: Héritage
* W6-S3: Surcharge d'opérateurs
* W6-S4: Assignation et référencement des variables et des attributs
* W6-S5: Conception d'itérateurs
* W6-S6: Conception d'exceptions personnalisées
* W6-S7: Conception de context manager

## Week 7
**Thème de la semaine**: l'ecosystème data science Python

* W7-S1: installer son environement et survol des différents outils (numpy, panda, matplotlib, scikitlearn, scipy)
* W7-S2: présentation de numpy
* W7-S3: présentation de pandas
* W7-S4: matplotlib

## Week 8 
**Thème de la semaine**: Sujets avancés de Python

* W8-S1: Méthodes statiques et de classe
* W8-S2: Les décorateurs
* W8-S3: La gestion avancée des attributs
: property et descripteurs 
* W8-S4: Les métaclasses
* W8-S5: La performance en Python


## Week 9

(asyncio est suffisament difficile pour avoir une semaine pour lui, si on est malin dans la présentation, on pourra faire de nouvelles vidéos rien que sur ça ou améliorer modulairement sans toucher aux autres semaines)

**Thème de la semaine**: asyncio

* W9-S1: co-routines
* W9-S2: asyncio

## Week 10

**Du temps pour les mini-projets ?**

Compléments
===========

* librairies utiles 
* type hints
	  * il faut à mon avis qu'on mentionne ça dans au moins une vidéo - même si c'est pour dire que ce sera traité comme un complément; par exemple W1-S5, quoique c'est sans doute trop tôt..
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



    
	
	
	
