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
  title: 'exercice: treescanner'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Exercice - niveau intermédiaire+

+++

On veut écrire **une fonction génératrice** qui énumère tous les noeuds d'un arbre en le parcourant en profondeur d'abord.

Pour simplifier l'exercice au maximum, nous ne considérons que des entrées constituées de listes et d'entiers.

```{code-cell} ipython3
from corrections.gen_treescanner import exo_treescanner
exo_treescanner.example()
```

+++ {"tags": []}

la présentation de l'exemple peut laisser penser qu'il faut retourner une liste  
mais ce n'est pas ce qui est demandé !  
**attention** à bien implémenter **une fonction génératrice**

```{code-cell} ipython3
# à vous de jouer
def treescanner(tree):
    ...
```

```{code-cell} ipython3
# pour le corriger

exo_treescanner.correction(treescanner)
```

### indice

rappelez-vous que pour parcourir un arbre en profondeur d'abord, un algorithme de parcours récursif est très adapté
