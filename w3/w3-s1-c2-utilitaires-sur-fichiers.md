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
  title: Fichiers et utilitaires
---

# Fichiers et utilitaires

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Complément - niveau basique

+++

Outre les objets fichiers créés avec la fonction `open`, comme on l'a vu dans la vidéo, et qui servent à lire et écrire à un endroit précis, une application a besoin d'un minimum d'utilitaires pour **parcourir l'arborescence de répertoires et fichiers**, c'est notre propos dans ce complément.

+++

### Le module `os.path` (obsolète)

+++

Avant la version python-3.4, la librairie standard offrait une conjonction d'outils pour ce type de fonctionnalités:

* le module `os.path`, pour faire des calculs sur les chemins et noms de fichiers [doc](https://docs.python.org/3/library/os.path.html),
* le module `os` pour certaines fonctions complémentaires comme renommer ou détruire un fichier [doc](https://docs.python.org/3/library/os.html),
* et enfin le module `glob` pour la recherche de fichiers, par exemple pour trouver tous les fichiers en `*.txt` [doc](https://docs.python.org/3/library/glob.html).

+++

Cet ensemble un peu disparate a été remplacé par une **librairie unique `pathlib`**, qui fournit toutes ces fonctionnalités sous un interface unique et moderne, que nous **recommandons** évidemment d'utiliser pour **du nouveau code**.

Avant d'aborder `pathlib`, voici un très bref aperçu de ces trois anciens modules, pour le cas - assez probable - où vous les rencontreriez dans du code existant; tous les noms qui suivent correspondent à des **fonctions** - par opposition à `pathlib` qui, comme nous allons le voir, offre une interface orientée objet:

+++

* `os.path.join` ajoute '/' ou '\' entre deux morceaux de chemin, selon l'OS
* `os.path.basename` trouve le nom de fichier dans un chemin
* `os.path.dirname` trouve le nom du directory dans un chemin
* `os.path.abspath` calcule un chemin absolu, c'est-à-dire à partir de la racine du filesystem

+++

* `os.path.exists` pour savoir si un chemin existe ou pas (fichier ou répertoire)
* `os.path.isfile` (et `isdir`) pour savoir si un chemin est un fichier  (et un répertoire)
* `os.path.getsize` pour obtenir la taille du fichier 
* `os.path.getatime` et aussi `getmtime` et `getctime`  pour obtenir les dates de création/modification d'un fichier

+++

* `os.remove` (ou son ancien nom `os.unlink`), qui permet de supprimer un fichier
* `os.rmdir` pour supprimer un répertoire (mais qui doit être vide)
* `os.removedirs` pour supprimer tout un répertoire avec son contenu, récursivement si nécessaire
* `os.rename` pour renommer un fichier

+++

* `glob.glob` comme dans par exemple `glob.glob("*.txt")`

+++

### Le module `pathlib`

+++

C'est la méthode recommandée aujourd'hui pour travailler sur les fichiers et répertoires.

+++

##### Orienté Objet

+++

Comme on l'a mentionné `pathlib` offre une interface orientée objet; mais qu'est-ce que ça veut dire au juste ? 

Ceci nous donne un prétexte pour une première application pratique des notions de module (que nous avons introduits en fin de semaine 2) et de classe (que nous allons voir en fin de semaine).

+++

De même que le langage nous propose les types *builtin* `int` et `str`, le module `pathlib` nous expose **un type** (on dira plutôt **une classe**) qui s'appelle `Path`, que nous allons importer comme ceci:

```{code-cell} ipython3
from pathlib import Path
```

Nous allons faire tourner un petit scénario qui va créer un fichier:

```{code-cell} ipython3
# le nom de notre fichier jouet 
nom = 'fichier-temoin'
```

Pour commencer, nous allons vérifier si le fichier en question existe. 

Pour ça nous créons un **objet** qui est une **instance** de la classe `Path`, comme ceci:

```{code-cell} ipython3
# on crée un objet de la classe Path, associé au nom de fichier
path = Path(nom)
```

Vous remarquez que c'est cohérent avec par exemple:

```{code-cell} ipython3
:cell_style: center

# transformer un float en int
i = int(3.5)
```

+++ {"cell_style": "center"}

en ce sens que le type (`int` ou `Path`) se comporte comme une usine pour créer des objets du type en question.

+++

Quoi qu'il en soit, cet objet `path` offre un certain nombre de méthodes; pour les voir puisque nous sommes dans un notebook, je vous invite dans la cellule suivante à utiliser l'aide en ligne en appuyant sur la touche 'Tabulation' après avoir ajouté un `.` comme si vous alliez envoyer une méthode à cet objet

```python
path.[taper la touche TAB]
```

et le notebook vous montrera la liste des méthodes disponibles.

```{code-cell} ipython3
# ajouter un . et utilisez la touche <Tabulation>
path
```

Ainsi par exemple on peut savoir si le fichier existe avec la méthode `exists()`

```{code-cell} ipython3
# au départ le fichier n'existe pas
path.exists()
```

```{code-cell} ipython3
# si j'écris dedans je le crée
with open(nom, 'w', encoding='utf-8') as output:
    output.write('0123456789\n')
```

```{code-cell} ipython3
# et maintenant il existe
path.exists()
```

##### Métadonnées

+++

Voici quelques exemples qui montrent comment accéder aux métadonnées de ce fichier:

```{code-cell} ipython3
# cette méthode retourne (en un seul appel système) les métadonnées agrégées
path.stat()
```

Pour ceux que ça intéresse, l'objet retourné par cette méthode `stat` est un `namedtuple`, que l'on va voir très bientôt.

On accède aux différentes informations comme ceci:

```{code-cell} ipython3
# la taille du fichier en octets est de 11 
# car il faut compter un caractère "newline" en fin de ligne 
path.stat().st_size
```

```{code-cell} ipython3
# la date de dernière modification, sous forme d'un nombre
# c'est le nombre de secondes depuis le 1er Janvier 1970
mtime = path.stat().st_mtime
mtime
```

```{code-cell} ipython3
# que je peux rendre lisible comme ceci
# en anticipant sur le module datetime
from datetime import datetime
mtime_datetime = datetime.fromtimestamp(mtime)
mtime_datetime
```

```{code-cell} ipython3
# ou encore, si je formatte pour n'obtenir que
# l'heure et la minute
f"{mtime_datetime:%H:%M}"
```

##### Détruire un fichier

```{code-cell} ipython3
# je peux maintenant détruire le fichier
path.unlink()
```

```{code-cell} ipython3
# ou encore mieux, si je veux détruire 
# seulement dans le cas où il existe je peux aussi faire
try: 
    path.unlink()
except FileNotFoundError:
    print("no need to remove")
```

```{code-cell} ipython3
# et maintenant il n'existe plus
path.exists()
```

```{code-cell} ipython3
# je peux aussi retrouver le nom du fichier comme ceci
# attention ce n'est pas une méthode mais un attribut 
# c'est pourquoi il n'y a pas de parenthèses
path.name
```

##### Recherche de fichiers

+++

Maintenant je voudrais connaître la liste des fichiers de nom `*.json` dans le directory `data`. 

La méthode la plus naturelle consiste à créer une instance de `Path` associée au directory lui-même:

```{code-cell} ipython3
dirpath = Path('./data/')
```

Sur cet objet la méthode `glob` nous retourne un itérable qui contient ce qu'on veut:

```{code-cell} ipython3
# tous les fichiers *.json dans le répertoire data/
for json in dirpath.glob("*.json"):
    print(json)
```

##### Documentation complète

+++

Voyez [la documentation complète ici](https://docs.python.org/3/library/pathlib.html)

+++

## Complément - niveau avancé

+++

Pour ceux qui sont déjà familiers avec les classes, j'en profite pour vous faire remarquer le type de notre objet path

```{code-cell} ipython3
type(path)
```

qui n'est pas `Path`, mais en fait une sous-classe de `Path` qui est - sur la plateforme du MOOC au moins, qui fonctionne sous linux - un objet de type `PosixPath`, qui est une sous-classe de `Path`, comme vous pouvez le voir:

```{code-cell} ipython3
from pathlib import PosixPath
issubclass(PosixPath, Path)
```

Ce qui fait que mécaniquement, path est bien une instance de `Path`

```{code-cell} ipython3
isinstance(path, Path)
```

ce qui est heureux puisqu'on avait utilisé `Path()` pour construire l'objet `path` au départ :)
