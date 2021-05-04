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
  display_name: Python 3
  language: python
  name: python3
language_info:
  name: python
  pygments_lexer: ipython3
notebookname: Tris de listes (1)
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Tris de listes

+++

## Complément - niveau basique

+++

Python fournit une méthode standard pour trier une liste, qui s'appelle, sans grande surprise, `sort`.

+++

### La méthode `sort`

+++

Voyons comment se comporte `sort` sur un exemple simple :

```{code-cell} ipython3
liste = [8, 7, 4, 3, 2, 9, 1, 5, 6]
print('avant tri', liste)
liste.sort()
print('apres tri', liste)
```

On retrouve ici, avec l'instruction `liste.sort()` un cas d'appel de méthode (ici `sort`) sur un objet (ici `liste`), comme on l'avait vu dans la vidéo.

+++

La première chose à remarquer est que la liste d'entrée a été modifiée, on dit "en place", ou encore "par effet de bord". Voyons cela sous pythontutor :

```{code-cell} ipython3
%load_ext ipythontutor
```

```{code-cell} ipython3
%%ipythontutor height=200 ratio=0.8
liste = [3, 2, 9, 1]
liste.sort()
```

On aurait pu imaginer que la liste d'entrée soit restée inchangée, et que la méthode de tri renvoie une copie triée de la liste, ce n'est pas le choix qui a été fait, cela permet d'économiser des allocations mémoire autant que possible et d'accélérer sensiblement le tri.

+++

### La fonction `sorted`

+++

Si vous avez besoin de faire le tri sur une copie de votre liste, la fonction `sorted` vous permet de le faire :

```{code-cell} ipython3
%%ipythontutor height=200 ratio=0.8
liste1 = [3, 2, 9, 1]
liste2 = sorted(liste1)
```

### Tri décroissant

+++

Revenons à la méthode `sort` et aux tris *en place*. Par défaut la liste est triée par ordre croissant, si au contraire vous voulez l'ordre décroissant, faites comme ceci :

```{code-cell} ipython3
liste = [8, 7, 4, 3, 2, 9, 1, 5, 6]
print('avant tri', liste)
liste.sort(reverse=True)
print('apres tri décroissant', liste)
```

Nous n'avons pas encore vu à quoi correspond cette formule `reverse=True` dans l'appel à la méthode - ceci sera approfondi dans le chapitre sur les appels de fonction - mais dans l'immédiat vous pouvez utiliser cette technique telle quelle.

+++

### Chaînes de caractères

+++

Cette technique fonctionne très bien sur tous les types numériques (enfin, à l'exception des complexes ; en guise d'exercice, pourquoi ?), ainsi que sur les chaînes de caractères :

```{code-cell} ipython3
liste = ['spam', 'egg', 'bacon', 'beef']
liste.sort()
print('après tri', liste)
```

Comme on s'y attend, il s'agit cette fois d'un **tri lexicographique**, dérivé de l'ordre sur les caractères. Autrement dit, c'est l'ordre du dictionnaire. Il faut souligner toutefois, pour les personnes n'ayant jamais été exposées à l'informatique, que cet ordre, quoique déterministe, est arbitraire en dehors des lettres de l'alphabet.

+++

Ainsi par exemple :

```{code-cell} ipython3
# deux caractères minuscules se comparent
# comme on s'y attend
'a' < 'z'
```

Bon, mais par contre :

```{code-cell} ipython3
# si l'un est en minuscule et l'autre en majuscule,
# ce n'est plus le cas
'Z' < 'a'
```

Ce qui à son tour explique ceci :

```{code-cell} ipython3
# la conséquence de 'Z' < 'a', c'est que
liste = ['abc', 'Zoo']
liste.sort()
print(liste)
```

Et lorsque les chaînes contiennent des espaces ou autres ponctuations, le résultat du tri peut paraître surprenant :

```{code-cell} ipython3
# attention ici notre premiere chaîne commence par une espace
# et le caractère 'Espace' est plus petit
# que tous les autres caractères imprimables
liste = [' zoo', 'ane']
liste.sort()
print(liste)
```

### À suivre

+++

Il est possible de définir soi-même le critère à utiliser pour trier une liste, et nous verrons cela bientôt, une fois que nous aurons introduit la notion de fonction.
