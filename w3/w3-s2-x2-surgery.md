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
  title: 'exercice: unpacking'
---

# *Sequence unpacking*

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

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
