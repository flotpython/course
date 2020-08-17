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
notebookname: 'exercice: dice'
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Exercice - niveau avancé

+++

## construire un tableau en dimension variable

+++

On étudie les probabilités d'obtenir une certaine somme avec plusieurs dés. 

Tout le monde connaît le cas classique avec deux dés à 6 faces, ou l'on construit mentalement la grille suivante:

|  +  | &#124; | 1 | 2 | 3 | 4 | 5 | 6 |
|:---:|:------:|:-:|:-:|:-:|:-:|:-:|:-:|
| *1* | &#124; | 2 | 3 | 4 | 5 | 6 | 7 | 
| *2* | &#124; | 3 | 4 | 5 | 6 | 7 | 8 | 
| *3* | &#124; | 4 | 5 | 6 | 7 | 8 | 9 | 
| *4* | &#124; | 5 | 6 | 7 | 8 | 9 |10 | 
| *5* | &#124; | 6 | 7 | 8 | 9 |10 |11 | 
| *6* | &#124; | 7 | 8 | 9 |10 |11 |12 | 

Imaginons que vous êtes étes étudiant, vous venez de faire un exercice de maths qui vous a mené à une formule qui permet de calculer, pour un jeu à `nb_dice` dés, chacun à `sides` faces, le nombre de tirages qui donnent une certaine somme `target`.

Vous voulez vérifer votre formule, en appliquant une méthode de force brute.

+++

C'est l'objet de cet exercice. Vous devez écrire une fonction `dice` qui prend en paramètres:

* `target` : la somme cible à atteindre,
* `nb_dice` : le nombre de dés,
* `sides`: le nombre de faces sur chaque dé.

On convient que par défaut `nb_dice`=2 et `sides`=6, qui correspond au cas habituel.

Dans ce cas-là par exemple, on voit, en comptant la longueur des diagonales sur la figure, que `dice(7)` doit valoir 6, puisque le tableau comporte 6 cases contenant 7 sur la diagonale.

```{code-cell} ipython3
import numpy as np

from corrections.exo_dice import exo_dice

# voici quelques exemples pour la fonction dice
exo_dice.example()
```

À nouveau, on demande explicitement ici un parcours de type force brute.

Pour devancer les remarques sur le forum de discussion:

* ce n'est pas parce cette semaine on étudie numpy que vous devez vous sentir obligé de le faire en numpy. 
* vous pouvez même vous donner comme objectif de le faire deux fois, avec et sans numpy :)

```{code-cell} ipython3
:latex:hidden-code-instead: dice=exo_dice.solution
:latex:hidden-silent: true

# à vous de jouer
def dice(target, nb_dice=2, sides=6):
    return "votre code"
```

```{code-cell} ipython3
# pour corriger votre code
exo_dice.correction(dice)
```
