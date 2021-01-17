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
notebookname: 'exercice: unpacking'
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# *Sequence unpacking*

+++

## Exercice - niveau basique

Cet exercice consiste à écrire une fonction `surgery`, qui prend en argument une liste, et qui retourne la **même** liste **modifiée** comme suit :

* si la liste est de taille 0 ou 1, elle n'est pas modifiée ;
* si la liste est de taille paire, on intervertit les deux premiers éléments de la liste ;
* si elle est de taille impaire, on intervertit les deux derniers éléments.

```{code-cell} ipython3
# voici quelques exemples de ce qui est attendu
from corrections.exo_surgery import exo_surgery
exo_surgery.example()
```

```{code-cell} ipython3
# écrivez votre code
def surgery(liste):
    "<votre_code>"
```

```{code-cell} ipython3
# pour le vérifier, évaluez cette cellule
exo_surgery.correction(surgery)
```
