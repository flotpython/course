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
  title: Instruction del
---

# L'instruction `del`

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Complément - niveau basique

+++

Voici un récapitulatif sur l'instruction `del` selon le contexte dans lequel elle est utilisée.

+++

### Sur une variable

+++

On peut annuler la définition d'une variable, avec `del`.

Pour l'illustrer, nous utilisons un bloc `try … except …` pour attraper le cas échéant l'exception `NameError`, qui est produite lorsqu'on référence une variable qui n'est pas définie.

```{code-cell} ipython3
# la variable a n'est pas définie
try:
    print('a=', a)
except NameError as e:
    print("a n'est pas définie")
```

```{code-cell} ipython3
# on la définit
a = 10

# aucun souci ici, l'exception n'est pas levée
try:
    print('a=', a)
except NameError as e:
    print("a n'est pas définie")
```

```{code-cell} ipython3
# maintenant on peut effacer la variable
del a

# c'est comme si on ne l'avait pas définie
# dans la cellule précédente
try:
    print('a=', a)
except NameError as e:
    print("a n'est pas définie")
```

### Sur une liste

+++

On peut enlever d'une liste les éléments qui correspondent à une *slice* :

```{code-cell} ipython3
# on se donne une liste
l = list(range(12))
print(l)
```

```{code-cell} ipython3
# on considère une slice dans cette liste
print('slice=', l[2:10:3])

# voyons ce que ça donne si on efface cette slice
del l[2:10:3]
print("après del", l)
```

### Sur un dictionnaire

+++

Avec `del` on peut enlever une clé, et donc la valeur correspondante, d'un dictionnaire :

```{code-cell} ipython3
# partons d'un dictionaire simple
d = dict(foo='bar', spam='eggs', a='b')
print(d)
```

```{code-cell} ipython3
# on peut enlever une clé avec del
del d['a']
print(d)
```

### On peut passer plusieurs arguments à `del`

```{code-cell} ipython3
# Voyons où en sont nos données
print('l', l)
print('d', d)
```

```{code-cell} ipython3
# on peut invoquer 'del' avec plusieurs expressions
# séparées par une virgule
del l[3:], d['spam']

print('l', l)
print('d', d)
```

### Pour en savoir plus

+++

La page sur [l'instruction `del`](https://docs.python.org/3/reference/simple_stmts.html#the-del-statement) dans la documentation Python.
