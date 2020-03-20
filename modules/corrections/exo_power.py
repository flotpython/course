from nbautoeval import Args, ExerciseFunction, PPrintRenderer, PPrintCallRenderer


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
class Number:
    def __init__(self, number):
        self.number = number
    def __repr__(self):
        return f"Number({self.number})"

    @staticmethod
    def get_number(obj):
        if isinstance(obj, Number):
            return obj.number
        elif isinstance(obj, (int, float, complex)):
            return obj

    def __mul__(self, other):
        return Number(self.number * self.get_number(other))
    def __eq__(self, other):
        return self.number == self.get_number(other)


# ceci ne devrait pas marcher avec des instances de Number
def power_ko(x, n):
    return x ** n

   
inputs_power = [
    Args(2, 1),
    Args(2, 10),
    Args(1j, 4),
    Args(Number(1j), 4),
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
    call_renderer=PPrintCallRenderer(width=30),
    result_renderer=PPrintRenderer(width=40),
)
