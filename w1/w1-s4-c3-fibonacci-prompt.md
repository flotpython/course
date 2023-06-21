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
  title: Fibonacci
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# La suite de Fibonacci

+++

## Complément - niveau basique

+++

Voici un premier exemple de code qui tourne.

Nous allons commencer par le faire tourner dans ce notebook. Nous verrons en fin de séance comment le faire fonctionner localement sur votre ordinateur.

+++

Le but de ce programme est de calculer la [suite de Fibonacci](https://fr.wikipedia.org/wiki/Suite_de_Fibonacci), qui est définie comme ceci&nbsp;:

* $u_0 = 0$
* $u_1 = 1$
* $\forall n >= 2, u_n = u_{n-1} + u_{n-2}$

Ce qui donne pour les premières valeurs :

+++

| n  | fibonacci(n)  |
|---:|--------------:|
| 0  | 0             |
| 1  | 1             |
| 2  | 1             |
| 3  | 2             |
| 4  | 3             |
| 5  | 5             |
| 6  | 8             |
| 7  | 13            |

+++

On commence par définir la fonction `fibonacci` comme il suit. Naturellement vous n'avez pas encore tout le bagage pour lire ce code, ne vous inquiétez pas, nous allons vous expliquer tout ça dans les prochaines semaines. Le but est uniquement de vous montrer un fonctionnement de l'interpréteur Python et de IDLE.

```{code-cell} ipython3
def fibonacci(n):
    "retourne le nombre de fibonacci pour l'entier n"
    # pour les deux petites valeurs de n, on peut retourner n
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

Pour en faire un programme utilisable on va demander à l'utilisateur de rentrer un nombre&nbsp;; il faut le convertir en entier car `input` renvoie une chaîne de caractères :

```{code-cell} ipython3
:latex:hidden-code-instead: entier = 12

entier = int(input("Entrer un entier "))
```

On imprime le résultat :

```{code-cell} ipython3
print(f"fibonacci({entier}) = {fibonacci(entier)}")
```

### Exercice

+++

Vous pouvez donc à présent&nbsp;:

* exécuter le code dans ce notebook
* télécharger ce code sur votre disque comme un fichier `fibonacci_prompt.py`
  * utiliser pour cela le menu *"File -> Download as -> Python"*
  * et **renommer le fichier obtenu** au besoin
* l'exécuter sous IDLE
* le modifier, par exemple pour afficher les résultats intermédiaires
  * on a laissé exprès une fonction `print` en commentaire que vous pouvez réactiver simplement
* l'exécuter avec l'interpréteur Python comme ceci :

```bash
$ python3 fibonacci_prompt.py
```

+++

Ce code est volontairement simple et peu robuste pour ne pas l'alourdir. Par exemple, ce programme se comporte mal si vous entrez un entier négatif.

+++

Nous allons voir tout de suite une version légèrement différente qui va vous permettre de donner la valeur d'entrée sur la ligne de commande.
