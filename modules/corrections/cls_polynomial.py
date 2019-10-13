# -*- coding: utf-8 -*-

# pylint: disable=c0111, c0103

from functools import reduce
from itertools import count, zip_longest, repeat, product

from nbautoeval.exercise_class import (
    ExerciseClass, ClassScenario, ClassExpression, ClassStatement)
from nbautoeval.args import Args

# @BEG@ name=polynomial
class Polynomial:
    """
    a class that models polynomials 
    
    example:
       >>> f = Polynomial(3, 2, 1)
       3Xˆ2 + 2X +1
       >>> f(10)
       321
    """

    # pretty print one monomial
    @staticmethod
    def repr_monomial(degre, coef):
        if coef == 0:
            return "0"
        elif degre == 0:
            return str(coef)
        elif degre == 1:
            return f"{coef}X"
        elif coef == 1:
            return f"X^{degre}"
        else:
            return f"{coef}X^{degre}"


    def __init__(self, *high_first):
        # internal structure is a tuple of coeficients, 
        # index 0 being the constant part
        # so we reverse the incoming parameters
        def skip_first_nulls(coefs):
            valid = False
            for coef in coefs:
                if coef:
                    valid = True
                if valid:
                    yield coef
        self.coefs = tuple(skip_first_nulls(high_first))[::-1]

    def __repr__(self):
        if not self.coefs:
            return '0'
        return " + ".join(reversed(
            [self.repr_monomial(d, c) for (d, c) in enumerate(self.coefs) if c]))

    def _get_degree(self):
        return 0 if not self.coefs else (len(self.coefs) - 1)
    degree = property(_get_degree)

    def __eq__(self, other):
        return self.coefs == other.coefs

    def __call__(self, param):
        """make instances callable"""
        # this is an interesting idiom
        # reduce allows to apply a 2-argument function
        # on an iterable from left to right 
        # that is to say for example
        # reduce(foo, [1, 2, 3, 4]) -> foo(1, foo(2, foo(3, 4))
        # in this code the function object created 
        # with the lambda expression is called a closure
        # it 'captures' the 'param' parameter in a function
        # that takes 2 arguments
        return reduce(lambda a, b: a*param + b, self.coefs[::-1])
    

    def __add__(self, other):
        """add 2 Polynomial instances"""
        # this interesting thing here is the use of zip_longest
        # so that our resulting Polynomial has a degree that is the max
        # of the degrees of our operands
        # also note the use of a so-called splat operator
        # beause we need to call e.g. Polynomial(1, 2, 3) and 
        # not Polynomial( [1, 2, 3])
        return Polynomial(
            *(c1+c2 for (c1, c2) in zip_longest(self.coefs, other.coefs,
                                                fillvalue=0)))

    def __mul__(self, other):
        """multiply 2 polynomials"""
        # a rather inefficient implementation
        # - because accessing a list by index is inefficient
        # just to illustrate product() and repeat()
        result_degree = self.degree + other.degree + 1
        result_coefs = list(repeat(0, result_degree))
        for (i, c), (j, d) in product(
                enumerate(self.coefs), enumerate(other.coefs)):
            result_coefs[i+j] += c*d
        return Polynomial(*reversed(result_coefs))

    def derivative(self):
        """
        the derivative is a polynomial as well
        """
        # 2 things are happening here
        # (*) we use the count() iterator; this never terminates
        #   except that it is embedded in a zip() that will
        #   terminate when iterating over our own coefficients expires
        # (*) here again observe the use of a splat operator

        derived_coefs = (n * c for (n, c) in zip(
                         count(1),
                         self.coefs[1:]
                        ))
        return Polynomial(*derived_coefs)
# @END@


polynomial_scenarios = [
    # build and display an instance
    ClassScenario(
        Args(), 
        ClassExpression("INSTANCE.degree"),
    ),
    ClassScenario(
        Args(0),
        ClassExpression("INSTANCE == CLASS() == CLASS(0, 0)"),
    ),
    ClassScenario(
        Args(1),
        ClassExpression("INSTANCE.degree"),
        ClassExpression("CLASS() == CLASS(0) == INSTANCE * CLASS()")
    ),
    ClassScenario(
        Args(1, 2, 3),
        ClassExpression("INSTANCE.degree"),
    ),
    ClassScenario(Args(1, 0, 3, 0, 0)),
    ClassScenario(
        Args(0, 0, 1, 0, 3),
        ClassExpression("INSTANCE == CLASS(1, 0, 3)"),
        ),
    ClassScenario(
        # init arguments
        Args(1, 2, 3),
        ClassExpression('INSTANCE(10)'),
        ClassExpression('INSTANCE(100)'),
    ),
    ClassScenario(
        # init arguments
        Args(1, 2, 3),
        ClassExpression('INSTANCE.derivative()'),
        ClassExpression('INSTANCE.derivative()(10)'),
    ),
    ClassScenario(
        Args(1, 2, 3),
        ClassExpression("INSTANCE + CLASS(3, 2, 1) == CLASS(0, 4, 4, 4)"),
        ClassExpression("CLASS() * INSTANCE"),
    ),
    # (3x2 + 2x + 1) * (x+2) = 3x3 + 8x2 + 5x + 2
    ClassScenario(
        Args(3, 2, 1),
        ClassExpression("INSTANCE * CLASS() == CLASS()"),
        ClassExpression("INSTANCE * CLASS(1) == INSTANCE"),
        ClassExpression("INSTANCE * CLASS(1, 2) == CLASS(3, 8, 5, 2)"),
    ),
]

exo_polynomial = ExerciseClass(
    Polynomial, polynomial_scenarios,
    layout='pprint',
    nb_examples=0,
    layout_args=(),
    obj_name='P',
)


class Polynomial_ko:
    
    def __init__(self, *args):
        self.coefs = args[::-1]
        
    def repr(self):
        return " + ".join(f"{c}X{d}" for c, d in zip(self.coefs, count()))