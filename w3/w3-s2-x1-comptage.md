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
notebookname: 'exercice: fichiers'
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Fichiers

+++

## Exercice - niveau basique

+++

### Calcul du nombre de lignes, de mots et de caractères

On se propose d'écrire une *moulinette* qui annote un fichier avec des nombres de lignes, de mots et de caractères.

Le but de l'exercice est d'écrire une fonction `comptage` :

 * qui prenne en argument un nom de fichier d'entrée (on suppose qu'il existe) et un nom de fichier de sortie (on suppose qu'on a le droit de l'écrire) ;
 * le fichier d'entrée est supposé encodé en UTF-8 ;
 * le fichier d'entrée est laissé intact ;
 * pour chaque ligne en entrée, le fichier de sortie comporte une ligne qui donne le numéro de ligne, le nombre de mots (**séparés par des espaces**), le nombre de caractères (y compris la fin de ligne), et la ligne d'origine.

```{code-cell} ipython3
# un exemple de ce qui est attendu
from corrections.exo_comptage import exo_comptage
exo_comptage.example()
```

```{code-cell} ipython3
# votre code
def comptage(in_filename, out_filename):
   "votre code"
```

**N'oubliez pas de vérifier** que vous ajoutez bien les **fins de ligne**, car la vérification automatique est pointilleuse (elle utilise l'opérateur `==`), et rejettera votre code si vous ne produisez pas une sortie rigoureusement similaire à ce qui est attendu.

```{code-cell} ipython3
# pour vérifier votre code
# voyez aussi un peu plus bas, une cellule d'aide au debugging

exo_comptage.correction(comptage)
```

La méthode `debug` applique votre fonction au premier fichier d'entrée, et affiche le résultat comme dans l'exemple ci-dessus :

```{code-cell} ipython3
# debugging
exo_comptage.debug(comptage)
```

### Accès aux fichiers d'exemples

+++

Vous pouvez télécharger les fichiers d'exemples :

 * [Romeo and Juliet](data/romeo_and_juliet.txt)
 * [Lorem Ipsum](data/lorem_ipsum.txt)
 * ["Une charogne" en UTF-8](data/une_charogne_unicode.txt)

***

Pour les courageux, je vous donne également ["Une charogne" en ISO-8859-15](data/une_charogne_iso15.txt), qui contient le même texte que "Une charogne", mais encodé en Latin-9, connu aussi sous le nom ISO-8859-15.

Ce dernier fichier n'est pas à prendre en compte dans la version basique de l'exercice, mais vous pourrez vous rendre compte par vous-mêmes, au cas où cela ne serait pas clair encore pour vous, qu'il n'est pas facile d'écrire une fonction `comptage` qui devine l'encodage, c'est-à-dire qui fonctionne correctement avec des entrées indifféremment en Unicode ou Latin, sans que cet encodage soit passé en paramètre à `comptage`.

+++

C'est d'ailleurs le propos de [la bibliothèque `chardet`](https://pypi.python.org/pypi/chardet) qui s'efforce de déterminer l'encodage de fichiers d'entrée, sur la base de modèles statistiques.
