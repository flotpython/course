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

# premiers exemples

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

### les concepts de base en action

```{code-cell}
import asyncio
```

## coroutine

```{code-cell}
async def morceaux(message):

    # on appelle le code synchrone normalement
    print(message, "début")
    # avec await on rend la main
    await asyncio.sleep(0.5)

    print(message, "milieu")
    await asyncio.sleep(1)
    
    print(message, "fin")
    return f'{message} par morceaux'
```

+++ {"cell_style": "center"}

# coroutines

+++ {"cell_style": "split"}

fonction coroutine

```{code-cell}
:cell_style: split

# la fonction coroutine
morceaux
```

+++ {"cell_style": "split"}

objet coroutine

```{code-cell}
:cell_style: split

# retourne un objet coroutine
morceaux("run")
```

# boucle d'événements

```{code-cell}
loop = asyncio.get_event_loop()
```

```{code-cell}
loop.run_until_complete(morceaux("run"))
```

# plusieurs traitements

```{code-cell}
loop.run_until_complete(
    asyncio.gather(morceaux("run1"),
                   morceaux("run2")))
```

![run1-run2](w8-s2-av-fig1.png)

+++

# ce qu'il ne faut pas faire

```{code-cell}
import time 

async def famine(message):

    print(message, "début")
    # avec await on rend la main
    await asyncio.sleep(0.5)

    print(message, "milieu")
    # on garde la main au lieu de la rendre
    time.sleep(1)
    print(message, "fin")
    return f'{message} par famine'
```

## famine en action

```{code-cell}
loop.run_until_complete(
    asyncio.gather(famine("run1"),
                   famine("run2")))
```

# chronologie

+++

![famine](w8-s2-av-fig2.png)

+++

# conclusion

+++

* on crée une fonction coroutine avec `async def`

+++

* une boucle d'événements 
  * pour orchestrer plusieurs coroutines

+++

* une coroutine peut appeler une autre coroutine avec `await`

+++

* une coroutine peut appeler une fonction synchrone
  * mais attention à ne pas bloquer trop longtemps
