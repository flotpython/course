from nbautoeval import Args, ExerciseFunction


# @BEG@ name=postfix_eval latex_size=footnotesize
def postfix_eval(chaine):
    """
    an evaluator for postfixed expressions

    all operands are integers, and division is integer division
    i.e. // i.e. quotient

    input is a string

    example:

    "5 3 + 4 2 - *" -> 16
    """
    stack = []
    # split the line into tokens
    tokens = chaine.split()
# @END@

# @BEG@ name=postfix_eval latex_size=footnotesize continued=true
    for token in tokens:
        operand = None
        try:
            # if it is an integer
            operand = int(token)
            # then all we need to do is push
            stack.append(operand)
        except ValueError:
            # if it's not, it's a little more complex
            operator = token
            # first our operations are all on 2 operands
            # so we can pop those, provided there's enough on the stack
            if len(stack) < 2:
                # error: not enough values to operate on
                return 'error-empty-stack'
            # first element in the stack is the rightmost operand
            right = stack.pop()
            left = stack.pop()
            # is it one of the supported operations ?
            if operator == '+':
                stack.append(left + right)
            elif operator == '-':
                stack.append(left - right)
            elif operator == '*':
                stack.append(left * right)
            elif operator == '/':
                stack.append(left // right)
            else:
                # error: unknown op
                return 'error-syntax'
    # at this point we must have **exactly one** item in the stack
    if len(stack) == 0:
        return 'error-empty-stack'
    elif len(stack) > 1:
        return 'error-unfinished'

    return stack.pop()
# @END@


# @BEG@ name=postfix_eval more=bis latex_size=footnotesize
# exact same behaviour, but this version uses a dictionary to
# avoid the awkward part where we check for a supported operator

# use a dictionary , to map
#    each operator sign (like '+')
#    -> to a binary function (i.e. that accepts 2 parameter)
#
# we could have defined these 4 functions manually, but
# it turns out the operator module comes in handy
from operator import add, mul, sub, floordiv

operator_map = { '+' : add, '*': mul, '-': sub, '/' : floordiv }

def postfix_eval_bis(chaine):
    """
    same
    """
    stack = []
    tokens = chaine.split()
    for token in tokens:
        operand = None
        try:
            operand = int(token)
            stack.append(operand)
        except ValueError:
            operator = token
            if len(stack) < 2:
                # error: not enough values to operate on
                return 'error-empty-stack'
            right = stack.pop()
            left = stack.pop()
            # operator here is typically '+'
            # and its value in the map is a binary function
            if operator in operator_map:
                function = operator_map[operator]
                stack.append(function(left, right))
            else:
                # error: unknown op
                return 'error-syntax'
    if len(stack) == 0:
        return 'error-empty-stack'
    elif len(stack) > 1:
        return 'error-unfinished'

    return stack.pop()
# @END@


inputs = [
    Args("20 40 + 10 *"),
    Args(" 20 40 + 10 * "),
    Args("20 6 6 + /"),
    Args("20 18 -6 + /"),
    Args("10 -3 /"),
    Args("10 +"),
    Args("10 20 30 +"),
    Args("10 20 30 oops"),
    Args("40 20 / 10 +"),
    Args("40 20 - 10 +"),
    Args("+"),
    Args("10 20 30 + - /"),
]

exo_postfix_eval = ExerciseFunction(
    postfix_eval,
    inputs,
    nb_examples=8,
)


# @BEG@ name=postfix_eval_typed latex_size=footnotesize
def postfix_eval_typed(chaine, type):
    """
    a postfix evaluator, using a parametric type
    that can be either `int`, `float` or `Fraction` or similars
    """
    def divide(a, b):
        if issubclass(type, int):
            return a // b
        else:
            return a / b
    stack = []
    tokens = chaine.split()
    for token in tokens:
        operand = None
        try:
            operand = type(token)
            stack.append(operand)
        except ValueError:
            operator = token
            if len(stack) < 2:
                # error: not enough values to operate on
                return 'error-empty-stack'
            right = stack.pop()
            left = stack.pop()
            if operator == '+':
                stack.append(left + right)
            elif operator == '-':
                stack.append(left - right)
            elif operator == '*':
                stack.append(left * right)
            elif operator == '/':
                stack.append(divide(left, right))
            else:
                # error: unknown op
                return 'error-syntax'
    # we must have exactly one item in the stack
    if len(stack) == 0:
        return 'error-empty-stack'
    elif len(stack) > 1:
        return 'error-unfinished'

    return stack.pop()
# @END@

from fractions import Fraction

inputs_typed = [
    Args("20 40 + 10 *", int),
    Args("20 40 + 10 *", float),
    Args("20 40 + 10 *", Fraction),
    Args("20 6 6 + /", int),
    Args("20 6 6 + /", float),
    Args("20 6 6 + /", Fraction),
    Args("20 18 -6 + /", int),
    Args("20 18 -6 + /", float),
    Args("20 18 -6 + /", Fraction),
]

exo_postfix_eval_typed = ExerciseFunction(
    postfix_eval_typed,
    inputs_typed,
    nb_examples=3,
    font_size='x-small',
)
