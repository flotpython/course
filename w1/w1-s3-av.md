Bonjour  

Aujourd'hui nous allons voir rapidement
comment utiliser les outils que nous
utiliserons dans les vidéos.

On va utiliser deux familles d'outils,
d'une part, vous aurez besoin d'un
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
pycharm, spyder, mais même dans ce cas il est
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

[[AL: oui, et comme c'est nul ce rappel de commande
tu peux proposer de faire un ALT-P et ALT-N également]]

Si maintenant je me trompe, que je fais une faute dans le nom de la fonction, par exemple

```
polynom(20)
```

j'obtiens un message d'erreur. Dans ce
cas précis le système envoie ce qu'on
appelle un exception, naturellement on
en reparlera

mais remarquez que le message essaie de
donner le maximum d'informations sur
l'endroit où s'est produit le souci

*****

je vous montre aussi rapidement
comment obtenir un peu d'aide. Je
commence par importer le module
mathématique - là encore je suis obligé
d'utiliser des notions que l'on verra
bien plus en détails par la suite, ne
vous en faites pas

```
import math
```

alors sur cet objet math, on verra que ça s'appelle un module,
je peux pour commencer voir ce qu'il y a dedans avec la fonction `dir`

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
def factoriel(n):
    if n <= 1:
        return 1
    else:
        return n * factoriel(n-1)
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

c'est pratique parce que ce qu'on veut, c'est voir ce que ça donnerait si on exécutait le programme contenu dans le fichier factoriel.

donc j'ai perdu `polynome` mais par contre comme j'ai chargé `factoriel` je peux maintenant utiliser `factoriel`

```
factoriel(10)
```

retourner dans le fichier. modifier le code  par exemple pour retourner 2 quand n<=1

refaire F5 et refaire factoriel(10)

montrer la boucle changer code - retourner le code

Conclure sur IDLE:

* créer des fichiers
* les sauver
* les exécuter dans un environnement "propre"

========================================

Je vais à present vous montrer comment utiliser l'interpréteur python.

L'interpréteur python, c'est central parce que si vous écrivez un programme python et que vous l'installez chez un client ou un utilisateur, il sera indispensable d'y installer l'interpréteur, c'est lui qui fait le travail à run-time.

Par contre on ne peut pas appeler ça un environnement de développement. Je vous montre tout de même le B-A-BA:

Je vais vous montrer son utilisation dans un terminal. Naturellement
une fois votre programme terminé et distribué, vos utilisateurs
n'auront pas besoin de lancer un terminal.

Je lance donc un terminal.

Selon les systèmes, vous pouvez lancer une console de ce genre en utilisant
"cmd" sur windows, "xterm" sur linux, ou l'application "Terminal" sur
macos, comme je vais le faire tout de suite.

====================
[[Ouvrir terminal]]

Je me deplace dans le repertoire ou j'ai créé factoriel.py

``
$ cd Documents
```

```
python -V
```

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
à l'heure dans IDLE, mais en plus basique (pas de couleur, pas de complétion, possibilités d'édition limitées..)

Mais pour ce genre d'usage, en tous cas dans les vidéos, nous utiliserons plutôt ipython, que je vais vous montrer dans un instant.

```
exit()
```

Par contre je vais vous montrer comment utiliser l'interpréteur pour lancer un programme.

```
cat factoriel.py
```

La façon de lancer un programme c'est tout simplement d'invoquer python avec un nom de ficher qui contient le programme;

Par exemple je vais repartir de `fact.py`, mais je vais devoir l'éditer pour qu'il fasse quelque chose par ce que dans l'état on a défini une fonction mais on ne l'a pas appelée

```
emacs factoriel.py
```

> ajouter à la fin print(fact(100))

```
python factoriel.py
```

Donc voilà, l'interpréteur python c'est tout simplement le programme que **l'on lance pour exécuter un programme python**

====================

Je vais maintenant vous montrer très rapidement **ipython**,
que l'on va utiliser assez fréquement
dans les vidéos; 

ipython, fonctionnellement c'est comme l'interpréteur python, ça
tourne dans un terminal et ça répond au
fur et à mesure, mais c'est juste **plus agréable** à utiliser

```
$ ipython
```

```
def fibonacci(n):
    return 1 if n <= 1 else return fibonacci(n-1) + fibonacci(n-2)
```

```
fibo[TAB]
```

```
fibonacci?
```

```
import math
math.[TAB]
```
> pick `math.ceil`

```
math.ceil?
```

**les flêches**

Je vous montre aussi comment on remonte dans l'historique, cette fois c'est plus simple que sous IDLE pour remonter, mais il faut bien penser à aller au bout de la ligne avant de faire Entrée

```
exit()
```

====================
Voila qui conclut la présentation de python, ipython et IDLE
Je vous retrouve la prochaine fois pour vous montrer les notebooks; 

à bientôt
