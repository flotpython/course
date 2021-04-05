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

# `asyncio` : historique et écosystème

+++ {"slideshow": {"slide_type": "slide"}}

# historique - python3

+++ {"slideshow": {"slide_type": "fragment"}}

* python-3.5 
  * syntaxe moderne `async` / `await`

+++ {"slideshow": {"slide_type": "fragment"}}

* python-3.4 : première introduction de `asyncio`

  * `async def` $\longleftrightarrow$ `@asyncio.coroutine` 
  * `await` $\longleftrightarrow$ `yield from` 

+++ {"slideshow": {"slide_type": "slide"}}

# historique - python2

+++ {"slideshow": {}}

* python-2.5 (2006 !)

  * générateurs avec `send()`

+++ {"slideshow": {"slide_type": "slide"}}

# inspiré de (pre-asyncio)

+++ {"slideshow": {}}

* gevent : http://www.gevent.org/
* tornado : http://www.tornadoweb.org/en/stable/
* twisted : https://twistedmatrix.com/trac/

+++ {"slideshow": {"slide_type": "slide"}}

# langage *vs* librairie (1) : langage

+++ {"slideshow": {"slide_type": "fragment"}}

* coroutine : `async def` et `await`

+++ {"slideshow": {"slide_type": "fragment"}}

* itérateurs asynchrones
  * `async for`
  * compréhensions asynchrones

+++ {"slideshow": {"slide_type": "fragment"}}

* context managers asynchrones
  * `async with` 

+++ {"slideshow": {"slide_type": "slide"}}

# langage *vs* librairie (2) : librairie

+++ {"slideshow": {"slide_type": "fragment"}}

* boucle d'événements

+++ {"slideshow": {"slide_type": "fragment"}}

* synchronisation: `Queue`, `Lock` et `Semaphore`

+++ {"slideshow": {"slide_type": "fragment"}}

* interaction avec les processus: - package `asyncio.subprocess`

+++ {"slideshow": {"slide_type": "fragment"}}

* `Transport` et `Protocol` / callback
* `Streams` / API orientées coroutine

+++ {"slideshow": {"slide_type": "slide"}}

# utilisable en production ?

+++ {"cell_style": "split", "slideshow": {"slide_type": "fragment"}}

* stable depuis 3.6

+++ {"cell_style": "split", "slideshow": {"slide_type": "fragment"}}

* performances OK

+++ {"slideshow": {"slide_type": "fragment"}}

* nombreux protocoles réseau disponibles
  * HTTP `aiohttp`
  * ssh `asyncssh`
  * telnet `telnetlib3`
* drivers bases de données
  * postgres `asyncpg`
  * ...
* ...

+++ {"slideshow": {"slide_type": "slide"}}

# mais ..

+++ {"slideshow": {"slide_type": "fragment"}}

* paradigme contagieux

+++ {"slideshow": {"slide_type": "fragment"}}

* travaux expérimentaux (post-asyncio)
  * `uvloop` 
  * `curio`
  * `trio`
