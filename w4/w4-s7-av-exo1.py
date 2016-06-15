# -*- coding: utf-8 -*-

## Je vais créer une variable globale et une fonction
L = 10

def f():
    L = 11

print L
f()
print L

## La variable locale L est différente de la
## variable gobale L

## Par contre, si l'on rajoute l'instruction global, alors
## ça veut dire que la variable L assignée dans la fonction
## est bien la variable globale. L'instruction global permet
## de changer le scope d'une variable assignée localement
## dans une fonction. 

def f():
    global L
    L = 11

print L
f()
print L

## global est une intruction un peu particulière en Python
## Ça n'est pas une instruction interprétée comme toutes les
## autres instruction, c'est une directive au compilateur
## qui génère le byte code avant l'exécution. Donc, une
## variable définie comme étant globale le sera pour tout le
## scope dans lequel l'instruction global est présente,
## quelque soit la position de global dans ce scope.

def f():
    L = 12
    global L
f()
print L

## L est globale pour toute la fonction h(), même si global
## est définie après l'assignation 'L = 12'. Attention,
## dans les nouvelles versions de Python, il sera interdit
## de mettre la directive global après la variable que l'on
## veut rendre globale. Il faut donc prendre l'habitude
## de mettre global au tout début des fonctions. 

# 2 minutes 30

## Pour finir, comme la directive global nuit à la clareté
## du code en rendant les modifications
## aux variable globales implicite, on doit éviter de
## l'utiliser.

## En effet, il faut toujours
## privilégier les modifications explicites par retour
## de fonction. Regardons ces deux exemples

x = 100
def f():
    global x
    x = x + 10
f()
print x

## Regardons maintenant une autre manière d'écrire
## le même code

x = 100
def f():
    return x + 10
x = f()
print x

## Maintenant, la modification de la variable globale x
## est explicite, mais on peut faire mieux en rendant aussi
## explicite l'accès à la variable globale x dans la
## fonction f. 

x = 100
def f(x):
    return x + 10
x = f(x)
print x

## dans le premier cas la modification de x est implicite,
## mais dans le deuxième cas  c'est explicite avec
## l'assignation du resultat de f() à la variable x. Il faut
## toujours privilégier ce deuxième cas. 

## 4 minutes. 
