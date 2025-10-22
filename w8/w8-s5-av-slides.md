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

# coroutines et awaitables

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

### *my first loop*

+++

# protocole awaitable

+++

| instruction | classe d'objets   | protocole               | exemple              | 
|------------:|------------------:|------------------------:|---------------------:|
|   `for`     |   itérables       |  `__iter__`             | liste, ensemble      |
|   `with`    | context managers  |`__enter__` & `__exit__` | fichier              |
|   `dict[x]` | hashables         | `__hash__`              | *builtins* immuables |
|   `await`   |   awaitables      | `__await__`             | objet coroutine      |

+++

# `__await__` renvoie un itérateur

```{code-cell}
:cell_style: split

class Awaitable():
    def __await__(self):
        print("in awaitable")
        yield "yielded"
```

```{code-cell}
:cell_style: split

# il nous faut 
# au moins une coroutine
# pour pouvoir faire await
async def main():
    await Awaitable()
```

```{code-cell}
:cell_style: split

# l'objet coroutine
coro = main()
```

```{code-cell}
:cell_style: split

coro.send(None)
```

# un peu moins simple

```{code-cell}
:cell_style: split

# itérateur à deux coups 
class Awaitable2():
    def __await__(self):
        print("step1")
        yield "yield 1"
        print("step2")
        yield "yield 2"
        return "returned"
```

```{code-cell}
:cell_style: split

# boilerplate
async def main():
    return await Awaitable2()
```

```{code-cell}
:cell_style: split

# l'objet coroutine
coro = main()
```

```{code-cell}
:cell_style: split

coro.send(None)
```

```{code-cell}
:cell_style: split

coro.send(None)
```

```{code-cell}
try:
    coro.send(None)
except Exception as e:
    x = e
    print('OOPS', type(e), e.value)
```

# plusieurs travaux en même temps

```{code-cell}
:cell_style: split

coro1 = main()
```

```{code-cell}
:cell_style: split

coro2 = main()
```

```{code-cell}
:cell_style: split

coro1.send(None)
```

```{code-cell}
:cell_style: split

coro2.send(None)
```

```{code-cell}
:cell_style: split

coro1.send(None)
```

```{code-cell}
:cell_style: split

coro2.send(None)
```

```{code-cell}
:cell_style: split

try:
    coro1.send(None)
except Exception as e:
    x = e
    print('OOPS', type(e), e.value)
```

```{code-cell}
:cell_style: split

try:
    coro2.send(None)
except Exception as e:
    x = e
    print('OOPS', type(e), e.value)
```

# pile, await et yield

```{code-cell}
:cell_style: split

class w1:

    def __init__(self, marker):
        self.marker = marker
    
    def __await__(self):
        # redonner la main à la boucle
        yield f"yield {self.marker}"
        # retourné à await
        return 1
```

```{code-cell}
:cell_style: split

async def w2():
    return await w1('first') + await w1('second')

async def w3():
    return await w2() + 1

async def w4():
    return await w3() + 1

coro = w4()
```

```{code-cell}
:cell_style: split

coro.send(None)
```

```{code-cell}
:cell_style: split

coro.send(None)
```

```{code-cell}
try:
    coro.send(None)
except Exception as e:
    x = e
    print('OOPS', type(e), e.value)
```

# [animation](single-stack/index.html)

+++

# dans les deux sens

```{code-cell}
:cell_style: split

class BothWays():
    def __await__(self):
        print("step1")
        received1 = yield "yielded1"
        print("received1", received1)
        print("step2")
        received2 = yield "yielded2"
        print("received2", received2)
        return "returned"
```

```{code-cell}
:cell_style: split

# boilerplate
async def main():
    return await BothWays()
```

```{code-cell}
:cell_style: split


# l'objet coroutine
coro = main()
```

```{code-cell}
:cell_style: split

# La première fois il FAUT envoyer None
coro.send(None)
```

```{code-cell}
:cell_style: split

coro.send("message")
```

# communication boucle - awaitable

+++

![both ways](w8-s5-av-fig1.png)

+++

# conclusion

+++

### protocole awaitable

+++ {"cell_style": "split"}

### méthode `send()`

+++ {"cell_style": "split"}

### liée aux `yield`

+++

### communication bi-directionnelle

+++

### ~~`import asyncio`~~
