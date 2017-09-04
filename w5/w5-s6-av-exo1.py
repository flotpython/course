# -*- coding: utf-8 -*-

## Lorsque l'on importe un module on utilise l'instruction import
## suivi du nom du module. Ce nom a deux rôles, Le premier est de
## donner le nom du fichier devant être importé pour créer l'objet
## module. Le deuxième est de donner le nom de la variable qui
## référencera l'objet module importé. Prenons l'exemple du module os.

import os

## os est une variable qui référence l'objet module os

print(os)

## mais c'est également un nom de fichier, le fichier os.py. 

## Regardons maintenant le processus d'importation. Ce processus se
## déroule en trois étapes.

## La première étape consiste à trouver le fichier module sur le
## disque dur. L'interpréteur va chercher le module à importer dans le
## répertoire courant. Si l'interpréteur Python ne trouve pas le
## fichier il va chercher dans les répertoires contenus dans la
## variable d'environement système PYTHONPATH.

## utilisons os.environ qui est un dictionnaire qui contient toutes
## les variables d'environement dans le système.

os.environ['PYTHONPATH']

## Si le fichier n'est toujours pas trouvé, il sera cherché
## dans les répertoires des librairies standards.

## Si vous n'êtes pas sûr des chemins suivis, ils sont tous dans
## l'attribut sys.path qui référence une liste de tous les chemins qui
## sont utilisés dans la recherche du module. Notons que ces chemins
## sont parcourus dans l'ordre de la liste.

import sys
print(sys.path)


## il est possible de modifier sys.path en cours d'exécution du
## programme et donc de modifier les chemins de recherche ou leur
## ordre.

## La deuxième étape consiste à compiler le fichier module en byte
## code. Attention, il ne s'agit pas de code machine mais de code
## préparé à être exécuté directement sur une machine virtuelle. Le
## fichier compilé finit par un .pyc et est contenu dans un répertoire
## spéciale qui s'appelle __pycache__.  Comme cette opération
## compilation prend du temps, elle n'est exécutée que si le fichier
## .pyc n'existe pas encore ou si le fichier source .py a changé
## depuis la derniere compilation.

## Pour finir, l'interpréteur Python va exécuter le fichier module (en
## fait, il va exécuter le byte code) pour créer l'objet module et
## tous les objets qu'il contient.  L'interpréteur va exécuter le code
## sequentiellement en créant chaque objet au fur et à mesure. Les
## fonctions sont un cas un peu particulier. L'objet fonction est bien
## créé à l'import séquentiel du module. Par contre, le code contenu
## dans le bloc de code de la fonction ne sera exécuté qu'a l'appel de
## la fonction.

