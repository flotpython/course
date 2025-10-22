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
  title: Intro. sur les types
---

# Un peu de calcul sur les types

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Complément - niveau basique

+++

### La fonction `type`

+++

Nous avons vu dans la vidéo que chaque objet possède un type. On peut très simplement accéder au type d'un objet en appelant une fonction *built-in*, c'est-à-dire prédéfinie dans Python, qui s'appelle, eh bien oui, `type`.

+++

On l'utilise tout simplement comme ceci :

```{code-cell} ipython3
:tags: [gridwidth-1-2]

type(1)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

type('spam')
```

Cette fonction est assez peu utilisée par les programmeurs expérimentés, mais va nous être utile à bien comprendre le langage, notamment pour manipuler les valeurs numériques.

+++

### Types, variables et objets

+++

On a vu également que le type est attaché **à l'objet** et non à la variable.

```{code-cell} ipython3
:tags: [gridwidth-1-2]

x = 1
type(x)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# la variable x peut référencer un objet de n'importe quel type

x = [1, 2, 3]
type(x)
```

## Complément - niveau avancé

+++

### La fonction `isinstance`

+++

Une autre fonction prédéfinie, voisine de `type` mais plus utile dans la pratique, est la fonction `isinstance` qui permet de savoir si un objet est d'un type donné. Par exemple :

```{code-cell} ipython3
isinstance(23, int)
```

À la vue de ce seul exemple, on pourrait penser que `isinstance` est presque identique à `type`&nbsp;; en réalité elle est un peu plus élaborée, notamment pour la programmation objet et l'héritage, nous aurons l'occasion d'y revenir.

+++

On remarque ici en passant que la variable `int` est connue de Python alors que nous ne l'avons pas définie. Il s'agit d'une variable prédéfinie, qui désigne le type des entiers, que nous étudierons très bientôt.

+++

Pour conclure sur `isinstance`, cette fonction est utile en pratique précisément parce que Python est à typage dynamique. Aussi il est souvent utile de s'assurer qu'une variable passée à une fonction est du (ou des) type(s) attendu(s), puisque contrairement à un langage typé statiquement comme C++, on n'a aucune garantie de ce genre à l'exécution. À nouveau, nous aurons l'occasion de revenir sur ce point.
