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
notebookname: "Affectation simultan\xE9e"
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Affectation simultanée

+++

## Complément - niveau basique

+++

Nous avons déjà parlé de l'affectation par *sequence unpacking* (en Semaine 3, séquence "Les tuples"), qui consiste à affecter à plusieurs variables des "morceaux" d'un objet, comme dans :

```{code-cell}
x, y = ['spam', 'egg']
```

Dans ce complément nous allons voir une autre forme de l'affectation, qui consiste à affecter **le même objet** à plusieurs variables. Commençons par un exemple simple :

```{code-cell}
a = b = 1
print('a', a, 'b', b)
```

La raison pour laquelle nous abordons cette construction maintenant est qu'elle a une forte relation avec les références partagées ; pour bien le voir, nous allons utiliser une valeur mutable comme valeur à affecter :

```{code-cell}
# on affecte a et b au même objet liste vide
a = b = []
```

Dès lors nous sommes dans le cas typique d'une référence partagée ; une modification de  `a` va se répercuter sur `b` puisque ces deux variables désignent **le même objet** :

```{code-cell}
a.append(1)
print('a', a, 'b', b)
```

Ceci est à mettre en contraste avec plusieurs affectations séparées :

```{code-cell}
# si on utilise deux affectations différentes
a = []
b = []

# alors on peut changer a sans changer b
a.append(1)
print('a', a, 'b', b)
```

On voit que dans ce cas chaque affectation crée une liste vide différente, et les deux variables ne partagent plus de donnée.

+++

D'une manière générale, utiliser l'affectation simultanée vers un objet mutable crée mécaniquement des **références partagées**, aussi vérifiez bien dans ce cas que c'est votre intention.
