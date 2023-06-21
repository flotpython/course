---
ipub:
  sphinx:
    toggle_input: true
    toggle_input_all: true
    toggle_output: true
    toggle_output_all: true
jupytext:
  cell_metadata_filter: all, -hidden, -heading_collapsed, -run_control, -trusted
  notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version, -jupytext.text_representation.format_version,
    -language_info.version, -language_info.codemirror_mode.version, -language_info.codemirror_mode,
    -language_info.file_extension, -language_info.mimetype, -toc
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
  title: instances mutables
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Manipuler des ensembles d'instances

+++

## Complément - niveau intermédiaire

+++

Souvenez-vous de ce qu'on avait dit en semaine 3 séquence 4, concernant les clés dans un dictionnaire ou les éléments dans un ensemble. Nous avions vu alors que, pour les types *built-in*, les clés devaient être des objets immuables et même globalement immuables.

+++

Nous allons voir dans ce complément quelles sont les règles qui s'appliquent aux instances de classe.

+++

### Instance mutable dans un ensemble

+++

Une instance de classe est par défaut un objet mutable. Malgré cela, le langage vous permet d'insérer une instance dans un ensemble - ou de l'utiliser comme clé dans un dictionnaire. Nous allons voir ce mécanisme en action.

+++

### Hachage par défaut : basé sur `id()`

```{code-cell} ipython3
# une classe Point
class Point1:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"Pt[{self.x}, {self.y}]"
```

Avec ce code, les instances de `Point` sont mutables :

```{code-cell} ipython3
:cell_style: split

# deux instances 
p1 = Point1(2, 2)
p2 = Point1(2, 3)
```

```{code-cell} ipython3
:cell_style: split

# objets mutables
p1.y = 3
```

Mais par contre soyez attentifs, car il faut savoir que pour la classe `Point1`, où nous n'avons rien redéfini, la fonction de hachage sur une instance de `Point1` ne dépend que de la valeur de `id()` sur cet objet.

Ce qui, dit autrement, signifie que deux objets qui sont distincts au sens de `id()` sont considérés comme différents, et donc peuvent coexister dans un ensemble (ou dans un dictionnaire) :

```{code-cell} ipython3
:cell_style: split

# nos deux objets se ressemblent
p1, p2
```

```{code-cell} ipython3
:cell_style: split

# mais peuvent coexister 
# dans un ensemble
# qui a alors 2 éléments
s = { p1, p2 }
len(s)
```

Si on recherche un de ces deux objets on le trouve :

```{code-cell} ipython3
:cell_style: split

p1 in s
```

```{code-cell} ipython3
:cell_style: split

# mais pas un troisième
# qui pourtant est "le même"
# point que p2
p3 = Point1(2, 3)
p3 in s
```

Cette possibilité de gérer des ensembles d'objets selon cette stratégie est très commode et peut apporter de gros gains de performance, notamment lorsqu'on a souvent besoin de faire des tests d'appartenance.

En pratique, lorsqu'un modèle de données définit une relation de type "1-n", je vous recommande d'envisager d'utiliser un ensemble plutôt qu'une liste.

+++ {"cell_style": "split"}

Par exemple envisagez :

```python
class Animal:
    # blabla

class Zoo:
    def __init__(self):
        self.animals = set()
```

+++ {"cell_style": "split"}

Plutôt que :

```python
class Animal:
    # blabla

class Zoo:
    def __init__(self):
        self.animals = []
```

+++

## Complément - niveau avancé

+++

### Ce n'est pas ce que vous voulez ?

+++

Le comportement qu'on vient de voir pour les instances de `Point1` dans les tables de hachage est raisonnable, si on admet que deux points ne sont égaux que s'ils sont **le même objet** au sens de `is`.

+++

Mais imaginons que vous voulez au contraire considérer que deux points son égaux lorsqu'ils coincident sur le plan. Avec ce modèle de données, vous voudriez que :

* un ensemble dans lequel on insère `p1` et `p2` ne contienne qu'un élément,
* et qu'on trouve `p3` quand on le cherche dans cet ensemble.

+++

### Le protocole *hashable*: `__hash__` et `__eq__`

+++

Le langage nous permet de faire cela, grâce au protocole *hashable*; pour cela il nous faut définir deux méthodes :

* `__eq__` qui, sans grande surprise, va servir à évaluer `p == q` ;
* `__hash__` qui va retourner la clé de hachage sur un objet.

La subtilité étant bien entendu que ces deux méthodes doivent être cohérentes, si deux objets sont égaux, il faut que leurs hashs soient égaux ; de bon sens, si l'égalité se base sur nos deux attributs `x` et `y`, il faudra bien entendu que la fonction de hachage utilise elle aussi ces deux attributs. Voir la documentation de [`__hash__`](https://docs.python.org/3/reference/datamodel.html?highlight=__hash__#object.__hash__).

+++

Voyons cela sur une sous-classe de `Point1`, dans laquelle nous définissons ces deux méthodes :

```{code-cell} ipython3
class Point2(Point1):

    # l'égalité va se baser naturellement sur x et y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # du coup la fonction de hachage 
    # dépend aussi de x et de y
    def __hash__(self):
        return hash((self.x, self.y))
```

On peut vérifier que cette fois les choses fonctionnent correctement :

```{code-cell} ipython3
q1 = Point2(2, 3)
q2 = Point2(2, 3)
```

Nos deux objets sont distincts pour `id()`/`is`, mais égaux pour `==` :

```{code-cell} ipython3
print(f"is → {q1 is q2} \n== → {q1 == q2}")
```

Et un ensemble contenant les deux points n'en contient qu'un :

```{code-cell} ipython3
:cell_style: split

s = {q1, q2}
len(s)
```

```{code-cell} ipython3
:cell_style: split

q3 = Point2(2, 3)
q3 in s
```

Comme les ensembles et les dictionnaires reposent sur le même mécanisme de table de hachage, on peut aussi indifféremment utiliser n'importe lequel de nos 3 points pour indexer un dictionnaire :

```{code-cell} ipython3
:cell_style: split

d = {}
d[q1] = 1
d[q2]
```

```{code-cell} ipython3
:cell_style: split

# les clés q1, q2 et q3 sont
# les mêmes pour le dictionnaire
d[q3] = 10000
d
```

### Attention !

+++

Tout ceci semble très bien fonctionner; sauf qu'en fait, il y a une **grosse faille**, c'est que nos objets `Point2` sont **mutables**. Du coup on peut maintenant imaginer un scénario comme celui-ci :

```{code-cell} ipython3
:cell_style: split

t1, t2 = Point2(10, 10), Point2(10, 10)
s = {t1, t2}
s
```

```{code-cell} ipython3
:cell_style: split

t1 in s, t2 in s
```

Mais si maintenant je change un des deux objets:

```{code-cell} ipython3
:cell_style: split

t1.x = 100
```

```{code-cell} ipython3
:cell_style: split

s
```

```{code-cell} ipython3
:cell_style: split

t1 in s
```

```{code-cell} ipython3
:cell_style: split

t2 in s
```

Évidemment cela n'est pas correct. Ce qui se passe ici c'est qu'on a

* d'abord inséré `t1` dans `s`, avec un indice de hachage calculé à partir de `10, 10`
* pas inséré `t2` dans `s` parce qu'on a déterminé qu'il existait déjà.

Après avoir modifié `t1` - qui est le seul élément de `s` à ce stade: 

* lorsqu'on cherche `t1` dans `s`, on le fait avec un indice de hachage calculé à partir de `100, 10` et du coup on ne le trouve pas,
* lorsqu'on cherche `t2` dans `s`, on utilise le bon indice de hachage, mais ensuite le seul élément qui pourrait faire l'affaire n'est pas égal à `t2`.

+++

### Conclusion

+++

La [documentation de Python sur ce sujet](https://docs.python.org/3/reference/datamodel.html#object.__hash__) indique ceci :

> If a class defines mutable objects and implements an `__eq__`() method, it should not implement `__hash__`(), since the implementation of hashable collections requires that a key’s hash value is immutable (if the object’s hash value changes, it will be in the wrong hash bucket).

+++

Notre classe `Point2` illustre bien cette limitation. Pour qu'elle soit utilisable en pratique, il faut **rendre ses instances immutables**. Cela peut se faire de plusieurs façons, dont deux que nous aborderons dans la prochaine séquence et qui sont - entre autres :

* le `namedtuple`
* et la `dataclass` (nouveau en 3.7).
