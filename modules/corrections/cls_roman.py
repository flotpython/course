from nbautoeval import (
    Args, ExerciseClass, ClassScenario, ClassExpression, ClassStatement)

# @BEG@ name=roman latex_size=footnotesize
from math import nan, isnan

class Roman:
    """
    a class to implement limited arithmetics on roman numerals

    example:
        >>> r1, r2 = Roman(2020), Roman('XXII')
        >>> r1
        MMXX=2020
        >>> r2
        XXII=22
        >>> r1-r2
        MCMXCVIII=1998
    """

    def __init__(self, letters_or_integer):
        if isinstance(letters_or_integer, str):
            self.letters = letters_or_integer.upper()
            # compute self.integer
            self.letters_to_integer()
        elif isinstance(letters_or_integer, int):
            self.integer = letters_or_integer
            self.integer_to_letters()
        elif isnan(letters_or_integer):
            self.letters = 'N'
            self.integer = nan
        else:
            raise ValueError(
                f"cannot initialize Roman from {letters_or_integer}")


    def __repr__(self):
        return f"{self.letters}={self.integer}"
# @END@

# @BEG@ name=roman latex_size=footnotesize continued=true
    def letters_to_integer(self):
        """
        return integer conversion
        """
        codes = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1,
            'N': nan,
        }
        self.integer = 0
        # we scan letters in reverse order
        # and keep track of the last one seen
        previous = 0

        for roman in self.letters[::-1]:
            n = codes[roman]
            # regular order: add
            if n >= previous:
                self.integer += n
            else:
                self.integer -= n
            previous = n
# @END@

# @BEG@ name=roman latex_size=footnotesize continued=true
    def integer_to_letters(self):
        codes = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I',
        }
        if self.integer <= 0 or self.integer >= 4000:
            self.integer = nan
            self.letters = 'N'
            return
        n = self.integer
        self.letters = ''
        while n:
            for code, letter in codes.items():
                if n >= code:
                    self.letters += letter
                    n -= code
                    break

    def __add__(self, other):
        return(Roman(self.integer + other.integer))
    def __sub__(self, other):
        return(Roman(self.integer - other.integer))
    def __eq__(self, other):
        return self.integer == other.integer
    def __int__(self):
        return self.integer
# @END@

roman_scenarios = [
    ClassScenario( Args(2020), ),
    ClassScenario(
        Args('MMXX'),
        ClassExpression("INSTANCE == CLASS(2020)"),
    ),
    ClassScenario(
        Args('MMIXX'),
        ClassExpression("INSTANCE + CLASS(19) == CLASS(2038)"),
        ClassExpression("INSTANCE - CLASS('MIM') == CLASS(20)"),
    ),
    ClassScenario(
        Args(5000),
    ),
    ClassScenario(
        Args(5000),
        ClassExpression("INSTANCE == CLASS(5000)"),
    ),
    ClassScenario(
        Args(2500),
        ClassExpression("INSTANCE + CLASS(2500)== CLASS(5000)"),
    ),
    ClassScenario(
        Args(1500),
        ClassExpression("int(INSTANCE) + 4500 == 6000")
    )
]

exo_roman = ExerciseClass(
    Roman, roman_scenarios,
    nb_examples=0,
    obj_name='R',
    header_font_size='small',
)