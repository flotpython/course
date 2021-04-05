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

# écueils classiques

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
import asyncio
```

+++ {"slideshow": {"slide_type": "slide"}}

## écueil n°1 :  fonction coroutine *vs* coroutine

```{code-cell} ipython3
:cell_style: split

# une fonction coroutine
async def foo(delay):
    await asyncio.sleep(1)
    print("foo")
```

```{code-cell} ipython3
:cell_style: split

# renvoie un objet coroutine
# si on l'appelle normalement
# il ne se passe rien
foo(4)
```

```{code-cell} ipython3
---
cell_style: split
slideshow:
  slide_type: fragment
---
# c'est exactement comme 
# une fonction génératrice
def squares(scope):
    for i in scope:
        print(i)
        yield i**2 
```

```{code-cell} ipython3
:cell_style: split

# qui retourne un
# itérateur, et là encore
# il ne se passe rien
squares(4)
```

+++ {"slideshow": {"slide_type": "slide"}}

### tous les scénarios

```{code-cell} ipython3
:cell_style: split

def synchro():
    pass
```

```{code-cell} ipython3
:cell_style: split

async def asynchro():
    pass
```

```{code-cell} ipython3
---
cell_style: split
slideshow:
  slide_type: fragment
---
def foo(): 
    synchro()        # 1 # OK
    asynchro()       # 2 # ** ATTENTION **
    await synchro()  # 3 # SyntaxError
    await asynchro   # 4 # SyntaxError
```

```{code-cell} ipython3
---
cell_style: split
slideshow:
  slide_type: fragment
---
async def afoo():
    synchro()        # 5 # OK
    await asynchro() # 6 # OK
    asynchro()       # 7 # ** ATTENTION **
    await synchro()  # 8 # ** ATTENTION **
```

+++ {"slideshow": {"slide_type": "slide"}}

### cas n°2

+++ {"cell_style": "split"}

* une fonction appelle une coroutine sans `await`
* ➠ avertissement 

```{code-cell} ipython3
:cell_style: split

!cat calls2.py
```

```{code-cell} ipython3
!python calls2.py 
```

+++ {"slideshow": {"slide_type": "slide"}}

### cas n°7

+++ {"cell_style": "split"}

* une coroutine appelle une autre coroutine sans `await`
* idem : avertissement

```{code-cell} ipython3
:cell_style: split

# avec until_complete
!cat calls7.py
```

```{code-cell} ipython3
:cell_style: center
:slideshow: {}

!python calls7.py
```

+++ {"cell_style": "center", "slideshow": {"slide_type": "slide"}}

### cas n°8

```{code-cell} ipython3
async def asynchro():
    await synchro()
```

+++ {"slideshow": {"slide_type": "-"}}

* ***peut*** être légitime - si `synchro()` retourne un awaitable

* mais en général, c'est suspect !

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
import inspect
inspect.isawaitable(synchro())
```

+++ {"slideshow": {"slide_type": "slide"}}

## écueil n°2 : code trop bloquant

```{code-cell} ipython3
---
cell_style: split
slideshow:
  slide_type: fragment
---
async def countdown(n, period):
    while n >= 0:
        print('.', end='', flush=True)
        await asyncio.sleep(period)
        n -= 1
```

```{code-cell} ipython3
:cell_style: split

import time
async def compute(n, period):
    for i in range(n):
        # on simule un calcul
        time.sleep(period)
        print('x', end='', flush=True)
```

```{code-cell} ipython3
from asynchelpers import reset_loop
reset_loop()
asyncio.get_event_loop().run_until_complete(
    asyncio.gather(countdown(10, .05), compute(10, .05)))
```

+++ {"slideshow": {"slide_type": "slide"}}

### faites respirer votre code

```{code-cell} ipython3
:cell_style: split

async def countdown(n, period):
    while n >= 0:
        print('.', end='', flush=True)
        await asyncio.sleep(period)
        n -= 1
```

```{code-cell} ipython3
:cell_style: split

import time
async def compute(n, period):
    for i in range(n):
        # on simule un calcul
        time.sleep(period)
        print('x', end='', flush=True)
        # await None n'est pas valide
        await asyncio.sleep(0)
```

```{code-cell} ipython3
reset_loop()
asyncio.get_event_loop().run_until_complete(
    asyncio.gather(countdown(10, .05), compute(10, .05)))
```

+++ {"slideshow": {"slide_type": "slide"}}

# écueil n°3 

+++ {"cell_style": "split"}

* exceptions non lues

```{code-cell} ipython3
:cell_style: split
:slideshow: {}

!cat raise.py
```

```{code-cell} ipython3
# interrompre avec ii
!python raise.py
```

+++ {"slideshow": {"slide_type": "slide"}}

# bonnes pratiques de développement

+++

* voir davantage de recettes de debug ici:
  https://docs.python.org/3/library/asyncio-dev.html

* notamment variable d'environnement `PYTHONASYNCIODEBUG`

+++ {"slideshow": {"slide_type": "slide"}}

# résumé

+++

* bien utiliser `await` avec les coroutines
* appels synchrones: oui mais brefs 
* lire les exceptions une fois la boucle terminée
* penser à activer le mode debug en cas de souci

+++ {"slideshow": {"slide_type": "slide"}}

# conclusion

+++ {"cell_style": "split"}

* (`async def` et `await`) + `asyncio`

  = une interface de programmation unifiée pour
  * les accès réseau
  * les processus externes
  * objets utilitaires asynchrones

+++ {"cell_style": "split"}

* technologie récente

  * très gros potentiel
  * évolutions à prévoir

+++ {"slideshow": {"slide_type": "slide"}}

************ Suppléments

+++ {"slideshow": {"slide_type": "slide"}}

# quel type de fonction ?

```{code-cell} ipython3
:cell_style: split
:slideshow: {}

from inspect import iscoroutinefunction
iscoroutinefunction(synchro)
```

```{code-cell} ipython3
:cell_style: split

iscoroutinefunction(asynchro)
```

+++ {"slideshow": {"slide_type": "fragment"}}

##### attention toutefois

```{code-cell} ipython3
:cell_style: split

# une vraie fonction qui renvoie un awaitable
iscoroutinefunction(asyncio.gather)
```

```{code-cell} ipython3
:cell_style: split

# ditto
iscoroutinefunction(asyncio.wait)
```
