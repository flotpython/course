# -*- coding: iso-8859-15 -*-

def f(a, b):
    x = a / b

## si b est 0, il y aura une exception ZeroDivisionError
## On voit que l'exception a un nom spécifique et
## contient un message d'explication. C'est 
## le cas pour toutes les exceptions built-in

#f(1,0)

## Heureusement, il est possible de capturer une exception
## pour continuer le programme. 
## Les exceptions se capture avec l'instruction try/except

def f(a, b):
    try:
        x = a/b
    except ZeroDivisionError:
        print "Division par 0"        
    print 'continuons...'

print f(10, 2)
print f(1,0)

## mais maintenant, comment afficher le résultat que s'il
## n'y a pas d'exception. On pourrait mettre un print juste
## après x = a/b. S'il y a une exception le print n'est pas
## exécuté, et s'il n'y a pas de exception il est exécuté
## Cependant, l'instruction print pourrait elle même générer
## une exception et être capturer par erreur.

def f(a, b):
    try:
        x = a/b
        print b/a #au lieu de faire str(x)
    except ZeroDivisionError:
        print "Division par 0"        
    print 'continuons...'

f(0, 2)

## Une bonne pratique et de ne mettre entre le try/except
## que l'instruction ou l'ensemble d'instructions
## que l'on veut évaluer pour une exception donnée.
## On peut alors mettre le code qui doit être exécuté
## que s'il n'y a pas d'exception dans une clause else

def f(a, b):
    try:
        x = a/b
    except ZeroDivisionError:
        print "Division par 0"
    else:
        print x
    print 'continuons...'
    
f(2, 0)
f(10,2)

## Lorsqu'il y a une exception non capturée le programme
## s'arrête à la ligne de l'exception. Cependant, il y a des
## cas dans lequels on veut exécuter une derniere instruction
## même s'il y a une exception non capturée. C'est
## par exemple le cas lorsque l'on travaille sur des fichiers.
## il faut toujours fermer les fichiers avant que le programme
## ne s'arrête. Il existe
## pour cela la clause finally. La clause finally s'exécute
## toujours même en cas d'exception non capturée.

def f(a, b):
    try:
        x = a/b
    except ZeroDivisionError:
        print "Division par 0"
    else:
        print x
    finally:
        print 'dans finally'
    print 'continuons...'

#f(1, 'b')

## on peut également avoir plusieurs except pour un même try
def f(a, b):
    try:
        x = a/b
    except ZeroDivisionError:
        print "Division par 0"
    except TypeError:
        print "Il faut des int !"
    else:
        print x
    finally:
        print 'dans finally'
    print 'continuons...'

f(1, 'b')

## Il est également possible de récupérer l'instance de
## l'exception générée pour en afficher son contenu.
## les informations de l'exceptions sont toujours
## stockée dans le tuple args

def f(a, b):
    try:
        x = a/b
    except ZeroDivisionError as i:
        print "Division par 0", i.args
    except TypeError as i:
        print "Il faut des int !", i.args
    else:
        print x
    finally:
        print 'dans finally'
    print 'continuons...'

f(1, 'b')
f(1,0)

## 6 minutes 50 secondes
