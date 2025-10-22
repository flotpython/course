---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# tâches, valeurs de retour, exceptions

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

# `ensure_future()`

+++

 retourne un objet `Task`

* qui connaît l'état (terminé ?)
* et le résultat de l'exécution

+++

[animation](loop-stacks/index.html)

+++

# bonnes pratiques

+++

* attraper les exceptions
  * dans le code asynchrone

+++

* autrement
  * lire les exceptions (appeler `Task.exception()`)

+++

# lire les tâches

+++

* méthode de classe `Task.all_tasks(`*loop=None*`)` 
* méthode de classe `Task.current_task(`*loop=None*`)`

```{code-cell}
:cell_style: split

from asyncio import (
    get_event_loop, ensure_future, Task )
```

```{code-cell}
:cell_style: split

async def foo():
    pass
```

```{code-cell}
:cell_style: split

task = ensure_future(foo())
task
```

```{code-cell}
:cell_style: split

# attention : retourne un set
tasks = Task.all_tasks()
tasks
```

```{code-cell}
:cell_style: split

task in tasks
```

```{code-cell}
:cell_style: split

# et comme on n'est pas dans la  boucle
print(task.current_task())
```

# `task.cancel()`

+++

pour annuler la tâche:

* continue de donner la main à la tâche
* mais envoie une exception `CancelledError` au prochain tour

+++

# résumé

+++

* une boucle = ensemble de tâches (de *futures*)

+++ {"cell_style": "split"}

* une tâche
  * une pile
  * un état (terminé ?)
  * un résultat ou une exception

+++ {"cell_style": "split"}

* responsabilité de l'appelant
  * de lire les résultats et exceptions
  * sinon : avertissement émis par le gc
