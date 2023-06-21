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
notebookname: Conditions
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Récapitulatif sur les conditions dans un `if`

+++

## Complément - niveau basique

+++

Dans ce complément nous résumons ce qu'il faut savoir pour écrire une condition dans un `if`.

+++

### Expression *vs* instruction

+++

Nous avons déjà introduit la différence entre instruction et expression, lorsque nous avons vu l'expression conditionnelle :

 * une expression est un fragment de code qui "retourne quelque chose",
 * alors qu'une instruction permet bien souvent de faire une action, mais ne retourne rien.

+++

Ainsi parmi les notions que nous avons vues jusqu'ici, nous pouvons citer dans un ordre arbitraire :

| Instructions      | &nbsp; | Expressions                     |
|------------------:|-------:|--------------------------------:|
| affectation       | &nbsp; | appel de fonction               | 
| `import`          | &nbsp; |opérateurs `is`, `in`, `==`, ... |
| instruction `if`  | &nbsp; |expression conditionnelle        |
| instruction `for` | &nbsp; | compréhension(s)                |

+++

### Toutes les expressions sont éligibles

+++

Comme condition d'une instruction `if`, on peut mettre n'importe quelle expression. On l'a déjà signalé, il n'est pas nécessaire que cette expression retourne un booléen :

```{code-cell} ipython3
# dans ce code le test 
# if n % 3:
# est équivalent à
# if n % 3 != 0:

for n in (18, 19):
    if n % 3:
        print(f"{n} non divisible par trois")
    else:
        print(f"{n} divisible par trois")
```

### Une valeur est-elle "vraie" ?

+++

Se pose dès lors la question de savoir précisément quelles valeurs sont considérées comme *vraies* par l'instruction `if`. 

Parmi les types de base, nous avons déjà eu l'occasion de l'évoquer, les valeurs *fausses* sont typiquement :

* 0 pour les valeurs numériques ;
* les objets vides pour les chaînes, listes, ensembles, dictionnaires, etc.

+++

Pour en avoir le cœur net, pensez à utiliser dans le terminal interactif la fonction `bool`. Comme pour toutes les fonctions qui portent le nom d'un type, la fonction `bool` est un constructeur qui fabrique un objet booléen. 

Si vous appelez `bool` sur un objet, la valeur de retour - qui est donc par construction une valeur booléenne - vous indique, cette fois sans ambiguïté - comment se comportera `if` avec cette entrée.

```{code-cell} ipython3
def show_bool(x):
    print(f"condition {repr(x):>10} considérée comme {bool(x)}")
```

```{code-cell} ipython3
for exp in [None, "", 'a', [], [1], (), (1, 2), {}, {'a': 1}, set(), {1}]:
    show_bool(exp)
```

### Quelques exemples d'expressions

+++

##### Référence à une variable et dérivés

```{code-cell} ipython3
:cell_style: split

a = list(range(4))
print(a)
```

```{code-cell} ipython3
:cell_style: split

if a:
    print("a n'est pas vide")
if a[0]:
    print("on ne passe pas par ici")
if a[1]:
    print("a[1] n'est pas nul")
```

##### Appels de fonction ou de méthode

```{code-cell} ipython3
chaine = "jean"
if chaine.upper():
    print("la chaine mise en majuscule n'est pas vide")
```

```{code-cell} ipython3
# on rappelle qu'une fonction qui ne fait pas 'return' retourne None
def procedure(a, b, c):
    "cette fonction ne retourne rien"
    pass

if procedure(1, 2, 3):
    print("ne passe pas ici car procedure retourne None")
else:
    print("par contre on passe ici")
```

##### Compréhensions

+++

Il découle de ce qui précède qu'on peut tout à fait mettre une compréhension comme condition, ce qui peut être utile pour savoir si au moins un élément remplit une condition, comme par exemple :

```{code-cell} ipython3
inputs = [23, 65, 24]

# y a-t-il dans inputs au moins un nombre 
# dont le carré est de la forme 10*n+5
def condition(n):
    return (n * n) % 10 == 5

if [value for value in inputs if condition(value)]:
    print("au moins une entrée convient")
```

##### Opérateurs

+++

Nous avons déjà eu l'occasion de rencontrer la plupart des opérateurs de comparaison du langage, dont voici à nouveau les principaux :

| Famille      | &nbsp; |Exemples                   |
|-------------:|-------:|--------------------------:|
| Égalité      | &nbsp; |`==`, `!=`, `is`, `is not` |
| Appartenance | &nbsp; | `in`                      |
| Comparaison  | &nbsp; | `<=`, `<`, `>`, `>=`      |
| Logiques     | &nbsp; | `and`, `or`, `not`        |

+++

## Complément - niveau intermédiaire

+++

### Remarques sur les opérateurs

+++

Voici enfin quelques remarques sur ces opérateurs

+++

##### opérateur d'égalité `==`

+++

L'opérateur `==` ne fonctionne en général (sauf pour les nombres) que sur des objets de même type ; c'est-à-dire que notamment un tuple ne sera jamais égal à une liste :

```{code-cell} ipython3
[] == ()
```

```{code-cell} ipython3
[1, 2] == (1, 2)
```

##### opérateur logiques

+++

Comme c'est le cas avec par exemple les opérateurs arithmétiques, les opérateurs logiques ont une *priorité*, qui précise le sens des phrases non parenthésées. C'est-à-dire pour être explicite, que de la même manière que

```python
12 + 4 * 8
```

est équivalent à

```python
12 + ( 4 * 8 )
```

pour les booléens il existe une règle de ce genre et

```python
a and not b or c and d
```

est équivalent à

```python
(a and (not b)) or (c and d)
```

Mais en fait, il est assez facile de s'emmêler dans ces priorités, et c'est pourquoi il est **très fortement conseillé** de parenthéser.

+++

##### opérateurs logiques (2)

+++

Remarquez aussi que les opérateurs logiques peuvent être appliqués à des valeurs qui ne sont pas booléennes :

```{code-cell} ipython3
2 and [1, 2]
```

```{code-cell} ipython3
None or "abcde"
```

Dans la logique de l'évaluation paresseuse qu'on a vue récemment, remarquez que lorsque l'évaluation d'un `and` ou d'un `or` ne peut pas être court-circuitée, le résultat est alors toujours le résultat de la dernière expression évaluée :

```{code-cell} ipython3
:cell_style: split

1 and 2 and 3
```

```{code-cell} ipython3
:cell_style: split

1 and 2 and 3 and '' and 4
```

```{code-cell} ipython3
:cell_style: split

[] or "" or {}
```

```{code-cell} ipython3
:cell_style: split

[] or "" or {} or 4 or set()
```

### Expression conditionnelle dans une instruction `if`

+++

En toute rigueur on peut aussi mettre un `<> if <> else <>` - donc une expression conditionnelle - comme condition dans une instruction `if`. Nous le signalons pour bien illustrer la logique du langage, mais cette pratique n'est bien sûr pas du tout conseillée.

```{code-cell} ipython3
# cet exemple est volontairement tiré par les cheveux 
# pour bien montrer qu'on peut mettre 
# n'importe quelle expression comme condition
a = 1

# ceci est franchement illisible
if 0 if not a else 2:
    print("une construction illisible")

# et encore pire
if 0 if a else 3 if a + 1 else 2:
    print("encore pire")
```

### Pour en savoir plus

+++

<https://docs.python.org/3/tutorial/datastructures.html#more-on-conditions>

+++

### Types définis par l'utilisateur

+++

Pour anticiper un tout petit peu, nous verrons que les classes en Python vous donnent le moyen de définir vos propres types d'objets. Nous verrons à cette occasion qu'il est possible d'indiquer à python quels sont les objets de type `MaClasse` qui doivent être considérés comme `True` ou comme `False`. 

De manière plus générale, tous les traits natifs du langage sont redéfinissables sur les classes. Nous verrons par exemple également comment donner du sens à des phrases comme


```python
mon_objet = MaClasse()
if mon_objet:
    <faire quelque chose>
```

ou encore 

```python
mon_objet = MaClasse()
for partie in mon_objet:
    <faire quelque chose sur partie>
```

Mais n'anticipons pas trop, rendez-vous en semaine 6.
