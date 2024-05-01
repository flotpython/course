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

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++ {"slideshow": {"slide_type": "slide"}}

# extensions asynchrones du langage

+++ {"slideshow": {"slide_type": "slide"}}

# accès http

```{code-cell} ipython3
import time

urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]
```

+++ {"slideshow": {"slide_type": "slide"}}

##### en version séquentielle

```{code-cell} ipython3
import requests

beg = time.time()

for url in urls:
    req = requests.get(url)
    print(f"{url} returned {len(req.text)} chars")
    
print(f"duration = {time.time()-beg}s")
```

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
import asyncio
import aiohttp
```

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
async def fetch(url):
    
    async with aiohttp.ClientSession() as session:
        print(f"fetching {url}")
        
        async with session.get(url) as response:
            #print(f"{url} returned status {response.status}")
            raw = await response.read()
            print(f"{url} returned {len(raw)} bytes")
```

+++ {"slideshow": {"slide_type": "slide"}}

# context managers asynchrones

+++ {"slideshow": {"slide_type": "fragment"}}

* `__aenter__` et `__aexit__` : awaitables

+++ {"slideshow": {"slide_type": "fragment"}}

* [défini dans PEP492](https://www.python.org/dev/peps/pep-0492/#asynchronous-context-managers-and-async-with)

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
# une coroutine qui va chercher toutes les URLs
# ne fait toujours rien, naturellement
async def fetch_urls():
    await asyncio.gather(*(fetch(url) for url in urls))
```

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
loop = asyncio.get_event_loop()

beg = time.time()
loop.run_until_complete(fetch_urls())
print(f"duration = {time.time()-beg}s")
```

+++ {"slideshow": {"slide_type": "slide"}}

# itérations asynchrones

+++

* boucle `async for` [PEP-492](https://www.python.org/dev/peps/pep-0492/#asynchronous-iterators-and-async-for)
* compréhensions asynchrones [PEP-530](https://www.python.org/dev/peps/pep-0530/)

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
import asyncio

# une variante
async def fetch2(url, i):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            # avec ici une itération asynchrone
            async for line in response.content: 
                print(f'{i}', end='')
    return url
```

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
asyncio.get_event_loop().run_until_complete(
    asyncio.gather(*(fetch2(url, i) for i, url in enumerate(urls))))
```

+++ {"slideshow": {"slide_type": "slide"}}

# résumé (1)

+++ {"slideshow": {"slide_type": "fragment"}}

* fonction coroutine `async def foo()`

+++ {"cell_style": "center", "slideshow": {"slide_type": "fragment"}}

* `foo()` → objet *coroutine* :  faire `await foo()`

+++ {"cell_style": "split", "slideshow": {"slide_type": "fragment"}}

**autorisé**

````
async def foo():
    await bar()
````

+++ {"cell_style": "split", "slideshow": {"slide_type": "-"}}

**pas autorisé** : *SyntaxError*

````
def foo():
    await bar()
````

+++ {"slideshow": {"slide_type": "slide"}}

# résumé (2)

+++ {"cell_style": "center", "slideshow": {"slide_type": "fragment"}}

* `async with`
* `async for`

+++ {"cell_style": "center", "slideshow": {"slide_type": "fragment"}}

* Boucle d'événements 
  * `asyncio.get_event_loop()`
