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
  title: "It\xE9rateurs"
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Itérateurs

+++

## Complément - niveau intermédiaire

+++

Dans ce complément nous allons dire quelques mots du module `itertools` qui fournit sous forme d'itérateurs des utilitaires communs qui peuvent être très utiles. On vous rappelle que l'intérêt premier des itérateurs est de parcourir des données sans créer de structure de données temporaire, donc à coût mémoire faible et constant.

+++

### Le module `itertools`

+++

À ce stade, j'espère que vous savez trouver [la documentation du module](https://docs.python.org/3/library/itertools.html) que je vous invite à avoir sous la main.

```{code-cell} ipython3
import itertools
```

Comme vous le voyez dans la doc, les fonctionnalités de `itertools` tombent dans 3 catégories :

 * des itérateurs infinis, comme par exemple `cycle` ;
 * des itérateurs pour énumérer les combinatoires usuelles en mathématiques, comme les permutations, les combinaisons, le produit cartésien, etc. ;
 * et enfin des itérateurs correspondants à des traits que nous avons déjà rencontrés, mais implémentés sous forme d'itérateurs.
 
À nouveau, toutes ces fonctionnalités sont offertes **sous la forme d'itérateurs**.

+++

Pour détailler un tout petit peu cette dernière famille, signalons :

+++

 * `chain` qui permet de **concaténer** plusieurs itérables sous la forme d'un **itérateur** :

```{code-cell} ipython3
for x in itertools.chain((1, 2), [3, 4]):
    print(x)
```

 * `islice` qui fournit un itérateur sur un slice d'un itérable. On peut le voir comme une généralisation de `range` qui parcourt n'importe quel itérable.

```{code-cell} ipython3
import string
support = string.ascii_lowercase
print(f'support={support}')
```

```{code-cell} ipython3
# range
for x in range(3, 8):
    print(x)
```

```{code-cell} ipython3
# islice
for x in itertools.islice(support, 3, 8):
    print(x)
```
