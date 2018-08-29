# -*- coding: utf-8 -*-

### cannot remember why this one file is unicode but there was a good reason
# I expect some parts of the file make it to the platform itself, or something
# in any case there is a hack in corriges.py to take care of that

from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args

import os

####################
# the function as it is specified does not fit in the 'exercice' framework
# so here create helpers to make all this compliant
def file_contents(filename):
    try:
        with open(filename, encoding='utf-8') as input:
            return input.read()
    except:
        return ""

# this decorator does what it takes to transform a student-written function
# into something that exercice/correction_table can deal with
def exercice_compliant(fun):
    def wrapped(in_name, out_name):
        # clean up output (in case the function does not create it
        try:
            os.unlink(out_name)
        except:
            pass
        # run
        fun(in_name, out_name)
        # return output's contents
        return file_contents(out_name)
    wrapped.__name__ = fun.__name__
    wrapped.__doc__ = fun.__doc__
    return wrapped

### might end up in exercice if there's enough interest
from IPython.display import HTML

# on lance la fonction dans un fichier temporaire et on le montre
def show_comptage(in_name, out_name, comptage, suffix):
    out_name += suffix
    comptage(in_name, out_name)
    try:
        input, output = file_contents(in_name), file_contents(out_name)
        os.unlink(out_name)
    except OSError:
        print("Votre fonction ne semble pas créer le fichier de sortie")
        return
    html = ""
    html += "<table>"
    html += "<tr><th>Entrée</th></tr>"
    for line in input.split("\n"):
        html += "<tr><td>{}</td></tr>".format(line)
    html += "<tr><th>Sortie</th></tr>"
    for line in output.split("\n"):
        html += "<tr><td>{}</td></tr>".format(line)
    html += "</table>"
    return HTML(html)

@exercice_compliant
# @BEG@ name=comptage
def comptage(in_filename, out_filename):
    """
    retranscrit le fichier in_filename dans le fichier out_filename
    en ajoutant des annotations sur les nombres de lignes, de mots
    et de caractères
    """
    # on ouvre le fichier d'entrée en lecture
    with open(in_filename, encoding='utf-8') as input:
        # on ouvre la sortie en écriture
        with open(out_filename, 'w', encoding='utf-8') as output:
            lineno = 1
            # pour toutes les lignes du fichier d'entrée
            # le numéro de ligne commence à 1
            for line in input:
                # autant de mots que d'éléments dans split()
                nb_words = len(line.split())
                # autant de caractères que d'éléments dans la ligne
                nb_chars = len(line)
                # on écrit la ligne de sortie; pas besoin
                # de newline (\n) car line en a déjà un
                output.write(f"{lineno}:{nb_words}:{nb_chars}:{line}")
                lineno += 1
# @END@

@exercice_compliant
# @BEG@ name=comptage more=bis
def comptage_bis(in_filename, out_filename):
    """
    un peu plus pythonique avec enumerate
    """
    with open(in_filename, encoding='utf-8') as input:
        with open(out_filename, 'w', encoding='utf-8') as output:
            # enumerate(.., 1) pour commencer avec une ligne
            # numérotée 1 et pas 0
            for lineno, line in enumerate(input, 1):
                # une astuce : si on met deux chaines
                # collées comme ceci elle sont concaténées
                # et on n'a pas besoin de mettre de backslash
                # puisqu'on est dans des parenthèses
                output.write(f"{lineno}:{len(line.split())}:"
                             f"{len(line)}:{line}")
# @END@

@exercice_compliant
# @BEG@ name=comptage more=ter
def comptage_ter(in_filename, out_filename):
    """
    pareil mais avec un seul with
    """
    with open(in_filename, encoding='utf-8') as input, \
         open(out_filename, 'w', encoding='utf-8') as output:
        for lineno, line in enumerate(input, 1):
            output.write(f"{lineno}:{len(line.split())}:"
                         f"{len(line)}:{line}")
# @END@



def comptage_ko(in_filename, out_filename):
    with open(in_filename) as input:
        with open(out_filename, 'w') as output:
            for lineno, line in enumerate(input):
                output.write(f"{lineno}:{len(line.split())}:"
                             f"{len(line)}:{line}")

# on passe ceci à ExerciseFunction donc pas besoin de rajouter les **keywords
comptage_args = [
    Args('data/romeo_and_juliet.txt', 'romeo_and_juliet.out'),
    Args('data/lorem_ipsum.txt', 'lorem_ipsum.out'),
    Args('data/une_charogne_unicode.txt', 'une_charogne_unicode.out'),
]

class ExoComptage(ExerciseFunction):

    def correction(self, student_comptage):
        # call the decorator on the student code
        return ExerciseFunction.correction(self, exercice_compliant(student_comptage))

    # on recherche les noms des fichers d'entrée et de sortie
    # à utiliser pour l'exemple (ou le debug, on prend le même)
    # associés au premier jeu de données (self.datasets[0])
    # et là-dedans il nous faut regarder dans .args qui va contenir
    # un tuple avec les deux valeurs qu'on recherche
    def example(self):
        (input, output) = self.datasets[0].args
        return show_comptage(input, output, comptage=comptage, suffix=".ok")

    def debug(self, student_comptage):
        (input, output) = self.datasets[0].args
        return show_comptage(input, output, comptage=student_comptage, suffix="")


exo_comptage = ExoComptage(
    comptage, comptage_args,
    layout='text_backslash_n',
    layout_args=(None, 'xx-small', 'xx-small'),
    call_layout='void',
    font_size='x-small', header_font_size='small',
)
