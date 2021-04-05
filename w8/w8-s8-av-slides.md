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

# la librairie `asyncio`

+++ {"slideshow": {"slide_type": "fragment"}}

* boucle d'événements

+++ {"slideshow": {"slide_type": "fragment"}}

* synchronisation: `Queue`, `Lock` et `Semaphore`

+++ {"slideshow": {"slide_type": "fragment"}}

* interaction avec les processus:
  * package `asyncio.subprocess`

+++ {"slideshow": {"slide_type": "fragment"}}

* `Transport` et `Protocol` 
* `Streams`

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
import asyncio

from asynchelpers import start_timer, show_timer
```

+++ {"slideshow": {"slide_type": "slide"}}

# synchronisation avec une queue

```{code-cell} ipython3
:cell_style: split

asyncio.Queue?
```

```{code-cell} ipython3
:cell_style: split
:slideshow: {}

queue = asyncio.Queue(maxsize=1)
```

```{code-cell} ipython3
---
cell_style: split
slideshow:
  slide_type: fragment
---
async def producer(queue):
    count = 1
    while True:
        await queue.put(f'tick{count}')
        count += 1
        await asyncio.sleep(1)
```

```{code-cell} ipython3
---
cell_style: split
slideshow:
  slide_type: fragment
---
async def consumer(queue):
    while True:
        received = await queue.get()
        show_timer(f"got {received}")
        
```

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
# on ajoute les coroutines dans la boucle
asyncio.ensure_future(producer(queue))
asyncio.ensure_future(consumer(queue))
```

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
start_timer()

# interrompre avec la touche 'i' 
# plusieurs fois si nécessaire

try:
    asyncio.get_event_loop().run_forever()
except KeyboardInterrupt as e:
    print("bye")
```

+++ {"slideshow": {"slide_type": "slide"}}

# limiter le parallèlisme avec `Queue`

```{code-cell} ipython3
---
cell_style: split
slideshow:
  slide_type: fragment
---
asyncio.set_event_loop(asyncio.new_event_loop())
```

```{code-cell} ipython3
:cell_style: split

window = asyncio.Queue(maxsize = 4)
```

```{code-cell} ipython3
async def job(i):
    # prendre un jeton dans la queue
    await window.put(None)
    # pas tout le monde la même durée
    duration = (i % 3) + 1
    message = f"job{i} - duration {duration}"
    show_timer(">>>", message)
    await asyncio.sleep(duration)
    show_timer("<<<", message)
    # libérer le jeton
    await window.get()
```

```{code-cell} ipython3
---
cell_style: split
slideshow:
  slide_type: slide
---
for i in range(8):
    asyncio.ensure_future(job(i))

start_timer()
try:
    asyncio.get_event_loop().run_forever()
except:
    print('bye')
```

+++ {"cell_style": "split", "slideshow": {"slide_type": "-"}}

### Séquencement des jobs

|     | j0 (1) | j1(2) | j2(3) | j3(1) | j4(2) | j5(3) | j6(1) | j7(2) |
|:---:|:------:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| 0-1 | `*`    | `*`   | `*`   | `*`   |       |       |       |       |
| 1-2 |        | `*`   | `*`   |       | `*`   | `*`   |       |       |
| 2-3 |        |       | `*`   |       | `*`   | `*`   | `*`   |       |
| 3-4 |        |       |       |       |       | `*`   |       | `*`   |
| 4-5 |        |       |       |       |       |       |       | `*`   |

+++ {"slideshow": {"slide_type": "slide"}}

# valeur ajoutée

+++ {"cell_style": "split"}

* boucle d'événements complice avec:
  * `sleep()`,
  * `subprocess.*`
  * les classes abstraites:
  
    `Transport`, `Protocol`, `Stream`

+++ {"cell_style": "split", "slideshow": {"slide_type": "fragment"}}

* tire profit de l'OS
  * *signal()* : interruptions
  * *select()* : événements liés aux entrée-sorties
  * ...

+++ {"slideshow": {"slide_type": "slide"}}

# usage

+++ {"cell_style": "split", "slideshow": {"slide_type": "fragment"}}

* commencer avec les librairies de haut niveau
  * HTTP (`aoihttp`) 
  * ssh (`asyncssh`)
  * telnet (`telnetlib3`) 
  * BdD's - ...
