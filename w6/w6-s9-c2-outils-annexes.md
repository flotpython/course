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
  display_name: Python 3
  language: python
  name: python3
language_info:
  name: python
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
notebookname: "Outils p\xE9riph\xE9riques"
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Outils périphériques

+++

## Compléments - niveau intermédiaire

+++

Pour conclure le tronc commun de ce cours Python, nous allons très rapidement citer quelques outils qui ne sont pas nécessairement dans la bibliothèque standard, mais qui sont très largement utilisés dans l'écosystème python.

Il s'agit d'une liste non exhaustive bien entendu.

+++

### Debugging

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

### Tests

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

### Documentation

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

### Linter

+++

Au delà de la vérification automatique de la présentation du code (PEP8), il existe un outil `pylint` qui fait de l'analyse de code source en vue de détecter des erreurs le plus tôt possible dans le cycle de développement.

En quelques mots, ma recommandation à ce sujet est que :

* tout d'abord, et comme dans tous les langages en fait, il est **très utile** de faire passer systématiquement son code dans un linter de ce genre ;
* idéalement on ne devrait commiter que du code qui passe cette étape ;
* cependant, il y a un petit travail de filtrage à faire au démarrage, car pylint détecte plusieurs centaines de sortes d'erreurs, du coup il convient de passer un moment à configurer l'outil pour qu'il en ignore certaines.

+++

Dès que vous commencez à travailler sur des projets sérieux, vous devez utiliser un éditeur qui intègre et exécute automatiquement `pylint`. On peut notamment recommander [PyCharm](https://www.jetbrains.com/pycharm/).

+++

### Type hints

+++

Je voudrais citer enfin l'outil `mypy` qui est un complément crucial dans la mise en oeuvre des *type hints*. 

Comme on l'a vu en Semaine 4 dans la séquence consacrée aux type hints, et en tous cas jusque Python-3.6, les annotations de typage que vous insérez éventuellement dans votre code sont complètement ignorées de l'interpréteur. 

Elles sont par contre analysées par l'outil `mypy` qui fournit une sorte de couche supplémentaire de *linter* et permet de détecter, ici encore, les éventuelles erreurs qui peuvent résulter notamment d'une mauvaise utilisation de telle ou telle librairie.

+++

### Conclusion

+++

À nouveau cette liste n'est pas exhaustive, elle s'efforce simplement de guider vos premiers pas dans cet écosystème.

Je vous invite à creuser de votre côté les différents aspects qui, parmi cette liste, vous semblent les plus intéressants pour votre usage.
