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
  title: Classe
---

# Classe

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Exercice - niveau basique

On veut implémenter une classe pour manipuler une queue d'événements. La logique de cette classe est que :

* on la crée sans argument ;
* on peut toujours ajouter un élément avec la méthode `incoming` ;
* et tant que la queue contient des éléments on peut appeler la méthode `outgoing`, qui retourne et enlève un élément dans la queue.

Cette classe s'appelle `Fifo` pour *First In, First Out*, c'est-à-dire que les éléments retournés par `outgoing` le sont dans le même ordre où ils ont été ajoutés.

La méthode `outgoing` retourne `None` lorsqu'on l'appelle sur une pile vide.

```{code-cell} ipython3
# voici un exemple de scénario
from corrections.cls_fifo import exo_fifo
exo_fifo.example()
```

```{code-cell} ipython3
# vous pouvez définir votre classe ici
class Fifo:
    def __init__(self):
        "votre code"
    def incoming(self, value):
        "votre code"
    def outgoing(self):
        "votre code"
```

```{code-cell} ipython3
# et la vérifier ici
exo_fifo.correction(Fifo)
```
