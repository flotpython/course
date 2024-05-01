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
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
language_info:
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
nbhosting:
  title: "H\xE9riter des types *builtin* ?"
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

# Hériter des types *built-in* ?

+++

## Complément - niveau avancé

+++

Vous vous demandez peut-être s'il est possible d'hériter des types *built-in*.

+++

La réponse est oui, et nous allons voir un exemple qui est parfois très utile en pratique, c'est le type - ou plus exactement la famille de types - `namedtuple`

+++

### La notion de *record*

+++

On se place dans un contexte voisin de celui de *record* - en français enregistrement - qu'on a déjà rencontré souvent ; pour ce notebook nous allons à nouveau prendre le cas du point à deux coordonnées x et y. Nous avons déjà vu que pour implémenter un point on peut utiliser :

+++

##### un dictionnaire

```{code-cell} ipython3
p1 = {'x': 1, 'y': 2}
# ou de manière équivalente
p1 = dict(x=1, y=2)
```

##### ou une classe

```{code-cell} ipython3
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p2 = Point(1, 2)
```

Nous allons voir une troisième façon de s'y prendre, qui présente deux caractéristiques :

* les objets seront non-mutables (en fait ce sont des tuples) ;
* et accessoirement on pourra accéder aux différents champs par leur nom aussi bien que par un index.

+++

Pous faire ça il nous faut donc créer une sous-classe de `tuple` ; pour nous simplifier la vie, [le module `collections`  nous offre un utilitaire](https://docs.python.org/3/library/collections.html#collections.namedtuple) :

+++

##### `namedtuple`

```{code-cell} ipython3
from collections import namedtuple
```

Techniquement, il s'agit d'une fonction :

```{code-cell} ipython3
type(namedtuple)
```

 qui **renvoie une classe** - oui les classes sont des objets comme les autres ; par exemple pour créer une classe `TuplePoint`, on ferait :

```{code-cell} ipython3
# on passe à namedtuple
#  - le nom du type qu'on veut créer
#  - la liste ordonnée des composants (champs)
TuplePoint = namedtuple('TuplePoint', ['x', 'y'])
```

Et maintenant si je crée un objet :

```{code-cell} ipython3
:tags: [gridwidth-1-2]

p3 = TuplePoint(1, 2)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# cet objet est un tuple
isinstance(p3, tuple)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# auquel je peux accéder par index
# comme un tuple
p3[0]
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# mais aussi par nom via un attribut
p3.x
```

```{code-cell} ipython3
# et comme c'est un tuple il est immuable
try:
    p3.x = 10
except Exception as e:
    print(f"OOPS {type(e)} {e}")
```

### À quoi ça sert

+++

Les `namedtuple` ne sont pas d'un usage fréquent, mais on en a déjà rencontré un exemple dans le notebook sur le module `pathlib`. En effet le type de retour de la méthode `Path.stat` est un `namedtuple` :

```{code-cell} ipython3
from pathlib import Path
dot_stat = Path('.').stat()
```

```{code-cell} ipython3
dot_stat
```

```{code-cell} ipython3
isinstance(dot_stat, tuple)
```

### Nom

+++

Quand on crée une classe avec l'instruction `class`, on ne mentionne le nom de la classe qu'une seule fois. Ici vous avez remarqué qu'il faut en pratique le donner deux fois. Pour être précis, le paramètre qu'on a passé à `namedtuple` sert à ranger le nom dans l'attribut `__name__` de la classe créée :

```{code-cell} ipython3
Foo = namedtuple('Bar', ['spam', 'eggs'])
```

```{code-cell} ipython3
# Foo est le nom de la variable classe
foo = Foo(1, 2)
```

```{code-cell} ipython3
# mais cette classe a son attribut __name__ mal positionné
Foo.__name__
```

Il est donc évidemment préférable d'utiliser deux fois le même nom..

+++

### Mémoire

+++

À titre de comparaison voici la place prise par chacun de ces objets ; le `namedtuple` ne semble pas de ce point de vue spécialement attractif par rapport à une instance :

```{code-cell} ipython3
import sys

# p1 = dict / p2 = instance / p3 = namedtuple

for p in p1, p2, p3:
    print(sys.getsizeof(p))
```

### Définir des méthodes sur un `namedtuple`

+++

Dans un des compléments de la séquence précédente, intitulé *"Manipuler des ensembles d'instances"*, nous avions vu comment redéfinir le protocole *hashable* sur des instances, en mettant en évidence la nécessité de disposer d'instances non mutables lorsqu'on veut redéfinir `__hash__()`.

Voyons ici comment on pourrait tirer parti d'un `namedtuple` pour refaire proprement notre classe `Point2` - souvenez-vous, il s'agissait de rechercher dans un ensemble de points.

```{code-cell} ipython3
Point2 = namedtuple('Point2', ['x', 'y'])
```

Sans utiliser le mot-clé `class`, il faudrait se livrer à une petite gymnastique pour redéfinir les méthodes spéciales sur la classe `Point2`. Nous allons utiliser l'héritage pour arriver au même résultat :

```{code-cell} ipython3
# ce code est très proche du code utilisé dans le précédent complément
class Point2(namedtuple('Point2', ['x', 'y'])):

    # l'égalité va se baser naturellement sur x et y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # du coup la fonction de hachage 
    # dépend aussi de x et de y
    def __hash__(self):
        return hash((self.x, self.y))
```

Avec ceci en place on peut maintenant faire:

```{code-cell} ipython3
:cell_style: center

# trois points égaux au sens de cette classe
q1, q2, q3 = Point2(10, 10), Point2(10, 10), Point2(10, 10)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# deux objets distincts
q1 is q2
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# mais égaux
q1 == q2
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# ne font qu'un dans un ensemble
s = {q1, q2}
len(s)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# et on peut les trouver
# par le troisiéme
q3 in s
```

```{code-cell} ipython3
# et les instances ne sont pas mutables
try:
    q1.x = 100
except Exception as e:
    print(f"OOPS {type(e)}")
```

# Pour en savoir plus

+++

Vous pouvez vous reporter [à la documentation officielle](https://docs.python.org/3/library/collections.html#collections.namedtuple).

+++

Si vous êtes intéressés de savoir comment on peut bien arriver à rendre les objets d'une classe immuable, vous pouvez commencer par regarder le code utilisé par `namedtuple` pour créer son résultat, en l'invoquant avec le mode bavard (cette possibilité a disparu, malheureusement, dans python-3.7).

Vous y remarquerez notamment :

* une redéfinition de [la méthode spéciale `__new__`](https://docs.python.org/3/reference/datamodel.html#object.__new__),

* et aussi un usage des `property` que l'on a rencontrés en début de semaine.

```{code-cell} ipython3
:latex-skip-eval: true

# exécuter ceci pour voir le détail de ce que fait `namedtuple` 
import sys
major, minor, *_ = sys.version_info
if minor <= 6:
    Point = namedtuple('Point', ['x', 'y'], verbose=True)
else:
    print("désolé, le paramètre verbose a été supprimé en 3.7")
```
