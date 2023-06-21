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
notebookname: yield from
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# `yield from` pour cascader deux générateurs

+++

Dans ce notebook nous allons voir comment fabriquer une fonction génératrice qui appelle elle-même une autre fonction génératrice.

+++

## Complément - niveau avancé

+++

### Une fonction génératrice

+++

Commençons à nous définir une fonction génératrice ; par exemple ici nous listons les diviseurs d'un entier, en excluant 1 et l'entier lui-même :

```{code-cell} ipython3
:cell_style: center

def divs(n, verbose=False):
    for i in range(2, n):
        if n % i == 0:
            if verbose: 
                print(f'trouvé diviseur {i} de {n}')
            yield i
```

Comme attendu, l'appel direct à cette fonction ne donne rien d'utile :

```{code-cell} ipython3
:cell_style: center

divs(28)
```

Mais lorsqu'on l'utilise dans une boucle `for`:

```{code-cell} ipython3
:cell_style: center

for d in divs(28):
    print(d)
```

### Une fonction génératrice qui appelle une autre fonction génératrice

+++

Bien, jusqu'ici c'est clair. Maintenant supposons que je veuille écrire une fonction génératrice qui énumère tous les diviseurs de tous les diviseurs d'un entier. Il s'agit donc, en sorte, d'écrire une fonction génératrice qui en appelle une autre - ici elle même.

+++

##### Première idée

+++

Première idée naïve pour faire cela, mais qui ne marche pas :

```{code-cell} ipython3
:cell_style: split

def divdivs(n):
    for i in divs(n):
        divs(i)
```

```{code-cell} ipython3
:cell_style: split

try:
    for i in divdivs(28):
        print(i)
except Exception as e:
    print(f"OOPS {e}")
```

Ce qui se passe ici, c'est que `divdivs` est perçue comme une fonction normale, lorsqu'on l'appelle elle ne retourne rien, donc `None` ; et c'est sur ce `None` qu'on essaie de faire la boucle `for` (à l'interieur du `try`), qui donc échoue.

+++

##### Deuxième idée

+++

Si on utilise juste `yield`, ça ne fait pas du tout ce qu'on veut :

```{code-cell} ipython3
:cell_style: split

def divdivs(n):
    for i in divs(n):
        yield divs(i)
```

```{code-cell} ipython3
:cell_style: split

try:
    for i in divdivs(28):
        print(i)
except Exception as e:
    print(f"OOPS {e}")
```

En effet, c'est logique, chaque `yield` dans `divdivs()` correspond à une itération de la boucle. Bref, il nous manque quelque chose dans le langage pour arriver à faire ce qu'on veut.

+++

##### `yield from`

+++

La construction du langage qui permet de faire ceci s'appelle `yield from`;

```{code-cell} ipython3
:cell_style: split

def divdivs(n):
    for i in divs(n):
        yield from divs(i, verbose=True)
```

```{code-cell} ipython3
:cell_style: split

try:
    for i in divdivs(28):
        print(i)
except Exception as e:
    print(f"OOPS {e}")
```

Avec `yield from`, on peut indiquer que `divdivs` est une fonction génératrice, et qu’il faut évaluer `divs(..)` comme un générateur à utiliser comme tel; une fonction génératrice attend des `yield`, on indique qu’elle doit aussi chercher dans la sous-fonction `divs`.

Tout ceci signifie, dit autrement, que l’appel

```
yield from divs(...)
```

est grosso-modo équivalent à

```
for truc in divs(...):
   yield truc
```
