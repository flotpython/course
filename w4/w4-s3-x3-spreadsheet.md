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

Merci à Adrien Ollier d'avoir proposé cet exercice

+++

## exercice - niveau basique

```{code-cell}
from corrections.exo_spreadsheet import exo_spreadsheet
```

Le but de l'exercice est d'écrire la fonction `spreadsheet` 

* qui prend en entrée un entier - disons `index`
* et qui en sortie retourne le nom de la colonne correspondante dans un fichier Excel.

Pour rappel dans un tableur les colonnes sont appelées d'abord `A` jusque `Z`, puis on passe à `AA`, `AB`, et ainsi de suite jusque `ZZ`, puis `AAA`, etc etc..

La valeur d'entrée index = 0 est considérée comme non valide.

```{code-cell}
# voici quelques exemples charnière
exo_spreadsheet.example()
```

Comme vous le voyez, il s'agit en quelque sorte de traduire cet entier en base 26 - si on considère les 26 lettres comme les chiffres (*digits*) de la numération dans cette base.

+++

Pour vous aider, on rappelle l'existence des fonctions prédéfinies `chr()` et `ord()` qui permettent de passer des caractères Unicode à leur représentation numérique (*codepoint*) et vice-versa.

+++

On vous invite également à envisager la progression suivante :

1. Exercice intermédiaire:
   Écrire la fonction qui prend les entiers de 0 à 25 et qui retourne les lettres de A à Z.

1. Écrire la fonction qui prend les entiers de 1 à 26 et qui retourne les lettres de A à Z.
   La valeur d'entrée index = 0 est considérée comme une erreur.

1. À partir de la fonction précédente, écrire la fonction spreadsheet() pour les indices commençant à 1 et allant au-delà de 26.

```{code-cell}
# écrivez votre code ici'
def spreadsheet(index):
    ...
```

```{code-cell}
# et validez-le ici
exo_spreadsheet.correction(spreadsheet)
```
