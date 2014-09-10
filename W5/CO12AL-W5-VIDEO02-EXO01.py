# -*- coding: iso-8859-15 -*-

## Lorsque l'on importe un module on utilise l'instruction
## import suivi du nom du module. Ce nom a deux rôles,
## Le premier est de donner le nom du fichier devant
## être importé pour créer l'objet module. Le deuxième
## est de donner le nom de la variable qui pointera vers
## l'objet module importé. Prenons l'exemple du module os. 

import os

## os est une variable qui pointe vers l'objet module os
print os

## mais c'est également un nom de fichier, le fichier os.py
## vous pouvez voir que le fichier de l'objet module
## s'appelle os.pyc, nous allons revenir dessus. 

## Revenons sur le processus d'importation. Ce processus
## se déroule en trois étapes.

## La première étape consiste à trouver le fichier module
## sur le disque dur. L'interpréteur va chercher le module
## à importer dans le répertoire courant, c'est-à-dire,
## dans le repertoire duquel vous avez lancer Python. Si vous
## avez lancé Python depuis un raccourci, le répertoire
## courant sera celui d'installation de Python sur votre
## système. Si l'interpréteur Python ne trouve pas le fichier
## il va chercher dans les répertoires contenus dans la
## variable d'environement système PYTHONPATH.

## utilisons os.environ qui est un dictionnaire qui contient
## toutes les variables d'environement dans le système.

print os.environ.get('PYTHONPATH', '') ## PYHTONPATH n'est pas
                                       ## nécessairement sur le
                                       ## système

## Si le fichier n'est toujours pas trouvé, il sera cherché
## dans le répertoire des librairies standards.

## Tous les chemins suivis par l'interpréteur sont dans
## la variable  sys.path
import sys
print sys.path


## Comme il s'agit d'une liste il est possible de la modifier
## en cours d'exécution du programme.

## La deuxième étape consiste à compiler le fichier module
## en byte code. Attention, il ne s'agit pas de code machine
## mais de code préparé à être exécuté directement sur une
## machine virtuelle. Le fichier compilé finit par un .pyc
## Comme cette opération prend du temps, elle n'est exécutée
## que si le fichier .pyc n'existe pas encore ou si le
## fichier source .py a changé depuis la derniere compilation.

## Pour finir, l'interpréteur Python va exécuter le fichier
## module (en fait, il va exécuter le byte code) pour créer
## l'objet module est tous les objets qu'il contient. 
## L'interpréteur va exécuter le code sequentiellement en
## créant chaque objet au fur et à mesure. Les fonctions
## sont un cas un peu particulier. L'objet fonction est bien
## créé à l'import séquentiel du module. Par contre, le code
## contenu dans le corps de la fonction ne sera exécuté
## qu'a l'appel de la fonction.

## Ouvrons un éditeur IDLE pour comprendre cette exécution
## séquentielle

#f()
#def f():
#    print 'dans f()'
#    g()

## l'objet fonction f() est maintenant créé

#f()
#def g():
#    print 'dans g()'

## l'objet fonction g() est maintenant créé

#f()
