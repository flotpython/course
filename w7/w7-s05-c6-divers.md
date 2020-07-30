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
notebookname: Divers
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Divers

+++

## Complément - niveau avancé

```{code-cell}
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
plt.ion()
```

Pour finir notre introduction à `numpy`, nous allons survoler à très grande vitesse quelques traits plus annexes mais qui peuvent être utiles. Je vous laisse approfondir de votre côté les parties qui vous intéressent.

+++ {"run_control": {"frozen": false, "read_only": false}, "slideshow": {"slide_type": "slide"}}

# Utilisation de la mémoire

+++

### Références croisées, vues, shallow et deep copies

+++ {"run_control": {"frozen": false, "read_only": false}}

Pour résumer ce qu'on a vu jusqu'ici :

* un tableau `numpy` est un objet mutable ;
* une slice sur un tableau retourne une vue, on est donc dans le cas d'une référence partagée ;
* dans tous les cas que l'on a vus jusqu'ici, comme les cases des tableaux sont des objets atomiques, il n'y a pas de différence entre *shallow* et *deep* copie ;
* pour créer une copie, utilisez `np.copy()`.

+++

Et de plus :

```{code-cell}
# un tableau de base
a = np.arange(3)
```

```{code-cell}
:cell_style: split

# une vue
v = a.view()
```

```{code-cell}
:cell_style: split

# une slice
s = a[:]
```

Les deux objets ne sont pas différentiables :

```{code-cell}
:cell_style: split

v.base is a
```

```{code-cell}
:cell_style: split

s.base is a
```

### L'option `out=`

+++

Lorsque l'on fait du calcul vectoriel, on peut avoir tendance à créer de nombreux tableaux intermédiaires qui coûtent cher en mémoire. Pour cette raison, presque tous les opérateurs `numpy` proposent un paramètre optionnel `out=` qui permet de spécifier un tableau déjà alloué, dans lequel ranger le résultat.

+++

Prenons l'exemple un peu factice suivant, ou on calcule $e^{sin(cos(x))}$ sur l'intervalle $[0, 2\pi]$ :

```{code-cell}
# le domaine
X = np.linspace(0, 2*np.pi)
```

```{code-cell}
Y = np.exp(np.sin(np.cos(X)))
plt.plot(X, Y);
```

```{code-cell}
# chaque fonction alloue un tableau pour ranger ses résultats,
# et si je décompose, ce qui se passe en fait c'est ceci
Y1 = np.cos(X)
Y2 = np.sin(Y1)
Y3 = np.exp(Y2)
# en tout en comptant X et Y j'aurai créé 4 tableaux
plt.plot(X, Y3);
```

```{code-cell}
# Mais moi je sais qu'en fait je n'ai besoin que de X et de Y
# ce qui fait que je peux optimiser comme ceci :

# je ne peux pas récrire sur X parce que j'en aurai besoin pour le plot
X1 = np.cos(X)
# par contre ici je peux recycler X1 sans souci
np.sin(X1, out=X1)
# etc ...
np.exp(X1, out=X1)
plt.plot(X, X1);
```

Et avec cette approche je n'ai créé que 2 tableaux en tout.

+++

**Notez bien :** je ne vous recommande pas d'utiliser ceci systématiquement, car ça défigure nettement le code. Mais il faut savoir que ça existe, et savoir y penser lorsque la création de tableaux intermédiaires a un coût important dans l'algorithme.

+++

##### `np.add` et similaires

+++

Si vous vous mettez à optimiser de cette façon, vous utiliserez par exemple `np.add` plutôt que `+`, qui ne vous permet pas de choisir la destination du résultat.

+++

# Types structurés pour les cellules

+++ {"run_control": {"frozen": false, "read_only": false}}

Sans transition, jusqu'ici on a vu des tableaux *atomiques*, où chaque cellule est en gros **un seul nombre**.

En fait, on peut aussi se définir des types structurés, c'est-à-dire que chaque cellule contient l'équivalent d'un *struct* en C.

Pour cela, on peut se définir un `dtype` élaboré, qui va nous permettre de définir la structure de chacun de ces enregistrements.

+++ {"run_control": {"frozen": false, "read_only": false}, "slideshow": {"slide_type": "slide"}}

### Exemple

```{code-cell}
---
run_control:
  frozen: false
  read_only: false
---
# un dtype structuré
my_dtype = [
    # prenom est un string de taille 12
    ('prenom', '|S12'),
    # nom est un string de taille 15
    ('nom', '|S15'),
    # age est un entier
    ('age', np.int)
]

# un tableau qui contient des cellules de ce type
classe = np.array(
    # le contenu
    [ ( 'Jean', 'Dupont', 32),
      ( 'Daniel', 'Durand', 18),
      ( 'Joseph', 'Delapierre', 54),
      ( 'Paul', 'Girard', 20)],
    # le type
    dtype = my_dtype)
classe
```

+++ {"run_control": {"frozen": false, "read_only": false}}

Je peux avoir l'impression d'avoir créé un tableau de 4 lignes et 3 colonnes ; cependant pour `numpy` ce n'est pas comme ça que cela se présente :

```{code-cell}
classe.shape
```

Rien ne m'empêcherait de créer des tableaux de ce genre en dimensions supérieures, bien entendu :

```{code-cell}
# ça n'a pas beaucoup d'intérêt ici, mais si on en a besoin
# on peut bien sûr avoir plusieurs dimensions
classe.reshape((2, 2))
```

+++ {"run_control": {"frozen": false, "read_only": false}, "slideshow": {"slide_type": "slide"}}

### Comment définir `dtype` ?

+++ {"run_control": {"frozen": false, "read_only": false}, "slideshow": {"slide_type": "-"}}

Il existe une grande variété de moyens pour se définir son propre `dtype`.

Je vous signale notamment la possibilité de spécifier à l'intérieur d'un `dtype` des cellules de type `object`, qui est l'équivalent d'une référence Python (approximativement, un pointeur dans un *struct* C) ; c'est un trait qui est utilisé par `pandas` que nous allons voir très bientôt.

Pour la définition de types structurés, [voir la documentation complète ici](https://docs.scipy.org/doc/numpy-1.13.0/user/basics.rec.html#defining-structured-arrays).

+++

# Assemblages et découpages

+++ {"run_control": {"frozen": false, "read_only": false}}

Enfin, toujours sans transition, et plus anecdotique : jusqu'ici nous avons vu des fonctions qui préservent la taille. Le *stacking* permet de créer un tableau plus grand en (juxta/super)posant plusieurs tableaux. Voici rapidement quelques fonctions qui permettent de faire des tableaux plus petits ou plus grands.

+++ {"run_control": {"frozen": false, "read_only": false}, "slideshow": {"slide_type": "slide"}}

### Assemblages : `hstack` et `vstack` (tableaux 2D)

```{code-cell}
---
cell_style: center
run_control:
  frozen: false
  read_only: false
slideshow:
  slide_type: '-'
---
a = np.arange(1, 7).reshape(2, 3)
print(a)
```

```{code-cell}
---
cell_style: center
run_control:
  frozen: false
  read_only: false
---
b = 10 * np.arange(1, 7).reshape(2, 3)
print(b)
```

```{code-cell}
---
cell_style: split
run_control:
  frozen: false
  read_only: false
---
print(np.hstack((a, b)))
```

```{code-cell}
---
cell_style: split
run_control:
  frozen: false
  read_only: false
---
print(np.vstack((a, b)))
```

### Assemblages : `np.concatenate` (3D et au delà)

```{code-cell}
---
cell_style: split
run_control:
  frozen: false
  read_only: false
---
a = np.ones((2, 3, 4))
print(a)
```

```{code-cell}
---
cell_style: split
run_control:
  frozen: false
  read_only: false
---
b = np.zeros((2, 3, 2))
print(b)
```

```{code-cell}
---
run_control:
  frozen: false
  read_only: false
---
print(np.concatenate((a, b), axis = 2))
```

+++ {"run_control": {"frozen": false, "read_only": false}, "slideshow": {"slide_type": "slide"}}

Pour conclure :

* `hstack` et `vstack` utiles sur des tableaux 2D ;
* au-delà, préférez `concatenate` qui a une sémantique plus claire.

+++ {"run_control": {"frozen": false, "read_only": false}, "slideshow": {"slide_type": "slide"}}

### Répétitions : `np.tile`

+++ {"run_control": {"frozen": false, "read_only": false}}

Cette fonction permet de répéter un tableau dans toutes les directions :

```{code-cell}
---
run_control:
  frozen: false
  read_only: false
---
motif = np.array([[0, 1], [2, 10]])
print(motif)
```

```{code-cell}
---
run_control:
  frozen: false
  read_only: false
---
print(np.tile(motif, (2, 3)))
```

+++ {"run_control": {"frozen": false, "read_only": false}, "slideshow": {"slide_type": "slide"}}

### Découpage : `np.split`

+++ {"run_control": {"frozen": false, "read_only": false}}

Cette opération, inverse du *stacking*, consiste à découper un tableau en parties plus ou moins égales :

```{code-cell}
---
run_control:
  frozen: false
  read_only: false
---
complet = np.arange(24).reshape(4, 6); print(complet)
```

```{code-cell}
---
cell_style: split
run_control:
  frozen: false
  read_only: false
---
h1, h2 = np.hsplit(complet, 2)
print(h1)
```

```{code-cell}
---
cell_style: split
run_control:
  frozen: false
  read_only: false
---
print(h2)
```

```{code-cell}
---
run_control:
  frozen: false
  read_only: false
slideshow:
  slide_type: slide
---
complet = np.arange(24).reshape(4, 6)
print(complet)
```

```{code-cell}
---
cell_style: split
run_control:
  frozen: false
  read_only: false
---
v1, v2 = np.vsplit(complet, 2)
print(v1)
```

```{code-cell}
---
cell_style: split
run_control:
  frozen: false
  read_only: false
---
print(v2)
```
