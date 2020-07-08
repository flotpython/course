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
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Ensembles

+++

## Exercice - niveau basique

```{code-cell}
# charger l'exercice
from corrections.exo_read_set import exo_read_set
```

On se propose d'écrire une fonction `read_set` qui construit un ensemble à partir du contenu d'un fichier. Voici par exemple un fichier d'entrée :

```{code-cell}
:cell_style: center

!cat data/setref1.txt
```

`read_set` va prendre en argument un nom de fichier (vous pouvez supposer qu'il existe), enlever les espaces éventuelles au début et à la fin de chaque ligne, et construire un ensemble de toutes les lignes ; par exemple :

```{code-cell}
exo_read_set.example()
```

```{code-cell}
# écrivez votre code ici
def read_set(filename):
    "votre code"
```

```{code-cell}
# vérifiez votre code ici
exo_read_set.correction(read_set)
```

*****

+++

## Deuxième partie - niveau basique

```{code-cell}
# la définition de l'exercice
from corrections.exo_read_set import exo_search_in_set
```

Ceci étant acquis, on veut écrire une deuxième fonction `search_in_set` qui prend en argument deux fichiers :

* `filename_reference` est le nom d'un fichier contenant des mots de référence ;
* `filename` est le nom d'un fichier contenant des mots, dont on veut savoir s'ils sont ou non dans les références.

Pour cela `search_in_set` doit retourner une liste, contenant pour chaque ligne du fichier `filename` un tuple avec :

* la ligne (sans les espaces de début et de fin, ni la fin de ligne) ;
* un booléen qui indique si ce mot est présent dans les références ou pas.

Par exemple :

```{code-cell}
:cell_style: split

!cat data/setref1.txt
```

```{code-cell}
:cell_style: split

!cat data/setsample1.txt
```

```{code-cell}
exo_search_in_set.example()
```

```{code-cell}
# à vous
def search_in_set(filename_reference, filename):
    "votre code"
```

```{code-cell}
# vérifiez
exo_search_in_set.correction(search_in_set)
```
