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
  title: "Les diff\xE9rentes copies"
---

# Les différentes copies

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

```{code-cell} ipython3
%load_ext ipythontutor
```

## Complément - niveau basique

+++

### Deux types de copie

+++

Pour résumer les deux grands types de copie que l'on a vus dans la vidéo :

* La *shallow copy* - de l'anglais *shallow* qui signifie superficiel ;
* La *deep copy* - de *deep* qui signifie profond.

+++

### Le module `copy`

+++

Pour réaliser une copie, la méthode la plus simple, en ceci qu'elle fonctionne avec tous les types de manière identique, consiste à utiliser [le module standard `copy`](https://docs.python.org/3/library/copy.html), et notamment :

* `copy.copy` pour une copie superficielle ;
* `copy.deepcopy` pour une copie en profondeur.

```{code-cell} ipython3
import copy
#help(copy.copy)
#help(copy.deepcopy)
```

### Un exemple

+++

Nous allons voir le résultat des deux formes de copie sur un même sujet de départ.

+++

#### La copie superficielle / *shallow* copie / `copy.copy`

+++

N'oubliez pas de cliquer le bouton `Next` dans la fenêtre pythontutor :

```{code-cell} ipython3
%%ipythontutor height=410 curInstr=6
import copy
# On se donne un objet de départ
source = [
    [1, 2, 3],  # une liste
    {1, 2, 3},  # un ensemble
    (1, 2, 3),  # un tuple
    '123',       # un string
    123,         # un entier
]
# une copie simple renvoie ceci
shallow_copy = copy.copy(source)
```

Vous remarquez que :

* la source et la copie partagent tous leurs (sous-)éléments, et notamment la liste `source[0]` et l'ensemble `source[1]` ;
* ainsi, après cette copie, on peut modifier l'un de ces deux objets (la liste ou l'ensemble), et ainsi modifier la source **et** la copie.

+++

On rappelle aussi que, la source étant une liste, on aurait pu aussi bien faire la copie superficielle avec

```python
shallow2 = source[:]
```

+++

#### La copie profonde / *deep* copie / `copy.deepcopy`

+++

Sur le même objet de départ, voici ce que fait la copie profonde :

```{code-cell} ipython3
%%ipythontutor height=410 curInstr=6
import copy
# On se donne un objet de départ
source = [
    [1, 2, 3],  # une liste
    {1, 2, 3},  # un ensemble
    (1, 2, 3),  # un tuple
    '123',       # un string
    123,         # un entier
]
# une copie profonde renvoie ceci
deep_copy = copy.deepcopy(source)
```

Ici, il faut remarquer que :

* les deux objets mutables accessibles via `source`, c'est-à-dire **la liste** `source[0]` et **l'ensemble `source[1]`**, ont été tous deux dupliqués ;
* **le tuple** correspondant à `source[2]` n'est **pas dupliqué**, mais comme il n'est **pas mutable** on ne peut pas modifier la copie au travers de la source ;
* de manière générale, on a la bonne propriété que la source et sa copie ne partagent rien qui soit modifiable ;
* et donc on ne peut pas modifier l'un au travers de l'autre.

On retrouve donc à nouveau l'optimisation qui est mise en place dans python pour implémenter les types immuables comme des singletons lorsque c'est possible. Cela a été vu en détail dans le complément consacré à l'opérateur `is`.

+++

## Complément - niveau intermédiaire

```{code-cell} ipython3
# on répète car le code précédent a seulement été exposé à pythontutor
import copy
source = [
    [1, 2, 3],  # une liste
    {1, 2, 3},  # un ensemble
    (1, 2, 3),  # un tuple
    '123',       # un string
    123,         # un entier
]
shallow_copy = copy.copy(source)
deep_copy = copy.deepcopy(source)
```

### Objets *égaux* au sens logique

+++

Bien sûr ces trois objets se ressemblent si on fait une comparaison *logique* avec `==` :

```{code-cell} ipython3
print('source == shallow_copy:', source == shallow_copy)
print('source == deep_copy:', source == deep_copy)
```

### Inspectons les objets de premier niveau

+++

Mais par contre si on compare **l'identité** des objets de premier niveau, on voit que `source` et `shallow_copy` partagent leurs objets :

```{code-cell} ipython3
# voir la cellule ci-dessous si ceci vous parait peu clair
for i, (source_item, copy_item) in enumerate(zip(source, shallow_copy)):
    compare = source_item is copy_item
    print(f"source[{i}] is shallow_copy[{i}] -> {compare}")
```

```{code-cell} ipython3
# rappel au sujet de zip et enumerate
# la cellule ci-dessous est essentiellement équivalente à
for i in range(len(source)):
    compare = source[i] is shallow_copy[i]
    print(f"source[{i}] is shallow_copy[{i}] -> {compare}")
```

Alors que naturellement ce **n'est pas le cas** avec la copie en profondeur :

```{code-cell} ipython3
for i, (source_item, deep_item) in enumerate(zip(source, deep_copy)):
    compare = source_item is deep_item
    print(f"source[{i}] is deep_copy[{i}] -> {compare}")
```

On retrouve ici ce qu'on avait déjà remarqué sous pythontutor, à savoir que les trois derniers objets - immuables - n'ont pas été dupliqués comme on aurait pu s'y attendre.

+++

### On modifie la source

+++

Il doit être clair à présent que, précisément parce que `deep_copy` est une copie en profondeur, on peut modifier `source` sans impacter du tout `deep_copy`.

+++

S'agissant de `shallow_copy`, par contre, seuls les éléments de premier niveau ont été copiés. Aussi si on fait une modification par exemple **à l'intérieur** de la liste qui est le premier fils de `source`, cela sera **répercuté** dans `shallow_copy` :

```{code-cell} ipython3
print("avant, source      ", source)
print("avant, shallow_copy", shallow_copy)
source[0].append(4)
print("après, source      ", source)
print("après, shallow_copy", shallow_copy)
```

Si par contre on remplace complètement un élément de premier niveau dans la source, cela ne sera pas répercuté dans la copie superficielle :

```{code-cell} ipython3
print("avant, source      ", source)
print("avant, shallow_copy", shallow_copy)
source[0] = 'remplacement'
print("après, source      ", source)
print("après, shallow_copy", shallow_copy)
```

### Copie et circularité

+++

 Le module `copy` est capable de copier - même en profondeur - des objets contenant des références circulaires.

```{code-cell} ipython3
l = [None]
l[0] = l
l
```

```{code-cell} ipython3
copy.copy(l)
```

```{code-cell} ipython3
copy.deepcopy(l)
```

### Pour en savoir plus

+++

On peut se reporter à [la section sur le module `copy`](https://docs.python.org/3/library/copy.html) dans la documentation Python.
