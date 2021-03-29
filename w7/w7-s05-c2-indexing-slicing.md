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
notebookname: Indexation et slices
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Index et slices

+++

## Complément - niveau basique

```{code-cell}
---
slideshow:
  slide_type: '-'
---
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
plt.ion()
```

J'espère que vous êtes à présent convaincus qu'il est possible de faire énormément de choses avec `numpy` en faisant des opérations entre tableaux, et sans aller référencer un par un les éléments des tableaux, ni faire de boucle `for`.

Il est temps maintenant de voir que l'on peut *aussi* manipuler les tableaux `numpy` avec des index.

+++

### Indexation par des entiers et tuples

+++

La façon la plus naturelle d'utiliser un tableau est habituellement à l'aide des indices. On peut aussi bien sûr accéder aux éléments d'un tableau `numpy` par des indices :

```{code-cell}
# une fonction qui crée un tableau
# tab[i, j] = i + 10 * j
def background(n):
    i = np.arange(n)
    j = i.reshape((n, 1))
    return i + 10 * j
```

```{code-cell}
a5 = background(5)
print(a5)
```

Avec un seul index on obtient naturellement une ligne :

```{code-cell}
a5[1]
```

```{code-cell}
# que l'on peut à nouveau indexer
a5[1][2]
```

```{code-cell}
# ou plus simplement indexer par un tuple
a5[1, 2]
```

```{code-cell}
---
slideshow:
  slide_type: slide
---
# naturellement on peut affecter une case
# individuellement
a5[2][1] = 221
a5[3, 2] += 300
print(a5)
```

```{code-cell}
# ou toute une ligne
a5[1] = np.arange(100, 105)
print(a5)
```

```{code-cell}
# et on on peut aussi changer
# toute une ligne par broadcasting
a5[4] = 400
print(a5)
```

+++ {"slideshow": {"slide_type": "slide"}}

# Slicing

+++

Grâce au slicing on peut aussi référencer une colonne :

```{code-cell}
a5 = background(5)
print(a5)
```

```{code-cell}
a5[:, 3]
```

C'est un tableau à une dimension, mais vous pouvez tout de même modifier la colonne par une affectation :

```{code-cell}
a5[:, 3] = range(300, 305)
print(a5)
```

Ou, ici également bien sûr, par broadcasting :

```{code-cell}
# on affecte un scalaire à une colonne
a5[:, 2] = 200
print(a5)
```

```{code-cell}
# ou on ajoute un scalaire à une colonne
a5[:, 4] += 400
print(a5)
```

Les slices peuvent prendre une forme générale :

```{code-cell}
a8 = background(8)
print(a8)
```

```{code-cell}
# toutes les lignes de rang 1, 4, 7
a8[1::3]
```

```{code-cell}
# toutes les colonnes de rang 1, 5, 9
a8[:, 1::4]
```

```{code-cell}
# et on peut bien sûr les modifier
a8[:, 1::4] = 0
print(a8)
```

+++ {"slideshow": {"slide_type": "slide"}}

Du coup, le slicing peut servir à extraire des blocs :

```{code-cell}
# un bloc au hasard dans a8
print(a8[5:8, 2:5])
```

### `newaxis`

+++

On peut utiliser également le symbole spécial `np.newaxis` en conjonction avec un slice pour "décaler" les dimensions :

```{code-cell}
---
slideshow:
  slide_type: slide
---
X = np.arange(1, 7)
print(X)
```

```{code-cell}
X.shape
```

```{code-cell}
Y = X[:, np.newaxis]
print(Y)
```

```{code-cell}
Y.shape
```

Et ainsi de suite :

```{code-cell}
Z = Y[:, np.newaxis]
Z
```

```{code-cell}
Z.shape
```

De cette façon, par exemple, en combinant le slicing pour créer X et Y, et le broadcasting pour créer leur somme,  je peux créer facilement la table de tous les tirages de 2 dés à 6 faces :

```{code-cell}
dice2 = X + Y
print(dice2)
```

Ou tous les tirages à trois dés :

```{code-cell}
dice3 = X + Y + Z
print(dice3)
```

J'en profite pour introduire un utilitaire qui n'a rien à voir, mais avec `np.unique`, vous pourriez calculer le nombre d'occurrences dans le tableau, et ainsi calculer les probabilités d'apparition de tous les nombres entre 3 et 18 :

```{code-cell}
np.unique(dice3, return_counts=True)
```

### Différences avec les listes

+++

Avec l'indexation et le slicing, on peut créer des tableaux qui sont des vues sur des fragments d'un tableau ; on peut également déformer leur dimension grâce à `newaxis` ; on peut modifier ces fragments, en utilisant un scalaire, un tableau, ou une slice sur un autre tableau. Les possibilités sont infinies.

+++

Il est cependant utile de souligner quelques différences entre les tableaux `numpy` et, les listes natives, pour ce qui concerne les indexations et le *slicing*.

+++

#### On ne peut pas changer la taille d'un tableau avec le slicing

La taille d'un objet `numpy` est par définition constante ; cela signifie qu'on ne peut pas, par exemple, modifier sa taille totale avec du slicing ; c'est à mettre en contraste avec, si vous vous souvenez :

+++

##### Listes

```{code-cell}
:cell_style: center

# on peut faire ceci
liste = [0, 1, 2]
liste[1:2] = [100, 102, 102]
liste
```

##### Tableaux

```{code-cell}
:cell_style: center

# on ne peut pas faire cela
array = np.array([0, 1, 2])
try:
    array[1:2] = np.array([100, 102, 102])
except Exception as e:
    print(f"OOPS, {type(e)}, {e}")
```

##### On peut modifier un tableau en modifiant une slice

Une slice sur un objet `numpy` renvoie une **vue** sur un extrait du tableau, et en changeant la vue on change le tableau ; ici encore c'est à mettre en contraste avec ce qui se passe sur les listes :

+++

##### Listes

```{code-cell}
# une slice d'une liste est une shallow copy
liste = [0, 1, 2]
liste[1:2]
```

```{code-cell}
# en modifiant la slice,
# on ne modifie pas la liste
liste[1:2][0] = 999999
liste
```

##### Tableaux

```{code-cell}
# une slice d'un tableau numpy est un extrait du tableau
array = np.array([0, 1, 2])
array[1:2]
```

```{code-cell}
array[1:2][0] = 100
array
```
