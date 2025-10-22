---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
language_info:
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
nbhosting:
  title: "Dessiner un carr\xE9"
---

# Dessiner un carré

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Exercice - niveau intermédiaire

+++

Voici un tout petit programme qui dessine un carré.

+++

Il utilise le module `turtle`, conçu précisément à des fins pédagogiques. Pour des raisons techniques, le module `turtle` n'est **pas disponible** au travers de la plateforme FUN.

+++

**Il est donc inutile d'essayer d'exécuter ce programme depuis le notebook**. L'objectif de cet exercice est plutôt de vous entraîner à télécharger ce programme en utilisant le menu *"File -> Download as -> Python"*, puis à le charger dans votre IDLE pour l'exécuter sur votre machine.

+++

**Attention** également à sauver le programme téléchargé **sous un autre nom** que `turtle.py`,  car sinon vous allez empêcher Python de trouver le module standard `turtle` ; appelez-le par exemple `turtle_basic.py`.

```{code-cell} ipython3
# on a besoin du module turtle
import turtle
```

On commence par définir une fonction qui dessine un carré de côté `length` :

```{code-cell} ipython3
def square(length):
    "have the turtle draw a square of side <length>"
    for side in range(4):
        turtle.forward(length)
        turtle.left(90)
```

Maintenant on commence par initialiser la tortue :

```{code-cell} ipython3
turtle.reset()
```

On peut alors dessiner notre carré :

```{code-cell} ipython3
:latex-skip-eval: true

square(200)
```

Et pour finir on attend que l'utilisateur clique dans la fenêtre de la tortue, et alors on termine  
en réalité on a juste besoin de faire
```{code} python
turtle.exitonclick()
```

toutefois je vais écrire un code un poil plus compliqué parce que sinon, au moment de la production du PDF, on va essayer de lancer ceci depuis le notebook, et ça va tout coincer ;(

```{code-cell} ipython3
:latex-skip-eval: true

try:
    __IPYTHON__
    print("on est dans un notebook, on ne fait rien")
except NameError:
    turtle.exitonclick()
```

## Exercice - niveau avancé

+++

Naturellement vous pouvez vous amuser à modifier ce code pour dessiner des choses un peu plus amusantes.

Dans ce cas, commencez par chercher "*module python turtle*" dans votre moteur de recherche favori, pour localiser la documentation du module [`turtle`](https://docs.python.org/3/library/turtle.html).

Vous trouverez quelques exemples pour commencer ici :

 * [turtle_multi_squares.py](media/turtle_multi_squares.py) pour dessiner des carrés à l'emplacement de la souris en utilisant plusieurs tortues ;
 * [turtle_fractal.py](media/turtle_fractal.py) pour dessiner une fractale simple ;
 * [turtle_fractal_reglable.py](media/turtle_fractal_reglable.py) une variation sur la fractale, plus paramétrable.
