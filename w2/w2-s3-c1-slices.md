---
ipub:
  sphinx:
    toggle_input: true
    toggle_input_all: true
    toggle_output: true
    toggle_output_all: true
jupytext:
  encoding: '# -*- coding: utf-8 -*-'
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
language_info:
  name: python
  pygments_lexer: ipython3
livereveal:
  auto_select: code
  auto_select_fragment: true
  autolaunch: false
  backimage: media/nologo.png
  height: 100%
  slideNumber: c
  start_slideshow_at: selected
  theme: simple
  transition: fade
  width: 100%
nbhosting:
  title: Slicing
---

# Les slices en Python

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Complément - niveau basique

+++

Ce support de cours reprend les notions de *slicing* vues dans la vidéo.

+++

Nous allons illustrer les slices sur la chaîne suivante, rappelez-vous toutefois que ce mécanisme fonctionne avec toutes les séquences que l'on verra plus tard, comme les listes ou les tuples.

```{code-cell} ipython3
chaine = "abcdefghijklmnopqrstuvwxyz"
print(chaine)
```

### Slice sans pas

+++

On a vu en cours qu'une slice permet de désigner toute une plage d'éléments d'une séquence. Ainsi on peut écrire :

```{code-cell} ipython3
chaine[2:6]
```

### Conventions de début et fin

+++

Les débutants ont parfois du mal avec les bornes. Il faut se souvenir que :

* les indices **commencent** comme toujours **à zéro** ;
* le premier indice `debut` est **inclus** ;
* le second indice `fin` est **exclu** ;
* on obtient en tout `fin-debut` items dans le résultat.

Ainsi, ci-dessus, le résultat contient `6 - 2 = 4` éléments.

+++

Pour vous aider à vous souvenir des conventions de début et de fin, souvenez-vous qu'on veut pouvoir facilement juxtaposer deux slices qui ont une borne commune.

C'est-à-dire qu'avec :

+++

![début et fin](media/brackets.png)

```{code-cell} ipython3
# chaine[a:b] + chaine[b:c] == chaine[a:c]
chaine[0:3] + chaine[3:7] == chaine[0:7]
```

#### Bornes omises

+++

On peut omettre une borne :

```{code-cell} ipython3
# si on omet la première borne, cela signifie que
# la slice commence au début de l'objet
chaine[:6]
```

```{code-cell} ipython3
# et bien entendu c'est la même chose si on omet la deuxième borne
chaine[24:]
```

```{code-cell} ipython3
# ou même omettre les deux bornes, auquel cas on
# fait une copie de l'objet - on y reviendra plus tard
chaine[:]
```

#### Indices négatifs

+++

On peut utiliser des indices négatifs pour compter à partir de la fin :

```{code-cell} ipython3
chaine[3:-3]
```

```{code-cell} ipython3
chaine[-3:]
```

### Slice avec pas

+++

Il est également possible de préciser un *pas*, de façon à ne choisir par exemple, dans la plage donnée, qu'un élément sur deux :

```{code-cell} ipython3
# le pas est précisé après un deuxième deux-points (:)
# ici on va choisir un caractère sur deux dans la plage [3:-3]
chaine[3:-3:2]
```

Comme on le devine, le troisième élément de la slice, ici `2`, détermine le pas. On ne retient donc, dans la chaîne `defghi...` que `d`, puis `f`, et ainsi de suite.

On peut préciser du coup la borne de fin (ici `-3`) avec un peu de liberté, puisqu'ici on obtiendrait un résultat identique avec `-4`.

```{code-cell} ipython3
chaine[3:-4:2]
```

### Pas négatif

+++

Il est même possible de spécifier un pas négatif. Dans ce cas, de manière un peu contre-intuitive, il faut préciser un début (le premier indice de la slice) qui soit *plus à droite* que la fin (le second indice).

Pour prendre un exemple, comme l'élément d'indice `-3`, c'est-à-dire `x`, est plus à droite que l'élément d'indice `3`, c'est-à-dire `d`, évidemment si on ne précisait pas le pas (qui revient à choisir un pas égal à `1`), on obtiendrait une liste vide :

```{code-cell} ipython3
chaine[-3:3]
```

Si maintenant on précise un pas négatif, on obtient cette fois :

```{code-cell} ipython3
chaine[-3:3:-2]
```

### Conclusion

+++

À nouveau, souvenez-vous que tous ces mécanismes fonctionnent avec de nombreux autres types que les chaînes de caractères. En voici deux exemples qui anticipent tous les deux sur la suite, mais qui devraient illustrer les vastes possibilités qui sont offertes avec les slices.

+++

#### Listes

+++

Par exemple sur les listes :

```{code-cell} ipython3
liste = [1, 2, 4, 8, 16, 32]
liste
```

```{code-cell} ipython3
liste[-1:1:-2]
```

Et même ceci, qui peut être déroutant. Nous reviendrons dessus.

```{code-cell} ipython3
liste[2:4] = [10, 20, 30]
liste
```

Voici une représentation imagée de ce qui se passe lorsqu'on exécute cette dernière ligne de code; cela revient en quelque sorte à *remplacer* la slice à gauche de l'affectation (ici `liste[2:4]`) par la liste à droite de l'affectation (ici `[10, 20, 30]` - ce qui a, en général, pour effet de modifier la longueur de la liste.

+++

![](media/writing-a-list-slice.png)

+++

## Complément - niveau avancé

+++

#### `numpy`

+++

La bibliothèque `numpy` permet de manipuler des tableaux ou des matrices. En anticipant (beaucoup) sur son usage que nous reverrons bien entendu en détail, voici un aperçu de ce que l'on peut faire avec des slices sur des objets `numpy` :

```{code-cell} ipython3
# ces deux premières cellules sont à admettre
# on construit un tableau ligne
import numpy as np

un_cinq = np.array([1, 2, 3, 4, 5])
un_cinq
```

```{code-cell} ipython3
# ces deux premières cellules sont à admettre
# on le combine avec lui-même - et en utilisant une slice un peu magique
# pour former un tableau carré 5x5

array = 10 * un_cinq[:, np.newaxis] + un_cinq
array
```

Sur ce tableau de taille 5x5, nous pouvons aussi faire du slicing et extraire le sous-tableau 3x3 au centre :

```{code-cell} ipython3
centre = array[1:4, 1:4]
centre
```

On peut bien sûr également utiliser un pas :

```{code-cell} ipython3
coins = array[::4, ::4]
coins
```

Ou bien retourner complètement dans une direction :

```{code-cell} ipython3
tete_en_bas = array[::-1,:]
tete_en_bas
```
