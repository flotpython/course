---
ipub:
  sphinx:
    toggle_input: true
    toggle_input_all: true
    toggle_output: true
    toggle_output_all: true
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
  title: exercices en vrac
---

# Quelques sujets d'exercice en vrac

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

```{code-cell} ipython3
# ceci permet de recharger les modules
# lorsqu'ils ont été modifiés en dehors du notebook

# pour commodité lors du développement des exercices

%load_ext autoreload
%autoreload 2
```

#### Niveaux de difficulté

+++

La plupart de (tous ?) ces exercices sont inspirés d'énoncés trouvés sur https://codewars.com/ ; dans ces cas-là j'indique la référence, ainsi que la difficulté affichée sur codewars ; [l'échelle est à la japonaise](https://github.com/Codewars/codewars.com/wiki/Kata-Ranking), 1 kyu c'est très difficile et 8 kyu c'est très simple.

+++

******

+++

## Trouver la somme

+++

**inspiré de https://www.codewars.com/kata/52c31f8e6605bcc646000082** (6 kyu)

+++

On cherche dans une liste deux nombres (à des indices différents) dont la somme est fixée

* en entrée : une liste de nombres, et une valeur cible
* en sortie : les index dans la liste de deux nombres dont la somme est égale à la valeur cible ;  
  on doit retourner un tuple, trié dans l'ordre croissant.

Hypothèses : on admet (pas besoin de le vérifier donc) que les entrées sont correctes, c'est-à-dire ne contiennent que des nombres et qu'il existe une solution.

Unicité : n'importe quelle solution est valable en cas de solutions multiples ; toutefois pour des raisons techniques, la correction automatique ne teste votre code que sur des entrées où la solution est unique.

```{code-cell} ipython3
# charger l'exercice et afficher un exemple

from corrections.exo_two_sum import exo_two_sum
exo_two_sum.example()
```

```{code-cell} ipython3
# indice : il y a peut-être des choses utiles dans ce module
# import itertools

def two_sum(data, target):
    ...
```

```{code-cell} ipython3
exo_two_sum.correction(two_sum)
```

*****

+++

## Plus grande distance

+++

**inspiré de https://www.codewars.com/kata/5442e4fc7fc447653a0000d5** (6 kyu)

+++

* en entrée : une liste d'objets (vous pouvez vous restreindre à des entiers pour commencer)
* en sortie : un entier qui décrit la plus grande distance (en termes d'indices) entre deux occurrences du même objet dans la liste ;  
  si aucun objet n'est présent en double, retournez 0.

```{code-cell} ipython3
from corrections.exo_longest_gap import exo_longest_gap

exo_longest_gap.example()
```

```{code-cell} ipython3
# votre code
def longest_gap(liste):
    ...
```

```{code-cell} ipython3
exo_longest_gap.correction(longest_gap)
```

## Meeting

+++

**inspiré de https://www.codewars.com/kata/59df2f8f08c6cec835000012** (6 kyu)

Je vous invite à lire l'énoncé directement sur codewars.  
**Notez bien** toutefois que, contrairement à ce qui est demandé sur codewars, notre variante ne met pas le texte en majuscule.

+++

**Rappel sur la concaténation des chaines**
remarquez aussi l'usage qu'on fait ici, pour la présentation, de la concaténation de chaines :

```{code-cell} ipython3
# rappel sur la concaténation des chaines
# grâce à la parenthèse on peut 
# se passer des \ qui sont assez vilains
x = ("une chaine unique "
     "que l'on coupe en morceaux "
     "parce qu'elle est très longue")
```

```{code-cell} ipython3
x
```

```{code-cell} ipython3
from corrections.exo_meeting import exo_meeting

exo_meeting.example()
```

```{code-cell} ipython3
def meeting(string):
    ...
```

```{code-cell} ipython3
exo_meeting.correction(meeting)
```

****
