# -*- coding: utf-8 -*-

## un descripteur est une classe qui a au moins une méthode __get__ et
## éventuellement une méthode __set__ pour l'affectation et une
## méthode __del__ pour l'effacement de l'attribut


class Temperature:

    ## La méthode __get__ a trois paramètres. Le premier est
    ## l'instance du descripteur, le deuxième est l'instance de la
    ## classe sur laquelle on a mis de descripteur (c'est un général
    ## cet argument que l'on veut utiliser) et le dernier est la
    ## classe sur laquelle on a mis le descripteur.
    def __get__(self, inst, instype):
        return inst._temperature

    ## La méthode __set__ a trois paramètres également. Le premier est
    ## l'instance du descripteur, le deuxième est l'instance de la
    ## classe sur laquelle on a mis le descripteur, le troisième est
    ## l'objet à affecter (celui après le signe égal)
    def __set__(self, inst, t):   # self est l'instance du
                                  # descripteur, inst, l'instance de
                                  # la classe Maison, et t la valeur a
                                  # affecter
        if 5 < t and t < 25:
            inst._temperature = t
            return
            raise TemperatureError()

    
class Maison:
    def __init__(self, t):
        self._temperature = t

    temperature = Temperature()

class TemperatureError(Exception):
    pass

m = Maison(18)
print(f"il fait {m.temperature} chez moi")
m.temperature = 24

#3m30s

