---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
language_info:
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
nbhosting:
  title: "Pr\xE9sentation du code"
---

# Bonnes pratiques de présentation de code

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Complément - niveau basique

+++

### La PEP-008

+++

On trouve [dans la PEP-008 (en anglais)](http://legacy.python.org/dev/peps/pep-0008/) les conventions de codage qui s'appliquent à toute la librairie standard, et qui sont certainement un bon point de départ pour vous aider à trouver le style de présentation qui vous convient. 

Nous vous recommandons en particulier les sections sur

 * [l'indentation](http://legacy.python.org/dev/peps/pep-0008/#code-lay-out)
 * [les espaces](http://legacy.python.org/dev/peps/pep-0008/#whitespace-in-expressions-and-statements) 
 * [les commentaires](http://legacy.python.org/dev/peps/pep-0008/#comments)

+++

### Un peu de lecture : le module `pprint`

+++

Voici par exemple le code du module `pprint` (comme PrettyPrint) de la librairie standard qui permet d'imprimer des données. 

La fonction du module - le pretty printing - est évidemment accessoire ici, mais vous pouvez y voir illustré

 * le *docstring* pour le module: les lignes de 11 à 35,
 * les indentations, comme nous l'avons déjà mentionné sont à 4 espaces, et sans tabulation,
 * l'utilisation des espaces, notamment autour des affectations et opérateurs, des définitions de fonction, des appels de fonctions...
 * les lignes qui restent dans une largeur "raisonnable" (79 caractères)
 * vous pouvez regarder notamment la façon de couper les lignes pour respecter cette limite en largeur.

```{code-cell} ipython3
:scrolled: true

from modtools import show_module_html
import pprint
show_module_html(pprint)
```

### Espaces

+++

Comme vous pouvez le voir dans `pprint.py`, les règles principales concernant les espaces sont les suivantes.

+++

* S'agissant des **affectations** et **opérateurs**, on fera

    `x = y + z` 
    
  Et non pas
    
    ~~`x=y+z`~~
    
  Ni 
    
    ~~`x = y+z`~~
    
  Ni encore 
    
    ~~`x=y + z`~~
    
L'idée étant d'aérer de manière homogène pour faciliter la lecture.

+++

* On **déclare une fonction** comme ceci

    `def foo(x, y, z):`
    
   Et non pas comme ceci (un espace en trop avant la parenthèse ouvrante)
   
    ~~`def foo (x, y, z):`~~

   Ni surtout comme ceci (pas d'espace entre les paramètres)

    ~~`def foo (x,y,z):`~~

+++

* La même règle s'applique naturellement aux **appels de fonction**:

    `foo(x, y, z)` 
    
    et non pas
    
    ~~`foo (x,y,z)`~~ 
    
    ni
    
    ~~`def foo (x, y, z):`~~

+++

Il est important de noter qu'il s'agit ici de **règles d'usage** et non pas de règles syntaxiques; tous les exemples barrés ci-dessus sont en fait **syntaxiquement corrects**, l'interpréteur les accepterait sans souci; mais ces règles sont **très largement adoptées**, et obligatoires pour intégrer du code dans la librairie standard.

+++

### Coupures de ligne

+++

Nous allons à présent zoomer dans ce module pour voir quelques exemples de coupure de ligne. Par contraste avec ce qui précède, il s'agit cette fois surtout de **règles syntaxiques**, qui peuvent rendre un code non valide si elles ne sont pas suivies.

+++

##### Coupure de ligne sans *backslash* (\\)

```{code-cell} ipython3
show_module_html(pprint, 
                 beg="def pprint",
                 end="def pformat")
```

La fonction `pprint` (ligne ~46) est une commodité (qui crée une instance de `PrettyPrinter`, sur lequel on envoie la méthode `pprint`).

Vous voyez ici qu'il n'est **pas nécessaire** d'insérer un *backslash* (`\`) à la fin des lignes 50 et 51, car il y a une parenthèse ouvrante qui n'est pas fermée à ce stade.

De manière générale, lorsqu'une parenthèse ouvrante `(` - idem avec les crochets `[` et accolades `{` - n'est pas fermée sur la même ligne, l'interpréteur suppose qu'elle sera fermée plus loin et n'impose pas de *backslash*.

+++

Ainsi par exemple on peut écrire sans *backslash*:

```python
valeurs = [ 
   1,
   2,
   3,
   5,
   7,
]
```

Ou encore

```python
x = un_nom_de_fonction_tres_tres_long(
       argument1, argument2,
       argument3, argument4,
    )
```

+++

À titre de rappel, signalons aussi les chaînes de caractères à base de `"""` ou `'''` qui permettent elles aussi d'utiliser plusieures lignes consécutives sans *backslash*, comme :

```python
texte = """Les sanglots longs
Des violons
De l'automne"""
```

+++

##### Coupure de ligne avec *backslash* (\\)

+++

Par contre il est des cas où le backslash est nécessaire:

```{code-cell} ipython3
show_module_html(pprint, 
                 beg="components), readable, recursive", 
                 end="elif len(object) ", 
                 lineno_width=3)
```

Dans ce fragment au contraire, voyez la ligne commençant par  
`if (issubclass(typ, list)...`  
et remarquez qu'**il a fallu cette fois** insérer un *backslash* `\` comme caractère de continuation pour que l'instruction puisse se poursuivre sur la ligne suivante.

+++

##### Coupures de lignes - épilogue

+++

Dans tous les cas où une instruction est répartie sur plusieurs lignes, c'est naturellement l'indentation de **la première ligne** qui est significative pour savoir à quel bloc rattacher cette instruction.

+++

Notez bien enfin qu'on peut toujours mettre un *backslash* même lorsque ce n'est pas nécessaire, mais on évite cette pratique en règle générale car les *backslash* nuisent à la lisibilité.

+++

## Complément - niveau intermédiaire

+++

### Outils liés à PEP008

Il existe plusieurs outils liés à la PEP0008, pour vérifier si votre code est conforme, ou même le modifier pour qu'il le devienne.

Ce qui nous donne un excellent prétexte pour parler un peu de [https://pypi.python.org](https://pypi.python.org), qui est la plateforme qui distribue les logiciels disponibles via l'outil `pip3`.

Je vous signale notamment:

* [l'outil `pep8`](https://pypi.python.org/pypi/pep8/) pour vérifier, et 
* [l'outil `autopep8`](https://pypi.python.org/pypi/autopep8/) pour modifier automatiquement votre code et le rendre conforme.

+++

### Les deux-points `:`

+++

Dans un autre registre entièrement, vous pouvez [vous reporter à ce lien](https://docs.python.org/3/faq/design.html#why-are-colons-required-for-the-if-while-def-class-statements) si vous êtes intéressé par la question de savoir pourquoi on a choisi un délimiteur (le caractère deux-points `:`) pour terminer les instructions comme `if`, `for` et `def`.
