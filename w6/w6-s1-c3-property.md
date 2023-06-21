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
nbhosting:
  title: properties
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Les *property*

+++

**Note** : nous reviendrons largement sur cette notion de property lorsque nous parlerons des _property et descripteurs_ en semaine 9. Cependant, cette notion est suffisamment importante pour que nous vous proposions un complément dès maintenant dessus.

+++

## Complément - niveau intermédiaire

+++

Comme on l'a vu dans le complément précédent, il est fréquent en Python qu'une classe expose dans sa documentation un ou plusieurs attributs ; c'est une pratique qui, en apparence seulement, paraît casser l'idée d'une bonne encapsulation.

En réalité, grâce au mécanisme de *property*, il n'en est rien. Nous allons voir dans ce complément comment une classe peut en quelque sorte intercepter les accès à ses attributs, et par là fournir une encapsulation forte.

+++

Pour être concret, on va parler d'une classe `Temperature`. Au lieu de proposer, comme ce serait l'usage dans d'autres langages, une interface avec `get_kelvin()` et `set_kelvin()`, on va se contenter d'exposer l'attribut `kelvin`, et malgré cela on va pouvoir faire diverses vérifications et autres.

+++

##### Implémentation naïve

+++

Je vais commencer par une implémentation naïve, qui ne tire pas profit des *properties* :

```{code-cell} ipython3
# dans sa version la plus épurée, une classe
# température pourrait ressembler à ça :

class Temperature1:
    def __init__(self, kelvin):
        self.kelvin = kelvin
        
    def __repr__(self):
        return f"{self.kelvin}K"
```

```{code-cell} ipython3
# créons une instance
t1 = Temperature1(20)
t1
```

```{code-cell} ipython3
# et pour accéder à la valeur numérique je peux faire
t1.kelvin
```

Avec cette implémentation il est très facile de créer une température négative, qui n'a bien sûr pas de sens physique, ce n'est pas bon.

+++

##### Interface *getter/setter*

+++

Si vous avez été déjà exposés à des langages orientés objet comme C++, Java ou autre, vous avez peut-être l'habitude d'accéder aux données internes des instances par des **méthodes** de type *getter** ou **setter*, de façon à contrôler les accès et, dans une optique d'encapsulation, de préserver des invariants, comme ici le fait que la température doit être positive.

C'est-à-dire que vous vous dites peut-être, ça ne devrait pas être fait comme ça, on devrait plutôt proposer une interface pour accéder à l'implémentation interne ; quelque chose comme :

```{code-cell} ipython3
class Temperature2:
    def __init__(self, kelvin):
        # au lieu d'écrire l'attribut il est plus sûr
        # d'utiliser le setter
        self.set_kelvin(kelvin)
        
    def set_kelvin(self, kelvin):
        # je m'assure que _kelvin est toujours positif
        # et j'utilise un nom d'attribut avec un _ pour signifier
        # que l'attribut est privé et qu'il ne faut pas y toucher directement
        # on pourrait aussi bien sûr lever une exception 
        # mais ce n'est pas mon sujet ici
        self._kelvin = max(0, kelvin)
        
    def get_kelvin(self):
        return self._kelvin
        
    def __repr__(self):
        return f"{self._kelvin}K"
```

Bon c'est vrai que d'un coté, c'est mieux parce que je garantis un invariant, la température est toujours positive :

```{code-cell} ipython3
t2 = Temperature2(-30)
t2
```

Mais par contre, d'un autre coté, c'est très lourd, parce que chaque fois que je veux utiliser mon objet, je dois faire pour y accéder :

```{code-cell} ipython3
t2.get_kelvin()
```

et aussi, si j'avais déjà du code qui utilisait `t.kelvin` il va falloir le modifier entièrement.

+++

##### Implémentation pythonique

+++

La façon de s'en sortir ici consiste à définir une property. Comme on va le voir ce mécanisme permet d'écrire du code qui fait référence à l'attribut `kelvin` de l'instance, mais qui passe tout de même par une couche de logique.

Ça ressemblerait à ceci :

```{code-cell} ipython3
class Temperature3:
    def __init__(self, kelvin):
        self.kelvin = kelvin

    # je définis bel et bien mes accesseurs de type getter et setter
    # mais _get_kelvin commence avec un _ 
    # car il n'est pas censé être appelé par l'extérieur
    def _get_kelvin(self):
        return self._kelvin

    # idem
    def _set_kelvin(self, kelvin):
        self._kelvin = max(0, kelvin)
        
    # une fois que j'ai ces deux éléments je peux créer une property
    kelvin = property(_get_kelvin, _set_kelvin)
    
    # et toujours la façon d'imprimer
    def __repr__(self):
        return f"{self._kelvin}K"    
```

```{code-cell} ipython3
t3 = Temperature3(200)
t3
```

```{code-cell} ipython3
# par contre ici on va le mettre à zéro
# à nouveau, une exception serait préférable sans doute
t3.kelvin = -30
t3
```

Comme vous pouvez le voir, cette technique a plusieurs avantages :

* on a ce qu'on cherchait, c'est-à-dire une façon d'ajouter une couche de logique lors des accès en lecture et en écriture à l'intérieur de l'objet,
* mais **sans toutefois** demander à l'utilisateur de passer son temps à envoyer des méthodes `get_` et `set()` sur l'objet, ce qui a tendance à alourdir considérablement le code.

C'est pour cette raison que vous ne rencontrerez presque jamais en Python une bibliothèque qui offre une interface à base de méthodes `get_something` et `set_something`, mais au contraire les API vous exposeront directement des attributs que vous devez utiliser directement.

+++

## Complément - niveau avancé

+++

À titre d'exemple d'utilisation, voici une dernière implémentation de `Temperature` qui donne l'illusion d'avoir 3 attributs (`kelvin`, `celsius` et `fahrenheit`), alors qu'en réalité le seul attribut de donnée est `_kelvin`.

```{code-cell} ipython3
class Temperature:

    ## les constantes de conversion
    # kelvin / celsius
    K = 273.16
    # fahrenheit / celsius
    RF = 5 / 9
    KF = (K / RF) - 32

    def __init__(self, kelvin=None, celsius=None, fahrenheit=None):
        """
        Création à partir de n'importe quelle unité
        Il faut préciser exactement une des trois unités
        """
        # on passe par les properties pour initialiser
        if kelvin is not None:
            self.kelvin = kelvin
        elif celsius is not None:
            self.celsius = celsius
        elif fahrenheit is not None:
            self.fahrenheit = fahrenheit
        else:
            self.kelvin = 0
            raise ValueError("need to specify at least one unit")

    # pour le confort
    def __repr__(self):
        return f"<{self.kelvin:g}K == {self.celsius:g}℃ " \
               f"== {self.fahrenheit:g}F>"

    def __str__(self):
        return f"{self.kelvin:g}K"


    # l'attribut 'kelvin' n'a pas de conversion à faire,
    # mais il vérifie que la valeur est positive
    def _get_kelvin(self):
        return self._kelvin

    def _set_kelvin(self, kelvin):
        if kelvin < 0:
            raise ValueError(f"Kelvin {kelvin} must be positive")
        self._kelvin = kelvin

    # la property qui définit l'attribut `kelvin`
    kelvin = property(_get_kelvin, _set_kelvin)


    # les deux autres properties font la conversion, puis 
    # sous-traitent à la property kelvin pour le contrôle de borne
    def _set_celsius(self, celsius):
        # using .kelvin instead of ._kelvin to enforce
        self.kelvin = celsius + self.K

    def _get_celsius(self):
        return self._kelvin - self.K
    
    celsius = property(_get_celsius, _set_celsius)

    def _set_fahrenheit(self, fahrenheit):
        # using .kelvin instead of ._kelvin to enforce
        self.kelvin = (fahrenheit + self.KF) * self.RF

    def _get_fahrenheit(self):
        return self._kelvin / self.RF - self.KF
    
    fahrenheit = property(_get_fahrenheit, _set_fahrenheit)
```

Et voici ce qu'on peut en faire :

```{code-cell} ipython3
:cell_style: split

t = Temperature(celsius=0)
t
```

```{code-cell} ipython3
:cell_style: split

t.fahrenheit
```

```{code-cell} ipython3
:cell_style: split

t.celsius += 100
print(t)
```

```{code-cell} ipython3
:cell_style: center

try:
    t = Temperature(fahrenheit = -1000)
except Exception as e:
    print(f"OOPS, {type(e)}, {e}")
```

##### Pour en savoir plus

+++

Voir aussi [la documentation officielle](https://docs.python.org/3.6/library/functions.html#property).

+++

Vous pouvez notamment aussi, en option, ajouter un *deleter* pour intercepter les instructions du type :

```{code-cell} ipython3
# comme on n'a pas défini de deleter, on ne peut pas faire ceci
try:
    del t.kelvin
except Exception as e:
    print(f"OOPS {type(e)} {e}")
```
