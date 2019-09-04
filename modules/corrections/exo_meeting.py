from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


# @BEG@ name=meeting
def meeting(string):
    persons = []
    person_strings = string.split(';')
    for person_string in person_strings:
        first, last = person_string.split(':')
        persons.append([first, last])
    persons.sort(key=lambda person: f"{person[1]}+{person[0]}")
    return "".join(f"({last}, {first})" for first, last in persons)
# @END@


inputs = [
    Args("Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;"
         "Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"),
]

exo_meeting = ExerciseFunction(
    meeting,
    inputs,
#    nb_examples=0,
#    layout_args=(40, 40 , 25),
#    layout='truncate', 
    #layout='pprint', 
    #layout='text', 
    #layout='text_backslash_n', 
    #layout_args=(10, 'xx-small', 'xx-small'),
)
