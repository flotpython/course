# -*- coding: iso-8859-15 -*-

## Commençons par créer une classe. Une utilise l'instruction
## class suivi du nom de la classe, puis d'un bloc d'instructions.
## Comme pour une fonction, le nom de la classe est une variable
## qui pointe vers l'objet classe qui est créé. 


class C:
    x = 1

print C

## Créons maintenant une instance de la classe C
I = C()

print I

## En Python, chaque classe et chaque instance a son propre
## espace de nommage.
## on accède à l'espace de nommage des objets avec la variable
## __dict__, l'espace de nommage est représenté comme un
## dictionnaire

print C.__dict__, I.__dict__

## Notons que toutes les variables commençant et finissant
## par des double tirets bas sont des variables définies par
## le langage. On ne doit donc jamais créer de nouvelles
## variables utilisant cette notion, par contre, comme
## on le verra bientôt, on peut surcharger ces variables.

## La relation d'héritage permet à un
## objet d'accéder à l'espace de nommage de l'objet dont
## il hérite. Une instance hérite toujours de la classe qui
## l'a créée, donc une instance peut toujours accéder à l'espace
## de nommage de sa classe. Comme toujours, on accède à une
## variable dans l'espace de nommage d'un objet avec la
## notation objet.variable

print C.x, I.x

## Pourquoi I1.x retourne 1 alors que cette variable n'existe
## pas dans l'espace de nommage de I1. Comme on vient de le dire
## I1 hérite de C, alors lorsqu'une variable n'est pas trouvé
## dans l'espace de nommage d'une instance, elle est automatiquement
## cherchée dans l'espace de nommage de la classe qui l'a créée.

## La classe qui a créé une instance est référencée par la variable
## __class__ sur l'instance 

print I.__class__, type(I.__class__)

## l'espace de nommage des instances est toujours vide
## a sa création. Mais comme les classes et les instance sont
## des objets mutables, on peut modifier leur espace de nommage.

C.x = 2

print C.x, I.x

## Non seulement la variable x dans C est changée, mais l'instance
## voit aussi ce changement. En effet la recherche d'une variable
## est faite dynamiquement en fonction de l'état de chaque objet
## au moment de la recherche. Si je crée une nouvelle variable dans C
## elle sera également vue par l'instance.

C.y = 10

## regardons les espaces de nommage
print C.__dict__, I.__dict__

## y est trouvé dans C lorsqu'on la recherche par I1, même si I1
## a été instanciée avant l'existance de y dans la classe C. 
print I.y

## évidemment, si  y est définie dans l'espace de nommage de I1,
## c'est elle qui sera retournée

I.y = 'a'

## regardons les espaces de nommage
print C.__dict__, I.__dict__

print C.y, I.y

## Comme les modules, les classes peuvent contenir des fonctions
## que l'on appelle habituellement méthodes. 
## Le méthodes des classes sont des fonctions un peu particulières,
## elles doivent obligatoirement avoir comme premier argument
## une instance. Cela permet aux méthodes de travailler sur les
## variables de l'instance puisque la méthode a un référence vers
## l'instance. Regardons un exemple

class C:
    x = 1
    def f(self, a):  #self n'est qu'un nom de variable, c'est pas un mot clef
        print self.x
        self.x = a

## créons une instance de C
I = C()

## Lorsque j'appelle la fonction sur l'instance, l'interpréteur
## passe automatiquement une référence de l'instance à la fonction
I.f(5)

## python fait automatiquement cette conversion
C.f(I, 5)

print C.x, I.x




