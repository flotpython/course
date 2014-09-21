from corrections.tools import correction_as_table

# example how to use
# 
def good_curve (a,b):
    return a ** 2 + 3 * a * b + 12
curve_sets = [ (0,1), (0,2), (0,3), (0,4), (1,2), (1,3), (1,4), (1,5) ]

def correction_curve (student_curve):
    return correction_as_table (student_curve, good_curve, curve_sets)
