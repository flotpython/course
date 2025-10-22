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

```{admonition} Note à propos de la production de PDF
:class: dropdown

lorsqu'on produit une version PDF (ou html d'ailleurs) de ce complément, on le notebook est exécuté par une tâche automatique pour pouvoir afficher les résultats de chaque cellule  
du coup si on ne fait rien de particulier les cellules qui font appel à `input()` bloquent puisque personne n'est là pour entrer une réponse à la question  
c'est pourquoi on se livre à une petite gymnastique qui consiste à
- ajouter avant l'appel à `input()` une initialisation
- et à "sauter" l'exécution de la cellule qui fait vraiment le `input()` lors des taches automatiques
```

+++

### La fonction `input`

+++

C'est le propos de la fonction `input`. Par exemple :

```{code-cell} ipython3
# à nouveau ceci n'est pas indispensable mais
# pour la production du PDF il nous faut ruser un peu...

nom_ville = "Nancy"
```

```{code-cell} ipython3
:latex-hidden-code-instead: nom_ville = 'Paris'
:tags: [skip-execution]

# et à nouveau ceci n'est pas exécuté pendant 
# la production du PDF parce que c'est bloquant

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
:tags: [skip-execution]

int(input("Nombre de lignes ? ")) + 3
```

### Limitations

+++

Cette fonction peut être utile pour vos premiers pas en Python.

En pratique toutefois, on utilise assez peu cette fonction, car les applications "réelles" viennent avec leur propre interface utilisateur, souvent graphique, et disposent donc d'autres moyens que celui-ci pour interagir avec l'utilisateur.

Les applications destinées à fonctionner dans un terminal, quant à elles, reçoivent traditionnellement leurs données de la ligne de commande. C'est le propos du module `argparse` que nous avons déjà rencontré en première semaine.
