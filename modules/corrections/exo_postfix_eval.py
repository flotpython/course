from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


# @BEG@ name=postfix_eval
def postfix_eval(chaine):
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
            operand2 = stack.pop()
            operand1 = stack.pop()
            if operator == '+':
                stack.append(operand1 + operand2)
            elif operator == '-':
                stack.append(operand1 - operand2)
            elif operator == '*':
                stack.append(operand1 * operand2)
            elif operator == '/':
                stack.append(operand1 // operand2)
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
    layout_args=(50, 15, 15),
)



# @BEG@ name=postfix_eval_typed
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
            operand2 = stack.pop()
            operand1 = stack.pop()
            if operator == '+':
                stack.append(operand1 + operand2)
            elif operator == '-':
                stack.append(operand1 - operand2)
            elif operator == '*':
                stack.append(operand1 * operand2)
            elif operator == '/':
                stack.append(divide(operand1, operand2))
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
    layout_args=(50, 50, 50),
    layout='pprint',
)