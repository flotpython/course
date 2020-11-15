from nbautoeval import (
    Args, ExerciseClass, ClassScenario, ClassExpression, ClassStatement)

# @BEG@ name=roman latex_size=footnotesize
import functools
from math import nan, isnan


@functools.total_ordering
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
        if isinstance(letters_or_integer, (int, str)):
            try:
                integer = int(letters_or_integer)
            except ValueError:
                letters = letters_or_integer.upper()
                self._decimal = Roman.roman_to_decimal(letters)
                self._roman = 'N' if isnan(self._decimal) else letters
            else:
                self._roman = Roman.decimal_to_roman(integer)
                self._decimal = nan if self._roman == 'N' else integer
        elif isnan(letters_or_integer):
            self._decimal = nan
            self._roman = 'N'
        else:
            raise TypeError(
              f"Cannot initialize Roman from {letters_or_integer}")
# @END@

# @BEG@ name=roman latex_size=footnotesize continued=true
    def __repr__(self):
        return f"{self._roman}={self._decimal}"

    def __str__(self):
        return f"{self._roman}"

    def __eq__(self, other):
        return self._decimal == other._decimal

    def __lt__(self, other):
        return self._decimal < other._decimal

    def __add__(self, other):
        return Roman(self._decimal + other._decimal)

    def __sub__(self, other):
        return Roman(self._decimal - other._decimal)

    def __int__(self):
        return self._decimal
# @END@

# @BEG@ name=roman latex_size=footnotesize continued=true
    symbols = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M'
    }

    @staticmethod
    def decimal_to_roman(decimal: int) ->str:
        """
        Conversion from decimal number to roman number.
        """
        if decimal <= 0:
            return 'N'

        roman = ""
        tens = 0

        try:
            while decimal:
                unit = decimal % 10
                if unit in (1, 2, 3):
                    roman = Roman.symbols[10 ** tens] * unit + roman
                elif 4 <= unit <= 8:
                    roman = (Roman.symbols[10 ** tens] * (5 - unit)
                             + Roman.symbols[5 * 10 ** tens]
                             + Roman.symbols[10 ** tens] * (unit - 5)
                             + roman)
                elif unit == 9:
                    roman = (Roman.symbols[10 ** tens]
                             + Roman.symbols[10 ** (tens + 1)]
                             + roman)
                tens += 1
                decimal //= 10
        except KeyError:
            return 'N'
        else:
            return roman
# @END@

# @BEG@ name=roman latex_size=footnotesize continued=true
    # inverted symbols
    isymbols = {v: k for k, v in symbols.items()}

    @staticmethod
    def roman_to_decimal(roman: str) ->int:
        """
        Conversion from roman number to decimal number
        """
        if not roman:
            return nan

        decimal = 0
        previous = None

        try:
            for r in roman:
                if previous and Roman.isymbols[previous] < Roman.isymbols[r]:
                    decimal -= 2 * Roman.isymbols[previous]
                decimal += Roman.isymbols[r]
                previous = r
        except KeyError:
            return nan
        else:
            return decimal
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
