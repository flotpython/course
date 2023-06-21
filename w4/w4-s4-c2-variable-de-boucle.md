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
nbhosting:
  title: variables de boucle
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Visibilité des variables de boucle

+++

## Complément - niveau basique

+++

### Une astuce

+++

Dans ce complément, nous allons beaucoup jouer avec le fait qu'une variable soit définie ou non. Pour nous simplifier la vie, et surtout rendre les cellules plus indépendantes les unes des autres si vous devez les rejouer, nous allons utiliser la formule un peu magique suivante :

```{code-cell} ipython3
# on détruit la variable i si elle existe
if 'i' in locals(): 
    del i      
```

qui repose d'une part sur l'instruction `del` que nous avons déjà vue, et sur la fonction *built-in* `locals` que nous verrons plus tard ; cette formule a l'avantage qu'on peut l'exécuter dans n'importe quel contexte, que `i` soit définie ou non.

+++

### Une variable de boucle reste définie au-delà de la boucle

+++

Une variable de boucle est définie (assignée) dans la boucle et **reste *visible*** une fois la boucle terminée. Le plus simple est de le voir sur un exemple :

```{code-cell} ipython3
# La variable 'i' n'est pas définie
try:
    i
except NameError as e:
    print('OOPS', e)
```

```{code-cell} ipython3
# si à présent on fait une boucle
# avec i comme variable de boucle
for i in [0]:
    pass

# alors maintenant i est définie
i
```

On dit que la variable *fuite* (en anglais "*leak*"), dans ce sens qu'elle continue d'exister  au delà du bloc de la boucle à proprement parler.

+++

On peut être tenté de tirer profit de ce trait, en lisant la valeur de la variable après la boucle ; l'objet de ce complément est de vous inciter à la prudence, et d'attirer votre attention sur certains points qui peuvent être sources d'erreur.

+++

### Attention aux boucles vides

+++

Tout d'abord, il faut faire attention à ne pas écrire du code qui dépende de ce trait **si la boucle peut être vide**. En effet, si la boucle ne s'exécute pas du tout, la variable n'est **pas affectée** et donc elle n'est **pas définie**. C'est évident, mais ça peut l'être moins quand on lit du code réel, comme par exemple :

```{code-cell} ipython3
# on détruit la variable i si elle existe
if 'i' in locals(): 
    del i   
```

```{code-cell} ipython3
# une façon très scabreuse de calculer la longueur de l
def length(l):
    for i, x in enumerate(l):
        pass
    return i + 1

length([1, 2, 3])
```

Ça a l'air correct, sauf que :

```{code-cell} ipython3
:latex:skip-eval: true

# ceci provoque une UnboundLocalError
length([])
```

Ce résultat mérite une explication. Nous allons voir très bientôt l'exception `UnboundLocalError`, mais pour le moment sachez qu'elle se produit lorsqu'on a dans une fonction une variable locale et une variable globale de même nom. Alors, pourquoi l'appel `length([1, 2, 3])` retourne-t-il sans encombre, alors que pour l'appel `length([])` il y a une exception ? Cela est lié à la manière dont python détermine qu'une variable est locale. 

Une variable est locale dans une fonction si elle est assignée dans la fonction explicitement (avec une opération d'affectation) ou implicitement (par exemple avec une boucle `for` comme ici) ; nous reviendrons sur ce point un peu plus tard. Mais pour les fonctions, pour une raison d'efficacité, une variable est définie comme locale à la phase de pré-compilation, c'est-à-dire *avant* l'exécution du code. Le pré-compilateur ne peut pas savoir quel sera l'argument passé à la fonction, il peut simplement savoir qu'il y a une boucle `for` utilisant la variable `i`, il en conclut que `i` est locale pour toute la fonction. 

Lors du premier appel, on passe une liste à la fonction, liste qui est parcourue par la boucle `for`. En sortie de boucle, on a bien une variable locale `i` qui vaut 3. Lors du deuxième appel par contre, on passe une liste vide à la fonction, la boucle `for` ne peut rien parcourir, donc elle termine immédiatement. Lorsque l'on arrive à la ligne `return i + 1` de la fonction, la variable `i` n'a pas de valeur (on doit donc chercher `i` dans le module), mais `i` a été définie par le pré-compilateur comme étant locale, on a donc dans la même fonction une variable `i` locale et une référence à une variable `i` globale, ce qui provoque l'exception `UnboundLocalError`.

+++

### Comment faire alors ?

+++

##### Utiliser une autre variable

+++

La première voie consiste à déclarer une variable externe à la boucle et à l'affecter à l'intérieur de la boucle, c'est-à-dire :

```{code-cell} ipython3
# on veut chercher le premier de ces nombres qui vérifie une condition
candidates = [3, -15, 1, 8]

# pour fixer les idées disons qu'on cherche un multiple de 5, peu importe
def checks(candidate):
    return candidate % 5 == 0
```

```{code-cell} ipython3
:cell_style: split

# plutôt que de faire ceci
for item in candidates:
    if checks(item):
        break
print('trouvé solution', item)
```

```{code-cell} ipython3
:cell_style: split

# il vaut mieux faire ceci
solution = None
for item in candidates:
    if checks(item):
        solution = item
        break

print('trouvé solution', solution)
```

##### Au minimum initialiser la variable

+++

Au minimum, si vous utilisez la variable de boucle après la boucle, il est vivement conseillé de l'**initialiser** explicitement **avant** la boucle, pour vous prémunir contre les boucles vides, comme ceci :

```{code-cell} ipython3
:cell_style: split

# la fonction length de tout à l'heure
def length1(l):
    for i, x in enumerate(l):
        pass
    return i + 1
```

```{code-cell} ipython3
:cell_style: split

# une version plus robuste 
def length2(l):
    # on initialise i explicitement
    # pour le cas où l est vide
    i = -1
    for i, x in enumerate(l):
        pass
    # comme cela i est toujours déclarée
    return i + 1
```

```{code-cell} ipython3
:cell_style: split
:latex:skip-eval: true

# comme ci-dessus: UnboundLocalError
length1([])
```

```{code-cell} ipython3
:cell_style: split

length2([])
```

### Les compréhensions

+++

Notez bien que par contre, les variables de compréhension **ne fuient pas** (contrairement à ce qui se passait en Python 2) :

```{code-cell} ipython3
# on détruit la variable i si elle existe
if 'i' in locals(): 
    del i   
```

```{code-cell} ipython3
# en Python 3, les variables de compréhension ne fuitent pas
[i**2 for i in range(3)]
```

```{code-cell} ipython3
# ici i est à nouveau indéfinie
try:
    i
except NameError as e:
    print("OOPS", e)
```
