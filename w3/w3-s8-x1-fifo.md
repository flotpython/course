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
notebookname: Classe
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Classe

+++

## Exercice - niveau basique

```{code-cell}
# charger l'exercice
from corrections.cls_fifo import exo_fifo
```

On veut implémenter une classe pour manipuler une queue d'événements. La logique de cette classe est que :

* on la crée sans argument ;
* on peut toujours ajouter un élément avec la méthode `incoming` ;
* et tant que la queue contient des éléments on peut appeler la méthode `outgoing`, qui retourne et enlève un élément dans la queue.

Cette classe s'appelle `Fifo` pour *First In, First Out*, c'est-à-dire que les éléments retournés par `outgoing` le sont dans le même ordre où ils ont été ajoutés.

La méthode `outgoing` retourne `None` lorsqu'on l'appelle sur une pile vide.

```{code-cell}
# voici un exemple de scénario
exo_fifo.example()
```

```{code-cell}
# vous pouvez définir votre classe ici
class Fifo:
    def __init__(self):
        "votre code"
    def incoming(self, value):
        "votre code"
    def outgoing(self):
        "votre code"
```

```{code-cell}
# et la vérifier ici
exo_fifo.correction(Fifo)
```
