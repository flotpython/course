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
notebookname: '`if` comme expression'
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Une forme alternative du `if`

+++

## Complément - niveau basique

+++

### Expressions et instructions

+++

Les constructions python que nous avons vues jusqu'ici peuvent se ranger en deux familles :

* d'une part les **expressions** sont les fragments de code qui **retournent une valeur** ;
  * c'est le cas lorsqu'on invoque n'importe quel opérateur numérique, pour les appels de fonctions, ...
* d'autre part les **instructions** ;
  * dans cette famille, nous avons vu par exemple l'affectation et `if`, et nous en verrons bien d'autres.

La différence essentielle est que les expressions peuvent être combinées entre elles pour faire des expressions arbitrairement grosses. Aussi, si vous avez un doute pour savoir si vous avez affaire à une expression ou à une instruction, demandez-vous si vous pourriez utiliser ce code **comme membre droit d'une affectation**. Si oui, vous avez une expression.

+++

### `if` est une instruction

+++

La forme du `if` qui vous a été présentée pendant la vidéo ne peut pas servir à renvoyer une valeur, c'est donc une **instruction**.

+++

Imaginons maintenant qu'on veuille écrire quelque chose d'aussi simple que *"affecter à y la valeur 12 ou 35, selon que x est vrai ou non"*.

+++

Avec les notions introduites jusqu'ici, il nous faudrait écrire ceci :

```{code-cell} ipython3
x = True  # ou quoi que ce soit d'autre
if x:
    y = 12
else:
    y = 35
print(y)
```

### Expression conditionnelle

+++

Il existe en Python une expression qui fait le même genre de test ; c'est la forme dite d'**expression conditionnelle**, qui est une **expression à part entière**, avec la syntaxe :

```python
<résultat_si_vrai> if <condition> else <résultat_si_faux>
```

+++

Ainsi on pourrait écrire l'exemple ci-dessus de manière plus simple et plus concise comme ceci :

```{code-cell} ipython3
y = 12 if x else 35
print(y)
```

Cette construction peut souvent rendre le style de programmation plus fonctionnel et plus fluide.

+++

## Complément - niveau intermédiaire

+++

### Imbrications

+++

Puisque cette forme est une expression, on peut l'utiliser dans une autre expression conditionnelle, comme ici :

```{code-cell} ipython3
# on veut calculer en fonction d'une entrée x
# une sortie qui vaudra
# -1 si x < -10
# 0 si -10 <= x <= 10
# 1 si x > 10

x = 5 # ou quoi que ce soit d'autre

valeur = -1 if x < -10 else (0 if x <= 10 else 1)

print(valeur)
```

Remarquez bien que cet exemple est équivalent à la ligne

```python
valeur = -1 if x < -10 else 0 if x <= 10 else 1
```

mais qu'il est fortement recommandé d'utiliser, comme on l'a fait, un parenthésage pour lever toute ambiguïté.

+++

### Pour en savoir plus

+++

 * La section sur les [expressions conditionnelles](https://docs.python.org/3/reference/expressions.html#conditional-expressions) de la documentation Python.
 * Le [PEP308](http://legacy.python.org/dev/peps/pep-0308/) qui résume les discussions ayant donné lieu au choix de la syntaxe adoptée.

De manière générale, les PEP rassemblent les discussions préalables à toutes les évolutions majeures du langage Python.
