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
  title: "\xC9valuation des tests"
---

# Évaluation des tests

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Complément - niveau basique

+++

### Quels tests sont évalués ?

+++

On a vu dans la vidéo que l'instruction conditionnelle `if` permet d'implémenter simplement des branchements à plusieurs choix, comme dans cet exemple :

```{code-cell} ipython3
s = 'berlin'
if 'a' in s:
    print('avec a')
elif 'b' in s:
    print('avec b')
elif 'c' in s:
    print('avec c')
else:
    print('sans a ni b ni c')
```

Comme on s'en doute, les expressions conditionnelles **sont évaluées jusqu'à obtenir un résultat vrai** - ou considéré comme vrai -, et le bloc correspondant est alors exécuté. Le point important ici est qu'**une fois qu'on a obtenu un résultat vrai**, on sort de l'expression conditionnelle **sans évaluer les autres conditions**. 
En termes savants, on parle d'évaluation paresseuse : on s'arrête dès qu'on peut.

+++

Dans notre exemple, on aura évalué à la sortie `'a' in s`, et aussi `'b' in s`, mais pas `'c' in s`

+++

### Pourquoi c'est important ?

+++

C'est important de bien comprendre quels sont les tests qui sont réellement évalués pour deux raisons :

* d'abord, pour des raisons de performance ; comme on n'évalue que les tests nécessaires, si un des tests prend du temps, il est peut-être préférable de le faire en dernier ;
* mais aussi et surtout, il se peut tout à fait qu'un test fasse des **effets de bord**, c'est-à-dire qu'il modifie un ou plusieurs objets.

+++

Dans notre premier exemple, les conditions elles-mêmes sont inoffensives ; la valeur de `s` reste *identique*, que l'on *évalue ou non* les différentes conditions.

Mais nous allons voir ci-dessous qu'il est relativement facile d'écrire des conditions qui **modifient** par **effet de bord** les objets mutables sur lesquelles elles opèrent, et dans ce cas il est crucial de bien assimiler la règle des évaluations des expressions dans un `if`.

+++

## Complément - niveau intermédiaire

+++

### Rappel sur la méthode `pop`

+++

Pour illustrer la notion d'**effet de bord**, nous revenons sur la méthode de liste `pop()` qui, on le rappelle, renvoie un élément de liste **après l'avoir effacé** de la liste.

```{code-cell} ipython3
# on se donne une liste
liste = ['premier', 'deuxieme', 'troisieme']
print(f"liste={liste}")
```

```{code-cell} ipython3
# pop(0) renvoie le premier élément de la liste, et raccourcit la liste
element = liste.pop(0)
print(f"après pop(0), element={element} et liste={liste}")
```

```{code-cell} ipython3
# et ainsi de suite
element = liste.pop(0)
print(f"après pop(0), element={element} et liste={liste}")
```

### Conditions avec effet de bord

+++

Une fois ce rappel fait, voyons maintenant l'exemple suivant :

```{code-cell} ipython3
liste = list(range(5))
print('liste en entree:', liste, 'de taille', len(liste))
```

```{code-cell} ipython3
if liste.pop(0) <= 0:
    print('cas 1')
elif liste.pop(0) <= 1:
    print('cas 2')
elif liste.pop(0) <= 2:
    print('cas 3')
else:
    print('cas 4')
print('liste en sortie de taille', len(liste))
```

Avec cette entrée, le premier test est vrai (car `pop(0)` renvoie 0), aussi on n'exécute en tout `pop()` qu'**une seule fois**, et donc à la sortie la liste n'a été raccourcie que d'un élément.

+++

Exécutons à présent le même code avec une entrée différente :

```{code-cell} ipython3
liste = list(range(5, 10))
print('en entree: liste=', liste, 'de taille', len(liste))
```

```{code-cell} ipython3
if liste.pop(0) <= 0:
    print('cas 1')
elif liste.pop(0) <= 1:
    print('cas 2')
elif liste.pop(0) <= 2:
    print('cas 3')
else:
    print('cas 4')
print('en sortie: liste=', liste, 'de taille', len(liste))
```

On observe que cette fois la liste a été **raccourcie 3 fois**, car les trois tests se sont révélés faux.

+++

Cet exemple vous montre qu'il faut être attentif avec des conditions qui font des effets de bord. Bien entendu, ce type de pratique est de manière générale à utiliser avec beaucoup de discernement.

+++

### Court-circuit (*short-circuit*)

+++

La logique que l'on vient de voir est celle qui s'applique aux différentes branches d'un `if` ; c'est la même logique qui est à l'œuvre aussi lorsque python évalue une condition logique à base de `and` et `or`. C'est ici aussi une forme d'évaluation paresseuse.

+++

Pour illustrer cela, nous allons nous définir deux fonctions toutes simples qui renvoient `True` et `False` mais avec une impression de sorte qu'on voit lorsqu'elles sont exécutées :

```{code-cell} ipython3
:tags: [gridwidth-1-2]

def true():
    print('true')
    return True
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

def false():
    print('false')
    return False
```

```{code-cell} ipython3
true()
```

Ceci va nous permettre d'illustrer notre point, qui est que lorsque python évalue un `and` ou un `or`, il **n'évalue la deuxième condition que si c'est nécessaire**. Ainsi par exemple :

```{code-cell} ipython3
:tags: [gridwidth-1-2]

false() and true()
```

+++ {"tags": ["gridwidth-1-2"]}

Dans ce cas, python évalue la première partie du `and` - qui provoque l'impression de `false` - et comme le résultat est faux, il n'est **pas nécessaire** d'évaluer la seconde condition, on sait que de toute façon le résultat du `and` est forcément faux. C'est pourquoi vous ne voyez pas l'impression de `true`.

+++

De manière symétrique avec un `or` :

```{code-cell} ipython3
:tags: [gridwidth-1-2]

true() or false()
```

+++ {"tags": ["gridwidth-1-2"]}

À nouveau ici il n'est pas nécessaire d'évaluer `false()`, et donc seul `true` est imprimé à l'évaluation.

+++

À titre d'exercice, essayez de dire combien d'impressions sont émises lorsqu'on évalue cette expression un peu plus compliquée :

```{code-cell} ipython3
true() and (false() or true()) or (true () and false())
```
