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
  title: "Installations suppl\xE9mentaires"
---

# Installations supplémentaires

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Complément - niveau basique

+++

Les outils que nous voyons cette semaine, bien que jouant un rôle majeur dans le succès de l'écosystème Python, **ne font pas** partie de la **distribution standard**. Cela signifie qu'il vous faut éventuellement procéder à des installations complémentaires sur votre ordinateur (évidemment vous pouvez utiliser les notebooks sans installation de votre part).

+++

### Comment savoir ?

+++

Pour savoir si votre installation est idoine, vous devez pouvoir faire ceci dans votre interpréteur Python (par exemple, IPython) sans erreur:

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
```

```{code-cell} ipython3
import pandas as pd
```

### Avec (ana)conda

+++

Si vous avez installé votre Python avec conda, selon toute probabilité, toutes ces bibliothèques sont déjà accessibles pour vous. Vous n'avez rien à faire de particulier pour pouvoir faire tourner les exemples du cours sur votre ordinateur.

+++

### Distribution standard

+++

Si vous avez installé Python à partir d'une distribution standard, vous pouvez utiliser `pip` comme ceci ; naturellement ceci doit être fait **dans un terminal** (sous Windows, cmd.exe avec les droits d'administrateur) et non pas dans l'interpréteur Python, ni dans IDLE :

+++

```python
$ pip3 install numpy matplotlib pandas
```

+++

### Debian/Ubuntu

+++

Si vous utilisez Debian ou Ubuntu, et que vous avez déjà installé Python avec `apt-get`, la méthode préconisée sera :

+++

```python
$ apt-get install python3-numpy python3-matplotlib python3-pandas
```

+++

### Fedora

+++

De manière similaire sur Fedora ou RHEL :

+++

```python
$ dnf install python3-numpy python3-matplotlib python3-pandas
```
