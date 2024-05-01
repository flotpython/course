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
  title: "H\xE9ritage multiple"
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

# Héritage multiple

+++

## Complément - niveau intermédiaire

+++

### La classe `object`

+++

Le symbole `object` est une variable prédéfinie (qui donc fait partie du module `builtins`) :

```{code-cell} ipython3
object
```

```{code-cell} ipython3
import builtins

builtins.object is object
```

La classe `object` est une classe spéciale ; toutes les classes en Python héritent de la classe `object`, même lorsqu'aucun héritage n'est spécifié :

```{code-cell} ipython3
class Foo:
    pass

Foo.__bases__
```

L'attribut spécial `__bases__`, comme on le devine, nous permet d'accéder aux superclasses directes, ici de la classe `Foo`.

+++

En Python moderne, on n'a **jamais besoin de mentionner** `object` dans le code. La raison de sa présence dans les symboles prédéfinis est liée à l'histoire de Python, et à la distinction que faisait Python 2 entre classes *old-style* et classes *new-style*. Nous le mentionnons seulement car on rencontre encore parfois du code qui fait quelque chose comme :

```{code-cell} ipython3
# ceci est du vieux code, on n'a pas besoin
# de faire hériter Bar de object
class Bar(object):
    pass
```

qui est un reste de Python 2, et que Python 3 accepte uniquement au titre de la compatibilité.

+++

## Complément - niveau avancé

+++

### Rappels

+++

L'héritage en Python consiste principalement en l'algorithme de recherche d'un attribut d'une instance ; celui-ci regarde :

1. d'abord dans l'instance ;
1. ensuite dans la classe ;
1. ensuite dans les super-classes.

+++

### Ordre sur les super-classes

+++

Le problème revient donc, pour le dernier point, à définir un **ordre** sur l'ensemble des **super-classes**. On parle bien, naturellement, de **toutes** les super-classes, pas seulement celles dont on hérite directement - en termes savants on dirait qu'on s'intéresse à la fermeture transitive de la relation d'héritage.

L'algorithme utilisé pour cela depuis la version 2.3 est connu sous le nom de **linéarisation C3**. Cet algorithme n'est pas propre à python, comme vous pourrez le lire dans les références citées dans la dernière section.

Nous ne décrirons pas ici l'algorithme lui-même dans le détail ; par contre nous allons :

* dans un premier temps résumer **les raisons** qui ont guidé ce choix, en décrivant les bonnes propriétés que l'on attend, ainsi que les **limitations** qui en découlent ;
* puis voir l'ordre obtenu sur quelques **exemples** concrets de hiérarchies de classes.
 
Vous trouverez dans les références (voir ci-dessous la dernière section, "Pour en savoir plus") des liens vers des documents plus techniques si vous souhaitez creuser le sujet.

+++

### Les bonnes propriétés attendues

+++

Il y a un certain nombre de bonnes propriétés que l'on attend de cet algorithme.

+++

##### Priorité au spécifique

+++

Lorsqu'une classe A hérite d'une classe B, on s'attend à ce que les méthodes définies sur A, qui sont en principe plus spécifiques, soient utilisées de préférence à celles définies sur B.

+++

##### Priorité à gauche

+++

Lorsqu'on utilise l'héritage multiple, on mentionne les classes mères dans un certain ordre, qui n'est pas anodin. Les classes mentionnées en premier sont bien entendu celles desquelles on veut hériter en priorité.

+++

# La Method Resolution Order (MRO)

+++

##### De manière un peu plus formelle

+++

Pour reformuler les deux points ci-dessus, on s'intéresse à la `mro` d'une classe O, et on veut avoir les deux bonnes propriétés suivantes :

* si O hérite (pas forcément directement) de A qui elle même hérite de B, alors A est avant B dans la `mro` de O ;
* si O hérite (pas forcément directement) de A, qui elle hérite de B, puis (pas forcément immédiatement) de C, alors dans la `mro` A est avant B qui est avant C.

+++

##### Limitations : toutes les hiérarchies ne peuvent pas être traitées

+++

L'algorithme C3 permet de calculer un ordre sur $\cal{S}$ qui respecte toutes ces contraintes, lorsqu'il en existe un. 

En effet, dans certains cas on ne peut pas trouver un tel ordre, on le verra plus bas, mais dans la pratique, il est assez rare de tomber sur de tels cas pathologiques ; et lorsque cela se produit c'est en général le signe d'erreurs de conception plus profondes.

+++

### Un exemple très simple

+++

On se donne la hiérarchie suivante :

```{code-cell} ipython3
class LeftTop:
    def attribut(self): 
        return "attribut(LeftTop)"
    
class LeftMiddle(LeftTop): 
    pass

class Left(LeftMiddle): 
    pass

class Middle: 
    pass

class Right:
    def attribut(self): 
        return "attribut(Right)"

class Class(Left, Middle, Right): 
    pass

instance = Class()
```

qui donne en version dessinée, avec deux points rouges pour représenter les deux définitions de la méthode `attribut` :

<img src="media/heritage-multiple01.png" height="40">

+++

Les deux règles, telles que nous les avons énoncées en premier lieu (priorité à gauche, priorité au spécifique) sont un peu contradictoires ici. En fait, c'est la méthode de `LeftTop` qui est héritée dans `Class`, comme on le voit ici :

```{code-cell} ipython3
instance.attribut() == 'attribut(LeftTop)'
```

**Exercice** : Remarquez qu'ici `Right` a elle-même un héritage très simple. À titre d'exercice, modifiez le code ci-dessus pour faire que `Right` hérite de la classe `LeftMiddle` ; de quelle classe d'après vous est-ce que `Class` hérite `attribut` dans cette configuration ?

+++

##### Si cela ne vous convient pas

+++

C'est une évidence, mais cela va peut-être mieux en le rappelant : si la méthode que vous obtenez "gratuitement" avec l'héritage n'est pas celle qui vous convient, vous avez naturellement toujours la possibilité de la redéfinir, et ainsi d'en **choisir** une autre. Dans notre exemple si on préfère la méthode implémentée dans `Right`, on définira plutôt la classe `Class` comme ceci :

```{code-cell} ipython3
class Class(Left, Middle, Right):
    # en redéfinissant explicitement la méthode
    # attribut ici on court-circuite la mro
    # et on peut appeler explicitement une autre
    # version de attribut()
    def attribut(*args, **kwds):
        return Right.attribut(*args, **kwds)
    
instance2 = Class()
instance2.attribut()
```

Ou encore bien entendu, si dans votre contexte vous devez appelez **les deux** méthodes dont vous pourriez hériter et les combiner, vous pouvez le faire aussi, par exemple comme ceci :

```{code-cell} ipython3
class Class(Left, Middle, Right):
    # pour faire un composite des deux méthodes
    # trouvées dans les classes mères
    def attribut(*args, **kwds):
        return (  LeftTop.attribut(*args, **kwds) 
                + " ** " 
                + Right.attribut(*args, **kwds))
    
instance3 = Class()
instance3.attribut()
```

### Un exemple un peu plus compliqué

+++

Voici un exemple, assez parlant, tiré de la deuxième référence (voir ci-dessous la dernière section, "Pour en savoir plus").

```{code-cell} ipython3
O = object
class F(O): pass
class E(O): pass
class D(O): pass
class C(D, F): pass
class B(E, D): pass
class A(B, C): pass
```

Cette hiérarchie nous donne, en partant de A, l'ordre suivant :

+++

```python
                               6
                              ---
    Level 3                  | O |
                           /  ---  \
                          /    |    \
                         /     |     \
                        /      |      \
                      ---     ---    ---
    Level 2        2 | E | 4 | D |  | F | 5
                      ---     ---    ---
                       \      / \     /
                        \    /   \   /
                         \  /     \ /
                          ---     ---
    Level 1            1 | B |   | C | 3
                          ---     ---
                           \       /
                            \     /
                              ---
    Level 0                0 | A |
                              ---
```

+++

Que l'on peut calculer, sous l'interpréteur python, avec la méthode `mro` sur la classe de départ :

```{code-cell} ipython3
A.mro()
```

### Un exemple qui ne peut pas être traité

+++

Voici enfin un exemple de hiérarchie pour laquelle on ne **peut pas trouver d'ordre** qui respecte les bonnes propriétés que l'on a vues tout à l'heure, et qui pour cette raison sera **rejetée par l'interpréteur python**. D'abord en version dessinée :

<img src="media/heritage-multiple02.png">

```{code-cell} ipython3
# puis en version code
class X: pass
class Y: pass
class XY(X, Y): pass
class YX(Y, X): pass

# on essaie de créer une sous-classe de XY et YX
try:
    class Class(XY, YX): pass 
# mais ce n'est pas possible
except Exception as e:
    print(f"OOPS, {type(e)}, {e}")
```

### Pour en savoir plus

+++

1. Un [blog de Guido Van Rossum](http://python-history.blogspot.fr/2010/06/method-resolution-order.html)
qui retrace l'historique des différents essais qui ont été faits avant de converger sur le modèle actuel.
1. Un [article technique](https://www.python.org/download/releases/2.3/mro/) qui décrit le fonctionnement de l'algorithme de calcul de la MRO, et donne des exemples.
1. L'[article de Wikipedia](http://en.wikipedia.org/wiki/C3_linearization) sur l'algorithme C3.
