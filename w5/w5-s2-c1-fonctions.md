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
notebookname: Prog. fonctionnelle
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Programmation fonctionnelle

+++

## Complément - niveau basique

+++

### Pour résumer

+++

La notion de programmation fonctionnelle consiste essentiellement à pouvoir manipuler les fonctions comme des objets à part entière, et à les passer en argument à d'autres fonctions, comme cela est illustré dans la vidéo.

+++

On peut créer une fonction par l'intermédiaire de :

 * l'*expression* `lambda:`, on obtient alors une fonction *anonyme* ;
 * l'*instruction* `def` et dans ce cas on peut accéder à l'objet fonction par son nom.

Pour des raisons de syntaxe surtout, on a davantage de puissance avec `def`.

+++

On peut calculer la liste des résultats d'une fonction sur une liste (plus généralement un itérable) d'entrées par :

 * `map`, éventuellement combiné à `filter` ;
 * une compréhension de liste, éventuellement assortie d'un `if`.

Nous allons revoir les compréhensions dans la prochaine vidéo.

+++

## Complément - niveau intermédiaire

+++

Pour les curieux qui ont entendu le terme de *map - reduce* , voici la logique derrière l'opération `reduce`, qui est également disponible en Python au travers du module `functools`.

+++

### `reduce`

+++

La fonction `reduce` permet d'appliquer une opération associative à une liste d'entrées. Pour faire simple, étant donné un opérateur binaire $\otimes$ on veut pouvoir calculer

 $x_1 \otimes x_2 ... \otimes x_n$

De manière un peu moins abstraite, on suppose qu'on dispose d'une **fonction binaire** `f` qui implémente l'opérateur $\otimes$, et alors 

   `reduce` $( f, [x_1, .. x_n] ) = f ( ... f(f(x_1,x_2), x_3), .. , x_n)$

+++

En fait `reduce` accepte un troisième argument - qu'il faut comprendre comme l'élément neutre de l'opérateur/fonction en question - et qui est retourné lorsque la liste en entrée est vide.

+++

Par exemple voici - encore - une autre implémentation possible de la fonction `factoriel`.

On utilise ici [le module `operator`](https://docs.python.org/3/library/operator.html), qui fournit sous forme de fonctions la plupart des opérateurs du langage, et notamment, dans notre cas, `operator.mul` ; cette fonction retourne tout simplement le produit de ses deux arguments.

```{code-cell} ipython3
# la fonction reduce dans Python 3 n'est plus une built-in comme en Python 2
# elle fait partie du module functools
from functools import reduce

# la multiplication, mais sous forme de fonction et non d'opérateur
from operator import mul

def factoriel(n):
    return reduce(mul, range(1, n+1), 1)

# ceci fonctionne aussi pour factoriel (0)
for i in range(5):
    print(f"{i} -> {factoriel(i)}")
```

##### Cas fréquents de `reduce`

+++

Par commodité, Python fournit des fonctions built-in qui correspondent en fait à des `reduce` fréquents, comme la somme, et les opérations `min` et `max` :

```{code-cell} ipython3
entrees = [8, 5, 12, 4, 45, 7]

print('sum', sum(entrees))
print('min', min(entrees))
print('max', max(entrees))
```
