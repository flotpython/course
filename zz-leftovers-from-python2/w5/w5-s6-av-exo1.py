# -*- coding: utf-8 -*-

## Commençons avec l'opérateur le plus courant que l'on
## appel le constructeur. C'est une méthode qui est appelée
## automatiquement à la création de chaque instance.
## Cette méthode __init__ permet d'initialiser des variables
## d'instance à la contruction de l'instance. Regardons
## un exemple

class C:
    def set_x(self, x):
        self.x = x
    def get_x(self):
        print self.x

I = C()

## si on appelle get_x avant de d'appeler set_x on
## va avoir une exception parce que la variable x
## n'a pas encore été créée dans l'espace de nommage
## de l'instance. On pourrait alors vouloir, dès la
## création de l'instance, initialiser x à une valeur
## par défaut, par exemple 0. On peut le faire avec
## le constructeur

#I.get_x()

class C:
    def __init__(self):
        print 'dans C'
        self.x = 0 
    def set_x(self, x):
        self.x = x
    def get_x(self):
        print self.x

I = C()
I.get_x()

## On peut, comme pour toutes fonctions, passer des arguments
## à init

class C:
    def __init__(self, x):
        print 'dans C'
        self.x = x
    def set_x(self, x):
        self.x = x
    def get_x(self):
        print self.x

I = C(10)
I.get_x()

## En cas d'héritage, le contructeur n'est appeler que sur
## la classe qui instancie l'objet et pas sur ces super-classes

class D(C):
    def __init__(self):
        print 'dans D'

I = D()

#I.get_x()

## pour appeler le contructeur de C lorsque l'on crée une
## instance de D, il faut le faire explicitement.

class D(C):
    def __init__(self):
        C.__init__(self, 100)
        print 'dans D'

I = D()
I.get_x()



## 5 minutes
## Pour voir les valeurs de x dans l'instance on appelle
## à chaque fois la méthode get_x(), mais 
## on pourrait vouloir utiliser directement l'instruction
## print. C'est possible en surchargeant la méthode __str__

class C:
    def __init__(self, x):
        print 'dans C'
        self.x = x
    def set_x(self, x):
        self.x = x
    def get_x(self):
        print self.x
    # doit retourner une chaîne de caractères
    def __str__(self):
        return str(self.x)

class D(C):
    def __init__(self):
        C.__init__(self, 100)
        print 'dans D'

## l'appel à la méthode __str__ suit l'arbre d'héritage,
## donc si elle est définie dans la super classe, toutes
## les sous classes pourront utiliser la même méthode
## lorsque print est appelé.
        
I = C(20)
J = D()
print I, J

