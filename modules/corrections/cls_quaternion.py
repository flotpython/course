from nbautoeval import (
    Args, ExerciseClass, ClassScenario, ClassExpression, ClassStatement)

# @BEG@ name=quaternion latex_size=footnotesize
def number_str(x):
    if isinstance(x, int):
        return f"{x}"
    elif isinstance(x, float):
        return f"{x:.1f}"

class Quaternion:

    def __init__(self, a, b, c, d):
        self.implem = (a, b, c, d)


    def __repr__(self):
        labels = ['', 'i', 'j', 'k']
        # on prépare des morceaux comme '3', '2i', '4j', '5k'
        # mais seulement si la dimension en question n'est pas nulle
        parts = (f"{number_str(x)}{label}"
                 for x, label in zip(self.implem, labels) if x)

        # on les assemble avec un + au milieu
        full = " + ".join(parts)

        # si c'est vide c'est que self est nul
        return full if full != "" else "0"


    # c'est la partie intéressante
    def __add__(self, other):
        """defines q1 + q2)"""
        return Quaternion(*(x+y for x, y in zip(self.implem, other.implem)))


    def __mul__(self, other):
        """defines q1 * q2"""
        a1, b1, c1, d1 = self.implem
        a2, b2, c2, d2 = other.implem
        a = a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2
        b = a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2
        c = a1 * c2 + c1 * a2 + d1 * b2 - b1 * d2
        d = a1 * d2 + d1 * a2 + b1 * c2 - c1 * b2
        return Quaternion(a, b, c, d)


    def __eq__(self, other):
        """implements q1 == q2"""
        if isinstance(other, (bool, int, float)):
            return self == Quaternion(other, 0, 0, 0)
        elif isinstance(other, complex):
            return self == Quaternion(other.real, other.imag, 0, 0)
        elif isinstance(other, Quaternion):
            return self.implem == other.implem
        else:
            return False
# @END@

quaternion_scenarios = [
    ClassScenario(
        Args(1, 0, 0, 0),
        ClassExpression('INSTANCE == 1'),
    ),
    ClassScenario(
        Args(0, 1, 0, 0),
        ClassExpression('''# attention ici j c'est en fait notre i
INSTANCE == 1j'''),
    ),
    ClassScenario(
        Args(-1, 0, 0, 0),
        ClassExpression(
            'CLASS(0, 1, 0, 0) * CLASS(0, 1, 0, 0) == INSTANCE'
        ),
        ClassExpression(
            'CLASS(0, 0, 1, 0) * CLASS(0, 0, 1, 0) == INSTANCE'
        ),
        ClassExpression(
            'CLASS(0, 0, 0, 1) * CLASS(0, 0, 0, 1) == INSTANCE'
        ),
        ClassExpression(
            'CLASS(0, 1, 0, 0) * CLASS(0, 0, 1, 0) == CLASS(0, 0, 0, 1)'
        ),
        ClassExpression(
            'CLASS(0, 0, 1, 0) * CLASS(0, 0, 0, 1) == CLASS(0, 1, 0, 0)'
        ),
        ClassExpression(
            'CLASS(0, 0, 0, 1) * CLASS(0, 1, 0, 0) == CLASS(0, 0, 1, 0)'
        ),
    ),
    ClassScenario(
        Args(0, 1, 0, 0),
        ClassExpression(
            'CLASS(0, 1, 0, 0) * CLASS(0, 0, 1, 0) == -1'
        ),
    ),
]

exo_quaternion = ExerciseClass(
    Quaternion, quaternion_scenarios,
    nb_examples=0,
    obj_name='Q',
    header_font_size='small',
)
