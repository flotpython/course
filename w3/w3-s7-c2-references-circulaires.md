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
notebookname: "R\xE9f\xE9rences circulaires"
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Listes infinies & références circulaires

+++

## Complément - niveau intermédiaire

```{code-cell}
%load_ext ipythontutor
```

Nous allons maintenant construire un objet un peu abscons. Cet exemple précis n'a aucune utilité pratique, mais permet de bien comprendre la logique du langage.

+++

Construisons une liste à un seul élément, peu importe quoi :

```{code-cell}
infini_1 = [None]
```

À présent nous allons remplacer le premier et seul élément de la liste par… la liste elle-même :

```{code-cell}
infini_1[0] = infini_1
print(infini_1)
```

Pour essayer de décrire l'objet liste ainsi obtenu, on pourrait dire qu'il s'agit d'une liste de taille 1 et de profondeur infinie, une sorte de fil infini en quelque sorte.

Naturellement, l'objet obtenu est difficile à imprimer de manière convaincante. Pour faire en sorte que cet objet soit tout de même imprimable, et éviter une boucle infinie, python utilise l'ellipse `...` pour indiquer ce qu'on appelle une référence circulaire. Si on n'y prenait pas garde en effet, il faudrait écrire `[[[[ etc. ]]]]` avec une infinité de crochets.

+++

Voici la même séquence exécutée sous [http://pythontutor.com](http://pythontutor.com) ; il s'agit d'un site très utile pour comprendre comment python implémente les objets, les références et les partages.

Cliquez sur le bouton `Next` pour avancer dans l'exécution de la séquence. À la fin de la séquence vous verrez - ce n'est pas forcément clair - la seule cellule de la liste à se référencer elle-même :

```{code-cell}
%%ipythontutor height=230
infini_1 = [None]
infini_1[0] = infini_1
```

Toutes les fonctions de python ne sont pas aussi intelligentes que `print`. Bien qu'on puisse comparer cette liste avec elle-même :

```{code-cell}
infini_1 == infini_1
```

il n'en est pas de même si on la compare avec un objet analogue mais pas identique :

```{code-cell}
infini_2 = [None]
infini_2[0] = infini_2
print(infini_2)
```

```{code-cell}
:latex:skip-eval: true

# attention, ceci provoque une erreur à l'exécution
# RecursionError: maximum recursion depth exceeded in comparison
infini_1 == infini_2
```

### Généralisation aux références circulaires

+++

On obtient un phénomène équivalent dès lors qu'un élément contenu dans un objet fait référence à l'objet lui-même. Voici par exemple comment on peut construire un dictionnaire qui contient une référence circulaire :

```{code-cell}
collection_de_points = [
    {'x': 10,'y': 20},
    {'x': 30,'y': 50},
    # imaginez plein de points
]

# on rajoute dans chaque dictionnaire une clé 'points'
# qui référence la collection complète
for point in collection_de_points:
    point['points'] = collection_de_points

# la structure possède maintenant des références circulaires
print(collection_de_points)
```

On voit à nouveau réapparaître les ellipses, qui indiquent que pour chaque point, le nouveau champ `points` est un objet qui a déjà été imprimé.

Cette technique est cette fois très utile et très utilisée dans la pratique, dès lors qu'on a besoin de naviguer de manière arbitraire dans une structure de données compliquée. Dans cet exemple, pas très réaliste naturellement, on pourrait à présent accéder depuis un point à tous les autres points de la collection dont il fait partie.

+++

À nouveau il peut être intéressant de voir le comportement de cet exemple avec <http://pythontutor.com> pour bien comprendre ce qui se passe, si cela ne vous semble pas clair à première vue :

```{code-cell}
%%ipythontutor curInstr=7
points = [
    {'x': 10,'y': 20},
    {'x': 30,'y': 50},
]

for point in points:
    point['points'] = points
```
