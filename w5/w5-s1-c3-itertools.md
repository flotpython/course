---
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

```{code-cell}
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

```{code-cell}
for x in itertools.chain((1, 2), [3, 4]):
    print(x)
```

 * `islice` qui fournit un itérateur sur un slice d'un itérable. On peut le voir comme une généralisation de `range` qui parcourt n'importe quel itérable.

```{code-cell}
import string
support = string.ascii_lowercase
print(f'support={support}')
```

```{code-cell}
# range
for x in range(3, 8):
    print(x)
```

```{code-cell}
# islice
for x in itertools.islice(support, 3, 8):
    print(x)
```
