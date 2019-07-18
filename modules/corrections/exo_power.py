# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


# @BEG@ name=power
def power(x, n):
    """
    mise à la puissance en O(log2(n))
    """
    if n == 1:
        return x
    elif n % 2 == 0:
        # on met au carré power(x, n//2)
        root = power(x, n//2)
        return root * root
    else:
        return x * power(x, n-1)
    
# @END@

# pour ne pas se contenter de x**n
class Foo:
    def __init__(self, number):
        self.number = number
    def __mul__(self, other):
        return Foo(self.number * other.number)
    def __repr__(self):
        return f"number <{self.number}>"
    def __eq__(self, other):
        return self.number == other.number
    
# ceci ne devrait pas marcher avec des instances de Foo
def power_ko(x, n):
    return x ** n

   
inputs_power = [
    Args(2, 1),
    Args(2, 10),
    Args(1j, 4),
    Args(Foo(1j), 4),
]

powers = (2, 3, 1024, 1025)

inputs_power += [
    Args(3, n) for n in powers
] 

i_powers = (2*128, 2**128+1, 2*128-1)

inputs_power += [
    Args(1j, n) for n in i_powers
]

exo_power = ExerciseFunction(
    power, inputs_power,
    nb_examples = 4,
    layout_args = (30, 30, 30),
)
