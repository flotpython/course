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
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
language_info:
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
nbhosting:
  title: Conditions
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Conditions & Expressions Booléennes

+++

## Complément - niveau basique

+++

Nous présentons rapidement dans ce notebook comment construire la condition qui contrôle l'exécution d'un `if`.

+++

### Tests considérés comme vrai

+++

Lorsqu'on écrit une instruction comme

```python
if <expression>:
   <do_something>
```

le résultat de l'expression peut **ne pas être un booléen**. 

Par exemple, pour n'importe quel type numérique, la valeur 0 est considérée comme fausse. Cela signifie que :

```{code-cell} ipython3
# ici la condition s'évalue à 0, donc on ne fait rien
if 3 - 3:
    print("ne passera pas par là")
```

```{code-cell} ipython3
# par contre si vous vous souvenez de notre cours sur les flottants
# ici la condition donne un tout petit réel mais pas 0.
if 0.1 + 0.2 - 0.3:
    print("par contre on passe ici")
```

De même, une chaîne vide, une liste vide, un tuple vide, sont considérés comme faux. Bref, vous voyez l'idée générale.

```{code-cell} ipython3
:tags: [gridwidth-1-2]

if "": 
    print("ne passera pas par là")
if []: 
    print("ne passera pas par là")
if ():
    print("ne passera pas par là")
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# assez logiquement, None aussi
# est considéré comme faux
if None:
    print("ne passe toujours pas par ici")
```

### Égalité

+++

Les tests les plus simples se font à l'aide des opérateurs d'égalité, qui fonctionnent sur presque tous les objets. L'opérateur `==` vérifie si deux objets ont la même valeur :

```{code-cell} ipython3
:tags: [gridwidth-1-2]

bas = 12
haut = 25.82

# égalité ?
if bas == haut:
    print('==')
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# non égalité ?
if bas != haut:
    print('!=')
```

+++ {"cell_style": "center"}

En général, deux objets de types différents ne peuvent pas être égaux.

```{code-cell} ipython3
# ces deux objets se ressemblent 
# mais ils ne sont pas du même type !
if [1, 2] != (1, 2):
    print('!=')
```

Par contre, des `float`, des `int` et des `complex` peuvent être égaux entre eux :

```{code-cell} ipython3
:tags: [gridwidth-1-2]

bas_reel = 12.
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

print(bas, bas_reel)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# le réel 12 et 
# l'entier 12 sont égaux
if bas == bas_reel:
    print('int == float')
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# ditto pour int et complex
if (12 + 0j) == 12:
    print('int == complex')
```

Signalons à titre un peu anecdotique une syntaxe ancienne : historiquement et **seulement en Python 2** on pouvait aussi noter `<>` le test de non égalité. On trouve ceci dans du code ancien mais il faut éviter de l'utiliser :

+++

```python
# l'ancienne forme de != en python2 s'écrivait
if 12 <> 25:
    print("<> est obsolete et ne fonctionne qu'en python2")
```

+++

### Les opérateurs de comparaison

+++

Sans grande surprise on peut aussi écrire

```{code-cell} ipython3
:tags: [gridwidth-1-2]

if bas <= haut:
    print('<=')
if bas < haut:
    print('<')
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

if haut >= bas:
    print('>=')
if haut > bas:
    print('>')
```

À titre de curiosité, on peut même écrire en un seul test une appartenance à un intervalle, ce qui donne un code plus lisible

```{code-cell} ipython3
:tags: [gridwidth-1-2]

x = (bas + haut) / 2
print(x)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# deux tests en une expression
if bas <= x <= haut:
    print("dans l'intervalle")
```

On peut utiliser les comparaisons sur une palette assez large de types, comme par exemple avec les listes

```{code-cell} ipython3
# on peut comparer deux listes, mais ATTENTION
[1, 2] <= [2, 3]
```

Il est parfois utile de vérifier le sens qui est donné à ces opérateurs selon le type ; ainsi par exemple sur les ensembles ils se réfèrent à l'**inclusion**.

Il faut aussi se méfier avec les types numériques, si un complexe est impliqué, comme dans l'exemple suivant :

```{code-cell} ipython3
# on ne peut pas par contre comparer deux nombres complexes
try:
    2j <= 3j
except Exception as e:
    print("OOPS", type(e), e)
```

### Connecteurs logiques et / ou / non

+++

On peut bien sûr combiner facilement plusieurs expressions entre elles, grâce aux opérateurs `and`, `or` et `not`

```{code-cell} ipython3
# il ne faut pas faire ceci, mettez des parenthèses
if 12 <= 25. or [1, 2] <= [2, 3] and not 12 <= 32:
    print("OK mais pourrait être mieux")
```

En matière de priorités : le plus simple si vous avez une expression compliquée reste de mettre les parenthèses qui rendent son évaluation claire et lisible pour tous. Aussi on préfèrera de beaucoup la formulation équivalente :

```{code-cell} ipython3
# c'est mieux avec un parenthésage
if 12 <= 25. or ([1, 2] <= [2, 3] and not 12 <= 32):
    print("OK, c'est équivalent et plus clair")
```

```{code-cell} ipython3
# attention, si on fait un autre parenthésage, on change le sens
if (12 <= 25. or [1, 2] <= [2, 3]) and not 12 <= 32 :
    print("ce n'est pas équivalent, ne passera pas par là")
```

### Pour en savoir plus

+++

Reportez-vous à la section sur les [opérateurs booléens](https://docs.python.org/3/library/stdtypes.html#truth-value-testing) dans la documentation python.
