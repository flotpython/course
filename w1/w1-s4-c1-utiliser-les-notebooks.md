---
jupytext:
  cell_metadata_filter: all
  notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# "Notebooks" Jupyter comme support de cours

+++

Pour illustrer les vidéos du MOOC, nous avons choisi d'utiliser Jupyter pour vous rédiger les documents "mixtes" contenant du texte et du code Python, qu'on appelle des "notebooks", et dont le présent document est un exemple.

Nous allons, dans la suite, utiliser du code Python, pourtant nous n'avons pas encore abordé le langage. Pas d'inquiétude, ce code est uniquement destiné à valider le fonctionnement des notebooks, et nous n'utilisons que des choses très simples.

+++

### Avertissement : réglages du navigateur

+++

Avant toute chose, pour un bon fonctionnement des notebooks, on rappelle qu'il est nécessaire d'avoir **autorisé** dans votre navigateur les **cookies** en provenance du site Internet **`nbhosting.inria.fr`**, qui héberge l'infrastructure qui héberge tous les notebooks.

+++

### Avantages des notebooks

+++

Comme vous le voyez, ce support permet un format plus lisible que des commentaires dans un fichier de code.

+++

Nous attirons votre attention sur le fait que **les fragments de code peuvent être évalués et modifiés**. Ainsi vous pouvez facilement essayer des variantes autour du notebook original.

Notez bien également que le code Python est interprété **sur une machine distante**, ce qui vous permet de faire vos premiers pas avant même d'avoir procédé à l'installation de Python sur votre propre ordinateur.

+++

### Comment utiliser les notebooks

+++

En haut du notebook, vous avez une barre de menu (sur fond bleu clair), contenant :

* un titre pour le notebook, avec un numéro de version ;
* une barre de menus avec les entrées `File`, `Insert`, `Cell`, `Kernel`;
* et une barre de boutons qui sont des raccourcis vers certains menus fréquemment utilisés. Si vous laissez votre souris au dessus d'un bouton, un petit texte apparaît, indiquant à quelle fonction correspond ce bouton.

Nous avons vu dans la vidéo qu'un notebook est constitué d'une suite de cellules, soit textuelles, soit contenant du code. Les cellules de code sont facilement reconnaissables, elles sont précédées de `In [ ]:`. La cellule qui suit celle que vous êtes en train de lire est une cellule de code.

Pour commencer, sélectionnez cette cellule de code avec votre souris, et appuyez dans la barre de menu - en haut du notebook, donc - sur celui en forme de flèche triangulaire vers la droite (Play) :
<img src="media/notebook-eval-button.png">

```{code-cell}
20 * 30
```

Comme vous le voyez, la cellule est "exécutée" (on dira plus volontiers évaluée), et on passe à la cellule suivante.

Alternativement, vous pouvez simplement taper au clavier ***Shift+Enter***, ou selon les claviers ***Maj-Entrée***, pour obtenir le même effet. D'une manière générale, il est important d'apprendre et d'utiliser les raccourcis clavier, cela vous fera gagner beaucoup de temps par la suite.

+++

La façon habituelle d'*exécuter* l'ensemble du notebook consiste :

* à sélectionner la première cellule,
* et à taper ***Shift+Enter*** jusqu'à atteindre la fin du notebook.

+++

Lorsqu'une cellule de code a été évaluée, Jupyter ajoute sous la cellule `In` une cellule `Out` qui donne le résultat du fragment Python, soit ci-dessus 600.

Jupyter ajoute également un nombre entre les crochets pour afficher, par exemple ci-dessus, `In [1]:`. Ce nombre vous permet de retrouver l'ordre dans lequel les cellules ont été évaluées.

+++

Vous pouvez naturellement modifier ces cellules de code pour faire des essais ; ainsi vous pouvez vous servir du modèle ci-dessous pour calculer la racine carrée de 3, ou essayer la fonction sur un nombre négatif et voir comment est signalée l'erreur.

```{code-cell}
# math.sqrt (pour square root) calcule la racine carrée
import math
math.sqrt(2)
```

On peut également évaluer tout le notebook en une seule fois en utilisant le menu *Cell -> Run All*.

+++

### Attention à bien évaluer les cellules dans l'ordre

+++

Il est important que les cellules de code soient évaluées dans le bon ordre. Si vous ne respectez pas l'ordre dans lequel les cellules de code sont présentées, le résultat peut être inattendu.

En fait, évaluer un programme sous forme de notebook revient à le découper en petits fragments, et si on exécute ces fragments dans le désordre, on obtient naturellement un programme différent.

+++

On le voit sur cet exemple :

```{code-cell}
message = "Faites attention à l'ordre dans lequel vous évaluez les notebooks"
```

```{code-cell}
print(message)
```

Si un peu plus loin dans le notebook on fait par exemple :

```{code-cell}
# ceci a pour effet d'effacer la variable 'message'
del message
```

qui rend le symbole `message` indéfini, alors bien sûr on ne peut plus évaluer la cellule qui fait `print` puisque la variable `message` n'est plus connue de l'interpréteur.

+++

### Réinitialiser l'interpréteur

+++

Si vous faites trop de modifications, ou perdez le fil de ce que vous avez évalué, il peut être utile de redémarrer votre interpréteur. Le menu *Kernel → Restart* vous permet de faire cela, un peu à la manière de IDLE qui repart d'un interpréteur vierge lorsque vous utilisez la fonction F5.

+++

Le menu *Kernel → Interrupt* peut être quant à lui utilisé si votre fragment prend trop longtemps à s'exécuter (par exemple vous avez écrit une boucle dont la logique est cassée et qui ne termine pas).

+++

### Vous travaillez sur une copie

+++

Un des avantages principaux des notebooks est de vous permettre de modifier le code que nous avons écrit, et de voir par vous-même comment se comporte le code modifié.

Pour cette raison, chaque élève dispose de sa **propre copie** de chaque notebook, vous pouvez bien sûr apporter toutes les modifications que vous souhaitez à vos notebooks sans affecter les autres étudiants.

+++

### Revenir à la version du cours

+++

Vous pouvez toujours revenir à la version "du cours" grâce au menu
*File → Reset to original*.

+++

Attention, avec cette fonction vous restaurez **tout le notebook** et donc **vous perdez vos modifications sur ce notebook**.

+++

### Télécharger au format Python

+++

Vous pouvez télécharger un notebook au format Python sur votre ordinateur grâce au menu
*File → Download as → Python*

+++

Les cellules de texte sont préservées dans le résultat sous forme de commentaires Python.

+++

### Partager un notebook en lecture seule

+++

Enfin, avec le menu *File → Share static version*, vous pouvez publier une version en lecture seule de votre notebook ; vous obtenez une URL que vous pouvez publier, par exemple pour demander de l'aide sur le forum. Ainsi, les autres étudiants peuvent accéder en lecture seule à votre code.

+++

Notez que lorsque vous utilisez cette fonction plusieurs fois, c'est toujours la dernière version publiée que verront vos camarades, l'URL utilisée reste toujours la même pour un étudiant et un notebook donné.

+++

### Ajouter des cellules

+++

Vous pouvez ajouter une cellule n'importe où dans le document avec le bouton **+** de la barre de boutons.

Aussi, lorsque vous arrivez à la fin du document, une nouvelle cellule est créée chaque fois que vous évaluez la dernière cellule ; de cette façon vous disposez d'un brouillon pour vos propres essais.

À vous de jouer.
