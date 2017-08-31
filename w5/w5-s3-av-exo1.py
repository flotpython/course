# -*- coding: utf-8 -*-

## La syntaxe de la compréhension de listes est simple et intuitive
## puisqu'elle est proche du langage naturel. Regardons un exemple :
## j'ai une liste de prénom et je souhaite extraire tous les prénoms
## qui commencent par la lettre a et mettre ces prénoms en minuscule.

prenoms = ['ana', 'eve', 'ALICE', 'Anne', 'bob']
prenoms.extend(prenoms) ## et créons des doublons

[[TP je comprends pas pourquoi on fait cet extend ?]]
[[AL: ça me permet après de montrer la compréhension de set sur cette
  liste]]

a_prenoms = [p.lower() for p in prenoms if p.lower().startswith('a')]

## si on relit cette expression c'est proche du langage naturel :
## donne moi une liste qui contient les prenoms p en minuscule pour
## tous les prenoms dans la liste prenom if le prenom en minuscule
## commence par 'a'

## Il est fréquent pour le débutant de commencer par écrire une boucle
## for et de se rendre compte ensuite que cette boucle peut-être
## remplacée par une compréhension de listes. C'est tout à fait
## normal, et vous verrez qu'avec l'habitude on écrit de plus en plus
## facilement des compréhensions des liste directement.

## Reprenons notre exemple, vous remarquez qu'il y a des prénoms en
## double, comment faire pour enlever les doublons ? On doit
## transformer notre liste en set.

set(a_prenoms)

## cependant, il serait plus efficace de faire directement une
## compréhension de set pour ne pas passer par une liste
## intermédiaire. C'est très simple à faire, il suffit de remplacer
## les crochets par des accolades et on a directement un compréhension
## de set. En effet, la compréhension de set supporte la même syntaxe
## qu'une compréhension de liste, la seul différence est le symbole
## qui entoure la compréhension. 

a_prenoms = {p.lower() for p in prenoms if p.lower().startswith('a')}


## il est important de comprendre ici que cette compréhension de set
## ne crée par une liste temporaire, mais contruit directement un set.

## Regardons maintenant la compréhension de dictionnaire.  Elle
## s'écrit exactement comme une compréhension de set, sauf que l'on
## sépare les clefs et les valeurs par un :

## Pour finir, j'aimerais vous montrer les compréhensions de
## dictionnaires. Les compréhensions de dictionnaires s'écrivent
## exactement comme des compréhensions de set, on utilise simplement
## un ":" pour séparer les clefs des valeurs. Prenons un exemple, j'ai
## une liste de tuple contenant un prénom et un age

ages = [('ana', 20), ('EVE', 30), ('bob', 40)]

## et je veux construire un dictionnaire avec toutes les clefs en
## minuscule uniquement pour les age inférieurs à 40 ans

d = {p.lower():a for p, a in ages if a <40}

## un autre usage courant des compréhensions de dictionnaires et de
## rehasher le dictionnaires en fonction des valeurs (donc d'inverser
## le rôle des clefs et des valeurs). L'intérêt et de pouvoir faire
## des recherchers rapides sur les valeurs. Évidemment, je dois avoir
## dans ce cas des valeurs hashables et uniques.

d2 = {a:p for p, a in d.items()}

d2[20]

