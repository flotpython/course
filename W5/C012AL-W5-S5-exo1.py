# -*- coding: iso-8859-15 -*-

## créons une classe C et une sous classe sousC heritant de C

class C:
    def set_x(self, x):
        self.x = x
    def get_x(self):
        print self.x

## sousC hérite de C et surcharge la méthode get_x, c'est-à-dire
## redéfini une méthode déjà définie dans une super classe. 
class sousC(C):
    def get_x(self):
        print 'x est :', self.x


c = sousC()
sc = C()

## on peut remonter tout l'arbre d'héritage avec la variable
##  __class__ que l'on a déjà vu et __bases__ qui
## sur un classe retourne un tuple de ses super-classes. 

print c.__class__, c.__class__.__bases__
print sc.__class__, sc.__class__.__bases__

## On voit que donc que c et sc n'ont pas le même arbre d'héritage.
## get_x sera celle de sousC pour c et celle de C pour sc

c.set_x(10) # set_x de C
sc.set_x(20) # set_x de C

c.get_x() #get_x de sousC
sc.get_x() #get_x de sousC

## finissons par regarder les différents espaces de nommage
print c.__dict__, C.__dict__, sousC.__dict__ #noter les addresses differentes
                                             # de get_x dans C et sousC

## En Python tout est un objet, et les classes sont mutables,
## on peut donc ajouter une fonction a une classe après sa création

def f(self):
    print 'depuis C, x est:', self.x

## je redéfinis simplement la variable get_x dans l'espace de nommage
## de C pour référencer l'objet fonction référencé par f
C.get_x = f

## et sc vois la nouvelle fonction dans C
sc.get_x()
                                            
