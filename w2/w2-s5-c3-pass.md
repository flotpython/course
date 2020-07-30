---
jupytext:
  cell_metadata_filter: all
  notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
notebookname: Instruction pass
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# L'instruction `pass`

+++

## Complément - niveau basique

+++

Nous avons vu qu'en Python les blocs de code sont définis par leur indentation.

+++

### Une fonction vide

+++

Cette convention a une limitation lorsqu'on essaie de définir un bloc vide. Voyons par exemple comment on définirait en C une fonction qui ne fait rien :

+++

```C
/* une fonction C qui ne fait rien */
void foo() {}
```

+++

Comme en Python on n'a pas d'accolade pour délimiter les blocs de code, il existe une instruction `pass`, qui ne fait rien. À l'aide de cette instruction on peut à présent définir une fonction vide comme ceci :

```{code-cell}
# une fonction Python qui ne fait rien
def foo():
    pass
```

### Une boucle vide

+++

Pour prendre un second exemple un peu plus pratique, et pour anticiper un peu sur l'instruction `while` que nous verrons très bientôt, voici un exemple d'une boucle vide, c'est à dire sans corps, qui permet de "dépiler" dans une liste jusqu'à l'obtention d'une certaine valeur :

```{code-cell}
liste = list(range(10))
print('avant', liste)
while liste.pop() != 5:
    pass
print('après', liste)
```

On voit qu'ici encore l'instruction `pass` a toute son utilité.

+++

## Complément - niveau intermédiaire

+++

### Un `if` sans `then`

```{code-cell}
# on utilise dans ces exemples une condition fausse
condition = False
```

Imaginons qu'on parte d'un code hypothétique qui fasse ceci :

```{code-cell}
# la version initiale
if condition:
    print("non")
else:
    print("bingo")
```

Et que l'on veuille modifier ce code pour simplement supprimer l'impression de `non`. La syntaxe du langage **ne permet pas** de simplement commenter le premier `print` :
```python
# si on commente le premier print
# la syntaxe devient incorrecte
if condition:
#    print "non"
else:
    print "bingo"
```

+++

Évidemment ceci pourrait être récrit autrement en inversant la condition, mais parfois on s'efforce de limiter au maximum l'impact d'une modification sur le code. Dans ce genre de situation on préférera écrire plutôt :

```{code-cell}
# on peut s'en sortir en ajoutant une instruction pass
if condition:
#    print "non"
    pass
else:
    print("bingo")
```

### Une classe vide

+++

Enfin, comme on vient de le voir dans la vidéo, on peut aussi utiliser `pass` pour définir une classe vide comme ceci :

```{code-cell}
class Foo:
    pass
```

```{code-cell}
foo = Foo()
```
