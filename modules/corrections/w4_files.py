# -*- coding: utf-8 -*-
from corrections.exercice import correction_table, correction_table_1arg, exemple_table, exemple_table_1arg

import os

# helpers
def file_contents (filename):
    try:
        with open(filename) as input:
            return input.read()
    except:
        return ""

# the function as it is specified does not fit the correction_table model
# this decorator does the trick to transform a student-written function
# into something that correction_table can deal with
def tools_compliant (fun):
    def wrapped (in_name, out_name):
        # clean up output (in case the function does not create it
        try: 
            os.unlink(out_name)
        except:
            pass
        # run 
        fun(in_name,out_name)
        # return output's contents
        return file_contents (out_name)
    return wrapped

####################
# comptage ()
@tools_compliant
def comptage (in_filename, out_filename):
    with open(in_filename) as input:
        with open(out_filename,"w") as output:
            lineno = 0
            total_words = 0
            total_chars = 0
            for line in input:
                lineno += 1
                nb_words = len(line.split())
                total_words += nb_words
                nb_chars = len(line)
                total_chars += nb_chars
                output.write ("{}:{}:{}:{}".\
                              format(lineno,nb_words,nb_chars,line))
            output.write("{}:{}:{}\n".format(lineno,total_words, total_chars))

comptage_inputs = [
    ('data/romeo_and_juliet.txt', 'romeo_and_juliet.out'),
    ('data/lorem_ipsum.txt', 'lorem_ipsum.out'),
]

def correction_comptage (student_comptage):
    # decorate before passing to the comparison engine
    student_comptage = tools_compliant(student_comptage)
    return correction_table (student_comptage, comptage, comptage_inputs)

#
from IPython.display import HTML

# on lance la fonction dans un fichier temporaire et on le montre
def show_comptage (in_name, out_name, comptage, suffix):
    out_name += suffix
    comptage (in_name, out_name)
    try:
        input, output = file_contents (in_name), file_contents (out_name)
        os.unlink(out_name)
    except OSError:
        print "Votre fonction ne semble pas créer le fichier de sortie"
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
    
def exemple_comptage ():
    return show_comptage (*comptage_inputs[0], comptage=comptage, suffix=".ok")

def debug_comptage (student_comptage):
    return show_comptage (*comptage_inputs[0], comptage=student_comptage, suffix="")
