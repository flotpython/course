---
ipub:
  sphinx:
    toggle_input: true
    toggle_input_all: true
    toggle_output: true
    toggle_output_all: true
jupytext:
  cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
  notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
notebookname: classe Temperature
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

## exercice - niveau avancé

+++

On se propose d'écrire une classe pour représenter les températures :

* avec un constructeur qui prend exactement un paramètre nommé
  * `Temperature(kelvin=0)` 
  * aussi bien que `Temperature(celsius=0)`
  
* avec un **attribut `kelvin`** et un **attribut `celsius`** pour accéder en lecture ou en écriture à la valeur actuelle de la température, dans l'échelle choisie.
  
**Note importante**

Le système de correction automatique a besoin également que votre classe définisse son comportement vis-à-vis de `repr()` ; regardez les exemples pour voir la représentation choisie. 

Pour simplifier cet aspect de l'exercice, on a choisi d'arrondir à `0°C = 273°K`, et de ne manipuler que des valeurs entières.

```{code-cell}
from corrections.cls_temperature import exo_temperature
exo_temperature.example()
```

*****

```{code-cell}
# votre code

class Temperature:
    
    K = 273
    
    def __init__(self, kelvin=None, celsius=None):
        ...
        
    def __repr__(self):
        return f"xxx"
```

```{code-cell}
# correction
exo_temperature.correction(Temperature)
```

*****

```{code-cell}
# peut-être utile pour debugger ?
K00 = Temperature()
K0 = Temperature(kelvin=0)
```

```{code-cell}
K0 == K00 
```

```{code-cell}
C0  = Temperature(celsius=0)
C00 = Temperature(kelvin=Temperature.K)
```

```{code-cell}
C0 == C00
```

```{code-cell}
C0
```

```{code-cell}
C00
```
