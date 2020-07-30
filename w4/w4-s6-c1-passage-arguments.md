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
notebookname: Passage d'arguments
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Passage d'arguments

+++

## Complément - niveau intermédiaire

+++

### Motivation

+++

Jusqu'ici nous avons développé le modèle simple qu'on trouve dans tous les langages de programmation, à savoir qu'une fonction a un nombre fixe, supposé connu, d'arguments. Ce modèle a cependant quelques limitations ; les mécanismes de passage d'arguments que propose python, et que nous venons de voir dans les vidéos, visent à lever ces limitations.

Voyons de quelles limitations il s'agit.

+++

### Nombre d'arguments non connu à l'avance

+++

##### Ou encore : introduction à la forme `*arguments`

+++

Pour prendre un exemple aussi simple que possible, considérons la fonction `print`, qui nous l'avons vu, accepte un nombre quelconque d'arguments.

```{code-cell}
print("la fonction", "print", "peut", "prendre", "plein", "d'arguments")
```

Imaginons maintenant que nous voulons implémenter une variante de `print`, c'est-à-dire une fonction `error`, qui se comporte exactement comme `print` sauf qu'elle ajoute en début de ligne une balise `ERROR`.

Se posent alors deux problèmes :

* D'une part il nous faut un moyen de spécifier que notre fonction prend un nombre quelconque d'arguments. 
* D'autre part il faut une syntaxe pour repasser tous ces arguments à la fonction `print`.
 
On peut faire tout cela avec la notation en `*` comme ceci :

```{code-cell}
# accepter n'importe quel nombre d'arguments
def error(*print_args):
    # et les repasser à l'identique à print en plus de la balise
    print('ERROR', *print_args)

# on peut alors l'utiliser comme ceci
error("problème", "dans", "la", "fonction", "foo")
# ou même sans argument
error()
```

### Légère variation

+++

Pour sophistiquer un peu cet exemple, on veut maintenant imposer à la fonction `erreur` qu'elle reçoive un argument obligatoire de type entier qui représente un code d'erreur, plus à nouveau un nombre quelconque d'arguments pour `print`. 

Pour cela, on peut définir une signature (les paramètres de la fonction) qui

* prévoit un argument traditionnel en première position, qui sera obligatoire lors de l'appel, 
* et le tuple des arguments pour `print`, comme ceci :

```{code-cell}
# le premier argument est obligatoire
def error1(error_code, *print_args):
    message = f"message d'erreur code {error_code}"
    print("ERROR", message, '--', *print_args)
    
# que l'on peut à présent appeler comme ceci
error1(100, "un", "petit souci avec", [1, 2, 3])
```

Remarquons que maintenant la fonction `error1` ne peut plus être appelée sans argument, puisqu'on a mentionné un paramètre **obligatoire** `error_code`.

+++

### Ajout de fonctionnalités

+++

##### Ou encore : la forme `argument=valeur_par_defaut`

+++

Nous envisageons à présent le cas - tout à fait indépendant de ce qui précède - où vous avez écrit une librairie graphique, dans laquelle vous exposez une fonction `ligne` définie comme suit. Évidemment pour garder le code simple, nous imprimons seulement les coordonnées du segment :

```{code-cell}
# première version de l'interface pour dessiner une ligne
def ligne(x1, y1, x2, y2):
    "dessine la ligne (x1, y1) -> (x2, y2)"
    # restons simple
    print(f"la ligne ({x1}, {y1}) -> ({x2}, {y2})")
```

Vous publiez cette librairie en version 1, vous avez des utilisateurs ; et quelque temps plus tard vous écrivez une version 2 qui prend en compte la couleur. Ce qui vous conduit à ajouter un paramètre pour `ligne`.

+++

Si vous le faites en déclarant 

```python
def ligne(x1, y1, x2, y2, couleur):
    ...
```

alors tous les utilisateurs de la version 1 vont **devoir changer leur code** - pour rester à fonctionnalité égale - en ajoutant un cinquième argument `'noir'` à leurs appels à `ligne`.

+++

Vous pouvez éviter cet inconvénient en définissant la deuxième version de `ligne` comme ceci :

```{code-cell}
# deuxième version de l'interface pour dessiner une ligne
def ligne(x1, y1, x2, y2, couleur="noir"):
    "dessine la ligne (x1, y1) -> (x2, y2) dans la couleur spécifiée"
    # restons simple
    print(f"la ligne ({x1}, {y1}) -> ({x2}, {y2}) en {couleur}")
```

Avec cette nouvelle définition, on peut aussi bien

```{code-cell}
# faire fonctionner du vieux code sans le modifier
ligne(0, 0, 100, 100)
# ou bien tirer profit du nouveau trait
ligne(0, 100, 100, 0, 'rouge')
```

##### Les paramètres par défaut sont très utiles

+++

Notez bien que ce genre de situation peut tout aussi bien se produire sans que vous ne publiiez de librairie, à l'intérieur d'une seule application. Par exemple, vous pouvez être amené à ajouter un argument à une fonction parce qu'elle doit faire face à de nouvelles situations imprévues, et que vous n'avez pas le temps de modifier tout le code.

+++

Ou encore plus simplement, vous pouvez choisir d'utiliser ce passage de paramètres dès le début de la conception ; une fonction `ligne` réaliste présentera une interface qui précise les points concernés, la couleur du trait, l'épaisseur du trait, le style du trait, le niveau de transparence, etc. Il n'est vraiment pas utile que tous les appels à `ligne` reprécisent tout ceci intégralement, aussi une bonne partie de ces paramètres seront très constructivement déclarés avec une valeur par défaut.

+++

## Complément - niveau avancé

+++

### Écrire un wrapper

+++

##### Ou encore : la forme `**keywords`

+++

La notion de *wrapper* - emballage, en anglais - est très répandue en informatique, et consiste, à partir d'un morceau de code souche existant (fonction ou classe) à définir une variante qui se comporte comme la souche, mais avec quelques légères différences.

La fonction `error` était déjà un premier exemple de *wrapper*. Maintenant nous voulons définir un *wrapper* `ligne_rouge`, qui sous-traite à la fonction `ligne` mais toujours avec la couleur rouge. 

Maintenant que l'on a injecté la notion de paramètre par défaut dans le système de signature des fonctions, se repose la question de savoir comment passer à l'identique les arguments de `ligne_rouge` à `ligne`.

+++

Évidemment, une première option consiste à regarder la signature de `ligne` :

```python3
def ligne(x1, y1, x2, y2, couleur="noir")
```

+++

Et à en déduire une implémentation de `ligne_rouge` comme ceci

```{code-cell}
# la version naïve - non conseillée - de ligne_rouge
def ligne_rouge(x1, y1, x2, y2):
    return ligne(x1, y1, x2, y2, couleur='rouge')

ligne_rouge(0, 0, 100, 100)
```

Toutefois, avec cette implémentation, si la signature de `ligne` venait à changer, on serait vraisemblablement amené à changer **aussi** celle de `ligne_rouge`, sauf à perdre en fonctionnalité. Imaginons en effet que `ligne` devienne dans une version suivante

```{code-cell}
# on ajoute encore une fonctionnalité à la fonction ligne
def ligne(x1, y1, x2, y2, couleur="noir", epaisseur=2):
    print(f"la ligne ({x1}, {y1}) -> ({x2}, {y2})"
          f" en {couleur} - ep. {epaisseur}")
```

Alors le wrapper ne nous permet plus de profiter de la nouvelle fonctionnalité. 
De manière générale, on cherche au maximum à se prémunir contre de telles dépendances. 
Aussi, il est de beaucoup préférable d'implémenter `ligne_rouge` comme suit, où vous remarquerez que **la seule hypothèse** faite sur `ligne` est qu'elle accepte un argument nommé `couleur`.

```{code-cell}
def ligne_rouge(*arguments, **keywords):
    # c'est le seul endroit où on fait une hypothèse sur la fonction `ligne`
    # qui est qu'elle accepte un argument nommé 'couleur'
    keywords['couleur'] = "rouge"
    return ligne(*arguments, **keywords)
```

Ce qui permet maintenant de faire

```{code-cell}
ligne_rouge(0, 100, 100, 0, epaisseur=4)
```

### Pour en savoir plus - la forme générale

+++

Une fois assimilé ce qui précède, vous avez de quoi comprendre une énorme majorité (99% au moins) du code Python. 

Dans le cas général, il est possible de combiner les 4 formes d'arguments :

 * arguments "normaux", dits positionnels
 * arguments nommés, comme `nom=<valeur>`
 * forme `*args`
 * forme `**dargs`
 
Vous pouvez [vous reporter à cette page](https://docs.python.org/3/reference/expressions.html#calls)
pour une description détaillée de ce cas général.

+++

À l'appel d'une fonction, il faut résoudre les arguments, c'est-à-dire associer une valeur à chaque paramètre formel (ceux qui apparaissent dans le `def`) à partir des valeurs figurant dans l'appel.

L'idée est que pour faire cela, les arguments de l'appel ne sont pas pris dans l'ordre où ils apparaissent, mais les arguments positionnels sont utilisés en premier. La logique est que, naturellement les arguments positionnels (ou ceux qui proviennent d'une `*expression`) viennent sans nom, et donc ne peuvent pas être utilisés pour résoudre des arguments nommés.

+++

Voici un tout petit exemple pour vous donner une idée de la complexité de ce mécanisme lorsqu'on mélange toutes les 4 formes d'arguments à l'appel de la fonction (alors qu'on a défini la fonction avec 4 paramètres positionnels)

```{code-cell}
# une fonction qui prend 4 paramètres simples
def foo(a, b, c, d):
    print(a, b, c, d)
```

```{code-cell}
# on peut l'appeler par exemple comme ceci
foo(1, c=3, *(2,), **{'d':4})
```

```{code-cell}
# mais pas comme cela
try:
    foo (1, b=3, *(2,), **{'d':4})
except Exception as e:
    print(f"OOPS, {type(e)}, {e}")
```

Si le problème ne vous semble pas clair, vous pouvez regarder la [documentation python décrivant ce problème](https://docs.python.org/3/reference/expressions.html#calls).
