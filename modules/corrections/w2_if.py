from corrections.tools import correction_as_table 

def divisible (a,b): 
    return a%b==0 or b%a==0

divisible_inputs = [
    (20,10),
    (200,-10),
    (-200,10),
    (-200,-10),
    (10,200),
    (10,-200),
    (-10,200),
    (-10,-200),
    (8,12),
    (12,-8),
    (-12,8),
    (-12,-8),
]

def correction_divisible (divisible_student):
    return correction_as_table (divisible_student, divisible, divisible_inputs)
