# pylint: disable=c0111, c0103

from nbautoeval import (
    Args, ExerciseClass, ClassScenario, ClassExpression, ClassStatement)

# @BEG@ name=temperature
class Temperature:
    """
    a class that models temperatures

    example:
       >>> k = Temperature(kelvin=0); k
       0 °K
       >>> c = Temperature(celsius=0); c
       -273 °K
       >>> c.kelvin
       -273
       >>> k.celsius
       273
    """

    KELVIN = 273

    def __init__(self, *,
                 # that star sign above means that any parameter
                 # **MUST BE NAMED**, and that one cannot call
                 # e.g. Temperature(10)
                 kelvin=None, celsius=None):
        # in case no parameter is set
        if kelvin is None and celsius is None:
            kelvin = 0
        # in case both are set
        if kelvin is not None and celsius is not None:
            raise ValueError("Temperature wants only one among kelvin and celsius")
        # our unique internal data is _kelvin
        # but even from the constructor we'll
        # access it **only through properties**
        if kelvin is not None:
            # this calls _set_kelvin()
            self.kelvin = kelvin
        else:
            # this calls _set_celsius()
            self.celsius = celsius
# @END@


# @BEG@ name=temperature continued=true
    def __repr__(self):
        return f"{self._kelvin:d}°"


    def __eq__(self, other):
        return self._kelvin == other._kelvin


    def __sub__(self, other):
        return self._kelvin - other.kelvin


    # PROPERTIES

    def _get_kelvin(self):
        return self._kelvin
    def _set_kelvin(self, kelvin):
        if kelvin < 0:
            raise ValueError(f"Temperature needs a positive kelvin (got {kelvin}K)")
        self._kelvin = kelvin

    kelvin = property(_get_kelvin, _set_kelvin)


    def _get_celsius(self):
        # celsius + KELVIN = kelvin
        return self._kelvin - self.KELVIN
    def _set_celsius(self, celsius):
        self.kelvin = celsius + self.KELVIN

    celsius = property(_get_celsius, _set_celsius)

# @END@


temperature_scenarios = [
    # build and display an instance
    ClassScenario(
        Args(),
        ClassExpression("INSTANCE.kelvin"),
        ClassExpression("INSTANCE.celsius"),
    ),
    ClassScenario(
        Args(kelvin=0),
        ClassExpression("INSTANCE.kelvin"),
        ClassExpression("INSTANCE.celsius"),
    ),
    ClassScenario(
        Args(celsius=0),
        ClassExpression("INSTANCE.kelvin"),
        ClassExpression("INSTANCE.celsius"),
    ),
    ClassScenario(
        Args(kelvin=0),
        ClassExpression("INSTANCE.kelvin"),
        ClassExpression("INSTANCE.celsius"),
    ),
]

exo_temperature = ExerciseClass(
    Temperature, temperature_scenarios,
    nb_examples=0,
    obj_name='temp',
)


class Temperature_ko:

    def __init__(self, **kwds):
        self._kelvin = 200

    def __repr__(self):
        return f"{self._kelvin:2f}°"
