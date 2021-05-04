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
notebookname: '*Context managers* et exceptions'
version: '3.0'
---

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
<span><img src="media/both-logos-small-alpha.png" /></span>
</div>

+++

# *Context managers* et exceptions

+++

## Complément - niveau intermédiaire

+++

On a vu jusqu'ici dans la vidéo comment écrire un context manager; on a vu notamment qu'il était bon pour la méthode `__exit__()` de retourner `False`, de façon à ce que l'exception soit propagée à l'instruction `with`:

```{code-cell} ipython3
import time

class Timer1:
    def __enter__(self):
        print("Entering Timer1")
        self.start = time.time()
        return self
    
    # en règle générale on se contente de propager l'exception 
    # à l'instruction with englobante
    def __exit__(self, *args):
        print(f"Total duration {time.time()-self.start:2f}")

        # et pour cela il suffit que __exit__ retourne False
        return False
```

Ainsi si le corps de l'instruction lève une exception, celle-ci est propagée :

```{code-cell} ipython3
import time
try:
    with Timer1():
        time.sleep(0.5)
        1/0
except Exception as exc:
    # on va bien recevoir cette exception
    print(f"OOPS -> {type(exc)}")
```

À la toute première itération de la boucle, on fait une division par 0 qui lève l'exception `ZeroDivisionError`, qui passe bien à l'appelant.

Il est important, lorsqu'on conçoit un context manager, de bien **propager** les exceptions qui ne sont pas liées au fonctionnement attendu du context manager. Par exemple un objet de type fichier va par exemple devoir attraper les exceptions liées à la fin du fichier, mais doit par contre laisser passer une exception comme `ZeroDivisionError`.

+++

### Les paramètres de `__exit__`

+++

Si on a besoin de filtrer entre les exceptions - c'est-à-dire en laisser passer certaines et pas d'autres - il nous faut quelque chose de plus pour pouvoir faire le tri. 
Comme [vous pouvez le retrouver ici](https://docs.python.org/3/reference/datamodel.html#with-statement-context-managers), la méthode `__exit__` reçoit trois arguments :

```python
def __exit__(self, exc_type, exc_value, traceback):
```

* si l'on sort du bloc `with` sans qu'une exception soit levée, ces trois arguments valent `None`;
* par contre si une exception est levée, ils permettent d'accéder respectivement au type, à la valeur de l'exception, et à l'état de la pile lorsque l'exception est levée.

+++

Pour illustrer cela, écrivons une nouvelle version de `Timer` qui filtre, disons, l'exception `ZeroDivisionError` que je choisis au hasard, c'est uniquement pour illustrer le mécanisme.

```{code-cell} ipython3
# une deuxième version de Timer
# qui propage toutes les exceptions sauf 'OSError'

class Timer2:
    def __enter__(self):
        print("Entering Timer1")
        self.start = time.time()
        # rappel : le retour de __enter__ est ce qui est passé
        # à la clause `as` du `with`
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            # pas d'exception levée dans le corps du 'with'
            print(f"Total duration {time.time()-self.start:2f}")
            # dans ce cas la valeur de retour n'est pas utilisée
        else:
            # il y a eu une exception de type 'exc_type'
            if exc_type in (ZeroDivisionError,) :
                print("on étouffe")
                # on peut l'étouffer en retournant True
                return True
            else:
                print(f"OOPS : on propage l'exception "
                      f"{exc_type} - {exc_value}")
                # et pour ça il suffit... de ne rien faire du tout
                # ce qui renverra None 
```

```{code-cell} ipython3
# commençons avec un code sans souci
try:
    with Timer2():
        time.sleep(0.5)
except Exception as e:
    # on va bien recevoir cette exception
    print(f"OOPS -> {type(e)}")
```

```{code-cell} ipython3
# avec une exception filtrée
try:
    with Timer2():
        time.sleep(0.5)
        1/0
except Exception as e:
    # on va bien recevoir cette exception
    print(f"OOPS -> {type(e)}")
```

```{code-cell} ipython3
# avec une autre exception 
try:
    with Timer2():
        time.sleep(0.5)
        raise OSError()
except Exception as e:
    # on va bien recevoir cette exception
    print(f"OOPS -> {type(e)}")
```

### La bibliothèque `contextlib`

+++

Je vous signale aussi [la bibliothèque `contextlib`](https://docs.python.org/3/library/contextlib.html) qui offre quelques utilitaires pour se définir un contextmanager.

Notamment, elle permet d'implémenter un context manager sous une forme compacte à l'aide d'une fonction génératrice - et du décorateur `contextmanager`:

```{code-cell} ipython3
from contextlib import contextmanager
```

```{code-cell} ipython3
# l'objet compact_timer est un context manager !
@contextmanager
def compact_timer(message):
    start = time.time()
    yield
    print(f"{message}: duration = {time.time() - start}")
```

```{code-cell} ipython3
with compact_timer("Squares sum"):
    print(sum(x**2 for x in range(10**5)))
```

Un peu comme on peut implémenter un itérateur à partir d'une fonction génératrice qui fait (n'importe quel nombre de) `yield`, ici on implémente un context manager compact sous la forme d'une fonction génératrice.

Comme vous l'avez sans doute deviné sur la base de cet exemple, il faut que la fonction fasse **exactement un `yield`**: ce qui se passe avant le `yield` est du ressort de `__enter__`, et la fin est du ressort de `__exit__()`. 

Bien entendu on n'a pas la même puissance d'expression avec cette méthode par rapport à une vraie classe, mais cela permet de créer des context managers avec le minimum de code.
