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

# Usage avancés de `import`

+++

## Complément - niveau avancé

```{code-cell}
# notre utilitaire pour afficher le code des modules
from modtools import show_module, find_on_disk
```

### Attributs spéciaux

+++

Les objets de type module possèdent des attributs spéciaux ; on les reconnaît facilement car leur nom est en *`__truc__`*, c'est une convention générale dans tous le langage : on en a déjà vu plusieurs exemples avec par exemple les méthodes `__iter__()`.

+++

Voici pour commencer les attributs spéciaux les plus utilisées ; pour cela nous reprenons le package d'un notebook précédent :

```{code-cell}
import package_jouet
```

##### `__name__`

+++

Le nom canonique du module :

```{code-cell}
package_jouet.__name__
```

```{code-cell}
package_jouet.module_jouet.__name__
```

##### `__file__`

+++

L'emplacement du fichier duquel a été chargé le module ; pour un package ceci dénote un fichier `__init__.py` :

```{code-cell}
package_jouet.__file__
```

```{code-cell}
package_jouet.module_jouet.__file__
```

##### `__all__`

+++

Il est possible de redéfinir dans un module la variable `__all__`, de façon à définir les symboles qui sont réellement concernés par un `import *`, [comme c'est décrit ici](https://docs.python.org/3/tutorial/modules.html#importing-from-a-package). 

Je rappelle toutefois que l'usage de `import *` est fortement déconseillé dans du code de production.

+++

### Import absolu

+++

La mécanique des imports telle qu'on l'a vue jusqu'ici est ce qui s'appelle un *import* absolu qui est depuis python-2.5 le mécanisme par défaut : le module importé est systématiquement cherché à partir de `sys.path`.

Dans ce mode de fonctionnement, si on trouve dans le même répertoire deux fichiers `foo.py` et `bar.py`, et que dans le premier on fait :

```python
import bar
```

eh bien alors, malgré le fait qu'il existe ici même un fichier `bar.py`, l'import ne réussit pas (sauf si le répertoire courant est dans `sys.path`; en général ce n'est pas le cas).

+++

### Import relatif

+++

Ce mécanisme d'import absolu a l'avantage d'éviter qu'un module local, par exemple `random.py`, ne vienne cacher le module `random` de la bibliothèque standard. Mais comment peut-on faire alors pour charger le module `random.py` local ? C'est à cela que sert l'import relatif.

Voyons cela sur un exemple qui repose sur la hiérarchie suivante :

```bash
package_relatif/
                __init__.py  (vide)
                main.py
                random.py
```

+++

Le fichier `__init__.py` ici est vide, et voici le code des deux autres modules :

```{code-cell}
import package_relatif
```

```{code-cell}
# le code de main.py
code = find_on_disk(package_relatif, "main.py")
!cat $code
```

Nous avons illustré dans le point d'entrée `main.py` deux exemples d'import relatif :

+++

Les deux clauses `as` sont bien sûr optionnelles, on les utilise ici uniquement pour bien identifier les différents objets en jeu.

+++

Le module local `random.py` expose une fonction `alea` qui génére un string aléatoire en se basant sur le module standard `random` :

```{code-cell}
# le code de random.py
code = find_on_disk(package_relatif, "random.py")
!cat $code
```

Cet exemple montre comment on peut importer un module local de nom `random` **et** le module `random` qui provient de la librairie standard :

```{code-cell}
import package_relatif.main
```

```{code-cell}
print(package_relatif.main.alea())
```

##### Pour remonter dans l'arborescence

+++

Il faut savoir également qu'on peut "remonter" dans l'arborescence de fichiers en utilisant plusieurs points `.` consécutifs. Voici un exemple fonctionnel, on part du même contenu que ci-dessus avec un sous-package, comme ceci :

+++

```bash
package_relatif/
                __init__.py      (vide)
                main.py
                random.py
                subpackage/
                           __init__.py  (vide)
                           submodule.py
```

```{code-cell}
# voyons le code de submodule:
import package_relatif.subpackage
```

```{code-cell}
# le code de submodule/submodule.py
code = find_on_disk(package_relatif.subpackage, "submodule.py")
!cat $code
```

```{code-cell}
import package_relatif.subpackage.submodule
```

```{code-cell}
print(package_relatif.subpackage.submodule.alea())
```

**Ce qu'il faut retenir**

Sur cet exemple, on montre comment un import relatif permet à un module d'importer un module local qui a le même nom qu'un module standard.

+++

### Avantages de l'import relatif

+++

Bien sûr ici on aurait pu faire 

```python
import package_relatif.random
```

au lieu de 

```python
from . import random
```

+++

Mais l'import relatif présente notamment l'avantage d'être insensible aux renommages divers à l'intérieur d'une bibliothèque.

+++

Dit autrement, lorsque deux modules sont situés dans le même répertoire, il semble naturel que l'import entre eux se fasse par un import relatif, plutôt que de devoir répéter *ad nauseam* le nom de la bibliothèque - ici `package_relatif` - dans tous les imports.

+++

### Frustrations liées à l'import relatif

+++

#### Se base sur `__name__` et non sur `__file__`

+++

Toutefois, l'import relatif ne fonctionne pas toujours comme on pourrait s'y attendre. Le point important à garder en tête est que lors d'un import relatif, **c'est l'attribut `__name__`** qui sert à déterminer le point de départ.

+++

Concrètement, lorsque dans `main.py` on fait :

```python
from . import random
```

l'interpréteur :

* détermine que dans `main.py`, `__name__` vaut `package_relatif.main`;
* il "oublie" le dernier morceau `main` pour calculer que le package courant est `package_relatif`
* et c'est ce nom qui sert à déterminer le point de départ de l'import relatif.

Aussi cet import est-il retranscrit en

```python
from package_relatif import random
```

+++

De la même manière

```python
from .random import run
```

devient

```python
from package_relatif.random import run
```

+++

Par contre **l'attribut `__file__` n'est pas utilisé** : ce n'est pas parce que deux fichiers python sont dans le même répertoire que l'import relatif va toujours fonctionner. Avant de voir cela sur un exemple, il nous faut revenir sur l'attribut `__name__`.

+++

#### Digression sur l'attribut `__name__`

+++

Il faut savoir en effet que le **point d'entrée** du programme - c'est-à-dire le fichier qui est passé directement à l'interpréteur python - est considéré comme un module dont l'attribut `__name__` vaut la chaîne `"__main__"`.

Concrètement, si vous faites

```bash
python3 tests/montest.py
```

alors la valeur observée dans l'attribut `__name__` n'est pas `"tests.montest"`, mais la constante `"__main__"`.

+++

C'est pourquoi d'ailleurs [(et c'est également expliqué ici)](https://docs.python.org/3/tutorial/modules.html#executing-modules-as-scripts) vous trouverez  parfois à la fin d'un fichier source une phrase comme celle-ci :

+++

```python
if __name__ == "__main__":
    <faire vraiment quelque chose>
    <comme par exemple tester le module>
```

+++

Cet idiome très répandu permet d'insérer à la fin d'un module du code - souvent un code de test - qui :

* va être exécuté quand on le passe directement à l'interpréteur python, mais 
* qui n'**est pas exécuté** lorsqu'on importe le module.

+++

#### L'attribut `__package__`

+++

Pour résumer :

* le point d'entrée - celui qui est donné à `python` sur la ligne de commande - voit comme valeur pour `__name__` la constante `"__main__"`,
* et le mécanisme d'import relatif se base sur `__name__` pour localiser les modules importés.

+++

Du coup, par construction, il n'est quasiment pas possible d'utiliser les imports relatifs à partir du script de lancement.

Pour pallier à ce type d'inconvénients, il a été introduit ultérieurment (voir PEP 366 ci-dessous) la possibilité pour un module de définir (écrire) l'attribut `__package__`, pour contourner cette difficulté.

+++

#### Ce qu'il faut retenir

+++

On voit que tout ceci est rapidement assez scabreux. Cela explique sans doute l'usage relativement peu répandu des imports relatifs. 

De manière générale, une bonne pratique consiste à :

* considérer votre ou vos points d'entrée comme des accessoires ; un point d'entrée typiquement se contente d'importer une classe d'un module, de créer une instance et de lui envoyer une méthode ;
* toujours placer ces points d'entrée dans un répertoire séparé ;
* notamment si vous utilisez `setuptools` pour distribuer votre application via `pypi.org`, vous verrez que ces points d'entrée sont complètement pris en charge par les outils d'installation.

S'agissant des tests: 

* la technique qu'on a vue rapidement - de tester si `__name__` vaut `"__main__"` - est extrêmement basique et limitée. Le mieux est de ne pas l'utiliser en fait, en dehors de micro-maquettes.
* en pratique on écrit les tests dans un répertoire séparé - souvent appelé `tests` - et en tirant profit de la librairie `unittest`. 
* du coup les tests sont toujours exécutés avec une phrase comme

```bash
python3 -m unittest tests.jeu_de_tests
```

et dans ce contexte-là, il est possible par exemple pour les tests de recourir à l'import relatif.

+++

### Pour en savoir plus

+++

Vous pourrez consulter :

* <https://www.python.org/dev/peps/pep-0328/> qui date du passage de 2.4 à 2.5, dans lequel on décide que tous les imports sans `.` sont absolus - ce n'était pas le cas au préalable.
* <https://www.python.org/dev/peps/pep-0366/> qui introduit la possibilité de définir `__package__` pour contourner les problèmes liés aux imports relatifs dans un script.
* <http://sametmax.com/un-gros-guide-bien-gras-sur-les-tests-unitaires-en-python-partie-1/> qui parle des tests unitaires qui est un tout autre et vaste sujet.
