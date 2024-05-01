---
jupytext:
  cell_metadata_filter: all, -hidden, -heading_collapsed, -run_control, -trusted
  notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version, -jupytext.text_representation.format_version,
    -language_info.version, -language_info.codemirror_mode.version, -language_info.codemirror_mode,
    -language_info.file_extension, -language_info.mimetype, -toc
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
  title: "Op\xE9rations logiques"
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

# Opérations logiques

+++

## Complément - niveau basique

+++

Même si les tableaux contiennent habituellement des nombres, on peut être amenés à faire des opérations logiques et du coup à manipuler des tableaux de booléens. Nous allons voir quelques éléments à ce sujet.

```{code-cell} ipython3
import numpy as np
```

### Opérations logiques

+++

On peut faire des opérations logiques entre tableaux exactement comme on fait des opérations arithmétiques.

+++

On va partir de deux tableaux presque identiques. J'en profite pour vous signaler qu'on peut copier un tableau avec, tout simplement, `np.copy` :

```{code-cell} ipython3
:tags: [gridwidth-1-2]

a = np.arange(25).reshape(5, 5)
print(a)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

b = np.copy(a)
b[2, 2] = 1000
print(b)
```

Dans la lignée de ce qu'on a vu jusqu'ici en matière de programmation vectorielle, une opération logique va ici aussi nous retourner un tableau de la même taille :

```{code-cell} ipython3
# la comparaison par == ne nous
# retourne pas directement un booléen
# mais un tableau de la même taille que a et b
print(a == b)
```

### `all` et `any`

+++

Si votre intention est de vérifier que les deux tableaux sont entièrement identiques, utilisez `np.all` - et non pas le *built-in* natif `all` de Python - qui va vérifier que tous les éléments du tableau sont vrais :

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# oui
np.all(a == a)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# oui
np.all(a == b)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# oui
# on peut faire aussi bien
#   np.all(x)
# ou
#   x.all()
(a == a).all()
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# par contre : non !
# ceci n'est pas conseillé
# même si ça peut parfois fonctionner
try:
    all(a == a)
except Exception as e:
    print(f'OOPS {type(e)} {e}')
```

C'est bien sûr la même chose pour `any` qui va vérifier qu'il y a au moins un élément vrai. Comme en Python natif, un nombre qui est nul est considéré comme faux :

```{code-cell} ipython3
:tags: [gridwidth-1-2]

np.zeros(5).any()
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

np.ones(5).any()
```

### Masques

+++

Mais en général, c'est rare qu'on ait besoin de consolider de la sorte un booléen sur tout un tableau, on utilise plutôt les tableaux logiques comme des masques, pour faire ou non des opérations sur un autre tableau.

+++

J'en profite pour introduire une fonction de `matplotlib` qui s'appelle `imshow` et qui permet d'afficher une image :

```{code-cell} ipython3
:cell_style: center

import matplotlib.pyplot as plt
%matplotlib inline
plt.ion()
```

```{code-cell} ipython3
# construisons un disque centré au milieu de l'image

width = 128
center = width / 2

ix, iy = np.indices((width, width))
image = (ix-center)**2 + (iy-center)**2
# pour afficher l'image en niveaux de gris
plt.imshow(image, cmap='gray');
```

Maintenant je peux créer un masque qui produise des rayures en diagonale, donc selon la valeur de `(i+j)`. Par exemple :

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# pour faire des rayures
# de 6 pixels de large
rayures = (ix + iy) % 8 <= 5
plt.imshow(rayures, cmap='gray');
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# en fait c'est bien sûr
# un tableau de booléens
print(rayures)
```

je vous montre aussi comment inverser un masque parce que c'est un peu abscons :

```{code-cell} ipython3
# on ne peut pas faire 
try:
    anti_rayures = not rayures
except Exception as e:
    print(f"OOPS - {type(e)} - {e}")
```

+++ {"tags": ["gridwidth-1-2"]}

on ne peut pas non plus faire `rayures.not()`, parce `not` est un mot clé

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# on a le choix entre utiliser
#   rayures.logical_not() 

anti_rayures = np.logical_not(rayures)
plt.imshow(anti_rayures, 
           cmap='gray');
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# ou encore l'opérateur ~ 
# qui fait un not bitwise

anti_rayures = ~rayures
plt.imshow(anti_rayures,
           cmap='gray');
```

Maintenant je peux utiliser le masque `rayures` pour faire des choses sur l'image. Par exemple simplement :

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# pour effacer les rayures
plt.imshow(image*rayures, cmap='gray');
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# ou garder l'autre moitié
plt.imshow(image*anti_rayures, cmap='gray');
```

```{code-cell} ipython3
image
```

```{code-cell} ipython3
np.logical_not(image)
```

### Expression conditionnelle et `np.where`

+++

Nous avons vu en Python natif l'expression conditionnelle :

```{code-cell} ipython3
3 if True else 2
```

Pour reproduire cette construction en `numpy` vous avez à votre disposition `np.where`. Pour l'illustrer nous allons construire deux images facilement discernables. Et, pour cela, on va utiliser `np.isclose`, qui est très utile pour comparer que deux nombres sont suffisamment proches, surtout pour les calculs flottants en fait, mais ça nous convient très bien ici aussi :

```{code-cell} ipython3
np.isclose?
```

Pour élaborer une image qui contient un grand cercle, je vais dire que la distance au centre (je rappelle que c'est le contenu de `image`) est suffisamment proche de $64^2$, ce que vaut `image` au milieu de chaque bord :

```{code-cell} ipython3
:tags: [gridwidth-1-2]

big_circle = np.isclose(image, 64 **2, 10/100)
plt.imshow(big_circle, cmap='gray');
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

small_circle = np.isclose(image, 32 **2, 10/100)
plt.imshow(small_circle, cmap='gray');
```

En utilisant `np.where`, je peux simuler quelque chose comme ceci :
```python
mixed = big_circle if rayures else small_circle
```

```{code-cell} ipython3
# sauf que ça se présente en fait comme ceci :
mixed = np.where(rayures, big_circle, small_circle)
plt.imshow(mixed, cmap='gray');
```

Remarquez enfin qu'on peut aussi faire la même chose en tirant profit que `True` == 1 et `False` == 0 :

```{code-cell} ipython3
mixed2 = rayures * big_circle + (1-rayures) * small_circle
plt.imshow(mixed2, cmap='gray');
```
