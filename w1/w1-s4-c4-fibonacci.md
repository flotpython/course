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
  title: Fibonacci (suite)
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# La suite de Fibonacci (version pour terminal)

+++

## Complément - niveau intermédiaire

+++

Nous reprenons le cas de la fonction `fibonacci` que nous avons déjà vue, mais cette fois nous voulons que l'utilisateur puisse indiquer l'entier en entrée de l'algorithme, non plus en répondant à une question, mais sur la ligne de commande, c'est-à-dire en tapant :

```bash
$ python3 fibonacci.py 12
```

+++

**Avertissement&nbsp;:**

Attention, cette version-ci **ne fonctionne pas dans ce notebook**, justement car on n'a pas de moyen dans un notebook d'invoquer un programme en lui passant des arguments de cette façon. Ce notebook est rédigé pour vous permettre de vous entraîner avec la fonction de téléchargement au format Python, qu'on a vue dans la vidéo, et de faire tourner ce programme sur votre propre ordinateur.

+++

### Le module `argparse`

+++

Cette fois nous importons le module `argparse`, c'est lui qui va nous permettre d'interpréter les arguments passés sur la ligne de commande.

```{code-cell} ipython3
from argparse import ArgumentParser
```

Puis nous répétons la fonction `fibonacci` :

```{code-cell} ipython3
def fibonacci(n):
    "retourne le nombre de fibonacci pour l'entier n"
    # pour les deux premières valeurs de n, on peut renvoyer n
    if n <= 1:
        return n
    # sinon on initialise f2 pour n-2 et f1 pour n-1
    f2, f1 = 0, 1
    # et on itère n-1 fois pour additionner
    for i in range(2, n + 1):
        f2, f1 = f1, f1 + f2
#        print(i, f2, f1)
    # le résultat est dans f1
    return f1
```

*Remarque :*

Certains d'entre vous auront évidemment remarqué que l'on aurait pu éviter de copier-coller la fonction `fibonacci` comme cela&nbsp;; c'est à ça que servent les modules, mais nous n'en sommes pas là.

+++

### Un objet `parser`

+++

À présent, nous utilisons le module `argparse`, pour lui dire qu'on attend exactement un argument sur la ligne de commande, et qu'il doit être un entier. Ici encore, ne vous inquiétez pas si vous ne comprenez pas tout le code. L'objectif est de vous donner un morceau de code utilisable tout de suite, pour jouer avec votre interpréteur Python.

```{code-cell} ipython3
:latex:hidden-code-instead: entier = 8

# à nouveau : ceci n'est pas conçu pour être exécuté dans le notebook !
parser = ArgumentParser()
parser.add_argument(dest="entier", type=int,
                    help="entier d'entrée")
input_args = parser.parse_args()
entier = input_args.entier
```

Nous pouvons à présent afficher le résultat :

```{code-cell} ipython3
print(f"fibonacci({entier}) = {fibonacci(entier)}")
```

Vous pouvez donc à présent :

* télécharger ce code sur votre disque comme un fichier `fibonacci.py` en utilisant le menu *"File -> Download as -> Python"*
* l'exécuter avec simplement l'interpréteur Python comme ceci :


```bash
$ python3 fibonacci.py 56
```

(sans taper le signe `$` qui indique simplement le prompt du terminal.)
