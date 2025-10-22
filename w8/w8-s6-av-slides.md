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

# boucle d'événements `asyncio`

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

```{code-cell}
import asyncio
```

# utilitaire

+++

fonctions synchrones (traditionnelles)

```{code-cell}
from asynchelpers import start_timer, show_timer
```

```{code-cell}
:cell_style: center

import time

start_timer()
time.sleep(1)
show_timer('un message')
```

# déjà vu

+++ {"cell_style": "split"}

`loop.run_until_complete()`

* exactement un argument

+++ {"cell_style": "split"}

```
asyncio.get_event_loop().run_until_complete(
    asyncio.gather(coro1, coro2, ...)
))
```

+++ {"cell_style": "center"}

# ajout de traitements

+++ {"cell_style": "split"}

`asyncio.ensure_future(coro)`

* exactement un argument
* ajoute une coroutine dans la boucle
* **avant** ou **après** le lancement de la boucle

+++ {"cell_style": "split"}

`loop.run_forever()`

* sans argument
* travaille sur le contenu courant de la boucle
* suppose l'utilisation de `ensure_future()`

+++

# *fork*

+++

![figure fork](w8-s6-av-fig1.png)

```{code-cell}
:cell_style: split

async def c1():
    show_timer(">>> c1")
    await asyncio.sleep(1)
    show_timer("forking")
    # fork
    asyncio.ensure_future(c2())
    await asyncio.sleep(1)
    show_timer("<<< c1")
```

```{code-cell}
:cell_style: split

# sera forkée par c1() après une seconde

async def c2():
    show_timer(">>> c2")
    await asyncio.sleep(2)
    show_timer("<<< c2")
    
    
```

```{code-cell}
:cell_style: split

asyncio.ensure_future(c1())
```

```{code-cell}
:cell_style: split

start_timer()

# interrompre après 2s
try:
    asyncio.get_event_loop().run_forever()
except KeyboardInterrupt:
    print("bye")
```

# réinitialisation de la boucle

```{code-cell}
asyncio.set_event_loop(asyncio.new_event_loop())
```

*je vous demande de l'admettre pour l'instant*

+++

# `loop.stop()`

```{code-cell}
:cell_style: split

async def c1_stop():
    show_timer(">>> c1")
    await asyncio.sleep(1)
    show_timer("forking")
    # fork
    asyncio.ensure_future(c2_stop())
    await asyncio.sleep(1)
    show_timer("<<< c1")
```

```{code-cell}
:cell_style: split

# sera forkée par c1() après une seconde

async def c2_stop():
    show_timer(">>> c2")
    await asyncio.sleep(2)
    show_timer("<<< c2")
    # attention c'est une méthode bloquante
    asyncio.get_event_loop().stop()
```

```{code-cell}
:cell_style: split

asyncio.ensure_future(c1_stop())
```

```{code-cell}
:cell_style: split

start_timer()

# s'arrête tout seul
try:
    asyncio.get_event_loop().run_forever()
except KeyboardInterrupt:
    print("bye")
    
print("done")
```

# `run_until_complete` sur une boucle non-vide

```{code-cell}
asyncio.set_event_loop(asyncio.new_event_loop())
```

```{code-cell}
:cell_style: center

# on simule un job asynchrone de durée duration
async def job(name, duration):
    show_timer(f">>> {name}")
    await asyncio.sleep(duration)
    show_timer(f"<<< {name}")    
```

```{code-cell}
:cell_style: split

async def short():
    await job("short", 1)
```

```{code-cell}
:cell_style: split

async def long():
    await job("long", 2)
```

```{code-cell}
# on remplit la boucle
asyncio.ensure_future(long())
```

```{code-cell}
:cell_style: split

# et on appelle run_until_complete
start_timer()

asyncio.get_event_loop().run_until_complete(short())
print("done")
```

```{code-cell}
:cell_style: split

# il reste des choses à faire dans la boucle
start_timer()

# interrompre après 1s
try:
    asyncio.get_event_loop().run_forever()
except KeyboardInterrupt:
    print("bye")
```

# `run_until_complete` vs `run_forever`

+++ {"cell_style": "center"}

* `run_until_complete`

   * prend exactement un argument
   * retourne la valeur
   * insérer un fragment asynchrone au milieu d'un code synchrone

+++

* `run_forever`
  * ne prend pas d'argument
  * ne retourne pas (sauf en cas de `stop()`)
  * orienté traitement massivement asynchrone

+++

# `get_event_loop()`

+++

* modèle mental
  * 1 thread = 1 boucle

+++

* `get_event_loop()` 
  * boucle par défaut du thread courant
  * utile pour référencer "la bonne boucle" - voir e.g. le code de `c2_stop()`
  * inutile de passer une instance de boucle
  * ne *crée pas* de boucle en dehors du thread principal

+++

# `new_event_loop()` et `set_event_loop()`

+++ {"cell_style": "split"}

* `new_event_loop()`
  * crée une nouvelle boucle
  * nécessaire dans un thread supplémentaire

+++ {"cell_style": "split"}

* set_event_loop(loop)
  * installe cet objet comme boucle par défaut

+++

# résumé

+++

* `ensure_future()`

+++

* `run_until_complete()` et `run_forever()`

+++

* `get_event_loop()` 
  * accéde à la boucle (du thread) courant(e)
  * `new_event_loop()` et `set_event_loop()`

+++

* `loop.stop()`
