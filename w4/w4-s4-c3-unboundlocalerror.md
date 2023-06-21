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
notebookname: UnboundLocalError
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# L'exception `UnboundLocalError`

+++

## Complément - niveau intermédiaire

+++

Nous résumons ici quelques cas simples de portée de variables.

+++

### Variable locale

+++

Les **arguments** attendus par la fonction sont considérés comme des variables **locales**, c'est-à-dire dans l'espace de noms de la fonction.

Pour définir une autre variable locale, il suffit de la définir (l'affecter), elle devient alors accessible en lecture :

```{code-cell} ipython3
def ma_fonction1():
    variable1 = "locale"
    print(variable1)

ma_fonction1()
```

et ceci que l'on ait ou non une variable globale de même nom

```{code-cell} ipython3
variable2 = "globale"

def ma_fonction2():
    variable2 = "locale"
    print(variable2)

ma_fonction2()
```

### Variable globale

+++

On peut accéder **en lecture**  à une variable globale sans précaution particulière :

```{code-cell} ipython3
variable3 = "globale"

def ma_fonction3():
    print(variable3)

ma_fonction3()
```

### Mais il faut choisir !

+++

Par contre on ne **peut pas** faire la chose suivante dans une fonction. On ne peut pas utiliser **d'abord** une variable comme une variable **globale**, **puis** essayer de l'affecter localement - ce qui signifie la déclarer comme une **locale** :

```{code-cell} ipython3
# cet exemple ne fonctionne pas et lève UnboundLocalError
variable4 = "globale"

def ma_fonction4():
    # on référence la variable globale
    print(variable4)
    # et maintenant on crée une variable locale
    variable4 = "locale"

# on "attrape" l'exception
try:
    ma_fonction4()
except Exception as e:
    print(f"OOPS, exception {type(e)}:\n{e}")
```

### Comment faire alors ?

+++

L'intérêt de cette erreur est d'interdire de mélanger des variables locales et globales de même nom dans une même fonction. On voit bien que ça serait vite incompréhensible. Donc une variable dans une fonction peut être **ou bien** locale si elle est affectée dans la fonction **ou bien** globale, mais **pas les deux à la fois**. Si vous avez une erreur `UnboundLocalError`, c'est qu'à un moment donné vous avez fait cette confusion.

+++

Vous vous demandez peut-être à ce stade, mais comment fait-on alors pour modifier une variable globale depuis une fonction ? Pour cela il faut utiliser l'instruction `global` comme ceci :

```{code-cell} ipython3
# Pour résoudre ce conflit il faut explicitement
# déclarer la variable  comme globale
variable5 = "globale"

def ma_fonction5():
    global variable5
    # on référence la variable globale
    print("dans la fonction", variable5)
    # cette fois on modifie la variable globale
    variable5 = "changée localement"

ma_fonction5()
print("après la fonction", variable5)
```

Nous reviendrons plus longuement sur l'instruction `global` dans la prochaine vidéo.

+++

### Bonnes pratiques

+++

Cela étant dit, l'utilisation de variables globales est généralement considérée comme une mauvaise pratique. 

Le fait d'utiliser une variable globale en *lecture seule* peut rester acceptable, lorsqu'il s'agit de matérialiser une constante qu'il est facile de changer. Mais dans une application aboutie, ces constantes elles-mêmes peuvent être modifiées par l'utilisateur via un système de configuration, donc on préférera passer en argument un objet *config*.

Et dans les cas où votre code doit recourir à l'utilisation de l'instruction `global`, c'est très probablement que quelque chose peut être amélioré au niveau de la conception de votre code.

Il est recommandé, au contraire, de passer en argument à une fonction tout le contexte dont elle a besoin pour travailler ; et à l'inverse d'utiliser le résultat d'une fonction plutôt que de modifier une variable globale.
