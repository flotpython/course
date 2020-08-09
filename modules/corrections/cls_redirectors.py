# pylint: disable=c0111, c0103

import random
import string


from nbautoeval import (
    Args, ExerciseClass, ClassScenario, ClassExpression, ClassStatement)


def random_name():
    choice = string.ascii_letters + '_'
    length = random.randint(4, 6)
    return "".join(random.choice(choice) for _ in range(length))

def random_arg():
    return random.randint(0, 100)



# @BEG@ name=redirector1
class Redirector1:
    """
    a class that redirects any attribute as a lowercase
    dash-separated version of the attribute name
    """
    def __repr__(self):
        return "redirector"

    # desired behaviour is obtained by a simple
    # invokation of __getattr__
    # that is invoked each time an attribute is read
    # but is found missing in the local namespace
    def __getattr__(self, attribute_name):
        return attribute_name.lower().replace('_', '-')
# @END@

redirector1_scenarios = [
    # build and display an instance
    ClassScenario(
        Args(),
        ClassExpression("INSTANCE.foo"),
    ),
    ClassScenario(
        Args(),
        ClassExpression("INSTANCE.Foo_Bar"),
    ),
]

for r in range(3, 6):
    redirector1_scenarios.append(
        ClassScenario(
            Args(),
            ClassExpression(f"INSTANCE.{random_name()}")
        ))

exo_redirector1 = ExerciseClass(
    Redirector1, redirector1_scenarios,
    nb_examples=2,
    obj_name='R',
)


class Redirector1_ko:

    def __init__(self):
        self.foo = 'foo'
        self.Foo_Bar = 'foo-bar'

    def __repr__(self):
        return "redirector"






# @BEG@ name=redirector2
class Redirector2:
    """
    a class that redirects any attribute as a method that returns
    a string made of (*) the redirector's id, (*) the attribute name,
    and (*) the argument passed to the method
    """

    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return f"Redirector2({self.id})"

    # in this version, we rely on the same special method
    # but this time __getattr__ needs to return a method
    # that accepts one argument

    def __getattr__(self, methodname):
        # doit retourner une 'bound method'
        # du coup on ne recevra pas `self` comme premier paramètre
        def synthetic_method(argument):
            return f"{self.id} -> {methodname}({argument})"
        # optionnel, voir chapitre sur décorateurs
        synthetic_method.__name__ = methodname
        return synthetic_method
# @END@


redirector2_scenarios = [
    # build and display an instance
    ClassScenario(
        Args(1),
        ClassExpression("INSTANCE.foo(10)"),
    ),
    ClassScenario(
        Args(2),
        ClassExpression("INSTANCE.bar(20)"),
    ),
]

for r in range(3, 6):
    redirector2_scenarios.append(
        ClassScenario(
            Args(f"{r}"),
            ClassExpression(f"INSTANCE.{random_name()}({random_arg()})")
        ))

exo_redirector2 = ExerciseClass(
    Redirector2, redirector2_scenarios,
    nb_examples=2,
    obj_name='R',
)


class Redirector2_ko:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Redirector2({self.name})"

    def foo(self, argument):
        return f"{self.name} -> foo({argument})"
