---
ipub:
  sphinx:
    toggle_input: true
    toggle_input_all: true
    toggle_output: true
    toggle_output_all: true
jupytext:
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
livereveal:
  auto_select: code
  auto_select_fragment: true
  autolaunch: false
  backimage: media/nologo.png
  height: 100%
  start_slideshow_at: selected
  theme: simple
  transition: fade
  width: 100%
nbhosting:
  title: asyncio et Python-3.7
---

#  Avertissement relatif à `asyncio` et Python-3.7

+++

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span>Inria - UCA</span>
</div>

+++

## Complément - niveau intermédiaire

+++

Puisque cette semaine est consacrée à **`asyncio`**, il faut savoir que cette brique
technologique est **relativement récente**, et qu'elle est du coup, plus que d'autres
aspects de Python, **sujette à des évolutions**.

+++

## Les vidéos utilisent Python-3.6

+++

Comme on l'a dit en préambule du cours, la version de **référence** lors du tournage était
**Python-3.6**. Par contre les notebooks sur FUN-MOOC utilisent à présent une version plus
récente.

```{code-cell} ipython3
import sys
major, minor, *_ = sys.version_info
print(f"les notebooks utilisent la version {major}.{minor}")
```

## Un résumé des nouveautés

+++

Vous trouverez à la fin de la semaine, dans la séquence consacrée aux bonnes pratiques, un
résumé des améliorations  apportées depuis la version 3.6.

+++

## L'essentiel est toujours d'actualité

+++

Cela étant dit, nos buts ici étaient principalement:

* de vous faire découvrir ce nouveau paradigme,
* de vous faire sentir dans quelles applications cela peut avoir un apport très précieux,
* de bien vous faire comprendre ce qui se passe à l'exécution,
* et de vous donner un aperçu de la façon dont tout cela est implémenté.

+++

## Les différences les plus visibles

+++

Les plus grosses différences concernent la prise en main. Comme nous allons bientôt le
voir, le "*hello world*" de `asyncio` était en Python-3.6 un peu *awkward*, cela
nécessitait pas mal de circonlocutions.

C'est-à-dire que pour faire fonctionner la coroutine :

```{code-cell} ipython3
# un exemple de coroutine 
import asyncio

async def hello_world():
    await asyncio.sleep(0.2)
    print("Hello World")
```

### En Python-3.6

+++

Pour exécuter cette coroutine dans un interpréteur Python-3.6, la syntaxe est un peu
lourdingue :

```python
# pour exécuter uniquement cette coroutine en Python-3.6
loop = asyncio.get_event_loop()
loop.run_until_complete(hello_world())
```

+++

### En Python-3.7

En 3.7, on arrive au même résultat de manière beaucoup plus simple :

```python
# c'est beaucoup plus simple en 3.7
asyncio.run(hello_world())
```

+++

### Avec IPython 7

Notez qu'avec IPython (et donc aussi dans les notebooks) c'est encore plus simple; en
effet IPython s'est débrouillé pour autoriser la syntaxe suivante :

```{code-cell} ipython3
# depuis ipython, ou dans un notebook, vous pouvez faire simplement

await hello_world()
```

***Mise en garde*** attention toutefois, je vous mets en garde contre le fait que ceci est
une **commodité** pour nous faciliter la vie, mais elle est **spécifique à IPython** et ne
va pas fonctionner tel quel dans un programme exécuté directement par l'interpréteur
Python standard.

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# un code cassé

!cat data/broken-await.py
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# la preuve

!python data/broken-await.py
```

Nous avons choisi de ne pas utiliser ce trait dans les notebooks, car cela pourrait créer
de la confusion, mais n'hésitez pas à l'utiliser de votre côté une fois que tout ceci est
bien acquis.

+++

### À propos de Python-3.8

Avec Python 3.8 et 3.9 il y a peu de changements concernant `asyncio`, ils sont décrits ici :

<https://docs.python.org/3/whatsnew/3.8.html#asyncio> 
<https://docs.python.org/3/whatsnew/3.9.html#asyncio> 

<span style="font-size: smaller">Notez toutefois l'apparition en 3.8 d'une REPL
(read-eval-print-loop) qui supporte justement `await` au toplevel</span>

+++

## Conclusion

+++

Pour conclure cet avertissement, ne vous formalisez pas si vous voyez dans le cours des
pratiques qui sont dépassées. Les différences par rapport aux pratiques actuelles - même
si elles sont assez visibles dans ce cours introductif - sont en réalité mineures au niveau
de ce qu'il est important de comprendre quand on aborde d'un oeil neuf ce nouveau
paradigme de programmation.
