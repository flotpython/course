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
notebookname: Prog. fonctionelle
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Comparaison de fonctions

+++

## Exercice - niveau avancé

À présent nous allons écrire une version très simplifiée de l'outil qui est utilisé dans ce cours pour corriger les exercices. Vous aurez sans doute remarqué que les fonctions de correction prennent en argument la fonction à corriger.

Par exemple un peu plus bas, la cellule de correction fait

```python
exo_compare_all.correction(compare_all)
```

dans lequel `compare_all` est l'objet fonction que vous écrivez en réponse à cet exercice.

+++

On vous demande d'écrire une fonction `compare` qui prend en argument :

 * deux fonctions `f` et `g` ; imaginez que l'une d'entre elles fonctionne et qu'on cherche à valider l'autre ; dans cette version simplifiée toutes les fonctions acceptent exactement un argument ;
 * une liste d'entrées `entrees` ; vous pouvez supposer que chacune de ces entrées est dans le domaine de `f` et de `g` (dit autrement, on peut appeler `f` et `g` sur chacune des entrées sans craindre qu'une exception soit levée).

Le résultat attendu pour le retour de `compare` est une liste qui contient autant de booléens que d'éléments dans `entrees`, chacun indiquant si avec l'entrée correspondante on a pu vérifier que `f(entree) == g(entree)`.

Dans cette première version de l'exercice vous pouvez enfin supposer que les entrées ne sont pas modifiées par `f` ou `g`.

+++

Pour information dans cet exercice :

 * `factorial` correspond à `math.factorial`
 * `fact` et `broken_fact` sont des fonctions implémentées par nos soins, la première est correcte alors que la seconde retourne 0 au lieu de 1 pour l'entrée 0.

```{code-cell} ipython3
# par exemple
from corrections.exo_compare_all import exo_compare_all
exo_compare_all.example()
```

Ce qui, dit autrement, veut tout simplement dire que `fact` et `factorial` coïncident sur les entrées 0, 1 et 5, alors que `broken_fact` et `factorial` ne renvoient pas la même valeur avec l'entrée `0`.

```{code-cell} ipython3
# c'est à vous
def compare_all(f, g, entrees):
    "<votre code>"
```

```{code-cell} ipython3
# pour vérifier votre code
exo_compare_all.correction(compare_all)
```

## Exercice optionnel - niveau avancé

### `compare` revisitée

+++

Nous reprenons ici la même idée que `compare`, mais en levant l'hypothèse que les deux fonctions attendent un seul argument. Il faut écrire une nouvelle fonction `compare_args` qui prend en entrée :

 * deux fonctions `f` et `g` comme ci-dessus ;
 * mais cette fois une liste (ou un tuple) `argument_tuples` de **tuples** d'arguments d'entrée.
 
Comme ci-dessus on attend en retour une liste `retour` de booléens, de même taille que `argument_tuples`, telle que, si `len(argument_tuples)` vaut $n$ :
 
$\forall i \in \{1,...,n\}$, si `argument_tuples[i]` == [ $a_1$,...,$a_j$ ], alors

`retour(i) == True` $\Longleftrightarrow$  f ($a_1$,...,$a_j$) == g ($a_1$,...,$a_j$)

+++

Pour information, dans tout cet exercice :

 * `factorial` correspond à `math.factorial` ;
 * `fact` et `broken_fact` sont des fonctions implémentées par nos soins, la première est correcte alors que la seconde retourne 0 au lieu de 1 pour l'entrée 0 ;
 * `add` correspond à l'addition binaire `operator.add` ;
 * `plus` et `broken_plus` sont des additions binaires que nous avons écrites, l'une étant correcte et l'autre étant fausse lorsque le premier argument est nul.

```{code-cell} ipython3
from corrections.exo_compare_args import exo_compare_args
exo_compare_args.example()
```

```{code-cell} ipython3
# ATTENTION vous devez aussi définir les arguments de la fonction
def compare_args(votre, signature):
    "<votre_code>"
```

```{code-cell} ipython3
exo_compare_args.correction(compare_args)
```
