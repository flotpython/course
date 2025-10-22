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
  title: "Les outils sur les cha\xEEnes"
---

# Les outils de base sur les chaînes de caractères (`str`)

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Complément - niveau intermédiaire

+++

### Lire la documentation

+++

Même après des années de pratique, il est difficile de se souvenir de toutes les méthodes travaillant sur les chaînes de caractères. Aussi il est toujours utile de recourir à la documentation embarquée

```{code-cell} ipython3
:latex-skip-eval: true

help(str)
```

Nous allons tenter ici de citer les méthodes les plus utilisées. Nous n'avons le temps que de les utiliser de manière très simple, mais bien souvent il est possible de passer en argument des options permettant de ne travailler que sur une sous-chaîne, ou sur la première ou dernière occurrence d'une sous-chaîne. Nous vous renvoyons à la documentation pour obtenir toutes les précisions utiles.

+++

### Découpage - assemblage : `split` et `join`

+++

Les méthodes `split` et `join` permettent de découper une chaîne selon un séparateur pour obtenir une liste, et à l'inverse de reconstruire une chaîne à partir d'une liste.

+++

`split` permet donc de découper :

```{code-cell} ipython3
'abc=:=def=:=ghi=:=jkl'.split('=:=')
```

Et à l'inverse :

```{code-cell} ipython3
"=:=".join(['abc', 'def', 'ghi', 'jkl'])
```

Attention toutefois si le séparateur est un terminateur, la liste résultat contient alors une dernière chaîne vide. En pratique, on utilisera la méthode `strip`, que nous allons voir ci-dessous, avant la méthode `split` pour éviter ce problème.

```{code-cell} ipython3
'abc;def;ghi;jkl;'.split(';')
```

Qui s'inverse correctement cependant :

```{code-cell} ipython3
";".join(['abc', 'def', 'ghi', 'jkl', ''])
```

### Remplacement : `replace`

+++

`replace` est très pratique pour remplacer une sous-chaîne par une autre, avec une limite éventuelle sur le nombre de remplacements :

```{code-cell} ipython3
"abcdefabcdefabcdef".replace("abc", "zoo")
```

```{code-cell} ipython3
"abcdefabcdefabcdef".replace("abc", "zoo", 2)
```

Plusieurs appels à `replace` peuvent être chaînés comme ceci :

```{code-cell} ipython3
"les [x] qui disent [y]".replace("[x]", "chevaliers").replace("[y]", "Ni")
```

### Nettoyage : `strip`

+++

On pourrait par exemple utiliser `replace` pour enlever les espaces dans une chaîne, ce qui peut être utile pour "nettoyer" comme ceci :

```{code-cell} ipython3
" abc:def:ghi ".replace(" ", "")
```

Toutefois bien souvent on préfère utiliser `strip` qui ne s'occupe que du début et de la fin de la chaîne, et gère aussi les tabulations et autres retour à la ligne :

```{code-cell} ipython3
" \tune chaîne avec des trucs qui dépassent \n".strip()
```

On peut appliquer `strip` avant `split` pour éviter le problème du dernier élément vide :

```{code-cell} ipython3
'abc;def;ghi;jkl;'.strip(';').split(';')
```

### Rechercher une sous-chaîne

+++

Plusieurs outils permettent de chercher une sous-chaîne. Il existe `find` qui renvoie le plus petit index où on trouve la sous-chaîne :

```{code-cell} ipython3
# l'indice du début de la première occurrence
"abcdefcdefghefghijk".find("def")
```

```{code-cell} ipython3
# ou -1 si la chaîne n'est pas présente
"abcdefcdefghefghijk".find("zoo")
```

`rfind` fonctionne comme `find` mais en partant de la fin de la chaîne :

```{code-cell} ipython3
# en partant de la fin
"abcdefcdefghefghijk".rfind("fgh")
```

```{code-cell} ipython3
# notez que le résultat correspond
# tout de même toujours au début de la chaîne

# NB: en python les indices commencent à zéro
# donc la notation ma_chaine[n] 
# permet d'accèder au n+1 ème caractère de la chaine
"abcdefcdefghefghijk"[13]
```

La méthode `index` se comporte comme `find`, mais en cas d'absence elle lève une **exception** (nous verrons ce concept plus tard) plutôt que de renvoyer `-1` :

```{code-cell} ipython3
"abcdefcdefghefghijk".index("def")
```

```{code-cell} ipython3
try:
    "abcdefcdefghefghijk".index("zoo")
except Exception as e:
    print("OOPS", type(e), e)
```

Mais le plus simple pour chercher si une sous-chaîne est dans une autre chaîne est d'utiliser l'instruction `in` sur laquelle nous reviendrons lorsque nous parlerons des séquences :

```{code-cell} ipython3
"def" in "abcdefcdefghefghijk"
```

La méthode `count` compte le nombre d'occurrences d'une sous-chaîne :

```{code-cell} ipython3
"abcdefcdefghefghijk".count("ef")
```

Signalons enfin les méthodes de commodité suivantes :

```{code-cell} ipython3
"abcdefcdefghefghijk".startswith("abcd")
```

```{code-cell} ipython3
"abcdefcdefghefghijk".endswith("ghijk")
```

S'agissant des deux dernières, remarquons que :

+++

`chaine.startswith(sous_chaine)` $\Longleftrightarrow$ `chaine.find(sous_chaine) == 0`

`chaine.endswith(sous_chaine)` $\Longleftrightarrow$ `chaine.rfind(sous_chaine) == (len(chaine) - len(sous_chaine))`

+++

On remarque ici la supériorité en terme d'expressivité des méthodes pythoniques `startswith` et `endswith`.

+++

### Changement de casse

+++

Voici pour conclure quelques méthodes utiles qui parlent d'elles-mêmes :

```{code-cell} ipython3
"monty PYTHON".upper()
```

```{code-cell} ipython3
"monty PYTHON".lower()
```

```{code-cell} ipython3
"monty PYTHON".swapcase()
```

```{code-cell} ipython3
"monty PYTHON".capitalize()
```

```{code-cell} ipython3
"monty PYTHON".title()
```

### Pour en savoir plus

+++

Tous ces outils sont [documentés en détail ici (en anglais)](https://docs.python.org/3/library/stdtypes.html#string-methods).
