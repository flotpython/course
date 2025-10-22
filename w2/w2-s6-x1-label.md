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
  title: Format
---

# Formatage des chaines de caractères

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Exercice - niveau basique

Vous devez écrire une fonction qui prend deux arguments :

* une chaîne de caractères qui désigne le prénom d'un élève ;
* un entier qui indique la note obtenue.

Elle devra retourner une chaîne de caractères selon que la note est

* $0  \leqslant note \lt 10$
* $10 \leqslant note \lt 16$
* $16 \leqslant note \leqslant 20$

comme on le voit sur les exemples :

```{code-cell} ipython3
from corrections.exo_label import exo_label
exo_label.example()
```

```{code-cell} ipython3
# à vous de jouer
def label(prenom, note):
    "votre code"
```

```{code-cell} ipython3
# pour corriger
exo_label.correction(label)
```
