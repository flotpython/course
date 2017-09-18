Plan général du MOOC sur Python 3
=================================

## Week 1

**Thème de la semaine**: Introduction au MOOC 

**Niveau**: BASIC

* W1-S0: Présentation de la première semaine
* W1-S1: Organisation du MOOC
* W1-S2: Pourquoi Python 3
* W1-S3: Les notebooks
* W1-S4: iPython
* W1-S5: IDLE
  * dire un mot sur pycharm pour expliquer que IDLE c'est super pour taper des petits exemples dans un environement de dev, les notebooks, c'est super pour faire pleins de petits exemples avec du texte formaté, des figures et voir immédiatement le résultat. Mais pour faire un gros programme (disons à partir d'une centaine de lignes), seul un vrai éditeur avec du refactoring intégré, des suggestions avancées, lint, etc. comme pycharm est utilisable. 
* W1-S6: Introduction aux notions de variables, objets et typage dynamique
* W1-S7: Les types numériques 

## Week 2 
**Thème de la semaine**: Notions de base 

**Niveau**: BASIC

* W2-S0: Présentation de la deuxième semaine
* W2-S1: Codage, jeux de caractères et unicode
* W2-S2: Les chaînes de caractères
* W2-S3: Les séquences
* W2-S4: Les listes
* W2-S5: Introduction aux tests if else, conventions de codage
* W2-S6: Introduction aux boucles for et aux fonctions
* W2-S7: Introduction aux compréhensions de listes
* W2-S8: Introduction aux modules

## Week 3 
**Thème de la semaine**: Suite des notions de base, références
partagées

**Niveau**: BASIC, sauf W3-S8 INTERMÉDIAIRE*

* W3-S0: Présentation de la troisième semaine
* W3-S1: Les fichiers
* W3-S2: Les tuples
* W3-S3: Tables de hash
* W3-S4: Les dictionnaires
* W3-S5: Les ensembles
* W3-S6: Les exceptions
* W3-S7: Les références partagées
* W3-S8: Introduction aux classes

## Week 4 
**Thème de la semaine**: Fonctions et portée des variables

**Niveau**: BASIC

* W4-S0: Présentation de la quatrième semaine
* W4-S1: Fonctions
* W4-S2: Les tests if/elif/else et les opérateurs booléens
* W4-S3: Boucle while
* W4-S4: Portée des variables dans les fonctions: règle LEGB
* W4-S5: Modification de la portée avec global et nonlocal
* W4-S6: Passage d'arguments et appel de fonctions

## Week 5 (NIVEAU BASIC)
**Thème de la semaine**: Itération, importation et espace de nommage

**Niveau**: BASIC

* W5-S0: Présentation de la cinquième semaine
* W5-S1: Itérable, itérateur, itération
* W5-S2: Objet fonction, fonction lambda, map et filter
* W5-S3: Compréhension de listes, sets et dictionnaires
* W5-S4: Expressions et fonctions génératrices
* W5-S5: Modules et espaces de nommage
* W5-S6: Processus d'importation des modules
* W5-S7: Impact de l'importation des modules sur les espaces de nommage


## Week 6 
**Thème de la semaine**: Conception des classes

**Niveau**: BASIC, sauf w6-s6, s6-s7, s6-s8 INTERMÉDIAIRE

* W6-S0: Présentation de la sixième semaine
* W6-S1: Classes, instances et méthodes
* W6-S2: Méthodes spéciales
* W6-S3: Héritage
* W6-S4: Héritage multiple et ordre de résolution des attributs
* W6-S5: Définition et référencement des variables et des attributs
* W6-S6: Conception d'itérateurs
* W6-S7: Conception d'exceptions personnalisées
* W6-S8: Conception de context manager

## Week 7
**Thème de la semaine**: L'ecosystème data science Python

**Niveau**: BASIC

* W7-S0: Présentation de la septième semaine
* W7-S1: installer son environnement et survol des différents outils (numpy, panda, matplotlib, scikitlearn, scipy)
* W7-S2: présentation de numpy
* W7-S3: présentation de pandas
* W7-S4: matplotlib

## Week 8
**Thème de la semaine**: Programmation asynchrone - asyncio

**Niveau**: AVANCÉ

* w8-s0: Présentation de la huitième semaine
* w8-s1: Programmation asynchrone
* w8-s2: Quelques exemples simples
* w8-s3: asyncio : historique et écosystème
* w8-s4: Extensions asynchrones du langage
* w8-s5: Boucles d'événements
* w8-s6: Tâches et exceptions
* w8-s7: La librairie asyncio
* w8-s8: Bonnes pratiques (écrite mais peut-être inutile)

### Notes
* liste des séquences me semble stable
  sauf la dernière que je vais peut-être supprime complètement
  
* (AL: on ne peut pas parler d'asyncio dans dire un mot sur les threads, le GIL et le multiprocess)
* (TP: je couvre très rapidement le multiprocess; par contre à ce stade je ne prévois pas de parler du GIL; dans un complément peut-être un jour..)

## Week 9
**Thème de la semaine**: Sujets avancés

**Niveau**: AVANCÉ

* W9-S0: Présentation de la neuvième semaine
* W9-S1: Méthodes statiques et de classe
* W9-S2: Les décorateurs
* W9-S3: La gestion avancée des attributs
	* property et descripteurs 
* W9-S4: Les métaclasses
* W9-S5: Conclusion du MOOC


## Week 10

**Du temps pour les mini-projets ?**

****
****
****

# DROPPED/TODO LATER

* W9-S5: La performance en Python
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



    
	
	
	
