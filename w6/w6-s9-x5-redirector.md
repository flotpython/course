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
notebookname: 'exercice: redirector'
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

## Exercice - niveau intermédiaire

+++

On se propose d'écrire une classe de redirection ; 
typiquement, une instance de cette classe est capable de résoudre **n'importe quel attribut** car son travail est de sous-traiter le travail à quelqu'un d'autre.

L'exercice vient en deux versions ; dans la première on considère seulement des attributs de données, dans la seconde, un attribut inconnu se comporte comme une méthode.

+++

### Première version : attributs de donnée

+++

Dans cette premiere version, on veut créer une instance à partir de laquelle on peut accéder à n'importe quel attribut dont le nom est un nom de variable légal en Python.

Et la valeur de l'attribut est dérivé de son nom en :

* le mettant en minuscules, et 
* en remplaçant les éventuels `_` par un signe `-`

```{code-cell}
from corrections.cls_redirectors import exo_redirector1
exo_redirector1.example()
```

```{code-cell}
# votre code pour la classe Redirector1
class Redirector1:

    def __repr__(self):
        return "redirector"

    ...
```

```{code-cell}
# pour la corriger
# 
exo_redirector1.correction(Redirector1)
```

## Exercice - niveau avancé

+++

### deuxième version : méthodes

+++

Cette fois-ci on considère qu'un attribut manquant est une méthode ; pour fixer les idées on décide que :

* ces méthodes prennent toutes **un seul argument** - en sus de l'objet qui les reçoit ;
* chacune de ces méthodes retourne une simple chaîne,
  qui contient des morceaux provenant de :

  * l'object redirecteur lui-même,
  * le nom de la méthode,
  * l'argument passé à la méthode, qui donc est unique.

Ce mécanisme est illustré sur les exemples suivants, avec deux méthodes `foo` et `bar` ; par contre le test automatique exercera votre code avec des noms de méthodes aléatoires.

```{code-cell}
from corrections.cls_redirectors import exo_redirector2
exo_redirector2.example()
```

```{code-cell}
# à vous de jouer
class Redirector2:
    def __init__(self, id):
        self.id = id
    def __repr__(self):
        return f"Redirector2({self.id})"
```

```{code-cell}
# pour corriger
exo_redirector2.correction(Redirector2)
```

## application


Un exemple en vraie grandeur de ce type de mécanisme est proposé dans la librairie standard Python :
https://docs.python.org/3/library/xmlrpc.client.html#serverproxy-objects.

Typiquement la classe générique `ServerProxy` ressemble à notre deuxième version de l'exercice, en ce sens qu'elle n'a aucune connaissance de l'API distante à laquelle elle est connectée ; autrement dit l'ensemble des méthodes effectivement proposées par la classe `ServerProxy` est totalement inconnu au moment où on écrit le code de cette classe.
