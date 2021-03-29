---
jupytext:
  cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
  notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
notebookname: "Exp. g\xE9n\xE9ratrices"
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Expressions génératrices

+++

## Complément - niveau basique

+++

### Comment transformer une compréhension de liste en itérateur ?

+++

Nous venons de voir les fonctions génératrices qui sont un puissant outil pour créer facilement des itérateurs. Nous verrons prochainement comment utiliser ces fonctions génératrices pour transformer en quelques lignes de code vos propres objets en itérateurs. 

Vous savez maintenant qu'en Python on favorise la notion d'itérateurs puisqu'ils se manipulent comme des objets itérables et qu'ils sont en général beaucoup plus compacts en mémoire que l'itérable correspondant. 

Comme les compréhensions de listes sont fréquemment utilisées en Python, mais qu'elles sont des itérables potentiellement gourmands en ressources mémoire, on souhaiterait pouvoir créer un itérateur directement à partir d'une compréhension de liste. C'est possible et très facile en Python. Il suffit de remplacer les crochets par des parenthèses, regardons cela.

```{code-cell}
# c'est une compréhension de liste
comprehension = [x**2 for x in range(100) if x%17 == 0] 
print(comprehension)
```

```{code-cell}
# c'est une expression génératrice
generator = (x**2 for x in range(100) if x%17 == 0) 
print(generator)
```

Ensuite pour utiliser une expression génératrice, c'est très simple, on l'utilise comme n'importe quel itérateur.

```{code-cell}
generator is iter(generator) # generator est bien un itérateur
```

```{code-cell}
# affiche les premiers carrés des multiples de 17
for count, carre in enumerate(generator, 1):
    print(f'Contenu de generator après {count} itérations : {carre}')
```

Avec une expression génératrice on n'est plus limité comme avec les compréhensions par le nombre d'éléments :

```{code-cell}
# trop grand pour une compréhension,
# mais on peut créer le générateur sans souci
generator = (x**2 for x in range(10**18) if x%17==0) 

# on va calculer tous les carrés de multiples de 17 
# plus petits que 10**10 et dont les 4 derniers chiffres sont 1316
recherche = set()

# le point important, c'est qu'on n'a pas besoin de 
# créer une liste de 10**18 éléments 
# qui serait beaucoup trop grosse pour la mettre dans la mémoire vive

# avec un générateur, on ne paie que ce qu'on utilise...
for x in generator:
    if x > 10**10:
        break
    elif str(x)[-4:] == '1316':
        recherche.add(x)
print(recherche)
```

## Complément - niveau intermédiaire

+++

### Compréhension *vs* expression génératrice

+++

#### Digression : liste *vs* itérateur

+++

En Python 3, nous avons déjà rencontré la fonction `range` qui retourne les premiers entiers.

Ou plutôt, c'est **comme si** elle retournait les premiers entiers lorsqu'on fait une boucle `for`

```{code-cell}
# on peut parcourir un range comme si c'était une liste
for i in range(4):
    print(i)
```

mais en réalité le résultat de `range` exhibe un comportement un peu étrange, en ce sens que :

```{code-cell}
# mais en fait la fonction range ne renvoie PAS une liste (depuis Python 3)
range(4)
```

```{code-cell}
# et en effet ce n'est pas une liste
isinstance(range(4), list)
```

La raison de fond pour ceci, c'est que **le fait de construire une liste** est une opération relativement coûteuse - toutes proportions gardées - car il est nécessaire d'allouer de la mémoire pour **stocker tous les éléments** de la liste à un instant donné ; alors qu'en fait dans l'immense majorité des cas, on n'a **pas réellement besoin** de cette place mémoire, tout ce dont on a besoin c'est d'itérer sur un certain nombre de valeurs mais **qui peuvent être calculées** au fur et à mesure que l'on parcourt la liste.

+++

#### Compréhension et expression génératrice

+++

À la lumière de ce qui vient d'être dit, on peut voir qu'une compréhension n'est **pas toujours le bon choix**, car par définition elle **construit une liste** de résultats - de la fonction appliquée successivement aux entrées.

Or dans les cas où, comme pour `range`, on n'a pas réellement besoin de cette liste **en tant que telle** mais seulement de cet artefact pour pouvoir itérer sur la liste des résultats, il est préférable d'utiliser une **expression génératrice**.

Voyons tout de suite sur un exemple à quoi cela ressemblerait.

```{code-cell}
depart = (-5, -3, 0, 3, 5, 10)
# dans le premier calcul de arrivee 
# pour rappel, la compréhension est entre []
# arrivee = [x**2 for x in depart]

# on peut écrire presque la même chose avec des () à la place 
arrivee2 = (x**2 for x in depart)
arrivee2
```

Comme pour `range`, le résultat de l'expression génératrice ne se laisse pas regarder avec `print`, mais comme pour `range`, on peut itérer sur le résultat :

```{code-cell}
for x, y in zip(depart, arrivee2):
    print(f"x={x} => y={y}")
```

Il n'est pas **toujours** possible de remplacer une compréhension par une expression génératrice, mais c'est **souvent souhaitable**, car de cette façon on peut faire de substantielles économies en matière de performances. On peut le faire dès lors que l'on a seulement besoin d'itérer sur les résultats.

+++

Il faut juste un peu se méfier, car comme on parle ici d'itérateurs, comme toujours si on essaie de faire plusieurs fois une boucle sur le même itérateur, il ne se passe plus rien, car l'itérateur a été épuisé :

```{code-cell}
for x, y in zip(depart, arrivee2):
    print(f"x={x} => y={y}")
```

### Pour aller plus loin

+++

Vous pouvez regarder [cette intéressante discussion de Guido van Rossum](http://python-history.blogspot.fr/2010/06/from-list-comprehensions-to-generator.html ) sur les compréhensions et les expressions génératrices.
