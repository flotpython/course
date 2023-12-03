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
  title: "S\xE9quences"
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Séquences

+++

## Exercice - niveau basique

+++

### Slicing

+++

Commençons par créer une chaîne de caractères. Ne vous inquiétez pas si vous ne comprenez pas encore le code d'initialisation utilisé ci-dessous.

Pour les plus curieux, l'instruction `import`  permet de charger dans votre programme une boîte à outils que l'on appelle un module. Python vient avec de nombreux modules qui forment la bibliothèque standard. Le plus difficile avec les modules de la bibliothèque standard est de savoir qu'ils existent. En effet, il y en a un grand nombre et bien souvent il existe un module pour faire ce que vous souhaitez.

Ici en particulier nous utilisons le module `string`.

```{code-cell} ipython3
# nous allons tirer profit ici d'une 
# constante définie dans le module string
import string
chaine = string.ascii_lowercase

# et voici sa valeur
print(chaine)
```

Pour chacune des sous-chaînes ci-dessous, écrire une expression de slicing sur `chaine` qui renvoie la sous-chaîne. La cellule de code doit retourner `True`.

+++

Par exemple, pour obtenir "def" :

```{code-cell} ipython3
chaine[3:6] == "def"
```

1) Écrivez une slice pour obtenir "vwx" (n'hésitez pas à utiliser les indices négatifs) :

```{code-cell} ipython3
:latex-skip-eval: true

chaine[ <votre_code> ] == "vwx"
```

2) Une slice pour obtenir "wxyz" (avec une seule constante) :

```{code-cell} ipython3
:latex-skip-eval: true

chaine[ <votre_code> ] == "wxyz"
```

3) Une slice pour obtenir "dfhjlnprtvxz" (avec deux constantes) :

```{code-cell} ipython3
:latex-skip-eval: true

chaine[ <votre_code> ] == "dfhjlnprtvxz"
```

4) Une slice pour obtenir "xurolifc" (avec deux constantes) :

```{code-cell} ipython3
:latex-skip-eval: true

chaine[ <votre_code> ] == "xurolifc"
```

## Exercice - niveau intermédiaire

+++

### Longueur

```{code-cell} ipython3
# il vous faut évaluer cette cellule magique
# pour charger l'exercice qui suit
# et autoévaluer votre réponse
from corrections.exo_inconnue import exo_inconnue
```

On vous donne une chaîne `composite` dont on sait qu'elle a été calculée à partir de deux chaînes `inconnue` et `connue` comme ceci :
```python
composite = connue + inconnue + connue
```

+++

On vous donne également la chaîne `connue`. Imaginez par exemple que vous avez (ce ne sont pas les vraies valeurs) :
```python
connue = '0bf1'
composite = '0bf1a9730e150bf1'
```
alors, dans ce cas :
```python
inconnue = 'a9730e15'
```

+++

L'exercice consiste à écrire une fonction qui retourne la valeur de `inconnue` à partir de celles de `composite` et `connue`. Vous pouvez admettre que `connue` n'est pas vide, c'est-à-dire qu'elle contient au moins un caractère.

+++

Vous pouvez utiliser du *slicing*, et la fonction `len()`, qui retourne la longueur d'une chaîne :

```{code-cell} ipython3
len('abcd')
```

```{code-cell} ipython3
# à vous de jouer
def inconnue(composite, connue):
    "votre code"
```

Une fois votre code évalué, vous pouvez évaluer la cellule suivante pour vérifier votre résultat.

```{code-cell} ipython3
:latex-skip-eval: true

# correction
exo_inconnue.correction(inconnue)
```

Lorsque vous évaluez cette cellule, la correction vous montre :

* dans la première colonne l'appel qui est fait à votre fonction ;
* dans la seconde colonne la valeur attendue pour `inconnue` ;
* dans la troisième colonne ce que votre code a réellement calculé.

Si toutes les lignes sont **en vert** c'est que vous avez réussi cet exercice.

+++

Vous pouvez essayer autant de fois que vous voulez, mais il vous faut alors à chaque itération :

* évaluer votre cellule-réponse (là où vous définissez la fonction `inconnue`) ;
* et ensuite évaluer la cellule correction pour la mettre à jour.
