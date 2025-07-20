---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
language_info:
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
nbhosting:
  title: Installer Python
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

# Installer la distribution standard Python

+++

## Complément - niveau basique

+++

Ce complément a pour but de vous donner quelques guides pour l'installation de la distribution standard Python 3.

Notez bien qu'il ne s'agit ici que d'indications, il existe de nombreuses façons de procéder.

En cas de souci, commencez par chercher par vous-même, sur Google ou autre, une solution à votre problème ; pensez également à utiliser le forum du cours.

+++

Le point important est de **bien vérifier le numéro de version** de votre installation qui doit être **au moins 3.6**

+++

## Sachez à qui vous parlez

+++

Mais avant qu'on n'avance sur l'installation proprement dite, il nous faut insister sur un point qui déroute parfois les débutants. On a parfois besoin de recourir à l'emploi d'un terminal, surtout justement pendant la phase d'installation. 

Lorsque c'est le cas, il est important de bien distinguer :

* les cas où on s'adresse **au terminal** (en jargon, on dit le *shell*), 
* et les cas où on s'adresse à **l'interpréteur Python**.

C'est très important car ces deux programmes ne parlent **pas** du tout le **même langage** ! 
Il peut arriver au début qu'on écrive une commande juste, mais au mauvais interlocuteur, et cela peut être source de frustration. Essayons de bien comprendre ce point.

+++

### Le terminal

Je peux dire que je parle à mon **terminal** quand l'invite de commande (en jargon on dit le *prompt*) **se termine par un dollar `$`** - ou un simple chevron `>` sur Windows 

Par exemple sur un mac :

```bash
~/git/flotpython/w1 $ 
```

Ou sur Windows :

```bash
C:\Users>
```

+++

### L'interprète Python

À partir du terminal, je peux lancer un **interpréteur Python**, qui se reconnaît car son prompt est fait de **3 chevrons `>>> `**

```bash
~/git/flotpython/w1 $ python3
Python 3.7.0 (default, Jun 29 2018, 20:14:27)
[Clang 9.0.0 (clang-900.0.39.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

+++

Pour sortir de l'interpréteur Python, et retourner au terminal, j'utilise la fonction Python `exit()` :

```bash
~/git/flotpython/w1 $ python3
>>> 20 * 60
1200
>>> exit()
~/git/flotpython/w1 $ python3
```

+++

### Les erreurs typiques

Gardez bien cette distinction présente à l'esprit, lorsque vous lisez la suite. 
Voici quelques symptômes habituels de ce qu'on obtient si on se trompe.

Par exemple, la commande `python3 -V` est une commande qui s'adresse au terminal ; c'est pourquoi nous la faisons précéder d'un dollar `$ `.

Si vous essayez de la taper alors que vous êtes déjà dans un interpréteur python - ou sous IDLE d'ailleurs -, vous obtenez un message d'erreur de ce genre :

```bash
>>> python3 -V
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'python3' is not defined
```

+++

Réciproquement, si vous essayez de taper du Python directement dans un terminal, ça se passe mal aussi, forcément. Par exemple sur Mac, avec des fragments Python tout simples :

```bash
~/git/flotpython/w1 $ import math
-bash: import: command not found
~/git/flotpython/w1 $ 30 * 60
-bash: 30: command not found
~/git/flotpython/w1 $ foo = 30 * 60
-bash: foo: command not found
```

+++

## Digression - coexistence de Python2 et Python3

+++

Avant l'arrivée de la version 3 de Python, les choses étaient simples, on
exécutait un programme Python avec une seule commande `python`. Depuis
2014-2015, les deux versions de Python ont coexisté, il est nécessaire d'adopter
une convention qui permette d'installer les deux langages sous des noms qui sont
non-ambigus

C'est pourquoi actuellement, on trouve **le plus souvent** la convention
suivante sous Linux et macOS :

* `python3` est pour exécuter les programmes en Python-3 ; du coup on trouve
  alors également les commandes comme `idle3` pour lancer IDLE, et par exemple
  `pip3` pour le gestionnaire de paquets (voir ci-dessous) ;

* `python2` est pour exécuter les programmes en Python-2  (il faut savoir par
ailleurs que MacOS arrive avec un python2 préinstallé, car certaines parties de
l'OS en ont besoin !; du coup sur cet OS on ne peut pas se débarrasser
complètement de Python2)

* enfin selon les systèmes, la commande `python` tout court est un alias pour
  `python2` ou `python3`. De plus en plus souvent bien entendu, `python` désigne
  `python3`.

à titre d'illustration, voici ce que j'obtiens sur mon mac dans mon
environnement de tous les jours (Déc 2022):

```bash
$ python3 -V
Python 3.11.0
$ python2 -V
Python 2.7.16
$ python -V
Python 3.11.0
```

Sous Windows, vous avez un lanceur qui s'appelle `py`. Par défaut, il lance la
version de Python la plus récente installée, mais vous pouvez spécifier une
version spécifique de la manière suivante&nbsp;:

```bash
C:\> py -2.7
```

pour lancer, par exemple, Python en version 2.7. Vous trouverez [toute la documentation nécessaire pour Windows sur cette page (en anglais)](https://docs.python.org/3/using/windows.html)

Pour éviter d'éventuelles confusions, nous précisons toujours `python3` dans le cours.

+++

## Installation de base

+++

### Vous utilisez Windows

+++

La méthode recommandée sur Windows est de partir de la page [https://www.python.org/download](https://www.python.org/download)
où vous trouverez un programme d'installation qui contient tout ce dont vous aurez besoin pour suivre le cours.

Pour vérifier que vous êtes prêt, il vous faut lancer IDLE (quelque part dans le menu Démarrer) et vérifier le numéro de version.

+++

### Vous utilisez macOS

+++

Ici encore, la méthode recommandée est de partir de la page [https://www.python.org/download](https://www.python.org/download)
et d'utiliser le programme d'installation.

Sachez aussi, si vous utilisez déjà MacPorts [https://www.macports.org](https://www.macports.org), que vous pouvez également utiliser cet outil pour installer, par exemple Python 3.6, avec la commande

+++

```bash
$ sudo port install python36
```

+++

### Vous utilisez Linux

+++

Dans ce cas il est très probable que Python-3.x soit déjà disponible sur votre machine. Pour vous en assurer, essayez de lancer la commande `python3` dans un terminal.

+++

##### RHEL / Fedora

+++

Voici par exemple ce qu'on obtient depuis un terminal sur une machine installée en Fedora-20 :

+++

```bash
$ python3
Python 3.6.2 (default, Jul 20 2017, 12:30:02)
[GCC 6.3.1 20161221 (Red Hat 6.3.1-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
```

+++

**Vérifiez bien le numéro de version** qui doit être en 3.*x*. Si vous obtenez un message du style `python3: command not found` utilisez `dnf` (anciennement connu sous le nom de `yum`) pour installer le rpm `python3` comme ceci :

+++

```bash
$ sudo dnf install python3
```

+++

S'agissant d'`idle`, l'éditeur que nous utilisons dans le cours (optionnel si vous êtes familier avec un éditeur de texte), vérifiez sa présence comme ceci :

+++

```bash
$ type idle3
idle is hashed (/usr/bin/idle3)
```

+++

Ici encore, si la commande n'est pas disponible vous pouvez l'installer avec :

+++

```bash
$ sudo yum install python3-tools
```

+++

##### Debian / Ubuntu

+++

Ici encore, Python-2.7 est sans doute déjà disponible. Procédez comme ci-dessus, voici un exemple recueilli dans un terminal sur une machine installée en Ubuntu-14.04/trusty :

+++

```bash
$ python3
Python 3.6.2 (default, Jul 20 2017, 12:30:02)
[GCC 6.3.1 20161221 (Red Hat 6.3.1-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
```

+++

Pour installer Python :

+++

```bash
$ sudo apt-get install python3
```

+++

Pour installer idle :

+++

```bash
$ sudo apt-get install idle3
```

+++

### Installation de bibliothèques complémentaires

+++

Il existe un outil très pratique pour installer des bibliothèques Python, il s'appelle `pip3`, [qui est documenté ici](https://pypi.python.org/pypi/pip)

+++

Sachez aussi, si par ailleurs vous utilisez un gestionnaire de paquets comme `rpm` sur RHEL, `apt-get` sur Debian, ou `port` sur macOS, que de nombreux paquets sont également disponibles au travers de ces outils.

+++

### Anaconda

+++

Sachez qu'il existe beaucoup de distributions alternatives qui incluent Python ; parmi elles, la plus populaire est sans aucun doute [Anaconda](https://www.anaconda.com/), qui contient un grand nombre de bibliothèques de calcul scientifique, et également d'ailleurs Jupyter pour travailler nativement sur des notebooks au format `.ipynb`.

Anaconda vient avec son propre gestionnaire de paquets pour l'installation de bibliothèques supplémentaires qui s'appelle `conda`.

**Mise à jour 2025**:  
Sachez qu'anaconda a récemment (2023?) adopté une nouvelle politique de
licences, et que désormais la version gratuite est limitée à un usage personnel
et éducatif. Si vous envisagez d'utiliser Anaconda dans un cadre professionnel,
il vous faudra souscrire une licence commerciale.  
Nous vous invitons à consulter la [page de
prix](https://www.anaconda.com/pricing) et les autres informations du site
anaconda pour plus de détails.
