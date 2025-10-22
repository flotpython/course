---
ipub:
  sphinx:
    toggle_input: true
    toggle_input_all: true
    toggle_output: true
    toggle_output_all: true
jupytext:
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
  start_slideshow_at: selected
  theme: simple
  transition: fade
  width: 100%
nbhosting:
  title: "Outils p\xE9riph\xE9riques"
---

# Outils périphériques

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Compléments - niveau intermédiaire

+++

Pour conclure le tronc commun de ce cours Python, nous allons très rapidement citer quelques outils qui ne sont pas nécessairement dans la bibliothèque standard, mais qui sont très largement utilisés dans l'écosystème python.

Il s'agit d'une liste non exhaustive bien entendu.

+++

## Environnements virtuels

Pour compléter ce qui vient d'être dit par rapport à l'organisation des sources, disons un mot des environnements virtuels.

Par le passé, on installait python **une seule fois** dans le système ;
en 2024, c'est une approche qui n'a **que des inconvénients** :

* quand on travaille sur plusieurs projets, on peut avoir besoin de Python-3.9 sur l'un et Python-3.12 sur un autre ;
* et/ou on peut avoir un projet qui a besoin de `Django==3.4` et un autre qui ne marche qu'avec `Django>=4.0` ;
* par-dessus le marché, dans certains cas il faut être super utilisateur pour modifier l'installation ; typiquement on passe son temps à faire `sudo pip` au lieu de `pip`…

et le seul avantage, c'est que tous les utilisateurs de l'ordi peuvent partager l'installation ; sauf que, plus de 99 fois sur 100, il n'y a qu'un seul utilisateur pour un ordi ! Bref, c'est une pratique totalement dépassée.

+++

La création et la gestion d'environnements virtuels sont **très faciles** aujourd'hui. Aussi c'est une **pratique recommandée** de se créer **un virtualenv par projet**. C'est tellement pratique qu'on n'hésite pas une seconde à repartir d'un environnement vide à la moindre occasion, par exemple lorsqu'on a un doute sur les dépendances.

Le seul point sur lequel il faut être attentif, c'est de trouver un moyen de **savoir en permanence** dans quel environnement on se trouve. Notamment :

* une pratique très répandue consiste à s'arranger pour que **le prompt dans le terminal** indique cela,
* dans vs-code, dans la bannière inférieure, on nous montre toujours l'environnement courant.

+++ {"cell_style": "center"}

````{figure} media/venv-terminal.png
:align: center
**dans le terminal**, le prompt nous montre le venv courant, ici d'abord `base`, puis ensuite `flotpython-course`
````

+++ {"cell_style": "center"}

````{figure} media/venv-vscode.png
:align: center

**vs-code** nous montre le venv courant et nous permet de le changer
````

+++

### Les outils

Par contre il reste le choix entre plusieurs outils, que j'essaie de lister ici :

* [`venv`](https://docs.python.org/3/library/venv.html) un module de la librairie standard
* [`miniconda`](https://docs.conda.io/en/latest/miniconda.html) un sous-produit de anaconda
* enfin [`virtualenv`](https://virtualenv.pypa.io/en/latest/) un module externe, qui préexistait à `venv` et qui a fourni la base des fonctionnalités de `venv`, mais qui me semble aujourd'hui obsolète
* et plein d'autres outils, comme `uv`, ...

+++

Actuellement **j'utilise quant à moi `miniconda`**

Voici à titre indicatif une session sous MacOS en guise de rapide introduction.
Vous remarquerez comme le *prompt* reflète **l'environnement dans lequel on se trouve**, ça semble relativement impératif si on ne veut pas s'emmêler les pinceaux.

+++

##### La liste de mes environnements

```
[base] ~ $ conda env list
# conda environments:
#
base                  *  /Users/jeanmineur/miniconda3
<snip ...>
```

+++

##### j'en crée un nouveau avec Python-3.12

```
[base] ~ $ conda create -n demo-py312 python=3.12
Collecting package metadata (current_repodata.json): done
Solving environment: done
<snip ...>
```

+++

##### on le voit
```
[base] ~ $ conda env list
# conda environments:
#
base                  *  /Users/jeanmineur/miniconda3
demo-py312               /Users/jeanmineur/miniconda3/envs/demo-py312
<snip...>
```

+++

##### pour entrer dans le nouvel environnement

```
[base] ~ $ conda activate demo-py312
[demo-py312] ~ $
```

+++

##### les packages installés

très peu de choses

```
[demo-py312] ~ $ pip list
Package    Version
---------- -------------------
certifi    2020.4.5.1
pip        20.0.2
setuptools 46.2.0.post20200511
wheel      0.34.2
```

+++

##### on y installe ce qu'on veut
```
[demo-py312] ~ $ pip install numpy
```

+++

##### la version de python
```
[demo-py312] ~ $ python --version
Python 3.12.2
```

+++

##### sortir
```
[demo-py312] ~ $ conda deactivate
[base] ~ $
```

+++

##### la version de python
```
[base] ~ $ python --version
Python 3.11.7
```

+++

##### on n'a pas perturbé l'environnement de départ
```
[base] ~ $ pip show numpy
Name: numpy
Version: 1.18.1
```

+++

##### pour détruire l'environnement en question
```
[base] ~ $ conda env remove -n demo-py312

Remove all packages in environment /Users/jeanmineur/miniconda3/envs/demo-py312:
```

+++

## Debugging

+++

Pour le debugging, la bibliothèque standard s'appelle `pdb`. Typiquement pour mettre un *breakpoint* on écrit :

```python
def foo(n):
    n = n ** 2
    # pour mettre un point d'arrêt
    import pdb
    pdb.set_trace()
    # la suite de foo()
    return n / 10
```

+++

Je vous signale d'ailleurs qu'**à partir de Python 3.7**, il est recommandé d'utiliser la nouvelle fonction *built-in* `breakpoint()` qui rend le même service.

+++

Une fois qu'on a dit ça, votre IDE dispose certainement d'une fonctionnalité pour faire ça avec la souris de manière plus flexible.

+++

## Tests

+++

Le module `unittest` de la bibliothèque standard fournit des fonctionnalités de base pour écrire des tests unitaires.

Je vous signale également des outils comme `pytest` (et `nosetests`), qui ne sont pas dans la distribution standard, mais qui enrichissent les capacités de `unittest` pour en rendre l'utilisation quotidienne (beaucoup) plus fluide.

Parmi les fonctionnalités fournies par un framework de test comme `pytest` :

* découverte automatique des tests : en respectant les règles de nommage, il vous suffit de lancer `pytest` à la racine de votre projet pour exécuter tous les tests.
  Vous pouvez en une commande lancer tous les tests, tous ceux d'un dossier ou d'un fichier, ou juste un test-case

* exécution automatique des tests : vous vous concentrez sur le fait d'écrire ce qui doit se passer, le framework se charge du reste

* *fixtures* pour expliciter plus simplement comment mettre le système dans un état contrôlé

* et beaucoup d'autres choses…

Pour approfondir le sujet, [cette note très courte](https://docs.pytest.org/en/latest/goodpractices.html) explicite les conventions pour la découverte des tests, et les bonnes pratiques.  
Personnellement je préfère mettre les tests dans un dossier séparé du package, mais bon, tous les goûts sont dans la nature apparemment :)

+++

## Documentation

+++

Le standard de fait dans ce domaine est clairement une combinaison basée sur

* l'outil `sphinx`, qui permet de générer la documentation à partir du source, avec
  * des plugins pour divers sous-formats dans les docstrings,
  * un système de templating,
  * et de nombreuses autres possibilités ;
* `readthedocs.io` qui est une plateforme ouverte pour l'hébergement des documentations, elle-même facilement intégrable avec un repository type `github.io`, 

Pour vous donner une idée du résultat, je vous invite à consulter un module de ma facture :

* les sources sur github sur <https://github.com/parmentelat/asynciojobs>, et notamment le sous-répertoire `sphinx`,
* et la documentation en ligne sur <http://asynciojobs.readthedocs.io/>.

+++

## Linter

+++

Au delà de la vérification automatique de la présentation du code (PEP8), il existe un outil `pylint` qui fait de l'analyse de code source en vue de détecter des erreurs le plus tôt possible dans le cycle de développement.

En quelques mots, ma recommandation à ce sujet est que :

* tout d'abord, et comme dans tous les langages en fait, il est **très utile** de faire passer systématiquement son code dans un linter de ce genre ;
* idéalement on ne devrait commiter que du code qui passe cette étape ;
* cependant, il y a un petit travail de filtrage à faire au démarrage, car pylint détecte plusieurs centaines de sortes d'erreurs, du coup il convient de passer un moment à configurer l'outil pour qu'il en ignore certaines.

+++

Dès que vous commencez à travailler sur des projets sérieux, vous devez utiliser un éditeur qui intègre et exécute automatiquement `pylint`. On peut notamment recommander [PyCharm](https://www.jetbrains.com/pycharm/).

+++

## Type hints

+++

Je voudrais citer enfin l'outil `mypy` qui est un complément crucial dans la mise en oeuvre des *type hints*. 

Comme on l'a vu en Semaine 4 dans la séquence consacrée aux type hints, et en tous cas jusque Python-3.6, les annotations de typage que vous insérez éventuellement dans votre code sont complètement ignorées de l'interpréteur. 

Elles sont par contre analysées par l'outil `mypy` qui fournit une sorte de couche supplémentaire de *linter* et permet de détecter, ici encore, les éventuelles erreurs qui peuvent résulter notamment d'une mauvaise utilisation de telle ou telle librairie.

+++

## Conclusion

+++

À nouveau cette liste n'est pas exhaustive, elle s'efforce simplement de guider vos premiers pas dans cet écosystème.

Je vous invite à creuser de votre côté les différents aspects qui, parmi cette liste, vous semblent les plus intéressants pour votre usage.
