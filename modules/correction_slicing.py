from corrections import correction_as_table 

def correction_slicing (composite, connue, inconnue):
    def regroup ():
        return connue + inconnue + connue
    def right_answer (): 
        return composite
    return correction_as_table (regroup, right_answer, [()])
    
