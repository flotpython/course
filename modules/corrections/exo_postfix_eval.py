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
    Args("10 +"),
    Args("10 20 30 +"),
    Args("10 20 30 oops"),
    Args(" 20 40 + 10 * "),
    Args("40 20 / 10 +"),
    Args("40 20 - 10 +"),
    Args("+"),
    Args("10 20 30 + - /"),
]

exo_postfix_eval = ExerciseFunction(
    postfix_eval,
    inputs,
    nb_examples=5,
    layout_args=(50, 15, 15),
)