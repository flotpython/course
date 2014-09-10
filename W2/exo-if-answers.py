def print_divisible (a,b):
    if a%b==0 or b%a==0:
        print 'DIVISIBLE'
    else:
        print 'NON'

def divisible (a,b):
    if a%b==0 or b%a==0:
        return True
    else:
        return False

# ou plus simplement
def divisible (a,b): 
    return a%b==0 or b%a==0
