# -*- autofill-mode:true; fill-column: 40 -*-
* [[ commencer avec le transparent ]]
* [[ capturer tout l'ecran ]]

Bonjour  
 
Aujourd'hui nous allons voir rapidement
comment utiliser les 2 outils que nous
utiliserons dans les vidéos.

D'une part, vous aurez besoin d'un
environnement de développement,
c'est-à-dire un outil pour écrire votre
code, et l'essayer au fur et à mesure.

D'autre part, pour exécuter un programme
écrit en python, il faut disposer du
"coeur" du langage, c'est-à-dire
l'interpréteur python lui-même.

====================

Je vais commencer par l'environnement de
développement. Nous avons choisi
d'utiliser IDLE dans les vidéos, car il
fait partie de la distribution standard.

Si vous préférez vous pouvez utiliser
autre chose bien sûr, comme emacs, vim,
eclipse, mais même dans ce cas il est
utile que vous sachiez comment
fonctionne IDLE pour suivre les vidéos
avec un maximum de confort.


Je vais lancer IDLE. 

***Montrer le numéro de version, vérifier >= 3.6***

Vous voyez d'abord une fenêtre qui
contient ce qu'on appelle l'interpréteur
interactif. Il est interactif car je
peux y taper directement du code, qui
est exécuté immédiatement au fur et à
mesure.

Commençons par une expression arithmétique toute simple

```
16 * 2000
```

python calcule le résultat et me l'affiche

Je vais un peu plus loin, je définis une petite fonction, par exemple une fonction qui calcule un polynôme, disons $2x^2 + 4x +10$

```
def polynome(x):
    return 2*x**2 + 4*x + 10
```

je vous rappelle que la syntaxe est guidée par la présentation, il me faut donc mettre une indentation au début de la deuxième ligne, j'utilise la touche `tabulation` qui fait ça très bien

```
polynome(10)
```

Si je veux relancer presque la même commande, regardez bien car ça n'est pas tres intuitif au début:

* je remonte avec les flêches du clavier
* une fois sur la ligne qui m'intéresse je fais Entrée; c'est ça qui est un peu perturbant, si je ne fais pas 
* et là l'outil me recopie la ligne et seulement maintenant je peux l'éditer 

```
polynome(100)
```

Si maintenant je me trompe, que je fais une faute dans le nom de la fonction, par exemple

```
polynom(20)
```

j'obtiens un message d'erreur. Dans ce cas précis le système envoie ce qu'on appelle un exception, naturellement on en reparlera 

mais remarquez que le message essaie de donner le maximum d'informations sur l'endroit où s'est produit le souci

*****
je vous montre aussi rapidement comment obtenir un peu d'aide. Je commence par importer le module mathématique - là encore je suis obligé d'utiliser des notions que l'on verra bien plus en détails par la suite, ne vous en faites pas

```
import math
```

alors sur cet objet math, on verra que ça s'appelle un module, je peux pour commencer voir ce qu'il y a dedans avec la fonction `dir` 

```
dir(
```

***s'arrêter et montrer le popup***

remarquez que lorsque j'entre la parenthèse on me montre un peu d'aide sur la fonction dir

```
dir(math)
```

et avec dir j'obtiens le contenu de ce module, par exemple je vois qu'il y a une fonction qui s'appelle `asin`, c'est sûrement arc-sinus; il y a une fonction `sqrt`, si je ne sais pas ce qu'elle fait je utiliser la fonction `help` comme ceci

```
help(math.sqrt) 
```

qui me dit que c'est la racine carrée, sqrt comme square root.

```
math.sqrt(10)
```


***laisser ouvert...***

******

C'est très bien pour faire de tous
petits calculs, et nous ferons ça
souvent pendant le cours

Mais on ne peut pas s'amuser a retaper
le programme a chaque fois - ni meme
bien sur a utiliser un terminal...

C'est pourquoi le programme est stocké
dans un ou plusieurs fichiers, en python
on dit des modules, nous y reviendrons
naturellement

Je vais donc utiliser IDLE pour créer un
fichier

Je fais donc *File* ➝ *New File*

et j'écris une fonction, disons l'incontournable fonction factoriel

```
def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)
```

* ***mettre un commentaire*** expliquer que
la fin de la ligne apres # est ignoré
par le langage sauf bien sur si le # est
dans une chaine de caracteres

* ***mettre un docstring***

C'est là que ça devient intéressant. Je veux exécuter ce morceau de code. Pour ça 
je peux faire *Run* -> *Run Module* - ou de manière équivalente `F5`, c'est plus rapide on fait toujours F5.

Sauf que, la première fois que je fais ça, IDLE va me demander dans quel fichier je veux sauver ça, il lui faut un fichier pour passer ce contenu à python

***choisir fichier `factoriel.py`***

et maintenant ce qui se passe c'est qu'on va redémarrer python; ça se voit très bien, il écrit en gros RESTART

alors ce que ça veut dire c'est qu'il redémarre complètement, tout ce que j'avais fait avant est écrasé, par exemple

```
polynome(10)
```
`polynome is not defined`

pourquoi on fait ça, eh bien en fait c'est simple, lorsque je vais vraiment exécuter ce module factoriel la prochaine fois, puisque polynome ne sera pas défini puisqu'il n'est pas dans le module `fact`.

donc j'ai perdu `polynome` mais par contre comme j'ai chargé `factoriel` je peux maintenant utiliser `fact` 

```
fact(10)
```

retourner dans le fichier. modifier le code  par exemple pour retourner 2 quand n<=1 

refaire F5 et refaire fact(10)

montrer la boucle changer code - retourner le code

Conclure sur IDLE:

* créer des fichiers 
* les sauver 
* les exécuter dans un environnement "propre"

========================================

Je vais à present vous montrer comment utiliser l'interpréteur python.

Comme je l'ai dit tout à l'heure, l'interpréteur est nécessaire
pour exécuter le code. Que vous développiez avec IDLE, ou avec autre
chose, vous avez besoin de l'interpréteur. Et si vous publiez votre
code, vos utilisateurs auront besoin de l'interpréteur.

Je vais vous montrer son utilisation dans un terminal. Naturellement
une fois votre programme terminé et distribué, vos utilisateurs
n'auront pas besoin de lancer un terminal, mais quelle que soit la
façon de lancer votre programme, il y aura une instance de
l'interpréteur à la manoeuvre quelque part dans les processus de
l'ordinateur.

Je lance donc un terminal. 

Selon les systèmes, vous pouvez lancer une console de ce genre en utilisant
"cmd" sur windows, "xterm" sur linux, ou l'application "Terminal" sur
macos, comme je vais le faire tout de suite. 

====================
[[Ouvrir terminal]]

Je me deplace dans le repertoire ou j'ai créé factoriel.py
$ cd MOOC/brouillon

Pour lancer python en mode interactif comme on dit, on le lance sans
argument comme ceci

```
$ python
```

 Taper un truc basique
```
3 * 5
```

c'est aussi simple que possible, cela fonctionne presque exactement comme tout
à l'heure, en plus basique (pas de couleur, d'indentation..)

retaper factoriel 

```
def fact(n):
    return 1 if n <= 1 else n * fact(n-1)
```

montrer qu'on peut remonter dans l'historique cette fois avec **les flêches**

**remplacer 1 par 2**

```
fact(20)
```

en fait python dans ce mode n'est pas connecté à la **souris** ni aux **menus**

```
exit() 
```
[[ Sortir de python ]]

==================== 
Je vous montre très rapidement ipython, que l'on va utiliser assez fréquement dans les vidéos; ipython, fonctionnellement c'est comme python, ça tourne dans un terminal et ça répond au fur et à mesure, mais c'est juste plus agréable à utiliser

```
$ ipython
```

```
def fibo(n):
    return 1 if n <= 1 else return fibo(n-1) + fibo(n-2)
```

**les flêches**

**ajouter un docstring**

```
fibo?
```


==================== 

Je voudrais maintenant vous montrer comment on utilise python pour lancer un vrai programme

reprendre factoriel.py (montrer le contenu)

lancer python factoriel.py, montrer que ça ne fait rien car on n'a pas appelé la fonction

expliquer que c'est le mode de fonctionnement "normal" de python
que le fichier passé en argument s'appelle le point d'entrée

relancer sur factoriel.py avec python -i
appeler la fonction 

***sortir***

====================
Voila qui conclut la présentation de python, ipython et IDLE

J'aimerais attirer votre attention sur le fait que dans les
vidéos, pour des raisons pratiques, on utilise massivement des noms de
variables très courts - pour ne pas passer trop de temps au clavier.
Nous vous recommandons contrairement à ce qui est fait dans la vidéo,
de bien prendre l'habitude, et même dans les exercices, d'utiliser des
identifiants qui soient parlants. 


====================
Je vous retrouve la prochaine fois pour vous montrer les notebooks; à bientôt
