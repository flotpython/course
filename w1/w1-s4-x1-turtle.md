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
  title: "Dessiner un carr\xE9"
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Dessiner un carré

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

Et pour finir on attend que l'utilisateur clique dans la fenêtre de la tortue, et alors on termine :

```{code-cell} ipython3
:latex-skip-eval: true

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
