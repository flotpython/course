# -*- coding: utf-8 -*-


## Nous allons illuster l'utilisation d'un context manager en créant
## un objet qui permet de calculer le temps d'exécution d'un bloc de
## code


import time
class Timer():
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        duree = time.time() - self.start
        print(f"{duree}s")
        return False # en cas d'exception relance l'exception après
                     # __exit__ sinon, capture l'exception

    def __str__(self):
        duree = time.time() - self.start
        return f"intermédiaire: {duree}s"

## __enter__() retourne l'objet qui sera référencé par la variable
## après le as

## __exit__() doit retourner un boolean. Si c'est False, en cas
## d'exception, l'exception sera remontée et elle arrêtera le
## programme, si c'est True, l'exception sera capturée, c'est donc
## comme si on faisait un except sur toutes les exceptions, mais je
## vous rappelle que c'est en général une mauvaise pratique de
## capturer toutes les exceptions.

with Timer() as t:
    sum(x for x in range(10_000_000))
    print(t)
    sum(x**2 for x in range(10_000_000))

## Regardons maintenant le cas d'une exception
    
with Timer() as t:
    sum(x for x in range(10_000_000))
    print(t)
    1/0                                    #new
    sum(x**2 for x in range(10_000_000))

## si __exit__ retourne True, alors l'exception sera capturée.
