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
  title: Tri de listes (2)
---

# Tri de listes

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Complément - niveau intermédiaire

+++

Nous avons vu durant une semaine précédente comment faire le tri simple d'une liste, en utilisant éventuellement le paramètre `reverse` de la méthode `sort` sur les listes. Maintenant que nous sommes familiers avec la notion de fonction, nous pouvons approfondir ce sujet.

+++

### Cas général

+++

Dans le cas général, on est souvent amené à trier des objets selon un critère propre à l'application. Imaginons par exemple que l'on dispose d'une liste de tuples à deux éléments, dont le premier est la latitude et le second la longitude :

```{code-cell} ipython3
coordonnees = [(43, 7), (46, -7), (46, 0)]
```

Il est possible d'utiliser la méthode `sort` pour faire cela, mais il va falloir l'aider un peu plus, et lui expliquer comment comparer deux éléments de la liste.

Voyons comment on pourrait procéder pour trier par longitude :

```{code-cell} ipython3
def longitude(element): 
    return element[1]

coordonnees.sort(key=longitude)
print("coordonnées triées par longitude", coordonnees)
```

Comme on le devine, le procédé ici consiste à indiquer à `sort` comment calculer, à partir de chaque élément, une valeur numérique qui sert de base au tri. 

Pour cela on passe à la méthode `sort` un argument `key` qui désigne **une fonction**, qui lorsqu'elle est appliquée à un élément de la liste, retourne la valeur qui doit servir de base au tri : dans notre exemple, la fonction `longitude`, qui renvoie le second élément du tuple.

+++

On aurait pu utiliser de manière équivalente une fonction lambda ou la méthode `itemgetter` du module `operator`

```{code-cell} ipython3
# fonction lambda 
coordonnees = [(43, 7), (46, -7), (46, 0)]
coordonnees.sort(key=lambda x: x[1])
print("coordonnées triées par longitude", coordonnees)

# méthode operator.getitem
import operator
coordonnees = [(43, 7), (46, -7), (46, 0)]
coordonnees.sort(key=operator.itemgetter(1))
print("coordonnées triées par longitude", coordonnees)
```

### Fonction de commodité : `sorted`

+++

On a vu que `sort` réalise le tri de la liste "en place". Pour les cas où une copie est nécessaire, python fournit également une fonction de commodité, qui permet précisément de renvoyer la **copie** triée d'une liste d'entrée. Cette fonction est baptisée `sorted`, elle s'utilise par exemple comme ceci, sachant que les arguments `reverse` et `key` peuvent être mentionnés comme avec `sort` :

```{code-cell} ipython3
liste = [8, 7, 4, 3, 2, 9, 1, 5, 6]
# on peut passer à sorted les mêmes arguments que pour sort
triee = sorted(liste, reverse=True)
# nous avons maintenant deux objets distincts
print('la liste triée est une copie ', triee)
print('la liste initiale est intacte', liste)
```

Nous avons qualifié `sorted` de fonction de commodité car il est très facile de s'en passer ; en effet on aurait pu écrire à la place du fragment précédent :

```{code-cell} ipython3
liste = [8, 7, 4, 3, 2, 9, 1, 5, 6]
# ce qu'on a fait dans la cellule précédente est équivalent à
triee = liste[:]
triee.sort(reverse=True)
# 
print('la liste triée est une copie ', triee)
print('la liste initiale est intacte', liste)
```

Alors que `sort` est une fonction sur les listes, `sorted` peut trier n'importe quel itérable et retourne le résultat dans une liste. Cependant, au final, le coût mémoire est le même. Pour utiliser `sort` on va créer une liste des éléments de l'itérable, puis on fait un tri en place avec `sort`. Avec `sorted` on applique directement le tri sur l'itérable, mais on crée une liste pour stocker le résultat. Dans les deux cas, on a une liste à la fin et aucune structure de données temporaire créée.

+++

### Pour en savoir plus

+++

Pour avoir plus d'informations sur `sort` et `sorted` vous pouvez [lire cette section de la documentation python sur le tri.](https://docs.python.org/3/howto/sorting.html)
