# -*- coding: iso-8859-15 -*-


## Actuellement, parmi les types de base,
## seul les fichiers ont un context manager.

## with est suivi d'un objet qui a deux méthodes
## __enter__ et __exit__. La méthode __enter__ doit
## retourner un objet que va référencer la variable f
## __enter__ est exécuté avant la première ligne du bloc
## d'instruction, puis on exécute le bloc d'instruction,
## et finalement on exécute __exit__(), même s'il y a
## une exception non capturée. Pour les fichiers, __exit__()
## ferme simplement le fichier. 

with open(r'c:\Temp\spam.txt', 'w') as f:
    for i in range(10):
        f.write(str(i) + '\n')


## On peut évidement implémenter un context manager
## pour nos propres objets. Regardons un exemple


class C():
    ## la méthode __enter__ retourne en général l'objet
    ## lui même
    def __enter__(self):
        print 'dans enter'
        return self

    ## la méthode __exit__ doit retourner un booléeen
    ## Si elle retourne False, en cas d'exception,
    ## l'exception sera relancée, c'est le cas classique
    ## Si elle retourne True, l'exception sera capturée

    def __exit__(self, *args):
        print 'dans exit'
        ## args contient les détails de l'exception
        print args
        return False

    def div(self, a, b):
        print a/b

#with C() as c:
#    c.div(1, 0)

## Si la valeur de retour de __exit__ est True, l'exception
## est capturée.

class C():
    ## la méthode __enter__ retourne en général l'objet
    ## lui même
    def __enter__(self):
        print 'dans enter'
        return self

    ## la méthode __exit__ doit retourner un booléeen
    ## Si elle retourne False, en cas d'exception,
    ## l'exception sera relancée, c'est le cas classique
    ## Si elle retourne True, l'exception sera capturée

    def __exit__(self, *args):
        print 'dans exit'
        ## args contient les détails de l'exception
        print args
        return True

    def div(self, a, b):
        print a/b

#with C() as c:
#    c.div(1, 0)

