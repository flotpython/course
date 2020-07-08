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

# Les attributs

+++

## Compléments - niveau basique

+++

### La notation `.` et les attributs

+++

La notation `module.variable` que nous avons vue dans la vidéo est un cas particulier de la notion d'attribut, qui permet d'étendre un objet, ou si on préfère de lui accrocher des données.

Nous avons déjà rencontré ceci de nombreuses fois à présent, c'est exactement le même mécanisme d'attribut qui est utilisé pour les méthodes ; pour le système d'attribut il n'y a pas de différence entre `module.variable`, `module.fonction`, `objet.methode`, etc.

Nous verrons très bientôt que ce mécanisme est massivement utilisé également dans les instances de classe.

+++

### Les fonctions de gestion des attributs

+++

Pour accéder programmativement aux attributs d'un objet, on dispose des 3 fonctions *built-in* `getattr`, `setattr`, et `hasattr`, que nous allons illustrer tout de suite.

+++

##### Lire un attribut

```{code-cell}
import math
# nous savons lire un attribut comme ceci 
# qui lit l'attribut de nom 'pi' dans le module math
math.pi
```

La [fonction *built-in* `getattr`](https://docs.python.org/3/library/functions.html#getattr) permet de lire un attribut programmativement :

```{code-cell}
# si on part d'une chaîne qui désigne le nom de l'attribut
# la formule équivalente est alors
getattr(math, 'pi')
```

```{code-cell}
# on peut utiliser les attributs avec la plupart des objets
# ici nous allons le faire sur une fonction
def foo(): 
    "une fonction vide"
    pass

# on a déjà vu certains attributs des fonctions
print(f"nom={foo.__name__}, docstring=`{foo.__doc__}`")
```

```{code-cell}
# on peut préciser une valeur par défaut pour le cas où l'attribut
# n'existe pas
getattr(foo, "attribut_inexistant", 'valeur_par_defaut')
```

##### Écrire un attribut

```{code-cell}
# on peut ajouter un attribut arbitraire (toujours sur l'objet fonction)
foo.hauteur = 100

foo.hauteur
```

Comme pour la lecture on peut écrire un attribut programmativement avec la [fonction *built-in* `setattr`](https://docs.python.org/3/library/functions.html#setattr) :

```{code-cell}
# écrire un attribut avec setattr
setattr(foo, "largeur", 200)

# on peut bien sûr le lire indifféremment
# directement comme ici, ou avec getattr
foo.largeur
```

##### Liste des attributs

+++

La [fonction *built-in* `hasattr`](https://docs.python.org/3/library/functions.html#hasattr) permet de savoir si un objet possède ou pas un attribut :

```{code-cell}
# pour savoir si un attribut existe
hasattr(math, 'pi')
```

Ce qui peut aussi être retrouvé autrement, avec la [fonction *built-in* `vars`](https://docs.python.org/3/library/functions.html#vars) :

```{code-cell}
vars(foo)
```

### Sur quels objets

+++

Il n'est pas possible d'ajouter des attributs sur les types de base, car ce sont des classes immuables :

```{code-cell}
for builtin_type in (int, str, float, complex, tuple, dict, set, frozenset):
    obj = builtin_type()
    try: 
        obj.foo = 'bar'
    except AttributeError as e: 
        print(f"{builtin_type.__name__:>10} → exception {type(e)} - {e}")
```

C'est par contre possible sur virtuellement tout le reste, et notamment là où c'est très utile, c'est-à-dire pour ce qui nous concerne sur les :

 * modules
 * packages
 * fonctions
 * classes
 * instances
