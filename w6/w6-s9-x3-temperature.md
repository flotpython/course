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
  title: classe Temperature
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
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

```{code-cell} ipython3
from corrections.cls_temperature import exo_temperature
exo_temperature.example()
```

*****

```{code-cell} ipython3
# votre code

class Temperature:
    
    K = 273
    
    def __init__(self, kelvin=None, celsius=None):
        ...
        
    def __repr__(self):
        return f"xxx"
```

```{code-cell} ipython3
# correction
exo_temperature.correction(Temperature)
```

*****

```{code-cell} ipython3
# peut-être utile pour debugger ?
K00 = Temperature()
K0 = Temperature(kelvin=0)
```

```{code-cell} ipython3
K0 == K00 
```

```{code-cell} ipython3
C0  = Temperature(celsius=0)
C00 = Temperature(kelvin=Temperature.K)
```

```{code-cell} ipython3
C0 == C00
```

```{code-cell} ipython3
C0
```

```{code-cell} ipython3
C00
```
