from corrections.tools import correction_table 

def correction_inconnue (composite, connue, inconnue):
    def regroup ():
        return connue + inconnue + connue
    def right_answer (): 
        return composite
    return correction_table (regroup, right_answer, [()])
