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

# `asyncio` : historique et écosystème

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

# historique - python3

+++

* python-3.5 
  * syntaxe moderne `async` / `await`

+++

* python-3.4 : première introduction de `asyncio`

  * `async def` $\longleftrightarrow$ `@asyncio.coroutine` 
  * `await` $\longleftrightarrow$ `yield from`

+++

# historique - python2

+++

* python-2.5 (2006 !)

  * générateurs avec `send()`

+++

# inspiré de (pre-asyncio)

+++

* gevent : http://www.gevent.org/
* tornado : http://www.tornadoweb.org/en/stable/
* twisted : https://twistedmatrix.com/trac/

+++

# langage *vs* librairie (1) : langage

+++

* coroutine : `async def` et `await`

+++

* itérateurs asynchrones
  * `async for`
  * compréhensions asynchrones

+++

* context managers asynchrones
  * `async with`

+++

# langage *vs* librairie (2) : librairie

+++

* boucle d'événements

+++

* synchronisation: `Queue`, `Lock` et `Semaphore`

+++

* interaction avec les processus: - package `asyncio.subprocess`

+++

* `Transport` et `Protocol` / callback
* `Streams` / API orientées coroutine

+++

# utilisable en production ?

+++ {"cell_style": "split"}

* stable depuis 3.6

+++ {"cell_style": "split"}

* performances OK

+++

* nombreux protocoles réseau disponibles
  * HTTP `aiohttp`
  * ssh `asyncssh`
  * telnet `telnetlib3`
* drivers bases de données
  * postgres `asyncpg`
  * ...
* ...

+++

# mais ..

+++

* paradigme contagieux

+++

* travaux expérimentaux (post-asyncio)
  * `uvloop` 
  * `curio`
  * `trio`
