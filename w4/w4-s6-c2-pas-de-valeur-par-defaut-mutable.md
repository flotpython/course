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
notebookname: "Un pi\xE8ge courant"
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Un piège courant

+++

## Complément - niveau basique

+++

### N'utilisez pas d'objet mutable pour les valeurs par défaut

+++

En Python il existe un piège dans lequel il est très facile de tomber. Aussi si vous voulez aller à l'essentiel : **n'utilisez pas d'objet mutable pour les valeurs par défaut** lors de la définition d'une fonction.

Si vous avez besoin d'écrire une fonction qui prend en argument par défaut une liste ou un dictionnaire vide, voici comment faire

```{code-cell} ipython3
# ne faites SURTOUT PAS ça
def ne_faites_pas_ca(options={}):
    "faire quelque chose"
```

```{code-cell} ipython3
# mais plutôt comme ceci
def mais_plutot_ceci(options=None):
    if options is None: 
        options = {}
    "faire quelque chose"
```

## Complément - niveau intermédiaire

+++

### Que se passe-t-il si on le fait ?

+++

Considérons le cas relativement simple d'une fonction qui calcule une valeur - ici un entier aléatoire entre 0 et 10 -, et l'ajoute à une liste passée par l'appelant.

+++

Et pour rendre la vie de l'appelant plus facile, on se dit qu'il peut être utile de faire en sorte que si l'appelant n'a pas de liste sous la main, on va créer pour lui une liste vide. Et pour ça on fait :

```{code-cell} ipython3
import random

# l'intention ici est que si l'appelant ne fournit pas 
# la liste en entrée, on crée pour lui une liste vide
def ajouter_un_aleatoire(resultats=[]):
    resultats.append(random.randint(0, 10))
    return resultats
```

Si on appelle cette fonction une première fois, tout semble bien aller

```{code-cell} ipython3
ajouter_un_aleatoire()
```

Sauf que, si on appelle la fonction une deuxième fois, on a une surprise !

```{code-cell} ipython3
ajouter_un_aleatoire()
```

### Pourquoi ?

+++

Le problème ici est qu'une valeur par défaut - ici l'expression `[]` - est évaluée **une fois** au moment de la **définition** de la fonction. 

Toutes les fois où la fonction est appelée avec cet argument manquant, on va utiliser comme valeur par défaut **le même objet**, qui la première fois est bien une liste vide, mais qui se fait modifier par le premier appel. 

Si bien que la deuxième fois on réutilise la même liste **qui n'est plus vide**. Pour aller plus loin, vous pouvez regarder la documentation Python sur [ce problème](https://docs.python.org/3/faq/programming.html#why-are-default-values-shared-between-objects).
