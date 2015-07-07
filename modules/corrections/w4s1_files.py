# -*- coding: utf-8 -*-

from __future__ import print_function

### cannot remember why this one file is unicode but there was a good reason
# I expect some parts of the file make it to the platform itself, or something
# in any case there is a hack in corriges.py to take care of that

from exercice_function import ExerciceFunction
from args import Args

import os

#################### 
# the function as it is specified does not fit in the 'exercice' framework
# so here create helpers to make all this compliant
def file_contents(filename):
    try:
        with open(filename) as input:
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
    
####################
# comptage ()
@exercice_compliant
# @BEG@ week=4 sequence=1 name=comptage 
def comptage(in_filename, out_filename):
    """
    retranscrit le fichier in_filename dans le fichier out_filename
    en ajoutant des annotations sur les nombres de lignes, de mots
    et de caractères
    """
    # on ouvre le fichier d'entrée en lecture
    # on aurait pu mettre open (in_filename, 'r')
    with open(in_filename) as input:
        # on ouvre la sortie en écriture
        with open(out_filename, "w") as output:
            # initialisations
            lineno = 0
            total_words = 0
            total_chars = 0
            # pour toutes les lignes du fichier d'entrée
            for line in input:
                # on maintient le nombre de lignes
                # qui est aussi la ligne courante
                lineno += 1
                # autant de mots que d'éléments dans split()
                nb_words = len(line.split())
                total_words += nb_words
                # autant de caractères que d'éléments dans la ligne
                nb_chars = len(line)
                total_chars += nb_chars
                # on écrit la ligne de sortie; pas besoin
                # de newline (\n) car line en a déjà un
                output.write("{}:{}:{}:{}"
                             .format(lineno, nb_words, nb_chars, line))
            # on écrit la ligne de synthèse
            output.write("{}:{}:{}\n".\
                         format(lineno, total_words, total_chars))
# @END@

def comptage_ko(in_filename, out_filename):
    with open(in_filename) as input:
        with open(out_filename, 'w') as output:
            for lineno, line in enumerate(input):
                output.write("{}:{}:{}:{}"
                             .format(lineno,
                                     len(line.split()),
                                     len(line),
                                     line))

# on passe ceci à Exercice donc pas besoin de rajouter les **keywords
comptage_args = [
    Args('data/romeo_and_juliet.txt', 'romeo_and_juliet.out'),
    Args('data/lorem_ipsum.txt', 'lorem_ipsum.out'),
]
for arg in comptage_args:
    arg.set_layout('void')

class ExerciceComptage(ExerciceFunction):

    def correction(self, student_comptage):
        self.layout = 'text_backslash_n'
        self.layout_args = (None, 'xx-small', 'xx-small')
        # call the decorator on the student code
        return ExerciceFunction.correction(self, exercice_compliant(student_comptage))

    # on recherche les noms des fichers d'entrée et de sortie
    # à utiliser pour l'exemple (ou le debug, on prend le même)
    # associés au premier jeu de données (self.datasets[0])
    # et là-dedans il nous faut regarder dans .args qui va contenir
    # un tuple avec les deux valeurs qu'on recherche
    def exemple(self):
        (input, output) = self.datasets[0].args
        return show_comptage(input, output, comptage=comptage, suffix=".ok")

    def debug(self, student_comptage):
        (input, output) = self.datasets[0].args
        return show_comptage(input, output, comptage=student_comptage, suffix="")


exo_comptage = ExerciceComptage(comptage, comptage_args)
