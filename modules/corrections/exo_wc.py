from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


# @BEG@ name=wc
def wc(string):
    """
    Compte les nombres de lignes, de mots et de caractères

    Retourne une liste de ces 3 nombres (notez qu'usuellement
    on renverrait plutôt un tuple, qu'on étudiera la semaine prochaine)
    """
    # on peut tout faire avec la bibliothèque standard
    nb_lines = string.count('\n')
    nb_words = len(string.split())
    nb_bytes = len(string)
    return [nb_lines, nb_words, nb_bytes]
# @END@

wc_input = (
    Args('''Python is a programming language
that lets you work quickly
and integrate systems more effectively.'''),
    Args(''),
    Args('abc'),
    Args('abc \t'),
    Args(' \tabc \n'),
    Args('a b c d e f g h i j k l m n o p q r s t u v w x y z\n'),
    Args('''The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''),
    )

exo_wc = ExerciseFunction(wc, wc_input, layout_args=(80, 15, 15))
