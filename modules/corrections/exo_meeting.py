from nbautoeval import (Args, ExerciseFunction,
                        PPrintRenderer, PPrintCallRenderer, CallRenderer, TextContent)


# pprint apparently knowns how to cut strings
# but only where they have a space
class MeetingCallRenderer(CallRenderer):
    def render(self, call):
        function_name = self.visible_function_name(call)
        text = f"{function_name}(\n"
        # the incoming string
        arg = call.args.args[0]
        pieces = arg.split(";")
        def indent(piece):
            return f"  '{piece};'"
        args_str = "\n".join(indent(piece) for piece in pieces)
        # remove last ;
        args_str = args_str[:-2]
        text += args_str
        text += "')"
        return TextContent(text, is_code=True)

# @BEG@ name=meeting
def meeting(string):
    """découpage et tri"""
    persons = []
    person_strings = string.split(';')
    for person_string in person_strings:
        first, last = person_string.split(':')
        # il faut 2 niveaux de parenthèse car on insére un tuples
        persons.append((last, first))
    # on s'appuie sur le tri des tuples qui fait justement 
    # ce qu'on veut
    persons.sort()
    return "".join(f"({last}, {first})" for last, first in persons)
# @END@

# @BEG@ name=meeting more=bis
def meeting_bis(string):
    # on élabore une liste de [first, last]
    exploded = [ token.split(':') for token in string.split(';') ]
    # on met le nom en premier, dans des tuples
    persons = [ (last, first) for (first, last) in exploded ]
    # on trie, toujours avec le tri sur les tuples
    persons.sort()
    # on met en forme
    return "".join(f"({last}, {first})" for last, first in persons)
# @END@

inputs = [
    Args("Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;"
         "Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"),
]

exo_meeting = ExerciseFunction(
    meeting,
    inputs,
    #call_renderer=PPrintCallRenderer(max_width=20),
    call_renderer=MeetingCallRenderer(),
    result_renderer=PPrintRenderer(width=25),
    font_size='x-small',
)

def meeting_ko(string):
    ok = meeting(string)
    return ok.replace(' ', '')