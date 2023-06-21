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
notebookname: dataclasses
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

## Aperçu

+++

La raison d'être de `dataclass` est de fournir - encore un - moyen de définir des classes d'enregistrements.

Voici par exemple comment on pourrait définir une classe `Personne`:

```{code-cell} ipython3
from dataclasses import dataclass
```

```{code-cell} ipython3
@dataclass
class Personne:
    nom: str
    age: int
    email: str = ""
        
Personne(nom='jean', age=12)        
```

Comme vous le voyez, on n'a pas eu besoin d'implémenter une *dundle* `__repr__` pour obtenir une présentation déjà plus agréable que `<__main__.Personne at 0x10ac991e0>`

+++

## Surcharge

+++

On n'est pas obligé d'adopter toutes les *dundle* automatiques; par exemple je peux toujours définir mon propre  `repr()` comme d'habitude :

```{code-cell} ipython3
@dataclass
class PrettyPersonne:
    nom: str
    age: int
    email: str = ""
    
    def __repr__(self):
        return f"{self.nom} <{self.email}>, {self.age} ans"

PrettyPersonne(nom='alice', age=25, email='alice@example.com')
```

Une fois qu'on a dit ça, il me semble personnellement plus propre d'être explicite, et d'indiquer au décorateur 
qu'on va se charger du repr; mais bon...

```{code-cell} ipython3
# on peut aussi être plus explicite
@dataclass(repr=False)
class PrettyPersonne:
    nom: str
    age: int
    email: str = ""
    
    def __repr__(self):
        return f"{self.nom} <{self.email}>, {self.age} ans"
    
PrettyPersonne(nom='alice', age=25, email='alice@example.com')    
```

## Instances non mutables

+++

En fait ça va beaucoup plus loin que cela, la dataclasse se retrouve avec pas mal de dundle méthodes implémentées gratuitement pour nous.

Nous reprenons ici le même scénario d'ensemble de points que nous avons déjà rencontré plusieurs fois; remarquez que la classe `Point` sait correctement **comparer** et **hasher** ses objets, et on va pouvoir les ranger dans un ensemble pour éliminer les doublons, sans avoir besoin de redéfinir les *dundle* `__eq__` et `__hash__` qu'il aurait fallu faire si on n'avait pas utilisé `dataclass` :

Enfin on illustre ici le fait que décorateur `dataclass` accepte divers arguments pour choisir le comportement de certains aspects de la classe. Reportez-vous à la documentation pour une liste complète, mais voici un exemple qui utilise `frozen=True` qui nous permet de créer des **instances non mutables**. 


```{code-cell} ipython3
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: float
    y: float
```

```{code-cell} ipython3
p1, p2, p3 = Point(1, 1), Point(1, 1), Point(1, 1)
```

```{code-cell} ipython3
s = {p1, p2}
len(s)
```

```{code-cell} ipython3
p3 in s
```

```{code-cell} ipython3
try:
    p1.x = 10
except Exception as e:
    print(f"OOPS {type(e)}")
```

## Résumé

+++

Donc bref, j'espère vous avoir convaincu que ce trait de `dataclass` permet d'éviter pas mal de code de type *boilerplate*, et comme chacun sait: *less code, fewer bugs*, donc n'hésitez pas à user et abuser de ce trait, d'autant qu'à présent la version 3.7 est vraiment acquise !

+++

## Pour aller plus loin

+++

Vous pouvez vous rapporter

* [au PEP 557](https://www.python.org/dev/peps/pep-0557/) qui a abouti au consensus, et
* [à la documentation officielle du module](https://docs.python.org/3/library/dataclasses.html).
