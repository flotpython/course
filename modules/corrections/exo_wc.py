from nbautoeval import ExerciseFunction, Args, PPrintRenderer, PPrintCallRenderer


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

wc_inputs = (
    Args('''Python is a programming language
that lets you work quickly
and integrate systems more effectively.'''),
    Args(''),
    Args('abc'),
    Args('abc \t'),
    Args('a  bc \t'),
    Args(' \tabc \n'),
    Args(" ".join("abcdefg") + "\n"),
    Args('''The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
...'''),
    )

exo_wc = ExerciseFunction(
    wc, wc_inputs,
    call_renderer=PPrintCallRenderer(max_width=40, show_function=True),
    result_renderer=PPrintRenderer(width=15))
