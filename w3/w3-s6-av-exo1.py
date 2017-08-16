# -*- coding: utf-8 -*-

def div(a, b):
    x = a / b

## si b est 0, il y aura une exception ZeroDivisionError
## On voit que l'exception a un nom spécifique et
## contient un message d'explication. C'est 
## le cas pour toutes les exceptions built-in

#div(1,0)

## prenons quelques instants pour regarder cette exception.
## Le message d'erreur indique la ligne qui a produit l'exception,
## le nom de l'exception ZeroDivisionError et un message d'erreur

## Heureusement, il est possible de capturer une exception
## pour continuer le programme. 
## Les exceptions se capturent avec l'instruction try/except

def div(a, b):
    try:
        x = a/b
    except ZeroDivisionError:
        print("Division par 0")
    print('continuons...')

print(div(10, 2))
print(div(1,0))

## mais maintenant, comment afficher le résultat que s'il
## n'y a pas d'exception. On pourrait mettre un print juste
## après x = a/b. S'il y a une exception le print n'est pas
## exécuté, et s'il n'y a pas de exception il est exécuté
## Cependant, l'instruction print pourrait elle même générer
## une exception qui serait capturée par erreur.

def div(a, b):
    try:
        x = a/b
        print(b/a) #au lieu de faire str(x)
    except ZeroDivisionError:
        print("Division par 0")        
    print('continuons...')

div(0, 2)

## Une bonne pratique et de ne mettre entre le try/except
## que l'instruction ou l'ensemble d'instructions
## que l'on veut évaluer pour une exception donnée.
## On peut alors mettre le code qui doit être exécuté
## que s'il n'y a pas d'exception dans une clause else

def div(a, b):
    try:
        x = a/b
    except ZeroDivisionError:
        print("Division par 0")
    else:
        print(x)
    print('continuons...')
    
div(2, 0)
div(10,2)

## Lorsqu'il y a une exception non capturée le programme
## s'arrête à la ligne de l'exception. Cependant, il y a des
## cas dans lequels on veut exécuter une derniere instruction
## même s'il y a une exception non capturée. C'est
## par exemple le cas lorsque l'on travaille sur des fichiers.
## il faut toujours fermer les fichiers avant que le programme
## ne s'arrête. Il existe
## pour cela la clause finally. La clause finally s'exécute
## toujours même en cas d'exception non capturée.

def div(a, b):
    try:
        x = a/b
    except ZeroDivisionError:
        print("Division par 0")
    else:
        print(x)
    finally:
        print('dans finally')
    print('continuons...')

#div(1, 'b')

## on peut avoir plusieurs except pour un même try et avoir un
## comportement spécifique par exception. 
def div(a, b):
    try:
        x = a/b
    except ZeroDivisionError:
        print("Division par 0")
    except TypeError:
        print("Il faut des int !")
    else:
        print(x)
    finally:
        print('dans finally')
    print('continuons...')

div(1, 'b')

## Finalement, il est possible de récupérer l'instance de l'exception
## générée pour en afficher son contenu.  les informations de
## l'exceptions sont toujours stockée dans le tuple args

def div(a, b):
    try:
        x = a/b
    except ZeroDivisionError as i:
        print("Division par 0", i.args)
    except TypeError as i:
        print("Il faut des int !", i.args)
    else:
        print(x)
    finally:
        print('dans finally')
    print('continuons...')

div(1, 'b')
div(1,0)

######################## 8 minutes #####################
