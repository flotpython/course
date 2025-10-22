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
  title: Formats JSON et autres
---

# Formats de fichiers : JSON et autres

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Compléments - niveau basique

+++

Voici quelques mots sur des outils Python fournis dans la bibliothèque standard, et qui permettent de lire ou écrire des données dans des fichiers.

+++

### Le problème

+++

Les données dans un programme Python sont stockées en mémoire (la RAM), sous une forme propice aux calculs. Par exemple un petit entier est fréquemment stocké en binaire dans un mot de 64 bits, qui est prêt à être soumis au processeur pour faire une opération arithmétique.

+++

Ce format ne se prête pas forcément toujours à être transposé tel quel lorsqu'on doit écrire des données sur un support plus pérenne, comme un disque dur, ou encore sur un réseau pour transmission distante - ces deux supports étant à ce point de vue très voisins.

Ainsi par exemple il pourra être plus commode d'écrire notre entier sur disque, ou de le transmettre à un programme distant, sous une forme décimale qui sera plus lisible, sachant que par ailleurs toutes les machines ne codent pas un entier de la même façon.

+++

Il convient donc de faire de la traduction dans les deux sens entre représentations d'une part en mémoire, et d'autre part sur disque ou sur réseau (à nouveau, on utilise en général les mêmes formats pour ces deux usages).

+++

### Le format JSON

+++

Le format sans aucun doute le plus populaire à l'heure actuelle est [le format JSON](http://fr.wikipedia.org/wiki/JavaScript_Object_Notation) pour *JavaScript Object Notation*.

Sans trop nous attarder nous dirons que JSON est un encodage - en anglais [marshalling](http://en.wikipedia.org/wiki/Marshalling_%28computer_science%29) - qui se prête bien à la plupart des types de base que l'on trouve dans les langages modernes comme Python, Ruby ou JavaScript.

La bibliothèque standard de Python contient [le module json](https://docs.python.org/3/library/json.html) que nous illustrons très rapidement ici :

```{code-cell} ipython3
import json

# En partant d'une donnée construite à partir de types de base
data = [
    # des types qui ne posent pas de problème
    [1, 2, 'a', [3.23, 4.32], {'eric': 32, 'jean': 43}],
    # un tuple
    (1, 2, 3),
]

# sauver ceci dans un fichier
with open("s1.json","w", encoding='utf-8') as json_output:
    json.dump(data, json_output)

# et relire le résultat
with open("s1.json", encoding='utf-8') as json_input:
    data2 = json.load(json_input)
```

##### Limitations de json

+++

Certains types de base ne sont pas supportés par le format JSON (car ils ne sont pas natifs en JavaScript), c'est le cas notamment pour :

 * `tuple`, qui se fait encoder comme une liste ;
 * `complex`, `set` et `frozenset`, que l'on ne peut pas encoder du tout (sans étendre la bibliothèque).

+++

C'est ce qui explique ce qui suit :

```{code-cell} ipython3
# le premier élément de data est intact,
# comme si on avait fait une *deep copy* en fait
print("première partie de data", data[0] == data2[0])
```

```{code-cell} ipython3
# par contre le `tuple` se fait encoder comme une `list`
print("deuxième partie", "entrée", type(data[1]), "sortie", type(data2[1]))
```

Malgré ces petites limitations, ce format est de plus en plus populaire, notamment parce qu'on peut l'utiliser pour communiquer avec des applications Web écrites en JavaScript, et aussi parce qu'il est très léger, et supporté par de nombreux langages.

+++

## Compléments - niveau intermédiaire

+++

### Le format `csv`

+++

Le format `csv` pour *Comma Separated Values*, originaire du monde des tableurs, peut rendre service à l'occasion, il est proposé [dans le module `csv`](https://docs.python.org/3/library/csv.html).

+++

### Le format pickle

+++

Le format `pickle` remplit une fonctionnalité très voisine de `JSON`, mais est spécifique à Python. C'est pourquoi, malgré des limites un peu moins sévères, son usage tend à rester plutôt marginal pour l'échange de données, on lui préfère en général le format JSON.

Par contre, pour la sauvegarde locale d'objets Python (pour, par exemple, faire des points de reprises d'un programme), il est très utile. Il est implémenté [dans le module `pickle`](https://docs.python.org/3/library/pickle.html).

+++

### Le format XML

+++

Vous avez aussi très probablement entendu parler de XML, qui est un format assez populaire également.

Cela dit, la puissance, et donc le coût, de XML et JSON ne sont pas du tout comparables, XML étant beaucoup plus flexible mais au prix d'une complexité de mise en œuvre très supérieure.

Il existe plusieurs souches différentes de bibliothèques prenant en charge le format XML, [qui sont introduites ici](https://docs.python.org/3/library/xml.html).

+++

### Pour en savoir plus

+++

Voyez la page sur [les formats de fichiers](https://docs.python.org/3/library/fileformats.html) dans la documentation Python.
