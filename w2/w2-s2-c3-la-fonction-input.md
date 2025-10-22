---
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
  title: La fonction input
---

# Obtenir une réponse de l'utilisateur

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Complément - niveau basique

+++

Occasionnellement, il peut être utile de poser une question à l'utilisateur.

+++

### La fonction `input`

+++

C'est le propos de la fonction `input`. Par exemple :

```{code-cell} ipython3
:latex-hidden-code-instead: nom_ville = 'Paris'

nom_ville = input("Entrez le nom de la ville : ")
```

```{code-cell} ipython3
print(f"nom_ville={nom_ville}")
```

### Attention à bien vérifier/convertir

+++

Notez bien que `input` renvoie **toujours une chaîne de caractères** (`str`). C'est assez évident, mais il est très facile de l'oublier et de passer cette chaîne directement à une fonction qui s'attend à recevoir, par exemple, un nombre entier, auquel cas les choses se passent mal :

+++

```python
>>> input("nombre de lignes ? ") + 3
nombre de lignes ? 12
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be str, not int
```

+++

Dans ce cas il faut appeler la fonction `int` pour convertir le résultat en un entier :

```{code-cell} ipython3
:latex-skip-eval: true

int(input("Nombre de lignes ? ")) + 3
```

### Limitations

+++

Cette fonction peut être utile pour vos premiers pas en Python.

En pratique toutefois, on utilise assez peu cette fonction, car les applications "réelles" viennent avec leur propre interface utilisateur, souvent graphique, et disposent donc d'autres moyens que celui-ci pour interagir avec l'utilisateur.

Les applications destinées à fonctionner dans un terminal, quant à elles, reçoivent traditionnellement leurs données de la ligne de commande. C'est le propos du module `argparse` que nous avons déjà rencontré en première semaine.
