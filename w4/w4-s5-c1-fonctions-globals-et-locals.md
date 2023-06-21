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
  title: globals et locals
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Les fonctions `globals` et `locals`

+++

## Complément - niveau intermédiaire

+++

### Un exemple

+++

python fournit un accès à la liste des noms et valeurs des variables visibles à cet endroit du code. Dans le jargon des langages de programmation on appelle ceci **l'environnement**.

Cela est fait grâce aux fonctions *built-in* `globals` et `locals`, que nous allons commencer par essayer sur quelques exemples. Nous avons pour cela écrit un module dédié :

```{code-cell} ipython3
import env_locals_globals
```

dont voici le code

```{code-cell} ipython3
from modtools import show_module
show_module(env_locals_globals)
```

et voici ce qu'on obtient lorsqu'on appelle

```{code-cell} ipython3
env_locals_globals.temoin(10)
```

### Interprétation

+++

Que nous montre cet exemple ?

* D'une part la fonction **`globals`** nous donne la liste des symboles définis au niveau de **l'espace de noms du module**. Il s'agit évidemment du module dans lequel est définie la fonction, pas celui dans lequel elle est appelée. Vous remarquerez que ceci englobe **tous** les symboles du module `env_locals_globals`, et non pas seulement ceux définis avant `temoin`, c'est-à-dire la variable `globale`, les deux fonctions `display_env` et `temoin`, et la classe `Foo`. 

* D'autre part **`locals`** nous donne les variables locales qui sont accessibles **à cet endroit du code**, comme le montre ce second exemple qui se concentre sur `locals` à différents points d'une même fonction.

```{code-cell} ipython3
import env_locals
```

```{code-cell} ipython3
# le code de ce module 
show_module(env_locals)
```

```{code-cell} ipython3
env_locals.temoin(10)
```

## Complément - niveau avancé

+++

**NOTE**: cette section est en pratique devenue obsolète maintenant que les *f-strings* sont présents dans la version 3.6.

Nous l'avons conservée pour l'instant toutefois, pour ceux d'entre vous qui ne peuvent pas encore utiliser les *f-strings* en production. N'hésitez pas à y passer si vous n'êtes pas dans ce cas.

+++

### Usage pour le formatage de chaînes

+++

Les deux fonctions `locals` et `globals` ne sont pas d'une utilisation très fréquente. Elles peuvent cependant être utiles dans le contexte du formatage de chaînes, comme on peut le voir dans les deux exemples ci-dessous.

+++

##### Avec `format`

+++

On peut utiliser `format` qui s'attend à quelque chose comme :

```{code-cell} ipython3
"{nom}".format(nom="Dupont")
```

que l'on peut obtenir de manière équivalente, en anticipant sur la prochaine vidéo, avec le passage d'arguments en `**` :

```{code-cell} ipython3
"{nom}".format(**{'nom': 'Dupont'})
```

En versant la fonction `locals` dans cette formule on obtient une forme relativement élégante

```{code-cell} ipython3
def format_et_locals(nom, prenom, civilite, telephone):
    return "{civilite} {prenom} {nom} : Poste {telephone}".format(**locals())

format_et_locals('Dupont', 'Jean', 'Mr', '7748')
```

##### Avec l'opérateur `%`

+++

De manière similaire, avec l'opérateur `%` - dont nous rappelons qu'il est obsolète - on peut écrire

```{code-cell} ipython3
def pourcent_et_locals(nom, prenom, civilite, telephone):
    return "%(civilite)s %(prenom)s %(nom)s : Poste %(telephone)s"%locals()

pourcent_et_locals('Dupont', 'Jean', 'Mr', '7748')
```

##### Avec un *f-string*

+++

Pour rappel si vous disposez de python 3.6, vous pouvez alors écrire simplement - et sans avoir recours, donc, à `locals()` ou autre :

```{code-cell} ipython3
# attention ceci nécessite python-3.6
def avec_f_string(nom, prenom, civilite, telephone):
    return f"{civilite} {prenom} {nom} : Poste {telephone}"

avec_f_string('Dupont', 'Jean', 'Mr', '7748')
```
