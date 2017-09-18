# -*- coding: utf-8 -*-


## faisons une classe maison qui représente, par exemple, un système
## de domotique. Cette classe me permet de fixer une température de
## chauffage entre 5 et 25 degré. Regardons comment implémenter cette
## classe.

class Maison:
    def __init__(self, t):
        self._temperature = t

    def get_temperature(self):
        return f"{self._temperature}\u2103"  # unicode pour degré
                                             # celcius
    def set_temperature(self, t):
        if 5 < t and t < 25:
            self._temperature = t
            return
        raise TemperatureError()


class TemperatureError(Exception):
    pass

    
m = Maison(10)
print(f"il fait {m.get_temperature()} chez moi")
m.set_temperature(80)

#4m00

## on a donc implémenté un getter et un setter pour l'attribut
## temperature. Cependant, on voir bien que ça alourdi le code
## d'appeler systématiquement get_temperature() et set_temperature().

## On Python, on peut ajouter une couche de logique à l'appel de
## l'attribut avec un mécanisme que l'on nomme property. Regardons
## cela.



class Maison:
    def __init__(self, t):
        self._temperature = t
    
    def get_temperature(self):
        return f"{self._temperature}\u2103"
    
    def set_temperature(self, t):
        if 5 < t and t < 25:
            self._temperature = t
            return
        raise TemperatureError()

    temperature = property(get_temperature,    # new 
                           set_temperature)    # new

## Attention, le nom de la propriété temperature doit être différent
## du nom de l'attribut dans l'instance _temperature, sinon, il y aura
## un appel récursif lors de l'affectation ou du référencement de
## l'attribut.
    
class TemperatureError(Exception):
    pass
 
m = Maison(10)                                 # new
print(f"il fait {m.temperature} chez moi")     # new
m.temperature = 79                             # new


## avec ce mécanisme de property, il devient inutile d'implémenter
## systématiquement les getter et setter, il suffit, lorsqu'on a
## besoin d'un getter et setter pour un attribut de rajouter une
## property pour l'attribut concerné.

#6m00


