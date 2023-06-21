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
  title: "Comptage dans une cha\xEEne"
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Comptage dans les chaines

+++

## Exercice - niveau basique

+++

Nous remercions Benoit Izac pour cette contribution aux exercices.

+++

## La commande UNIX wc(1)

---

Sur les systèmes de type UNIX, la commande [wc](http://pubs.opengroup.org/onlinepubs/9699919799/utilities/wc.html) permet de compter le nombre de lignes, de mots et d'octets (ou de caractères) présents sur l'entrée standard ou contenus dans un fichier.

L'exercice consiste à écrire une fonction nommée *wc* qui prendra en argument une chaîne de caractères et retournera une liste contenant trois éléments :

1. le nombre de lignes (plus précisément le nombre de retours à la ligne) ;
2. le nombre de mots (un mot étant séparé par des espaces) ;
3. le nombre de caractères (on utilisera uniquement le jeu de caractères ASCII).

```{code-cell} ipython3
# exemple
from corrections.exo_wc import exo_wc
exo_wc.example()
```

**Indice** : nous avons vu rapidement la boucle `for`, sachez toutefois qu'on peut tout à fait résoudre l'exercice en utilisant uniquement la bibliothèque standard.

**Remarque** : usuellement, ce genre de fonctions retournerait plutôt un tuple qu'une liste, mais comme nous ne voyons les tuples que la semaine prochaine..

+++

À vous de jouer :

```{code-cell} ipython3
# la fonction à implémenter
def wc(string):
    # remplacer pass par votre code
    pass
```

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
# correction
exo_wc.correction(wc)
```
