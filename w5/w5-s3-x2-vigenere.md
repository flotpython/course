---
ipub:
  sphinx:
    toggle_input: true
    toggle_input_all: true
    toggle_output: true
    toggle_output_all: true
jupytext:
  cell_metadata_filter: all
  notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
notebookname: "Le code de Vigen\xE8re"
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Le code de Vigenère

+++

## Exercice, niveau intermédiaire

+++

Le [code ou chiffre de Vigénère](https://fr.wikipedia.org/wiki/Chiffre_de_Vigen%C3%A8re) est une méthode de chiffrement très rustique, qui est une version un peu améliorée du [chiffre de César](https://fr.wikipedia.org/wiki/Chiffrement_par_d%C3%A9calage).

Les deux méthodes fonctionnent par simple décalage dans l'alphabet modulo 26.

*Je précise tout de suite que les conventions que nous avons adoptées dans cet exercice sont légèrement différentes de celles décrites dans les deux pages wikipédia citées ci-dessus.*

+++

Dans le chiffre de **César**, on se donne une **clé** constituée d'**un seul caractère**, disons par exemple `C` (la 3-ième lettre de l'alphabet), et avec cette clé on chiffre l'alphabet par un décalage de 3, ce qui donne :

```
clé     : C    
clair   : ABCDEFGHIJKLMNOPQRSTUVWXYZ
chiffré : DEFGHIJKLMNOPQRSTUVWXYZABC
```

ou avec d'autres clés

```
clé     : L
clair   : ABCDEFGHIJKLMNOPQRSTUVWXYZ
chiffré : MNOPQRSTUVWXYZABCDEFGHIJKL
```

```
clé     : E    
clair   : ABCDEFGHIJKLMNOPQRSTUVWXYZ
chiffré : FGHIJKLMNOPQRSTUVWXYZABCDE
```

+++

La méthode de **Vigenère** consiste à choisir cette fois pour **clé** un **mot**, qui est utilisé de manière répétitive. 

Ainsi par exemple si je choisis la clé `CLE`, on va chiffrer un message en appliquant la méthode de César

* avec la clé 'C' sur le 1-er caractère, 
* avec la clé 'L' sur le 2-ème caractère, 
* avec la clé 'E' sur le 3-ème caractère, 
* avec la clé 'C' sur le 4-ème caractère, 
* avec la clé 'L' sur le 5-ème caractère, 
* ...

+++

Le but de cet exercice est d'écrire une fonction qui implémente la méthode de Vigenère pour, à partir d'une clé **connue**, coder ou décoder des messages.

+++

## Première partie : le code de César

+++

Dans un premier temps on se propose d'implémenter le code de César ; pour rester simple, nous allons nous limiter à ne chiffrer que **les caractères alphabétiques** dans la plage des caractères ASCII, c'est-à-dire sans accent, cédille ou autre.

Je rappelle par ailleurs l'existence en Python de deux fonctions qui peuvent être très utiles dans ce contexte :

* `ord()` qui projette les caractères vers les entiers (codepoints)
* et `chr()` qui réalise l'opération inverse.

```{code-cell}
:cell_style: split

# la fonction ord() retourne le codepoint
# d'un caractère
ord('a')
```

```{code-cell}
:cell_style: split

# et réciproquement avec chr()
chr(97)
```

Une fois qu'on a dit ça, il est intéressant de constater que les caractères minuscules et majuscules auxquels nous nous intéressons sont, fort heureusement, contigus dans l'espace des codepoints.

```{code-cell}
:cell_style: split

import string
string.ascii_letters
```

```{code-cell}
:cell_style: split

string.ascii_lowercase
```

```{code-cell}
COLUMNS = 7
```

```{code-cell}
:cell_style: split

for index, char in enumerate(string.ascii_uppercase, 1):
    print(f"{char}→{ord(char):3d} ", end="")
    if index % COLUMNS == 0:
        print()    
```

```{code-cell}
:cell_style: split

for index, char in enumerate(string.ascii_lowercase, 1):
    print(f"{char}→{ord(char):3d} ", end="")
    if index % COLUMNS == 0:
        print()    
```

Forts de ces observations, vous devez pouvoir à présent écrire une première fonction qui implémente le décalage de César. 

Comme par ailleurs les opérations d'encodage et de décodage sont symétriques l'une de l'autre, on choisit pour éviter d'avoir à dupliquer du code, d'écrire une fonction dont la signature est :

```python
def cesar(clear, key, encode=True):
    # retourne un caractère
```

+++

La fonction en question doit :

* laisser le texte tel quel si ce n'est pas un caractère alphabétique ASCII,
* accepter une clé qui peut être minuscule ou majuscule ; dit autrement, deux clés qui valent 'C' et 'c' produisent toutes les deux le même résultat,
* retourner une majuscule si le texte clair est en majuscule et une minuscule si le texte en clair est une minuscule.

+++

Voici ce que cela donnerait sur quelques exemples :

```{code-cell}
from corrections.exo_vigenere import exo_cesar
```

```{code-cell}
exo_cesar.example()
```

```{code-cell}
# à vous de jouer pour implémenter la fonction cesar
def cesar(clear, key, encode=True):
    pass
```

```{code-cell}
# et pour vous corriger
exo_cesar.correction(cesar)
```

## Deuxième partie : le code de Vigenère

+++

Cette première partie étant acquise, nous pouvons passer à l'amélioration de Vigenère, qui comme on l'a vu dans l'introduction consiste à prendre un mot dont on utilise les lettres successivement, et en boucle, comme clé pour la méthode de César.

Donc pour calculer le chiffrement de `ce message` avec la clé `cle`, on va se souvenir que

+++ {"cell_style": "split"}

```
clé     : C    
clair   : ABCDEFGHIJKLMNOPQRSTUVWXYZ
chiffré : DEFGHIJKLMNOPQRSTUVWXYZABC
```

```
clé     : L
clair   : ABCDEFGHIJKLMNOPQRSTUVWXYZ
chiffré : MNOPQRSTUVWXYZABCDEFGHIJKL
```

```
clé     : E    
clair   : ABCDEFGHIJKLMNOPQRSTUVWXYZ
chiffré : FGHIJKLMNOPQRSTUVWXYZABCDE
```

+++ {"cell_style": "split"}

et du coup faire

```
cesar('c', 'c') → 'f'
cesar('e', 'l') → 'q'
cesar(' ', 'e') → ' '
cesar('m', 'c') → 'p'
cesar('e', 'l') → 'q'
cesar('s', 'e') → 'x'
cesar('s', 'c') → 'v'
cesar('a', 'l') → 'm'
cesar('g', 'e') → 'l'
cesar('e', 'c') → 'h'
```

+++

Voyons cet exemple sous forme de code :

```{code-cell}
from corrections.exo_vigenere import exo_vigenere
```

```{code-cell}
exo_vigenere.example()
```

### indices

+++

* Bien entendu vous êtes invités à utiliser la fonction `cesar` pour implémenter `vigenere`.

* Par ailleurs, pour cet exercice je vous recommande d'aller voir ou revoir le module `itertools` qui contient des outils qui sont exactement adaptés à ce traitement.  
  C'est-à-dire, pour être encore plus explicite, qu'il est possible d'écrire cette fonction sans recourir à aucun indice entier sur le texte ni sur la clé.

```{code-cell}
# à vous de jouer
def vigenere(clear, key, encode=True):
    pass
```

```{code-cell}
# et pour corriger
exo_vigenere.correction(vigenere)
```
