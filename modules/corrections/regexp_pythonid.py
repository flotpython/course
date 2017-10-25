# -*- coding: utf-8 -*-
from nbautoeval.exercise_regexp import ExerciseRegexp, ExerciseRegexpGroups
from nbautoeval.args import Args

germs = [ 'aa1', 'A1a', '1Aa']
pythonid_strings = [ 'a', '_', '__', '-', ] + germs [:]
for germ in germs:
    for i in range (len(germ)):
        for seed in '-_':
            pythonid_strings.append(germ[:i]+seed+germ[i:])

# @BEG@ name=pythonid more=regexp
# un identificateur commence par une lettre ou un underscore
# et peut être suivi par n'importe quel nombre de
# lettre, chiffre ou underscore, ce qui se trouve être \w
# si on ne se met pas en mode unicode
pythonid = "[a-zA-Z_]\w*"
# @END@

# @BEG@ name=pythonid more=bis
# on peut aussi bien sûr l'écrire en clair
pythonid_bis = "[a-zA-Z_][a-zA-Z0-9_]*"
# @END@

exo_pythonid = ExerciseRegexp(
    'pythonid', pythonid,
    [Args(x) for x in pythonid_strings],
    nb_examples = 8)

pythonid_ko = "\w+"


