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
  title: += et autres
---

# Affectations et Opérations (à la `+=`)

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Complément - niveau intermédiaire

+++

Il existe en Python toute une famille d'opérateurs dérivés de l'affectation qui permettent de faire en une fois une opération et une affectation. En voici quelques exemples.

+++

### Incrémentation

+++

On peut facilement augmenter la valeur d'une variable numérique comme ceci :

```{code-cell} ipython3
entier = 10

entier += 2
print('entier', entier)
```

Comme on le devine peut-être, ceci est équivalent à :

```{code-cell} ipython3
entier = 10

entier = entier + 2
print('entier', entier)
```

### Autres opérateurs courants

+++

Cette forme, qui combine opération sur une variable et réaffectation du résultat à la même variable, est disponible avec tous les opérateurs courants :

```{code-cell} ipython3
entier -= 4
print('après décrément', entier)
entier *= 2
print('après doublement', entier)
entier /= 2
print('mis à moitié', entier)
```

### Types non numériques

+++

En réalité cette construction est disponible sur tous les types qui supportent l'opérateur en question. Par exemple, les listes (que nous verrons bientôt) peuvent être additionnées entre elles :

```{code-cell} ipython3
liste = [0, 3, 5]
print('liste', liste)

liste += ['a', 'b']
print('après ajout', liste)
```

Beaucoup de types supportent l'opérateur `+`, qui est sans doute de loin celui qui est le plus utilisé avec cette construction.

+++

### Opérateurs plus abscons

+++

Signalons enfin que l'on trouve aussi cette construction avec d'autres opérateurs moins fréquents, par exemple :

```{code-cell} ipython3
entier = 2
print('entier:', entier)
entier **= 10
print('à la puissance dix:', entier)
entier %= 5
print('modulo 5:', entier)
```

Et pour ceux qui connaissent déjà un peu Python, on peut même le faire avec des opérateurs de décalage, que nous verrons très bientôt :

```{code-cell} ipython3
entier <<= 2
print('double décalage gauche:', entier)
```
