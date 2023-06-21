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
notebookname: Listes
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

Vous devez écrire une fonction `laccess` qui prend en argument une liste, et qui retourne :

* `None` si la liste est vide ;
* sinon le dernier élément de la liste si elle est de taille paire ;
* et sinon l'élément du milieu.

```{code-cell} ipython3
from corrections.exo_laccess import exo_laccess
exo_laccess.example()
```

```{code-cell} ipython3
# écrivez votre code ici
def laccess(liste):
    return "votre code"
```

```{code-cell} ipython3
# pour le corriger
exo_laccess.correction(laccess)
```

Une fois que votre code fonctionne, vous pouvez regarder si par hasard il marcherait aussi avec des chaînes :

```{code-cell} ipython3
from corrections.exo_laccess import exo_laccess_strings
exo_laccess_strings.correction(laccess)
```
