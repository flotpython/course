---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.1
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

<span style="float:left;">Licence CC BY-NC-ND</span><span style="float:right;">Thierry Parmentelat &amp; Arnaud Legout&nbsp;<img src="media/both-logos-small-alpha.png" style="display:inline"></span><br/>

+++ {"slideshow": {"slide_type": "slide"}}

# tâches, valeurs de retour, exceptions

+++ {"slideshow": {"slide_type": "slide"}}

# `ensure_future()`

+++ {"slideshow": {"slide_type": "-"}}

 retourne un objet `Task`
* qui connaît l'état (terminé ?)
* et le résultat de l'exécution

+++ {"slideshow": {"slide_type": "fragment"}}

[animation](loop-stacks/index.html)

+++ {"slideshow": {"slide_type": "slide"}}

# bonnes pratiques

+++ {"slideshow": {"slide_type": "fragment"}}

* attraper les exceptions
  * dans le code asynchrone

+++ {"slideshow": {"slide_type": "fragment"}}

* autrement
  * lire les exceptions (appeler `Task.exception()`)

+++ {"slideshow": {"slide_type": "slide"}}

# lire les tâches

+++

* méthode de classe `Task.all_tasks(`*loop=None*`)` 
* méthode de classe `Task.current_task(`*loop=None*`)` 

```{code-cell} ipython3
:cell_style: split

from asyncio import (
    get_event_loop, ensure_future, Task )
```

```{code-cell} ipython3
:cell_style: split

async def foo():
    pass
```

```{code-cell} ipython3
:cell_style: split

task = ensure_future(foo())
task
```

```{code-cell} ipython3
:cell_style: split

# attention : retourne un set
tasks = Task.all_tasks()
tasks
```

```{code-cell} ipython3
:cell_style: split

task in tasks
```

```{code-cell} ipython3
:cell_style: split

# et comme on n'est pas dans la  boucle
print(task.current_task())
```

+++ {"slideshow": {"slide_type": "slide"}}

# `task.cancel()`

+++

pour annuler la tâche:

* continue de donner la main à la tâche
* mais envoie une exception `CancelledError` au prochain tour

+++ {"slideshow": {"slide_type": "slide"}}

# résumé

+++ {"slideshow": {"slide_type": "fragment"}}

* une boucle = ensemble de tâches (de *futures*)

+++ {"cell_style": "split", "slideshow": {"slide_type": "fragment"}}

* une tâche
  * une pile
  * un état (terminé ?)
  * un résultat ou une exception

+++ {"cell_style": "split", "slideshow": {"slide_type": "fragment"}}

* responsabilité de l'appelant
  * de lire les résultats et exceptions
  * sinon : avertissement émis par le gc
