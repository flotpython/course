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
  title: Valeurs de retour
---

# Fonctions avec ou sans valeur de retour

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Complément - niveau basique

+++

### Le style procédural

+++

Une procédure est une fonction qui se contente de dérouler des instructions. Voici un exemple d'une telle fonction :

```{code-cell} ipython3
def affiche_carre(n):
    print("le carre de", n, "vaut", n*n)
```

qui s'utiliserait comme ceci :

```{code-cell} ipython3
affiche_carre(12)
```

### Le style fonctionnel

+++

Mais en fait, dans notre cas, il serait beaucoup plus commode de définir une fonction qui **retourne** le carré d'un nombre, afin de pouvoir écrire quelque chose comme :

+++

```python
surface = carre(15)
```

+++

quitte à imprimer cette valeur ensuite si nécessaire. Jusqu'ici nous avons fait beaucoup appel à `print`, mais dans la pratique, imprimer n'est pas un but en soi.

+++

### L'instruction `return`

+++

Voici comment on pourrait écrire une fonction `carre` qui **retourne** (on dit aussi **renvoie**) le carré de son argument :

```{code-cell} ipython3
def carre(n):
    return n*n

if carre(8) <= 100:
    print('petit appartement')
```

La sémantique (le mot savant pour "comportement") de l'instruction `return` est assez simple. La fonction qui est en cours d'exécution **s'achève** immédiatement, et l'objet cité dans l'instruction `return` est retourné à l'appelant, qui peut utiliser cette valeur comme n'importe quelle expression.

+++

### Le singleton `None`

+++

Le terme même de fonction, si vous vous rappelez vos souvenirs de mathématiques, suggère qu'on calcule un résultat à partir de valeurs d'entrée. Dans la pratique il est assez rare qu'on définisse une fonction qui ne retourne rien.

+++

En fait **toutes** les fonctions retournent quelque chose. Lorsque le programmeur n'a pas prévu d'instruction `return`, Python retourne un objet spécial, baptisé `None`. Voici par exemple ce qu'on obtient si on essaie d'afficher la valeur de retour de notre première fonction, qui, on le rappelle, ne retourne rien :

```{code-cell} ipython3
# ce premier appel provoque l'impression d'une ligne
retour = affiche_carre(15)
```

```{code-cell} ipython3
# voyons ce qu'a retourné la fonction affiche_carre
print('retour =', retour)
```

L'objet `None` est un singleton prédéfini par Python, un peu comme `True` et `False`. Ce n'est pas par contre une valeur booléenne, nous aurons l'occasion d'en reparler.

+++

### Un exemple un peu plus réaliste

+++

Pour illustrer l'utilisation de `return` sur un exemple plus utile, voyons le code suivant :

```{code-cell} ipython3
def premier(n):
    """
    Retourne un booléen selon que n est premier ou non
    Retourne None pour les entrées négatives ou nulles
    """
    # retourne None pour les entrées non valides
    if n <= 0:
        return
    # traiter le cas singulier
    # NB: elif est un raccourci pour else if
    # c'est utile pour éviter une indentation excessive
    elif n == 1:
        return False
    # chercher un diviseur dans [2..n-1]
    # bien sûr on pourrait s'arrêter à la racine carrée de n
    # mais ce n'est pas notre sujet
    else:
        for i in range(2, n):
            if n % i == 0:
                # on a trouvé un diviseur,
                # on peut sortir de la fonction
                return False
    # à ce stade, le nombre est bien premier
    return True
```

Cette fonction teste si un entier est premier ou non ; il s'agit naturellement d'une version d'école, il existe  d'autres méthodes beaucoup plus adaptées à cette tâche. On peut toutefois vérifier que cette version est fonctionnelle pour de petits entiers comme suit. On rappelle que `1` n'est pas considéré comme un nombre premier :

```{code-cell} ipython3
for test in [-2, 1, 2, 4, 19, 35]:
    print(f"premier({test:2d}) = {premier(test)}")
```

##### `return` sans valeur

+++

Pour les besoins de cette discussion, nous avons choisi de retourner `None` pour les entiers négatifs ou nuls, une manière comme une autre de signaler que la valeur en entrée n'est pas valide.

Ceci n'est pas forcément une bonne pratique, mais elle nous permet ici d'illustrer que dans le cas où on ne mentionne pas de valeur de retour, Python retourne `None`.

+++

##### `return` interrompt la fonction

+++

Comme on peut s'en convaincre en instrumentant le code - ce que vous pouvez faire à titre d'exercice en ajoutant des fonctions `print` - dans le cas d'un nombre qui n'est pas premier la boucle `for` ne va pas jusqu'à son terme.

+++

On aurait pu d'ailleurs tirer profit de cette propriété pour écrire la fonction de manière légèrement différente comme ceci :

```{code-cell} ipython3
def premier_sans_else(n):
    """
    Retourne un booléen selon que n est premier ou non
    Retourne None pour les entrées négatives ou nulles
    """
    # retourne None pour les entrées non valides
    if n <= 0:
        return
    # traiter le cas singulier
    if n == 1:
        return False
    # par rapport à la première version, on a supprimé
    # la clause else: qui est inutile
    for i in range(2, n):
        if n % i == 0:
            # on a trouve un diviseur
            return False
    # a ce stade c'est que le nombre est bien premier
    return True
```

C'est une question de style et de goût. En tout cas, les deux versions sont tout à fait équivalentes, comme on le voit ici :

```{code-cell} ipython3
for test in [-2, 2, 4, 19, 35]:
    print(f"pour n = {test:2d} : premier → {premier(test)}\n"
          f"    premier_sans_else → {premier_sans_else(test)}\n")
```

##### Digression sur les chaînes

+++

Vous remarquerez dans cette dernière cellule, si vous regardez bien le paramètre de `print`,  qu'on peut accoler deux chaînes (ici deux *f-strings*) sans même les ajouter ; un petit détail pour éviter d'alourdir le code :

```{code-cell} ipython3
# quand deux chaînes apparaissent immédiatement
# l'une après l'autre sans opérateur, elles sont concaténées
"abc" "def"
```
