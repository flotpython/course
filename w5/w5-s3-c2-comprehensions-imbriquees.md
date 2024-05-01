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
nbhosting:
  title: Rappels
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

# Compréhensions imbriquées

+++

## Compléments - niveau intermédiaire

+++

### Imbrications

+++

On peut également imbriquer plusieurs niveaux pour ne construire qu'une seule liste, comme par exemple :

```{code-cell} ipython3
[n + p for n in [2, 4] for p in [10, 20, 30]]
```

Bien sûr on peut aussi restreindre ces compréhensions, comme par exemple :

```{code-cell} ipython3
[n + p for n in [2, 4] for p in [10, 20, 30] if n*p >= 40]
```

Observez surtout que le résultat ci-dessus est une liste simple (de profondeur 1), à comparer avec :

```{code-cell} ipython3
[[n + p for n in [2, 4]] for p in [10, 20, 30]]
```

qui est de profondeur 2, et où les résultats atomiques apparaissent dans un ordre différent.

+++

Un moyen mnémotechnique pour se souvenir dans quel ordre les compréhensions imbriquées produisent leur résultat, est de penser à la version "naïve" du code qui produirait le même résultat ; dans ce code les clause `for` et `if` apparaissent **dans le même ordre** que dans la compréhension :

```{code-cell} ipython3
# notre exemple :
# [n + p for n in [2, 4] for p in [10, 20, 30] if n*p >= 40]

# est équivalent à ceci :
resultat = []
for n in [2, 4]:
    for p in [10, 20, 30]:
        if n*p >= 40:
            resultat.append(n + p)
resultat
```

### Ordre d'évaluation de `[[ .. for .. ] .. for .. ]`

+++

Pour rappel, on peut imbriquer des compréhensions de compréhensions. Commençons par poser

```{code-cell} ipython3
n = 4
```

On peut alors créer une liste de listes comme ceci :

```{code-cell} ipython3
[[(i, j) for i in range(1, j + 1)] for j in range(1, n + 1)]
```

Et dans ce cas, très logiquement, l'évaluation se fait **en commençant par la fin**, ou si on préfère **"par l'extérieur"**, c'est-à-dire que le code ci-dessus est équivalent à :

```{code-cell} ipython3
# en version bavarde, pour illustrer l'ordre des "for"
resultat_exterieur = []
for j in range(1, n + 1):
    resultat_interieur = []
    for i in range(1, j + 1):
        resultat_interieur.append((i, j))
    resultat_exterieur.append(resultat_interieur)
resultat_exterieur
```

### Avec `if`

+++

Lorsqu'on assortit les compréhensions imbriquées de cette manière de clauses `if`, l'ordre d'évaluation est tout aussi logique. Par exemple, si on voulait se limiter - arbitrairement - aux lignes correspondant à `j` pair, et aux diagonales où `i+j` est pair, on écrirait :

```{code-cell} ipython3
[[(i, j) for i in range(1, j + 1) if (i + j)%2 == 0]
         for j in range(1, n + 1) if j % 2 == 0]
```

ce qui est équivalent à :

```{code-cell} ipython3
# en version bavarde à nouveau
resultat_exterieur = []
for j in range(1, n + 1):
    if j % 2 == 0:
        resultat_interieur = []
        for i in range(1, j + 1):
            if (i + j) % 2 == 0:
                resultat_interieur.append((i, j))
        resultat_exterieur.append(resultat_interieur)
resultat_exterieur
```

Le point important ici est que l'**ordre** dans lequel il faut lire le code est **naturel**, et dicté par l'imbrication des `[ .. ]`.

+++

## Compléments - niveau avancé

+++

### Les variables de boucle *fuient*

+++

Nous avons déjà signalé que les variables de boucle **restent définies** après la sortie de la boucle, ainsi nous pouvons examiner :

```{code-cell} ipython3
i, j
```

C'est pourquoi, afin de comparer les deux formes de compréhension imbriquées nous allons explicitement retirer les variables `i` et `j` de l'environnement

```{code-cell} ipython3
del i, j
```

### Ordre d'évaluation de `[ .. for .. for .. ]`

+++

Toujours pour rappel, on peut également construire une compréhension imbriquée mais **à un seul niveau**. Dans une forme simple cela donne :

```{code-cell} ipython3
[(x, y) for x in [1, 2] for y in [1, 2]]
```

**Avertissement** méfiez-vous toutefois, car il est facile de ne pas voir du premier coup d'oeil qu'ici on évalue les deux clauses `for` **dans un ordre différent**.

+++

Pour mieux le voir, essayons de reprendre la logique de notre tout premier exemple, mais avec une forme de double compréhension *à plat* :

```{code-cell} ipython3
:latex-skip-eval: true

# ceci ne fonctionne pas
# NameError: name 'j' is not defined

[ (i, j) for i in range(1, j + 1) for j in range(1, n + 1) ]
```

On obtient une erreur, l'interpréteur se plaint à propos de la variable `j` (c'est pourquoi nous l'avons effacée de l'environnement au préalable).

+++

Ce qui se passe ici, c'est que, comme nous l'avons déjà mentionné en semaine 3, le code que nous avons écrit est en fait équivalent à :

```{code-cell} ipython3
:latex-skip-eval: true

# la version bavarde de cette imbrication à plat, à nouveau :
# [ (i, j) for i in range(1, j + 1) for j in range(1, n + 1) ]
# serait
resultat = []
for i in range(1, j + 1):
    for j in range(1, n + 1):
        resultat.append((i, j))
```

Et dans cette version * dépliée* on voit bien qu'en effet on utilise `j` avant qu'elle ne soit définie.

+++

### Conclusion

+++

La possibilité d'imbriquer des compréhensions avec plusieurs niveaux de `for` dans la même compréhension est un trait qui peut rendre service, car c'est une manière de simplifier la structure des entrées (on passe essentiellement d'une liste de profondeur 2 à une liste de profondeur 1).

Mais il faut savoir ne pas en abuser, et rester conscient de la confusion qui peut en résulter, et en particulier être prudent et prendre le temps de bien se relire. N'oublions pas non plus ces deux phrases du Zen de Python : "*Flat is better than nested*" et surtout "*Readability counts*".
