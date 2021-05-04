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
  start_slideshow_at: selected
  theme: simple
  transition: fade
  width: 100%
notebookname: sort & reverse
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

## Exercice - niveau basique

+++

### Tri de plusieurs listes

Écrivez une fonction qui :

 * accepte en argument une liste de listes,
 * et qui retourne **la même liste**, mais avec toutes les sous-listes **triées en place**.

```{code-cell} ipython3
# voici un exemple de ce qui est attendu
from corrections.exo_multi_tri import exo_multi_tri
exo_multi_tri.example()
```

Écrivez votre code ici :

```{code-cell} ipython3
def multi_tri(listes): 
    "<votre_code>"
```

```{code-cell} ipython3
# pour vérifier votre code
exo_multi_tri.correction(multi_tri)
```

## Exercice - niveau intermédiaire

+++

### Tri de plusieurs listes, dans des directions différentes

```{code-cell} ipython3
# pour charger l'exercice
from corrections.exo_multi_tri_reverse import exo_multi_tri_reverse
```

Modifiez votre code pour qu'il accepte cette fois **deux** arguments listes que l'on suppose de tailles égales. 

Comme tout à l'heure le premier argument est une liste de listes à trier.

À présent le second argument est une liste (ou un tuple) de booléens, de même cardinal que le premier argument, et qui indiquent l'ordre dans lequel on veut trier la liste d'entrée de même rang. `True` signifie un tri descendant, `False` un tri ascendant.

Comme dans l'exercice `multi_tri`, il s'agit de modifier en place les données en entrée, et de retourner la liste de départ.

```{code-cell} ipython3
# Pour être un peu plus clair, voici à quoi on s'attend
exo_multi_tri_reverse.example()
```

À vous de jouer :

```{code-cell} ipython3
def multi_tri_reverse(listes, reverses):
    "<votre_code>"
```

```{code-cell} ipython3
# et pour vérifier votre code
exo_multi_tri_reverse.correction(multi_tri_reverse)
```

## Exercice - niveau intermédiaire

+++

### Tri de listes, avec critère personnalisé

+++

Cet exercice consiste à écrire une fonction de tri selon un critère choisi par le programmeur.

On vous passe en entrée une liste de dictionnaires qui :

* ont tous les clés `'n'` et `'p'` (pensez nom et prénom, je choisis des noms courts pour que la présentation des données soit plus compacte)
* ont parfois une clé 'p2' (deuxième prénom)

L'exercice consite à trier la liste en place, selon le critère suivant :

* on trie d'abord les gens selon leur prénom
* en cas de prénoms identiques, on trie selon les entrées concernées selon le nom
* en cas d'homonymes pour le nom et le prénom, on retient d'abord les gens qui n'ont pas de deuxième prénom, et on trie les autres selons leur deuxième prénom.

```{code-cell} ipython3
# voyons cela sur un premier exemple
from corrections.exo_tri_custom import exo_tri_custom
exo_tri_custom.example()
```

```{code-cell} ipython3
def tri_custom(liste):
    ... # votre code
    return liste
```

**Indice** on peut bien sûr utiliser `list.sort()` pour faire ce travail en quelques lignes; voyez notamment le paramètre `key`.

```{code-cell} ipython3
# pour corriger votre code
exo_tri_custom.correction(tri_custom)
```
