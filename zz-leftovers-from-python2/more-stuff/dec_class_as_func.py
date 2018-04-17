# -*- coding: utf-8 -*-

# exemple de decorateur de classe, simple (sans argument) et implementé comme une fonction

# la classe Foo ne definit que le champ 'x'
# apres decoration elle a les champs 'id' et 'x' 
# qui sont tous les deux requis par le constructeur

# le decorateur prend en argument une classe et la modifie par effet de bord

def add_id_field (original_class):

    # on preserve le constructeur de la classe originelle
    orig_init = original_class.__init__

    # on definit un nouveau constructeur qui requiert et gere l'argument 'id'
    def __init__(self, id, *args, **kws):
        self.id = id
        orig_init(self, *args, **kws) # call the original __init__

    # qu'on attache a la classe originelle en ecrasant __init__
    original_class.__init__ = __init__ 

    return original_class


#################### voici comment on l'utilise

@add_id_field
class Foo:
    def __init__ (self, x):
        self.x=x
    # self.x est defini grace a add_id_field
    def __repr__ (self):
        return "id={id} - x={x}".format(id=self.id, x=self.x)

# Foo reconnait 'id' alors qu'on ne l'a pas precise dans la definition ci-dessus
foo = Foo(id=3, x=20)

print 'created Foo',foo
