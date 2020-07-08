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
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# `dataclasses` 


***Nouveauté de la version 3.7***

Python 3.7 apporte un nouveauté pour simplifier la définition de classes dites "de données" ; ce type de classes s'applique pour des objets qui sont essentiellement un assemblage de quelques champs de données.

+++

### Aperçu

+++

La raison d'être de `dataclass` est de fournir - encore un - moyen de définir des classes d'enregistrements.

Voici par exemple comment on pourrait définir une classe `Personne`:

```{code-cell}
from dataclasses import dataclass

@dataclass
class Personne:
    nom: str
    age: int
    email: str = ""
```

```{code-cell}
personne = Personne(nom='jean', age=12)
print(personne)
```

### Instances non mutables

+++

Le décorateur `dataclass` accepte divers arguments pour choisir le comportement de certains aspects de la classe. Reportez-vous à la documentation pour une liste complète, mais voici un exemple qui utilise `frozen=True` et qui illustre la possibilité de créer des instances non mutables. Nous retrouvons ici le même scénario d'ensemble de points que nous avons déjà rencontré plusieurs fois :

```{code-cell}
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: float
    y: float

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return (11 * self.x + self.y) // 16
```

```{code-cell}
p1, p2, p3 = Point(1, 1), Point(1, 1), Point(1, 1)
```

```{code-cell}
s = {p1, p2}
len(s)
```

```{code-cell}
p3 in s
```

```{code-cell}
try:
    p1.x = 10
except Exception as e:
    print(f"OOPS {type(e)}")
```

### Pour aller plus loin

+++

Vous pouvez vous rapporter

* [au PEP 557](https://www.python.org/dev/peps/pep-0557/) qui a abouti au consensus, et
* [à la documentation officielle du module](https://docs.python.org/3/library/dataclasses.html).
