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
notebookname: Le scope builtin
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Le module `builtins`

+++

## Complément - niveau avancé

+++

### Ces noms qui viennent de nulle part

+++

Nous avons vu déjà un certain nombre de **fonctions *built-in*** comme par exemple

```{code-cell} ipython3
open, len, zip
```

Ces noms font partie du **module `builtins`**. Il est cependant particulier puisque tout se passe **comme si** on avait fait avant toute chose :

```python
from builtins import *
```

sauf que cet import est implicite.

+++

### On peut réaffecter un nom *built-in*

+++

Quoique ce soit une pratique déconseillée, il est tout à fait possible de redéfinir ces noms ; on peut faire par exemple

```{code-cell} ipython3
# on réaffecte le nom open à un nouvel objet fonction
def open(encoding='utf-8', *args):
    print("ma fonction open")
    pass
```

qui est naturellement **très vivement déconseillé**. Notez, cependant, que la coloration syntaxique vous montre clairement que le nom que vous utilisez est un *built-in* (en vert dans un notebook).

+++

### On ne peut pas réaffecter un mot clé

+++

À titre de digression, rappelons que les noms prédéfinis dans le module `builtins` sont, à cet égard aussi, très différents des mots-clés comme `if`, `def`, `with` et autres `for` qui eux, ne peuvent pas être modifiés en aucune manière :

```python
>>> lambda = 1
  File "<stdin>", line 1
    lambda = 1
           ^
SyntaxError: invalid syntax
```

+++

### Retrouver un objet *built-in*

+++

Il faut éviter de redéfinir un nom prédéfini dans le module `builtins` ; un bon éditeur de texte vous signalera les fonctions *built-in* avec une coloration syntaxique spécifique. Cependant, on peut vouloir redéfinir un nom *built-in* pour changer un comportement par défaut, puis vouloir revenir au comportement original. 

Sachez que vous pouvez toujours "retrouver" alors la fonction *built-in* en l'important explicitement du module `builtins`. Par exemple, pour réaliser notre ouverture de fichier, nous pouvons toujours faire :

```{code-cell} ipython3
# nous ne pouvons pas utiliser open puisque
open()
```

```{code-cell} ipython3
# pour être sûr d'utiliser la bonne fonction open

import builtins 

with builtins.open("builtins.txt", "w", encoding="utf-8") as f:
    f.write("quelque chose")
```

Ou encore, de manière équivalente :

```{code-cell} ipython3
from builtins import open as builtins_open

with builtins_open("builtins.txt", "r", encoding="utf-8") as f:
    print(f.read())
```

### Liste des fonctions prédéfinies

+++

Vous pouvez trouver la liste des fonctions prédéfinies ou *built-in* avec la fonction `dir` sur le module `builtins` comme ci-dessous (qui vous montre aussi les exceptions prédéfinies, qui commencent par une majuscule), ou dans la documentation sur [les fonctions prédéfinies](https://docs.python.org/3/library/functions.html#built-in-funcs) :

```{code-cell} ipython3
dir(builtins)
```

Vous remarquez que les exceptions (les symboles qui commencent par des majuscules) représentent à elles seules une proportion substantielle de cet espace de noms.
