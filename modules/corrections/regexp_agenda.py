# -*- coding: utf-8 -*-
from nbautoeval.exercise_regexp import ExerciseRegexp, ExerciseRegexpGroups
from nbautoeval.args import Args


agenda_strings = [
    "Daniel:Durand",
    "Jean:Dupont:",
    "Jean:Dupont::",
    ":Dupontel:",
    "Jean-Noël:Dupont-Nemours",
    "Charles-Henri:Du Pré",
    "Charles Henri:DuPré",
]


# @BEG@ name=agenda more=regexp
# l'exercice est basé sur re.match, ce qui signifie que
# le match est cherché au début de la chaine
# MAIS il nous faut bien mettre \Z à la fin de notre regexp,
# sinon par exemple avec la cinquième entrée le nom 'Du Pré'
# sera reconnu partiellement comme simplement 'Du'
# au lieu d'être rejeté à cause de l'espace
# 
# du coup pensez à bien toujours définir
# vos regexps avec des raw-strings
#
# remarquez sinon l'utilisation à la fin de :? pour signifier qu'on peut
# mettre ou non un deuxième séparateur ':' 
#   
agenda = r"\A(?P<prenom>[-\w]*):(?P<nom>[-\w]+):?\Z"
# @END@


agenda_groups = ['nom', 'prenom']


exo_agenda = ExerciseRegexpGroups(
    'agenda', agenda, agenda_groups,
    [Args(x) for x in agenda_strings],
    nb_examples = 0)


agenda_ko = r"\A(?P<prenom>[-\w]*):(?P<nom>[-\w]+):?"
