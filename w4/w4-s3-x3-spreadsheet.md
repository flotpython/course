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
  title: Spreadsheet
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

Merci à Adrien Ollier d'avoir proposé cet exercice

+++

## exercice - niveau intermédiaire

Le but de l'exercice est d'écrire la fonction `spreadsheet` 

* qui prend en entrée un entier - disons `index`
* et qui en sortie retourne le nom de la colonne correspondante dans un fichier Excel.

Pour rappel dans un tableur les colonnes sont appelées d'abord `A` jusque `Z`, puis on passe à `AA`, `AB`, et ainsi de suite jusque `ZZ`, puis `AAA`, etc etc..

La valeur d'entrée index = 0 est considérée comme non valide.

```{code-cell} ipython3
# voici quelques exemples charnière
from corrections.exo_spreadsheet import exo_spreadsheet
exo_spreadsheet.example()
```

+++

Pour vous aider, on rappelle l'existence des fonctions prédéfinies `chr()` et `ord()` qui permettent de passer des caractères Unicode à leur représentation numérique (*codepoint*) et vice-versa.

+++

On vous invite également à envisager la progression suivante :

1. Exercice intermédiaire:
   Écrire la fonction qui prend les entiers de 0 à 25 et qui retourne les lettres de A à Z.

2. Écrire la fonction qui prend les entiers de 1 à 26 et qui retourne les lettres de A à Z.
   La valeur d'entrée index = 0 est considérée comme une erreur.

3. À partir de la fonction précédente, écrire la fonction spreadsheet() pour les indices commençant à 1 et allant au-delà de 26.

+++

Remarquez que, contrairement à ce qu'on indiquait dans une version antérieure de cet énoncé, il ne s'agit pas exactement de faire une décomposition en base 26; les nombres "charnière", c'est-à-dire ceux qui correspondent à un passage de `Z*` à `A*`, sont donnés - à 1 près - par la formule $n + n^2 + n^3 + ... + n^k$, avec ici $n=26$

```{code-cell} ipython3
# écrivez votre code ici'
def spreadsheet(index):
    ...
```

```{code-cell} ipython3
# et validez-le ici
exo_spreadsheet.correction(spreadsheet)
```
