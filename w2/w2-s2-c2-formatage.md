---
ipub:
  sphinx:
    toggle_input: true
    toggle_input_all: true
    toggle_output: true
    toggle_output_all: true
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
livereveal:
  auto_select: code
  auto_select_fragment: true
  autolaunch: false
  backimage: media/nologo.png
  height: 100%
  slideNumber: c
  start_slideshow_at: selected
  theme: simple
  transition: fade
  width: 100%
nbhosting:
  title: "Formatage de cha\xEEnes"
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

# Formatage de chaînes de caractères

+++

## Complément - niveau basique

+++

On désigne par formatage les outils qui permettent d'obtenir une présentation fine des résultats, que ce soit pour améliorer la lisibilité lorsqu'on s'adresse à des humains, ou pour respecter la syntaxe d'un outil auquel on veut passer les données pour un traitement ultérieur.

+++

### La fonction `print`

+++

Nous avons jusqu'à maintenant presque toujours utilisé la fonction `print` pour afficher nos résultats. Comme on l'a vu, celle-ci réalise un formatage sommaire&nbsp;: elle insère un espace entre les valeurs qui lui sont passées.

```{code-cell} ipython3
print(1, 'a', 12 + 4j)
```

La seule subtilité notable concernant `print` est que, par défaut, elle ajoute un saut de ligne à la fin. Pour éviter ce comportement, on peut passer à la fonction un argument `end`, qui sera inséré *au lieu* du saut de ligne. Ainsi par exemple :

```{code-cell} ipython3
# une première ligne
print("une", "seule", "ligne")
```

```{code-cell} ipython3
# une deuxième ligne en deux appels à print
print("une", "autre", end=' ')
print("ligne")
```

Il faut remarquer aussi que `print` est capable d'imprimer **n'importe quel objet**. Nous l'avons déjà fait avec les listes et les tuples, voici par exemple un module :

```{code-cell} ipython3
# on peut imprimer par exemple un objet 'module'
import math

print('le module math est', math)
```

En anticipant un peu, voici comment `print` présente les instances de classe (ne vous inquiétez pas, nous apprendrons dans une semaine ultérieure ce que sont les classes et les instances).

```{code-cell} ipython3
# pour définir la classe Personne
class Personne:
    pass

# et pour créer une instance de cette classe
personne = Personne()
```

```{code-cell} ipython3
# voilà comment s'affiche une instance de classe
print(personne)
```

On rencontre assez vite les limites de `print` :

* d'une part, il peut être nécessaire de formater une chaîne de caractères sans nécessairement vouloir l'imprimer, ou en tout cas pas immédiatement ;
* d'autre part, les espaces ajoutées peuvent être plus néfastes qu'utiles ;
* enfin, on peut avoir besoin de préciser un nombre de chiffres significatifs, ou de choisir comment présenter une date.

C'est pourquoi il est plus courant de **formater** les chaînes - c'est-à-dire de calculer des chaînes en mémoire, sans nécessairement les imprimer de suite, et c'est ce que nous allons étudier dans ce complément.

+++

### Les *f-strings*

+++

Depuis la version 3.6 de Python, on peut utiliser les f-strings, le premier mécanisme de formatage que nous étudierons. C'est le mécanisme de formatage le plus simple et le plus agréable à utiliser.

Je vous recommande tout de même de lire les sections à propos de `format` et de `%`, qui sont encore massivement utilisées dans le code existant (surtout `%` d'ailleurs, bien que essentiellement obsolète).

+++

Mais définissons d'abord quelques données à afficher :

```{code-cell} ipython3
# donnons-nous quelques variables
prenom, nom, age = 'Jean', 'Dupont', 35
```

```{code-cell} ipython3
# mon premier f-string
f"{prenom} {nom} a {age} ans"
```

Vous remarquez d'abord que la chaine commence par `f"`, c'est bien sûr pour cela qu'on l'appelle un *f-string*.

On peut bien entendu ajouter le `f` devant toutes les formes de strings, qu'ils commencent par `'` ou `"` ou `'''` ou `"""`.

+++

Ensuite vous remarquez que les zones délimitées entre `{}` sont remplacées. La logique d'un *f-string*, c'est tout simplement de considérer l'intérieur d'un `{}` comme du code Python (une expression pour être précis), de l'évaluer, et d'utiliser le résultat pour remplir le `{}`.

+++

Ça veut dire, en clair, que je peux faire des calculs à l'intérieur des `{}`.

```{code-cell} ipython3
# toutes les expressions sont autorisées à l'intérieur d'un {}
f"dans 10 ans {prenom} aura {age + 10} ans"
```

```{code-cell} ipython3
# on peut donc aussi mettre des appels de fonction
notes = [12, 15, 19]
f"nous avons pour l'instant {len(notes)} notes"
```

Nous allons en rester là pour la partie en niveau basique. Il nous reste à étudier comment chaque `{}` est formaté (par exemple comment choisir le nombre de chiffres significatifs sur un flottant), ce point est expliqué plus bas.

Comme vous le voyez, les *f-strings* fournissent une méthode très simple et expressive pour formater des données dans des chaînes de caractère. Redisons-le pour être bien clair&nbsp;: un *f-string* **ne réalise pas d'impression**, il faut donc le passer à `print` si l'impression est souhaitée.

+++

### La méthode `format`

+++

Avant l'introduction des *f-strings*, la technique recommandée pour faire du formatage était d'utiliser la méthode `format` qui est définie sur les objets `str` et qui s'utilise comme ceci :

```{code-cell} ipython3
"{} {} a {} ans".format(prenom, nom, age)
```

Dans cet exemple le plus simple, les données sont affichées en lieu et place des `{}`, dans l'ordre où elles sont fournies.

+++

Cela convient bien lorsqu'on a peu de données. Si par la suite on veut changer l'ordre par exemple des nom et prénom, on peut bien sûr échanger l'ordre des arguments passés à format, ou encore utiliser la **liaison par position**, comme ceci :

```{code-cell} ipython3
"{1} {0} a {2} ans".format(prenom, nom, age)
```

Dans la pratique toutefois, cette forme est assez peu utile, on lui préfère souvent la **liaison par nom** qui se présente comme ceci :

```{code-cell} ipython3
("{le_prenom} {le_nom} a {l_age} ans"
   .format(le_nom=nom, le_prenom=prenom, l_age=age))
```

*Petite digression* : remarquez l'usage des parenthèses, qui me permettent de couper ma ligne en deux, car sinon ce code serait trop long pour la PEP8; on s'efforce toujours de ne pas dépasser 80 caractères de large, dans notre cas c'est utile notamment pour l'édition du cours au format PDF.

+++

Reprenons : dans ce premier exemple de liaison par nom, nous avons délibérément utilisé des noms différents pour les données externes et pour les noms apparaissant dans le format, pour bien illustrer comment la liaison est résolue, mais on peut aussi bien faire tout simplement :

```{code-cell} ipython3
"{prenom} {nom} a {age} ans".format(nom=nom, prenom=prenom, age=age)
```

Voici qui conclut notre courte introduction à la méthode `format`.

+++

## Complément - niveau intermédiaire

+++

### La toute première version du formatage : l'opérateur `%`

+++

`format` a été en fait introduite assez tard dans Python, pour remplacer la technique que nous allons présenter maintenant.

Étant donné le volume de code qui a été écrit avec l'opérateur `%`, il nous a semblé important d'introduire brièvement cette construction ici. Vous ne devez cependant pas utiliser cet opérateur dans du code moderne, la manière pythonique de formater les chaînes de caractères est le f-string.

+++

Le principe de l'opérateur `%` est le suivant. On élabore comme ci-dessus un "format" c'est-à-dire le patron de ce qui doit être rendu, auquel on passe des arguments pour "remplir" les trous. Voyons les exemples de tout à l'heure avec l'opérateur `%` :

```{code-cell} ipython3
# l'ancienne façon de formater les chaînes avec %
# est souvent moins lisible
"%s %s a %s ans" % (prenom, nom, age)
```

On pouvait également avec cet opérateur recourir à un mécanisme de liaison par nommage, en passant par un dictionnaire. Pour anticiper un tout petit peu sur cette notion que nous verrons très bientôt, voici comment

```{code-cell} ipython3
variables = {'le_nom': nom, 'le_prenom': prenom, 'l_age': age}
"%(le_nom)s, %(le_prenom)s, %(l_age)s ans" % variables
```

## Complément - niveau avancé

+++

De retour aux *f-strings* et à la fonction `format`, il arrive qu'on ait besoin de spécifier plus finement la façon dont une valeur doit être affichée; cela se fait en précisant un **format** à l'intérieur des `{}` comme ceci :

![f-string](media/f-string.svg)

* à gauche du `:` vous pouvez mettre **n'importe quelle expression** (opérations arithmétiques, appels de fonctions, …); bien sûr s'il n'y a pas de `:` tout ce qui est entre les `{}` constitue l'expression à évaluer;
* à droite du `:` vous pouvez préciser **un format**, nous allons en voir quelques exemples.

+++

### Précision des arrondis

+++

C'est typiquement le cas avec les valeurs flottantes pour lesquelles la précision de l'affichage vient au détriment de la lisibilité. 

Voici comment on obtient une valeur de pi arrondie :

```{code-cell} ipython3
from math import pi
```

```{code-cell} ipython3
# un f-string
f"2pi avec seulement 2 chiffres apres la virgule {2*pi:.2f}"
```

Vous remarquez que la façon de construire un *format* est la même pour les *f-strings* et pour `format`.

+++

### `0` en début de nombre

+++

Pour forcer un petit entier à s'afficher sur 4 caractères, avec des `0` ajoutés au début si nécessaire :

```{code-cell} ipython3
x = 15

f"{x:04d}"
```

Ici on utilise le format `d` (toutes ces lettres `d`, `f`, `g` viennent des formats ancestraux de la libc comme `printf`). Ici avec `04d` on précise qu'on veut une sortie sur 4 caractères et qu'il faut remplir à gauche si nécessaire avec des `0`.

+++

### Largeur fixe

+++

Dans certains cas, on a besoin d'afficher des données en colonnes de largeur fixe, on utilise pour cela les formats `<` `^` et `>` pour afficher à gauche, au centre, ou à droite d'une zone de largeur fixe :

```{code-cell} ipython3
# les données à afficher
comptes = [
 ('Apollin', 'Dupont', 127),
 ('Myrtille', 'Lamartine', 25432),
 ('Prune', 'Soc', 827465),
]

for prenom, nom, solde in comptes:
    print(f"{prenom:<10} -- {nom:^12} -- {solde:>8} €")
```

### Voir aussi

+++

Nous vous invitons à vous reporter à la documentation de `format` pour plus de détails [sur les formats disponibles](https://docs.python.org/3/library/string.html#formatstrings), et notamment aux [nombreux exemples](https://docs.python.org/3/library/string.html#format-examples) qui y figurent.
