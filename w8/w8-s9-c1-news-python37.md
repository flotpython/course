---
jupytext:
  cell_metadata_filter: all, -hidden, -heading_collapsed, -run_control, -trusted
  notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version, -jupytext.text_representation.format_version,
    -language_info.version, -language_info.codemirror_mode.version, -language_info.codemirror_mode,
    -language_info.file_extension, -language_info.mimetype, -toc
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
language_info:
  name: python
  pygments_lexer: ipython3
notebookname: "Nouveaut\xE9s en Python-3.7"
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# Nouveautés par rapport aux vidéos

+++

## Complément - niveau intermédiaire

+++

Comme on l'a signalé au début de la semaine, `asyncio` a subi quelques modifications dans
Python-3.7, que nous allons rapidement illustrer dans ce complément.

Nous verrons aussi par ailleurs une curiosité liée à la dernière version de IPython, qui
vise à faciliter le debug et la mise au point de code asynchrone.

+++

### Python-3.7 et `asyncio`

+++

#### Documentation

+++

L'évolution la plus radicale est une refonte totale de la documentation.

C'est une très bonne nouvelle, car de l'aveu même de Guido van Rossum, la documentation en
place pour les versions 3.5 et 3.6 était particulièrement obscure; [voici comment il l'a
annoncé](https://twitter.com/gvanrossum/status/1041889574052429826?lang=en) :

> Finally the asyncio docs are not an embarrassment to us all.

Si vous avez déjà eu l'occasion de parcourir ces anciennes documentations, et que vous les
avez trouvées indigestes, sachez que vous n'êtes pas seul dans ce cas ;) Dans tous les cas
je vous invite à [parcourir la nouvelle
version](https://docs.python.org/3/library/asyncio.html), qui a le mérite d'apporter plus
de réponses qu'elle ne soulève d'interrogations. Ce qui n'était pas vraiment le cas avant,
c'est donc un grand progrès :)

+++

#### Accès plus facile

+++

Un certain nombre de changements ont été apportés à la librairie pour en rendre l'accès
plus facile.

Notamment, comme on l'a évoqué en début de semaine, on peut maintenant faire fonctionner
une simple coroutine à des fins pédagogiques en faisait plus simplement:

```python
>>> import asyncio
>>> async def hello_world():
...     await asyncio.sleep(0.2)
...     print("hello world")
...
>>> asyncio.run(hello_world())
hello world
```

+++

On a également créé des raccourcis, comme par exemple:

* `asyncio.create_task()` est un alias pour `asyncio.get_event_loop().create_task()`;
* de même `asyncio.current_task()` et `asyncio.all_tasks()` font ce que vous imaginez;

+++

#### Commodité

+++

Changement un peu plus profond, la fonction `asyncio.get_running_loop()` permet d'accéder
à la boucle courante.

Si vous avez lu du code `asyncio` plus ancien, vous avez peut-être remarqué une tendance
prononcée à passer un objet loop en paramètre à peu près partout. Grâce à cette fonction,
cela n'est plus nécessaire, on est garanti de pouvoir retrouver, à partir de n'importe
quelle coroutine, l'objet boucle qui nous pilote.

De manière corollaire, une méthode `get_loop` a été ajoutée aux classes `Future` et `Task`.

+++

#### Pas de changement de fond

+++

Sinon, en terme des concepts fondamentaux, tout le contenu du cours reste valide.

+++

#### Pour en savoir plus

VOus retrouverez tous les détails dans la page suivante :

<https://docs.python.org/3/whatsnew/3.7.html#whatsnew37-asyncio>

+++

### IPython7 et `asyncio`

+++

### `await` dans ipython-7

Cette section ne s'applique pas *stricto sensu* à Python-3.7, mais à la version 7 de
IPython.

Le sujet, c'est ici encore de raccourcir le *boilerplate* nécessaire, lorsque vous avez
écrit une coroutine et que vous voulez la tester.

+++

##### Python standard

+++

Voici d'abord ce qui se passe avec l'interpréteur Python standard (ici en 3.7) :

+++

```python
$ python3
Python 3.7.0 (default, Jun 29 2018, 20:14:27)
    <snip>
>>> import asyncio
>>>
>>> async def hello_world():
...     await asyncio.sleep(0.2)
...     print("hello world")
...
>>> await(hello_world())
  File "<stdin>", line 1
SyntaxError: 'await' outside function
>>>
>>> asyncio.run(hello_world())
hello world
```

+++

La syntaxe de Python nous interdit en effet d'utiliser `await` en dehors du code d'une
coroutine, on l'a vu dans une des vidéos, et il nous faut faire appel à `asyncio.run()`.

+++

##### IPython-7: on peut faire `await` au toplevel !

+++

Pour **simplifier encore** la mise en place de code asynchrone, depuis ipython-7, on peut
carrément déclencher une coroutine en invoquant `await` dans la boucle principale de
l'interpréteur :

+++

```python
$ ipython3
Python 3.7.0 (default, Jun 29 2018, 20:14:27)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.0.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import asyncio

In [2]: async def hello_world():
   ...:     await asyncio.sleep(0.2)
   ...:     print("hello world")

In [3]: await(hello_world())
hello world
```

+++

Du coup, cette façon de faire fonctionnera aussi dans un notebook, si vous avez la bonne
version de IPython en dessous de Jupyter.
