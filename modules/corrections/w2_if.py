from corrections.tools import correction_table, exemple_table

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
    return correction_table (divisible_student, divisible, divisible_inputs)

####################
def spam (l):
    if not l:
        pass
    elif len(l)%2 == 0:
        l[0],l[1]=l[1],l[0]
    else:
        l.pop()
    return l

spam_inputs = [
    [ [] ],
    [ ['spam'] ],
    [ ['spam', 'eggs' ] ],
    [ ['spam', 'eggs', 'bacon' ] ],
    [ [1,2,3,4 ] ],
    [ [1,2,3,4,5] ] ,
]

def correction_spam (spam_student):
    return correction_table (spam_student, spam, spam_inputs)

def exemple_spam ():
    return exemple_table ('spam', spam, spam_inputs, how_many=4)
