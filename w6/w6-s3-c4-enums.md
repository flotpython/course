---
jupytext:
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
  title: "\xC9num\xE9rations"
---

# Énumérations

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Complément - niveau basique

+++

On trouve dans d'autres langages la notion de types énumérés.

+++

L'usage habituel, c'est typiquement un code d'erreur qui peut prendre certaines valeurs précises. Pensez par exemple aux [codes prévus par le protocole HTTP](https://fr.wikipedia.org/wiki/Liste_des_codes_HTTP). Le protocole prévoit un code de retour qui peut prendre un ensemble fini de valeurs, comme par exemple 200, 301, 302, 404, 500, mais pas 90 ni 110.

+++

On veut pouvoir utiliser des noms parlants dans les programmes qui gèrent ce type de valeurs, c'est une application typique des types énumérés.

+++

La bibliothèque standard offre depuis Python-3.4 un module qui s'appelle sans grande surprise `enum`, et qui expose entre autres une classe `Enum`. On l'utiliserait comme ceci, dans un cas d'usage plus simple :

```{code-cell} ipython3
from enum import Enum
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

class Flavour(Enum):
    CHOCOLATE = 1
    VANILLA = 2
    PEAR = 3
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

vanilla = Flavour.VANILLA
```

Un premier avantage est que les représentations textuelles sont plus parlantes :

```{code-cell} ipython3
:tags: [gridwidth-1-2]

str(vanilla)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

repr(vanilla)
```

Vous pouvez aussi retrouver une valeur par son nom :

```{code-cell} ipython3
:tags: [gridwidth-1-2]

chocolate = Flavour['CHOCOLATE']
chocolate
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

Flavour.CHOCOLATE
```

Et réciproquement :

```{code-cell} ipython3
chocolate.name
```

### `IntEnum`

+++

En fait, le plus souvent on préfère utiliser `IntEnum`, une sous-classe de `Enum` qui permet également de faire des comparaisons. Pour reprendre le cas des codes d'erreur HTTP :

```{code-cell} ipython3
from enum import IntEnum

class HttpError(IntEnum):

    OK = 200
    REDIRECT = 301
    REDIRECT_TMP = 302
    NOT_FOUND = 404
    INTERNAL_ERROR = 500

    # avec un IntEnum on peut faire des comparaisons
    def is_redirect(self):
        return 300 <= self.value <= 399
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

code = HttpError.REDIRECT_TMP
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

code.is_redirect()
```

### Itération

+++

Un des avantages de cette construction est qu'avec une énumération, l'objet **classe** (et non une instance) est un itérable :

```{code-cell} ipython3
class Couleur(IntEnum):
    TREFLE = 0
    CARREAU = 1
    COEUR = 2
    PIQUE = 3

    def glyph(self):
        glyphs = {
            Couleur.TREFLE: '\u2663',
            Couleur.CARREAU: '\x1b[31;1m\u2666\x1b[39;0m',
            Couleur.COEUR: '\x1b[31;1m\u2665\x1b[39;0m',
            Couleur.PIQUE: '\u2660',
        }
        return glyphs[self]
```

```{code-cell} ipython3
for couleur in Couleur:
    print(f"Couleur {couleur} -> {couleur.glyph()}")
```

### Pour en savoir plus

Consultez [la documentation officielle du module `enum`](https://docs.python.org/3/library/enum.html).
