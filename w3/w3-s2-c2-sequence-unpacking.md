---
jupytext:
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
nbhosting:
  title: Sequence unpacking
---

# Sequence unpacking

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Complément - niveau basique

+++

**Remarque préliminaire** : nous avons vainement cherché une traduction raisonnable pour ce trait du langage, connue en anglais sous le nom de *sequence unpacking* ou encore parfois *tuple unpacking*, aussi pour éviter de créer de la confusion nous avons finalement décidé de conserver le terme anglais à l'identique.

+++

### Déjà rencontré

+++

L'affectation dans Python peut concerner plusieurs variables à la fois. En fait nous en avons déjà vu un exemple en Semaine 1, avec la fonction `fibonacci` dans laquelle il y avait ce fragment :

```python
for i in range(2, n + 1):
    f2, f1 = f1, f1 + f2
```

Nous allons dans ce complément décortiquer les mécanismes derrière cette phrase qui a probablement excité votre curiosité. :)

+++

### Un exemple simple

+++

Commençons par un exemple simple à base de tuple. Imaginons que l'on dispose d'un tuple `couple` dont on sait qu'il a deux éléments :

```{code-cell} ipython3
couple = (100, 'spam')
```

On souhaite à présent extraire les deux valeurs, et les affecter à deux variables distinctes. Une solution naïve consiste bien sûr à faire simplement :

```{code-cell} ipython3
gauche = couple[0]
droite = couple[1]
print('gauche', gauche, 'droite', droite)
```

Cela fonctionne naturellement très bien, mais n'est pas très pythonique - comme on dit ;) Vous devez toujours garder en tête qu'il est rare en Python de manipuler des indices. Dès que vous voyez des indices dans votre code, vous devez vous demander si votre code est pythonique.

On préfèrera la formulation équivalente suivante :

```{code-cell} ipython3
(gauche, droite) = couple
print('gauche', gauche, 'droite', droite)
```

La logique ici consiste à dire : affecter les deux variables de sorte que le tuple `(gauche, droite)` soit égal à `couple`. On voit ici la supériorité de cette notion d'unpacking sur la manipulation d'indices : vous avez maintenant des variables qui expriment la nature de l'objet manipulé, votre code devient expressif, c'est-à-dire auto-documenté.

Remarquons que les parenthèses ici sont optionnelles - comme lorsque l'on construit un tuple - et on peut tout aussi bien écrire, et c'est le cas d'usage le plus fréquent d'omission des parenthèses pour le tuple :

```{code-cell} ipython3
gauche, droite = couple
print('gauche', gauche, 'droite', droite)
```

### Autres types

+++

Cette technique fonctionne aussi bien avec d'autres types. Par exemple, on peut utiliser :

* une syntaxe de liste à gauche du `=` ;
* une liste comme expression à droite du `=`.

```{code-cell} ipython3
# comme ceci
liste = [1, 2, 3]
[gauche, milieu, droit] = liste
print('gauche', gauche, 'milieu', milieu, 'droit', droit)
```

Et on n'est même pas obligés d'avoir le même type à gauche et à droite du signe `=`, comme ici :

```{code-cell} ipython3
# membre droit: une liste
liste = [1, 2, 3]
# membre gauche : un tuple
gauche, milieu, droit = liste
print('gauche', gauche, 'milieu', milieu, 'droit', droit)
```

En réalité, les seules contraintes fixées par Python sont que :

* le terme à droite du signe `=` soit un *itérable* (tuple, liste, string, etc.) ;
* le terme à gauche soit écrit comme un tuple ou une liste - notons tout de même que l'utilisation d'une liste à gauche est rare et peu pythonique ;
* les deux termes aient la même longueur - en tout cas avec les concepts que l'on a vus jusqu'ici, mais voir aussi plus bas l'utilisation de `*arg` avec le *extended unpacking*.

+++

La plupart du temps le terme de gauche est écrit comme un tuple. C'est pour cette raison que les deux termes *tuple unpacking* et *sequence unpacking* sont en vigueur.

+++

### La façon *pythonique* d'échanger deux variables

+++

Une caractéristique intéressante de l'affectation par *sequence unpacking* est qu'elle est sûre ; on n'a pas à se préoccuper d'un éventuel ordre d'évaluation, les valeurs **à droite** de l'affectation sont **toutes** évaluées en premier, et ainsi on peut par exemple échanger deux variables comme ceci :

```{code-cell} ipython3
a = 1
b = 2
a, b = b, a
print('a', a, 'b', b)
```

### *Extended unpacking*

+++

Le *extended unpacking* a été introduit en Python 3 ; commençons par en voir un exemple :

```{code-cell} ipython3
reference = [1, 2, 3, 4, 5]
a, *b, c = reference
print(f"a={a} b={b} c={c}")
```

Comme vous le voyez, le mécanisme ici est une extension de *sequence unpacking* ; Python vous autorise à mentionner **une seule fois**, parmi les variables qui apparaissent à gauche de l'affectation, une variable **précédée de `*`**, ici `*b`.

Cette variable est interprétée comme une **liste de longueur quelconque** des éléments de `reference`. On aurait donc aussi bien pu écrire :

```{code-cell} ipython3
reference = range(20)
a, *b, c = reference
print(f"a={a} b={b} c={c}")
```

Ce trait peut s'avérer pratique, lorsque par exemple on s'intéresse seulement aux premiers éléments d'une structure :

```{code-cell} ipython3
# si on sait que data contient prenom, nom, 
# et un nombre inconnu d'autres informations
data = [ 'Jean', 'Dupont', '061234567', '12', 'rue du four', '57000', 'METZ', ]

# on peut utiliser la variable _
# ce n'est pas une variable spéciale dans le langage,
# mais cela indique au lecteur que l'on ne va pas s'en servir
prenom, nom, *_ = data
print(f"prenom={prenom} nom={nom}")
```

## Complément - niveau intermédiaire

+++

On a vu les principaux cas d'utilisation de la *sequence unpacking*, voyons à présent quelques subtilités.

+++

### Plusieurs occurrences d'une même variable

+++

On peut utiliser **plusieurs fois** la même variable dans la partie gauche de l'affectation :

```{code-cell} ipython3
# ceci en toute rigueur est légal
# mais en pratique on évite de le faire
entree = [1, 2, 3]
a, a, a = entree
print(f"a = {a}")
```

**Attention** toutefois, comme on le voit ici, Python **n'impose pas** que les différentes occurrences de `a` correspondent **à des valeurs identiques** (en langage savant, on dirait que cela ne permet pas de faire de l'unification). De manière beaucoup plus pragmatique, l'interpréteur se contente de faire comme s'il faisait l'affectation plusieurs fois de gauche à droite, c'est-à-dire comme s'il faisait :

```{code-cell} ipython3
a = 1; a = 2; a = 3
```

Cette technique n'est utilisée en pratique que pour les parties de la structure dont on n'a que faire dans le contexte. Dans ces cas-là, il arrive qu'on utilise le nom de variable `_`, dont on rappelle qu'il est légal, ou tout autre nom comme `ignored` pour manifester le fait que cette partie de la structure ne sera pas utilisée, par exemple :

```{code-cell} ipython3
entree = [1, 2, 3]

_, milieu, _ = entree
print('milieu', milieu)

ignored, ignored, right = entree
print('right', right)
```

### En profondeur

+++

Le *sequence unpacking* ne se limite pas au premier niveau dans les structures, on peut extraire des données plus profondément imbriquées dans la structure de départ ; par exemple avec en entrée la liste :

```{code-cell} ipython3
structure = ['abc', [(1, 2), ([3], 4)], 5]
```

Si on souhaite extraire la valeur qui se trouve à l'emplacement du `3`, on peut écrire :

```{code-cell} ipython3
(a, (b, ((trois,), c)), d) = structure
print('trois', trois)
```

Ou encore, sans doute un peu plus lisible :

```{code-cell} ipython3
(a, (b, ([trois], c)), d) = structure
print('trois', trois)
```

Naturellement on aurait aussi bien pu écrire ici quelque chose comme :

```{code-cell} ipython3
trois = structure[1][1][0][0]
print('trois', trois)
```

Affaire de goût évidemment. Mais n'oublions pas une des phrases du Zen de Python $\textit{Flat is better than nested}$, ce qui veut dire que ce n'est pas parce que vous pouvez faire des structures imbriquées complexes que vous devez le faire. Bien souvent, cela rend la lecture et la maintenance du code complexe, j'espère que l'exemple précédent vous en a convaincu.

+++

### *Extended unpacking* et profondeur

+++

On peut naturellement ajouter de l'*extended unpacking* à n'importe quel étage d'un *unpacking* imbriqué :

```{code-cell} ipython3
# un exemple très alambiqué 
tree = [1, 2, [(3, 33, 'three', 'thirty-three')],
        ( [4, 44, ('forty', 'forty-four')])]
tree
```

```{code-cell} ipython3
# unpacking avec plusieurs variables *extended
*_,  ((_, *x3, _),), (*_, x4) = tree
print(f"x3={x3}, x4={x4}")
```

Dans ce cas, la limitation d'avoir une seule variable de la forme `*extended` s'applique toujours, naturellement, mais à chaque niveau dans l'imbrication, comme on le voit sur cet exemple.

+++

## Pour en savoir plus

* [Le PEP (en anglais) qui introduit le *extended unpacking*](https://www.python.org/dev/peps/pep-3132/).
