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

# programmation asynchrone

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

# typologie d'applications

* CPU-intensive
* IO-intensive

+++

# requête à un serveur

+++

![délais dans les traitements](w8-s1-av-fig1.png)

+++

# deux requêtes en séquence

+++

![délais dans les traitements](w8-s1-av-fig2.png)

+++

# processus simple

![single-thread](w8-s1-av-fig3.png)

+++

# avantages / inconvénients

+++ {"cell_style": "split"}

* parallèlisme
* isolation

+++ {"cell_style": "split"}

* *trop* d'isolation
* échelle : 10x - 100x

+++

# threads

![multi-thread](w8-s1-av-fig4.png)

+++

# avantages / inconvénients

+++ {"cell_style": "split"}

* disponible en python 

  [`import threading`](https://docs.python.org/3/library/threading.html#module-threading)

+++ {"cell_style": "split"}

* utilisation **très** délicate
* échelle 1000x

+++

# commutations de contexte (1)

+++

### deux pages téléchargées par 2 threads différents

+++

![2 threads](w8-s1-av-fig5.png)

+++

# commutations de contexte (2)

+++

![zoom](w8-s1-av-fig6.png)

+++

# callbacks

+++ {"cell_style": "center"}

* associer à un événement
* une fonction à exécuter

+++ {"cell_style": "center"}

* induit un découpage du code en petits morceaux
* logique difficile à suivre

+++

# `asyncio`

+++

* notion de **coroutines**
* qui s'exécutent en parallèle
* mais dans **un seul thread**
* avec du code **lisible**
* en donnant du contrôle sur les changements de contexte
* et sans besoin de saucissonner son code en callbacks
* échelle 10 000x - 100 000x

+++

# callback *vs* coroutine

+++ {"cell_style": "split"}

```
function pong_handler(client) {
    client.on('data', function (data) {
        client.on('data_written', function () {
            client.close()
        });
        client.write(data)
        client.flush()
    });
}
```

+++ {"cell_style": "split"}

le serveur du protocole 'ping-pong'
```
async function pong_handler()
{
    client.write(await client.read())
    await client.flush()
    client.close()
}
```

+++ {"cell_style": "center"}

<span style="font-size:smaller;">
exemple tiré de https://mdk.fr/blog/python-coroutines-with-async-and-await.html
</span>

+++

![avec asyncio](w8-s1-av-fig7.png)
