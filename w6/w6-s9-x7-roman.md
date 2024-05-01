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
nbhosting:
  title: classe Roman
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## exercice - niveau intermédiaire

+++

On se propose d'écrire une classe pour représenter les chiffres romains :

* avec un constructeur qui prend en argument :
  * soit une chaine comme `'MCMX'`
  * soit un nombre entier  
    (en général compris entre 0 et 4000, bornes exclues - voir plus bas pour les autres cas)

* et qui sait s'**additionner**, et se **soustraire** et se comparer (`==`) avec ses congénères

Pour les cas de débordement (par exemple si on ajoute 2000 et 2500), 
on choisit de représenter le résultat par 

* la valeur flottante `math.nan` (not a number)
* la représentation textuelle `'N'`

**Notes importantes**

* cet exercice va vous donner l'occasion d'observer un comportement assez étrange, en tous cas peu usuel, de `math.nan` vis à vis de la comparaison (voir cellule suivante)

* le système de correction automatique a besoin également que votre classe définisse son comportement vis-à-vis de `repr()` ; regardez les exemples pour voir la représentation choisie

```{code-cell} ipython3
:cell_style: center

# ATTENTION à ceci !!
# ce n'est pas un bug, c'est par design
# deux trucs indéfinis ne peuvent pas être égaux !

from math import nan

nan == nan
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# pour tester si quelque chose est indéfini
# utiliser cette fonction

from math import isnan

isnan(nan)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# enfin pour info (on n'en a pas besoin ici)
# les mêmes symboles sont dispos dans numpy 

import numpy as np

np.isnan(nan), isnan(np.nan)
```

```{code-cell} ipython3
from corrections.cls_roman import exo_roman
exo_roman.example()
```

*****

```{code-cell} ipython3
# votre code

class Roman:
    
    def __init__(self, letters_or_integer):
        ...
```

```{code-cell} ipython3
# correction
exo_roman.correction(Roman)
```

*****

```{code-cell} ipython3
# peut-être utile pour debugger ?
raw = """
MCMXXXIX=1939
MCMXL=1940
MCMXLI=1941
MCMXLII=1942
MCMXLIII=1943
MCMXLIV=1944
MCMXLV=1945
MCMXLVI=1946
MCMXLVII=1947
MCMXLVIII=1948
MCMXLIX=1949
MCML=1950
MCMLI=1951
MCMLII=1952
MCMLIII=1953
MCMLIV=1954
MCMLV=1955
MCMLVI=1956
MCMLVII=1957
MCMLVIII=1958
MCMLIX=1959
MCMLX=1960
MCMLXI=1961
MCMXCVIII=1998
MCMXCIX=1999
MM=2000
MMI=2001
MMII=2002
MMIII=2003
MMIV=2004
MMV=2005
MMVI=2006
MMVII=2007
MMVIII=2008
MMIX=2009
MMX=2010
MMXI=2011
MMXII=2012
MMXIII=2013
MMXIV=2014
MMXV=2015
MMXVI=2016
MMXVII=2017
MMXVIII=2018
MMXIX=2019
MMXX=2020
MMXXI=2021
MMXXII=2022
MMXXIII=2023
MMXXIV=2024
MMXXV=2025
MMXXVI=2026
MMXXVII=2027
MMXXVIII=2028"""
```

```{code-cell} ipython3
for line in raw.split():
    l, n = line.split('=')
    if Roman(l) != Roman(n):
        print(f"OOPS with {Roman(l)} != {Roman(n)}")
```
