---
jupytext:
  cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
  notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
notebookname: De la lecture
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Un peu de lecture

+++

## Complément - niveau basique

+++

### Mise à jour de Juillet 2018

+++

Le 12 Juillet 2018, Guido van Rossum [a annoncé qu'il quittait la fonction de BDFL](https://lwn.net/Articles/759654/) qu'il occupait depuis près de trois décennies. Il n'est pas tout à fait clair à ce stade comment va évoluer la gouvernance de Python.

+++

### Le Zen de Python

+++

Vous pouvez lire le "Zen de Python", qui résume la philosophie du langage, en important le module `this` avec ce code&nbsp;: (pour exécuter ce code, cliquez dans la cellule de code, et faites au clavier "Majuscule/Entrée" ou "Shift/Enter")

```{code-cell}
# le Zen de Python
import this
```

### Documentation

+++

* On peut commencer par citer l'[article de Wikipédia sur Python en français](http://fr.wikipedia.org/wiki/Python_%28langage%29).
* La [page sur le langage en français](https://wiki.python.org/moin/FrenchLanguage).
* La [documentation originale](https://docs.python.org/3/) de Python 3 - donc, en anglais - est un très bon point d'entrée lorsqu'on cherche un sujet particulier, mais (beaucoup) trop abondante pour être lue d'un seul trait. Pour chercher de la documentation sur un module particulier, le plus simple est encore d'utiliser Google - ou votre moteur de recherche favori - qui vous redirigera, dans la grande majorité des cas, vers la page qui va bien dans, précisément, la documentation de Python.

  À titre d'exercice, cherchez la documentation du module `pathlib` en [cherchant sur Google](https://www.google.fr/search?q=python+module+pathlib) les mots-clé `"python module pathlib"`.

* J'aimerais vous signaler également une initiative pour [traduire la documentation officielle en français](https://docs.python.org/fr/3/).

+++

### Historique et survol

+++

* La FAQ officielle de Python (en anglais) sur [les choix de conception et l'historique du langage](https://docs.python.org/3/faq/design.html).
* L'article de Wikipédia (en anglais) sur l'[historique du langage](http://en.wikipedia.org/wiki/History_of_Python).
* Sur Wikipédia, un article (en anglais) sur [la syntaxe et la sémantique de Python](http://en.wikipedia.org/wiki/Python_syntax_and_semantics).

+++

### Un peu de folklore

+++

* Le [discours de Guido van Rossum à PyCon 2016](https://www.youtube.com/watch?v=YgtL4S7Hrwo).
* Sur YouTube, le [sketch des Monty Python](https://www.truestories.fr/1325-L_origine_du_mot_Spam), (malheureusement plus disponible sur YouTube) d'où proviennent les termes `spam`, `eggs` et autres `beans` que l'on utilise traditionnellement dans les exemples en Python plutôt que `foo` et `bar`.
* L'[article Wikipédia correspondant](http://en.wikipedia.org/wiki/Spam_%28Monty_Python%29), qui cite le langage Python.

+++

## Complément - niveau intermédiaire

+++

### Licence

+++

* La [licence d'utilisation est disponible ici](https://docs.python.org/3/license.html).
* La page de la [Python Software Foundation](https://www.python.org/psf/), qui est une entité légale similaire à nos associations de 1901, à but non lucratif&nbsp;; elle possède les droits sur le langage.

+++

### Le processus de développement

+++

* Comment les choix d'évolution sont proposés et discutés, [au travers des PEP (Python Enhancement Proposals) - sur wikipedia](http://en.wikipedia.org/wiki/Python_%28programming_language%29#Development)
* [Le premier PEP: PEP-001 donc](http://legacy.python.org/dev/peps/pep-0001/) décrit en détail le cycle de vie des PEPs
* Le [PEP 008](http://legacy.python.org/dev/peps/pep-0008), qui préconise un style de présentation (*style guide*)
* L'[index de tous les PEPs](http://legacy.python.org/dev/peps/)
