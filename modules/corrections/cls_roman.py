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
                # pour gérer les chaînes de caractères
                # représentant un nombre entier
                # ex. : convertir '123' en l'entier 123
                integer = int(letters_or_integer)
            # si la conversion échoue, c'est qu'on a affaire à une str
            except ValueError:
                letters = letters_or_integer.upper()
                self._decimal = Roman.roman_to_decimal(letters)
                self._roman = 'N' if isnan(self._decimal) else letters
            # sinon c'est que c'est bien un entier
            else:
                self._roman = Roman.decimal_to_roman(integer)
                self._decimal = nan if self._roman == 'N' else integer
        elif isnan(letters_or_integer):
            self._decimal = nan
            self._roman = 'N'
        else:
            raise TypeError(
              f"Cannot initialize Roman from type {type(letters_or_integer)}")
# @END@

# @BEG@ name=roman latex_size=footnotesize continued=true
    def __repr__(self):
        return f"{self._roman}={self._decimal}"

    def __str__(self):
        return self._roman

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
    # table de correspondance des nombres décimaux et
    # des nombres romains clés
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

        # la chaîne de caractères résultante, construite étape par étape
        roman = ""
        # les puissances de 10 successives
        tens = 0

        try:
            while decimal:
                unit = decimal % 10
                if unit in (1, 2, 3):
                    # mettre unit fois le symbole de
                    # la puissance de 10 correspondante
                    roman = Roman.symbols[10 ** tens] * unit + roman
                elif 4 <= unit <= 8:
                    # mettre le symbole de 5 fois la puissance de 10
                    # correspondante précédé ou suivi du symbole de la
                    # puissance de 10 correspondante
                    roman = (Roman.symbols[10 ** tens] * (5 - unit)
                             + Roman.symbols[5 * 10 ** tens]
                             + Roman.symbols[10 ** tens] * (unit - 5)
                             + roman)
                elif unit == 9:
                    # le symbole de la puissance de 10 correspondante
                    # suivi de la puissance de 10 suivante
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
    # table de correspondance inversée
    # isymbols = inverted symbols
    isymbols = {v: k for k, v in symbols.items()}

    @staticmethod
    def roman_to_decimal(roman: str) ->int:
        """
        Conversion from roman number to decimal number
        """
        if not roman:
            return nan

        # la valeur décimale résultante, construite petit à petit
        decimal = 0
        # pour stocker le caractère précédent
        previous = None

        try:
            for r in roman:
                # Si le symbole précédent a une valeur moins grande,
                # il faut l'enlever une fois parce qu'on l'a compté
                # au coup précédent alors qu'il ne fallait pas,
                # et l'enlever une seconde fois parce qu'il faut
                # le soustraire à la valeur du symbole courant.
                # C'est ainsi que fonctionne le système numérique romain.
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
        Args('MMXIX'),
        ClassExpression("INSTANCE + CLASS(19) == CLASS(2038)"),
        ClassExpression("INSTANCE - CLASS('MCMXCIX') == CLASS(20)"),
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

# peut-être utile pour debugger ?
raw = """
MCMXXXIX=1939
MCMXL=1940
MCMXLI=1941
MCMXLII=1942
MCMXLIII=1943
MCMXLIV=1944
MCMXLV=1945
MCMXLVI=1946
MCMXLVII=1947
MCMXLVIII=1948
MCMXLIX=1949
MCML=1950
MCMLI=1951
MCMLII=1952
MCMLIII=1953
MCMLIV=1954
MCMLV=1955
MCMLVI=1956
MCMLVII=1957
MCMLVIII=1958
MCMLIX=1959
MCMLX=1960
MCMLXI=1961
MCMXCVIII=1998
MCMXCIX=1999
MM=2000
MMI=2001
MMII=2002
MMIII=2003
MMIV=2004
MMV=2005
MMVI=2006
MMVII=2007
MMVIII=2008
MMIX=2009
MMX=2010
MMXI=2011
MMXII=2012
MMXIII=2013
MMXIV=2014
MMXV=2015
MMXVI=2016
MMXVII=2017
MMXVIII=2018
MMXIX=2019
MMXX=2020
MMXXI=2021
MMXXII=2022
MMXXIII=2023
MMXXIV=2024
MMXXV=2025
MMXXVI=2026
MMXXVII=2027
MMXXVIII=2028
"""

for line in raw.split():
    letters, number = line.split('=')
    roman_scenarios.append(
        ClassScenario(
            Args(letters),
            ClassExpression(f"INSTANCE == CLASS({number})"),
        ))
    roman_scenarios.append(
        ClassScenario(
            Args(number),
            ClassExpression(f"INSTANCE == CLASS('{letters}')"),
        ))

exo_roman = ExerciseClass(
    Roman, roman_scenarios,
    nb_examples=0,
    obj_name='R',
    header_font_size='small',
)
