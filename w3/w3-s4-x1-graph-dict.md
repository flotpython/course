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
notebookname: Dictionnaires
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Dictionnaires et listes

+++

## Exercice - niveau basique

On veut implémenter un petit modèle de graphes. Comme on a les données dans des fichiers, on veut analyser des fichiers d'entrée qui ressemblent à ceci :

```{code-cell} ipython3
:cell_style: split

!cat data/graph1.txt
```

+++ {"cell_style": "split"}

qui signifierait :

* un graphe à 3 sommets *s1*, *s2* et *s3*;
* et 4 arêtes
  * une entre *s1* et *s2* de longueur 10;
  * une entre *s2* et *s3* de longueur 12;
  * etc…

+++

On vous demande d'écrire une fonction qui lit un tel fichier texte, et construit (et retourne) un dictionnaire Python qui représente ce graphe.

Dans cet exercice on choisit :

* de modéliser le graphe comme un dictionnaire indexé sur les (noms de) sommets ;
* et chaque valeur est une liste de tuples de la forme (*suivant*, *longueur*), dans l'ordre d'apparition dans le fichier d'entrée.

```{code-cell} ipython3
# voici ce qu'on obtiendrait par exemple avec les données ci-dessus
from corrections.exo_graph_dict import exo_graph_dict
exo_graph_dict.example()
```

**Notes**

* Vous remarquerez que l'exemple ci-dessus retourne un dictionnaire standard; une solution qui utiliserait `defaultdict` est acceptable également;
* Notez bien également que dans le résultat, la longueur d'un arc est attendue comme un **`int`**.

```{code-cell} ipython3
# n'oubliez pas d'importer si nécessaire

# à vous de jouer
def graph_dict(filename):
    "votre code"
```

```{code-cell} ipython3
exo_graph_dict.correction(graph_dict)
```
