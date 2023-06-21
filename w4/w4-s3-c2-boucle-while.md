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
  title: while..else
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# La boucle `while` ... `else`

+++

## Complément - niveau basique

+++

### Boucles sans fin - `break`

+++

Utiliser `while` plutôt que `for` est une affaire de style et d'habitude. Cela dit en Python, avec les notions d'itérable et d'itérateur, on a tendance à privilégier l'usage du `for` pour les boucles finies et déterministes.

+++

Le `while` reste malgré tout d'un usage courant, et notamment avec une condition `True`.

Par exemple le code de l'interpréteur interactif de python pourrait ressembler, vu de très loin, à quelque chose comme ceci :

```python
while True:
    print(eval(read()))
```

+++

Notez bien par ailleurs que les instructions `break` et `continue` fonctionnent, à l'intérieur d'une boucle `while`, exactement comme dans un `for`, c'est-à-dire que :

* `continue` termine l'itération courante mais reste dans la boucle, alors que
* `break` interrompt l'itération courante et sort également de la boucle.

+++

## Complément - niveau intermédiaire

+++

### Rappel sur les conditions

+++

On peut utiliser dans une boucle `while` toutes les formes de conditions que l'on a vues à l'occasion de l'instruction `if`.

Dans le contexte de la boucle `while` on comprend mieux, toutefois, pourquoi le langage autorise d'écrire des conditions dont le résultat n'est **pas nécessairement un booléen**. Voyons cela sur un exemple simple :

```{code-cell} ipython3
# une autre façon de parcourir une liste
liste = ['a', 'b', 'c']

while liste:
    element = liste.pop()
    print(element)
```

### Une curiosité : la clause `else`

+++

Signalons enfin que la boucle `while` - au même titre d'ailleurs que la boucle `for`, peut être assortie [d'une clause `else`](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement), qui est exécutée à la fin de la boucle, **sauf dans le cas d'une sortie avec `break`**

```{code-cell} ipython3
# Un exemple de while avec une clause else

# si break_mode est vrai on va faire un break
# après le premier élément de la liste
def scan(liste, break_mode):

    # un message qui soit un peu parlant
    message = "avec break" if break_mode else "sans break"
    print(message)
    while liste:
        print(liste.pop())
        if break_mode:
            break
    else:
        print('else...')
```

```{code-cell} ipython3
:cell_style: split

# sortie de la boucle sans break
# on passe par else
scan(['a'], False)
```

```{code-cell} ipython3
:cell_style: split

# on sort de la boucle par le break
scan(['a'], True)
```

Ce trait est toutefois **très rarement** utilisé.
