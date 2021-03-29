---
jupytext:
  cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
  notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
notebookname: Tuples
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# La construction de tuples

+++

## Complément - niveau intermédiaire

+++

### Les tuples et la virgule terminale

+++

Comme on l'a vu dans la vidéo, on peut construire un tuple à deux éléments - un couple - de quatre façons :

```{code-cell}
# sans parenthèse ni virgule terminale
couple1 = 1, 2
# avec parenthèses
couple2 = (1, 2)
# avec virgule terminale
couple3 = 1, 2,
# avec parenthèses et virgule
couple4 = (1, 2,)
```

```{code-cell}
# toutes ces formes sont équivalentes ; par exemple
couple1 == couple4
```

Comme on le voit :

* en réalité la **parenthèse est parfois superflue** ; mais il se trouve qu'elle est **largement utilisée** pour améliorer la lisibilité des programmes, sauf dans le cas du _tuple unpacking_ ; nous verrons aussi plus bas qu'elle est **parfois nécessaire** selon l'endroit où le tuple apparaît dans le programme ;
* la **dernière virgule est optionnelle** aussi, c'est le cas pour les tuples à au moins 2 éléments - nous verrons plus bas le cas des tuples à un seul élément.

+++

### Conseil pour la présentation sur plusieurs lignes

+++

En général d'ailleurs, la forme avec parenthèses et virgule terminale est plus pratique. Considérez par exemple l'initialisation suivante ; on veut créer un tuple qui contient des listes (naturellement un tuple peut contenir n'importe quel objet Python), et comme c'est assez long on préfère mettre un élément du tuple par ligne :

```{code-cell}
mon_tuple = ([1, 2, 3],
             [4, 5, 6],
             [7, 8, 9],
            )
```

L'avantage lorsqu'on choisit cette forme (avec parenthèses, et avec virgule terminale), c'est d'abord qu'il n'est pas nécessaire de mettre un backslash à la fin de chaque ligne ; parce que l'on est à l'intérieur d'une zone parenthésée, l'interpréteur Python "sait" que l'instruction n'est pas terminée et va se continuer sur la ligne suivante.

Deuxièmement, si on doit ultérieurement ajouter ou enlever un élément dans le tuple, il suffira d'enlever ou d'ajouter toute une ligne, sans avoir à s'occuper des virgules ; si on avait choisi de ne pas faire figurer la virgule terminale, alors pour ajouter un élément dans le tuple après le dernier, il ne faut pas oublier d'ajouter une virgule à la ligne précédente. Cette simplicité se répercute au niveau du gestionnaire de code source, où les différences dans le code sont plus faciles à visualiser.

Signalons enfin que ceci n'est pas propre aux tuples. La virgule terminale est également optionnelle pour les listes, ainsi d'ailleurs que pour tous les types Python où cela fait du sens, comme les dictionnaires et les ensembles que nous verrons bientôt. Et dans tous les cas où on opte pour une présentation multi-lignes, il est conseillé de faire figurer une virgule terminale.

+++

### Tuples à un élément

+++

Pour revenir à présent sur le cas des tuples à un seul élément, c'est un cas particulier, parmi les quatre syntaxes que l'on a vues ci-dessus, on obtiendrait dans ce cas :

```{code-cell}
# ATTENTION : ces deux premières formes ne construisent pas un tuple !
simple1 = 1
simple2 = (1)
# celles-ci par contre construisent bien un tuple
simple3 = 1,
simple4 = (1,)
```

* Il est bien évident que la première forme ne crée pas de tuple ;
* et en fait la seconde non plus, car Python lit ceci comme une expression parenthésée, avec seulement un entier.

Et en fait ces deux premières formes créent un entier simple :

```{code-cell}
type(simple2)
```

Les deux autres formes créent par contre toutes les deux un tuple à un élément comme on cherchait à le faire :

```{code-cell}
type(simple3)
```

```{code-cell}
simple3 == simple4
```

Pour conclure, disons donc qu'il est conseillé de **toujours mentionner une virgule terminale** lorsqu'on construit des tuples.

+++

### Parenthèse parfois obligatoire

+++

Dans certains cas vous vous apercevrez que la parenthèse est obligatoire. Par exemple on peut écrire :

```{code-cell}
x = (1,)
(1,) == x
```

Mais si on essaie d'écrire le même test sans les parenthèses :

```{code-cell}
:latex:skip-eval: true

# ceci provoque une SyntaxError
1, == x
```

Python lève une erreur de syntaxe ; encore une bonne raison pour utiliser les parenthèses.

+++

### Addition de tuples

+++

Bien que le type tuple soit immuable, il est tout à fait légal d'additionner deux tuples, et l'addition va produire un **nouveau** tuple :

```{code-cell}
tuple1 = (1, 2,)
tuple2 = (3, 4,)
print('addition', tuple1 + tuple2)
```

Ainsi on peut également utiliser  l'opérateur `+=` avec un tuple qui va créer, comme précédemment, un nouvel objet tuple :

```{code-cell}
tuple1 = (1, 2,)
tuple1 += (3, 4,)
print('apres ajout', tuple1)
```

### Construire des tuples élaborés

+++

Malgré la possibilité de procéder par additions successives, la construction d'un tuple peut s'avérer fastidieuse.

+++

Une astuce utile consiste à penser aux fonctions de conversion, pour construire un tuple à partir de - par exemple - une liste. Ainsi on peut faire par exemple ceci :

```{code-cell}
# on fabrique une liste pas à pas
liste = list(range(10))
liste[9] = 'Inconnu'
del liste [2:5]
liste
```

```{code-cell}
# on convertit le résultat en tuple
mon_tuple = tuple(liste)
mon_tuple
```

### Digression sur les noms de fonctions prédéfinies

+++

**Remarque** : Vous avez peut-être observé que nous avons choisi de ne pas appeler notre tuple simplement `tuple`. C'est une bonne pratique en général d'éviter les noms de fonctions prédéfinies par Python.

Ces variables en effet sont des variables "comme les autres". Imaginez qu'on ait en fait deux tuples à construire comme ci-dessus, voici ce qu'on obtiendrait si on n'avait pas pris cette précaution :

```{code-cell}
liste = range(10)
# ATTENTION : ceci redéfinit le symbole tuple
tuple = tuple(liste)
tuple
```

```{code-cell}
:latex:skip-eval: true

# si bien que maintenant on ne peut plus faire ceci
# car à ce point, tuple ne désigne plus le type tuple
# mais l'objet qu'on vient de créer
autre_liste = range(100)
autre_tuple = tuple(autre_liste)
```

Il y a une erreur parce que nous avons remplacé (ligne 2) la valeur de la variable `tuple`, qui au départ référençait  le **type** tuple (ou si on préfère la fonction de conversion), par un **objet** tuple. Ainsi en ligne 5, lorsqu'on appelle à nouveau `tuple`, on essaie d'exécuter un objet qui n'est pas 'appelable' (*not callable* en anglais).

D'un autre côté, l'erreur est relativement facile à trouver dans ce cas. En cherchant toutes les occurrences de `tuple` dans notre propre code on voit assez vite le problème. De plus, je vous rappelle que votre éditeur de texte **doit** faire de la coloration syntaxique, et que toutes les fonctions built-in (dont `tuple` et `list` font partie) sont colorées spécifiquement (par exemple, en violet sous IDLE). En pratique, avec un bon éditeur de texte et un peu d'expérience, cette erreur est très rare.
