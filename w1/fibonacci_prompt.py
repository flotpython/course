#!/usr/bin/env python
# coding: utf-8

# <style>div.title-slide {    width: 100%;    display: flex;    flex-direction: row;            /* default value; can be omitted */    flex-wrap: nowrap;              /* default value; can be omitted */    justify-content: space-between;}</style><div class="title-slide">
# <span style="float:left;">Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# <span>Inria - UCA</span>
# </div>

# # La suite de Fibonacci

# ## Complément - niveau basique

# Voici un premier exemple de code qui tourne.
#
# Nous allons commencer par le faire tourner dans ce notebook. Nous verrons en fin de séance comment le faire fonctionner localement sur votre ordinateur.

# Le but de ce programme est de calculer la [suite de Fibonacci](https://fr.wikipedia.org/wiki/Suite_de_Fibonacci), qui est définie comme ceci&nbsp;:
#
# * $u_0 = 0$
# * $u_1 = 1$
# * $\forall n >= 2, u_n = u_{n-1} + u_{n-2}$
#
# Ce qui donne pour les premières valeurs :

# | n  | fibonacci(n)  |
# |---:|--------------:|
# | 0  | 0             |
# | 1  | 1             |
# | 2  | 1             |
# | 3  | 2             |
# | 4  | 3             |
# | 5  | 5             |
# | 6  | 8             |
# | 7  | 13            |

# On commence par définir la fonction `fibonacci` comme il suit. Naturellement vous n'avez pas encore tout le bagage pour lire ce code, ne vous inquiétez pas, nous allons vous expliquer tout ça dans les prochaines semaines. Le but est uniquement de vous montrer un fonctionnement de l'interpréteur Python et de IDLE.

# In[ ]:


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


# Pour en faire un programme utilisable on va demander à l'utilisateur de rentrer un nombre&nbsp;; il faut le convertir en entier car `input` renvoie une chaîne de caractères :

# In[ ]:


entier = int(input("Entrer un entier "))


# On imprime le résultat :

# In[ ]:


print(f"fibonacci({entier}) = {fibonacci(entier)}")


# ### Exercice

# Vous pouvez donc à présent&nbsp;:
#
# * exécuter le code dans ce notebook
# * télécharger ce code sur votre disque comme un fichier `fibonacci_prompt.py`
#   * utiliser pour cela le menu *"File -> Download as -> Python"*
#   * et **renommer le fichier obtenu** au besoin
# * l'exécuter sous IDLE
# * le modifier, par exemple pour afficher les résultats intermédiaires
#   * on a laissé exprès une fonction `print` en commentaire que vous pouvez réactiver simplement
# * l'exécuter avec l'interpréteur Python comme ceci :
#
# ```bash
# $ python3 fibonacci_prompt.py
# ```

# Ce code est volontairement simple et peu robuste pour ne pas l'alourdir. Par exemple, ce programme se comporte mal si vous entrez un entier négatif.

# Nous allons voir tout de suite une version légèrement différente qui va vous permettre de donner la valeur d'entrée sur la ligne de commande.
