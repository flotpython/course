---
jupytext:
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
  title: Listes
---

# Listes

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

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
