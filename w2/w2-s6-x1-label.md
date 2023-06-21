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
  title: Format
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Formatage des chaines de caractères

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
