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
notebookname: Listes
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Listes

+++

## Exercice - niveau basique

```{code-cell}
from corrections.exo_laccess import exo_laccess
```

Vous devez écrire une fonction `laccess` qui prend en argument une liste, et qui retourne :

* `None` si la liste est vide ;
* sinon le dernier élément de la liste si elle est de taille paire ;
* et sinon l'élément du milieu.

```{code-cell}
exo_laccess.example()
```

```{code-cell}
# écrivez votre code ici
def laccess(liste):
    return "votre code"
```

```{code-cell}
# pour le corriger
exo_laccess.correction(laccess)
```

Une fois que votre code fonctionne, vous pouvez regarder si par hasard il marcherait aussi avec des chaînes :

```{code-cell}
from corrections.exo_laccess import exo_laccess_strings
```

```{code-cell}
exo_laccess_strings.correction(laccess)
```
