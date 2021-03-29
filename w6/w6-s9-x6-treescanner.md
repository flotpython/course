---
jupytext:
  cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
  notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
notebookname: 'exercice: treescanner'
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

## Exercice - niveau intermédiaire+

+++

On veut écrire **une fonction génératrice** qui énumère tous les noeuds d'un arbre en le parcourant en profondeur d'abord.

Pour simplifier l'exercice au maximum, nous ne considérons que des entrées constituées de listes et d'entiers.

```{code-cell}
from corrections.gen_treescanner import exo_treescanner
exo_treescanner.example()
```

+++ {"tags": []}

la présentation de l'exemple peut laisser penser qu'il faut retourner une liste  
mais ce n'est pas ce qui est demandé !  
**attention** à bien implémenter **une fonction génératrice**

```{code-cell}
# à vous de jouer
def treescanner(tree):
    ...
```

```{code-cell}
# pour le corriger

exo_treescanner.correction(treescanner)
```

### indice

rappelez-vous que pour parcourir un arbre en profondeur d'abord, un algorithme de parcours récursif est très adapté
