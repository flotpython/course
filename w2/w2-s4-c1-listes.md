---
ipub:
  sphinx:
    toggle_input: true
    toggle_input_all: true
    toggle_output: true
    toggle_output_all: true
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
language_info:
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
livereveal:
  auto_select: code
  auto_select_fragment: true
  autolaunch: false
  backimage: media/nologo.png
  height: 100%
  slideNumber: c
  start_slideshow_at: selected
  theme: simple
  transition: fade
  width: 100%
nbhosting:
  title: "M\xE9thodes de listes"
---

# Méthodes spécifiques aux listes

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Complément - niveau basique

+++

Voici quelques unes des méthodes disponibles sur le type `list`.

+++

### Trouver l'information

+++

Pour commencer, rappelons comment retrouver la liste des méthodes définies sur le type `list` :

```{code-cell} ipython3
:latex-skip-eval: true

help(list)
```

Ignorez les méthodes dont le nom commence et termine par `__` (nous parlerons de ceci en semaine 6),  vous trouvez alors les méthodes utiles listées entre `append` et `sort`.

Certaines de ces méthodes ont été vues dans la vidéo sur les séquences, c'est le cas notamment de `count` et `index`.

+++

Nous allons à présent décrire les autres, partiellement et brièvement. Un autre complément décrit la méthode `sort`. Reportez-vous au lien donné en fin de notebook pour obtenir une information plus complète.

+++

Donnons-nous pour commencer une liste témoin :

```{code-cell} ipython3
liste = [0, 1, 2, 3]
print('liste', liste)
```

**Avertissements** :

* soyez bien attentifs au nombre de fois où vous exécutez les cellules de ce notebook ;
* par exemple une liste renversée deux fois peut donner l'impression que `reverse` ne marche pas ;
* n'hésitez pas à utiliser le menu *Cell -> Run All* pour réexécuter en une seule fois le notebook entier.

+++

### `append`

+++

La méthode `append` permet d'ajouter **un élément** à la fin d'une liste :

```{code-cell} ipython3
liste.append('ap')
print('liste', liste)
```

### `extend`

+++

La méthode `extend` réalise la même opération, mais avec **tous les éléments** de la liste qu'on lui passe en argument :

```{code-cell} ipython3
liste2 = ['ex1', 'ex2']
liste.extend(liste2)
print('liste', liste)
```

### `append` *vs* `+`

+++

Ces deux méthodes `append` et `extend` sont donc assez voisines ; avant de voir d'autres méthodes de `list`, prenons un peu le temps de comparer leur comportement avec l'addition `+` de liste. L'élément clé ici, on l'a déjà vu dans la vidéo, est que la liste est un objet **mutable**. `append` et `extend` **modifient** la liste sur laquelle elles travaillent, alors que l'addition **crée un nouvel objet**.

```{code-cell} ipython3
# pour créer une liste avec les n premiers entiers, on utilise
# la fonction built-in range(), que l'on convertit en liste
# on aura l'occasion d'y revenir
a1 = list(range(3))
print(a1)
```

```{code-cell} ipython3
a2 = list(range(10, 13))
print(a2)
```

```{code-cell} ipython3
# le fait d'utiliser + crée une nouvelle liste
a3 = a1 + a2
```

```{code-cell} ipython3
# si bien que maintenant on a trois objets différents
print('a1', a1)
print('a2', a2)
print('a3', a3)
```

Comme on le voit, après une addition, les deux termes de l'addition sont inchangés. Pour bien comprendre, voyons exactement le même scénario sous pythontutor :

```{code-cell} ipython3
%load_ext ipythontutor
```

**Note** : une fois que vous avez évalué la cellule avec `%%ipythontutor`, vous devez cliquer sur le bouton `Next` pour voir pas à pas le comportement du programme.

```{code-cell} ipython3
%%ipythontutor height=230 ratio=0.7
a1 = list(range(3))
a2 = list(range(10, 13))
a3 = a1 + a2
```

Alors que si on avait utilisé `extend`, on aurait obtenu ceci :

```{code-cell} ipython3
%%ipythontutor height=200 ratio=0.75
e1 = list(range(3))
e2 = list(range(10, 13))
e3 = e1.extend(e2)
```

Ici on tire profit du fait que la liste est un objet mutable : `extend` **modifie** l'objet sur lequel on l'appelle (ici `e1`). Dans ce scénario on ne crée en tout que deux objets, et du coup il est inutile pour extend de renvoyer quoi que ce soit, et c'est pourquoi `e3` ici vaut None.

+++

C'est pour cette raison que :

* l'addition est disponible sur tous les types séquences - on peut toujours réaliser l'addition puisqu'on crée un nouvel objet pour stocker le résultat de l'addition ;
* mais `append` et `extend` ne sont par exemple **pas disponibles** sur les chaînes de caractères, qui sont **immuables** - si `e1` était une chaîne, on ne pourrait pas la modifier pour lui ajouter des éléments.

+++

### Digression : les *magic* de IPython

+++

Arrêtons-nous une seconde pour commenter l'usage qu'on vient de faire de `%load_ext` et `%%ipythontutor`.

Ces commandes, qui commencent par un signe pourcent `%`, sont des commandes magiques (*magic*) de IPython; du coup elles ne sont **disponibles que** dans IPython ou un notebook.

Et je signale pour finir, pour les curieux, que 

* vous pouvez trouver [une liste de ces commandes ici](https://ipython.readthedocs.io/en/stable/interactive/magics.html
)

* et qu'une commande peut exister sous deux formes : avec un seul pourcent, la commande s'applique à la ligne, alors qu'avec deux pourcent cela concerne toute la cellule.

+++

Ainsi notamment la commande magique `%timeit`, qui permet de faire des benchmarks et comparer finement des temps d'exécution, s'utilise comme ceci

```{code-cell} ipython3
# avec un seul pourcent une commande magique concerne une seule ligne
# un peu de patience, c'est un petit peu long à exécuter

%timeit L1 = list(range(1000))

L2 = list(range(1000))
```

```{code-cell} ipython3
%%timeit
# avec deux pourcent, cela concerne toute la cellule
L1 = list(range(1000))
L2 = list(range(1000))
```

```{code-cell} ipython3
:tags: [raises-exception]

# et comme vous le voyez ici il faut dans ce cas-là 
# la mettre en première ligne de la cellule
# il y a une certaine logique à cela, mais bon
%%timeit
L1 = list(range(1000))
L2 = list(range(1000))
```

Vous remarquez surtout que `%timeit` exécute l'instruction un grand nombre de fois, c'est pour pouvoir faire une moyenne qui soit pertinente (on peut modifier ce nombre en passant des options à `timeit`, mais ne nous égarons pas…)

+++

### `insert`

+++

Mais reprenons notre inventaire des méthodes de `list`, et pour cela rappelons nous le contenu de la variable `liste` :

```{code-cell} ipython3
liste
```

La méthode `insert` permet, comme le nom le suggère, d'insérer un élément à une certaine position ; comme toujours les indices commencent à zéro et donc :

```{code-cell} ipython3
# insérer à l'index 2
liste.insert(2, '1 bis')
print('liste', liste)
```

On peut remarquer qu'un résultat analogue peut être obtenu avec une affectation de slice ; par exemple pour insérer au rang 5 (i.e. avant `ap`), on pourrait aussi bien faire :

```{code-cell} ipython3
liste[5:5] = ['3 bis']
print('liste', liste)
```

### `remove`

+++

La méthode `remove` détruit la **première occurrence** d'un objet dans la liste :

```{code-cell} ipython3
liste.remove(3)
print('liste', liste)
```

### `pop`

+++

La méthode `pop` prend en argument un indice ; elle permet d'extraire l'élément à cet indice. En un seul appel on obtient la valeur de l'élément et on l'enlève de la liste :

```{code-cell} ipython3
popped = liste.pop(0)
print('popped', popped, 'liste', liste)
```

Si l'indice n'est pas précisé, c'est le dernier élément de la liste qui est visé :

```{code-cell} ipython3
popped = liste.pop()
print('popped', popped, 'liste', liste)
```

### `reverse`

+++

Enfin `reverse` renverse la liste, le premier élément devient le dernier :

```{code-cell} ipython3
liste.reverse()
print('liste', liste)
```

On peut remarquer ici que le résultat se rapproche de ce qu'on peut obtenir avec une opération de slicing comme ceci :

```{code-cell} ipython3
liste2 = liste[::-1]
print('liste2', liste2)
```

**À la différence toutefois** qu'avec le slicing c'est une copie de la liste initiale qui est retournée, la liste de départ quant à elle n'est pas modifiée.

+++

### Pour en savoir plus

+++

<https://docs.python.org/3/tutorial/datastructures.html#more-on-lists>

+++

### Note spécifique aux notebooks

+++

#### `help` avec `?`

+++

Je vous signale en passant que dans un notebook vous pouvez obtenir de l'aide avec un point d'interrogation `?` inséré avant ou après un symbole. Par exemple pour obtenir des précisions sur la méthode `list.pop`, on peut faire soit :

```{code-cell} ipython3
# fonctionne dans tous les environnements Python
help(list.pop)
```

```{code-cell} ipython3
# spécifique aux notebooks
# l'affichage obtenu est légèrement différent
# tapez la touche 'Esc' - ou cliquez la petite croix
# pour faire disparaitre le dialogue qui apparaît en bas
list.pop?
```

#### Complétion avec `Tab`

+++

Dans un notebook vous avez aussi la complétion ; si vous tapez, dans une cellule de code, le début d'un mot connu dans l'environnement, vous voyez apparaître un dialogue avec les noms connus qui commencent par ce mot ici `li`; utilisez les flèches pour choisir, et 'Return' pour sélectionner.

```{code-cell} ipython3
:latex-skip-eval: true
:tags: [raises-exception]

# placez votre curseur à la fin de la ligne après 'li'
# et appuyez sur la touche 'Tab'
li
```
