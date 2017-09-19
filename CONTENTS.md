Plan du MOOC sur Python 3
=================================

## Semaine 1
### Thème: Bienvenue, et prise en main des outils utilisés dans le MOOC
### Niveau: BASIC

* w1-s1: Organisation du MOOC
* w1-s2: Pourquoi Python 3
* w1-s3: Interpréteur et IDLE
* w1-s4: Les notebooks
* w1-s5: Introduction aux notions de variables, objets et typage dynamique
* w1-s6: Les types numériques 


## Semaine 2 
### Thème: Notions de base pour écrire son premier programme en Python
### Niveau: BASIC

* w2-s0: Présentation de la deuxième semaine
* w2-s1: Codage, jeux de caractères et unicode
* w2-s2: Les chaînes de caractères
* w2-s3: Les séquences
* w2-s4: Les listes
* w2-s5: Introduction aux tests if/else et aux conventions de codage
* w2-s6: Introduction aux boucles for et aux fonctions
* w2-s7: Introduction aux compréhensions de listes
* w2-s8: Introduction aux modules


## Semaine 3 
### Thème: Renforcement des notions de base, références partagées
### Niveau: BASIC, sauf w3-s8 INTERMÉDIAIRE

* w3-s0: Présentation de la troisième semaine
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

* w4-s0: Présentation de la quatrième semaine
* w4-s1: Fonctions
* w4-s2: Les tests if/elif/else et les opérateurs booléens
* w4-s3: Boucle while
* w4-s4: Portée des variables dans les fonctions: règle LEGB
* w4-s5: Modification de la portée avec global et nonlocal
* w4-s6: Passage d'arguments et appel de fonctions


## Semaine 5 
### Thème: Itération, importation et espace de nommage
### Niveau: BASIC

* w5-s0: Présentation de la cinquième semaine
* w5-s1: Itérable, itérateur, itération
* w5-s2: Objet fonction, fonction lambda, map et filter
* w5-s3: Compréhension de listes, sets et dictionnaires
* w5-s4: Expressions et fonctions génératrices
* w5-s5: Modules et espaces de nommage
* w5-s6: Processus d'importation des modules
* w5-s7: Impact de l'importation des modules sur les espaces de nommage


## Semaine 6 
### Thème: Conception des classes
### Niveau: BASIC, sauf w6-s6, s6-s7, s6-s8 INTERMÉDIAIRE

* w6-s0: Présentation de la sixième semaine
* w6-s1: Classes, instances et méthodes
* w6-s2: Méthodes spéciales
* w6-s3: Héritage
* w6-s4: Héritage multiple et ordre de résolution des attributs
* w6-s5: Définition et référencement des variables et des attributs
* w6-s6: Conception d'itérateurs
* w6-s7: Conception d'exceptions personnalisées
* w6-s8: Conception de context manager


## Semaine 7
### Thème: L'écosystème data science Python
### Niveau: BASIC

* w7-s0: Présentation de la septième semaine
* w7-s1: installer son environnement et survol des différents outils (numpy, panda, matplotlib, scikitlearn, scipy)
* w7-s2: présentation de numpy
* w7-s3: présentation de pandas
* w7-s4: matplotlib


## Semaine 8
### Thème: Programmation asynchrone - asyncio
### Niveau: AVANCÉ

* w8-s0: Présentation de la huitième semaine
* w8-s1: Programmation asynchrone
* w8-s2: Quelques exemples simples
* w8-s3: asyncio : historique et écosystème
* w8-s4: Extensions asynchrones du langage
* w8-s5: Boucles d'événements
* w8-s6: Tâches et exceptions
* w8-s7: La librairie asyncio
* w8-s8: Bonnes pratiques (écrite mais peut-être inutile)


## Semaine 9
### Thème: Sujets avancés
### Niveau: AVANCÉ

* w9-s0: Présentation de la neuvième semaine
* w9-s1: Méthodes statiques et de classe
* w9-s2: Les décorateurs
* w9-s3: La gestion avancée des attributs
	* property et descripteurs 
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



    
	
	
	
