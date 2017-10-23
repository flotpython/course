# -*- coding: utf-8 -*-
from nbautoeval.exercise_regexp import ExerciseRegexp, ExerciseRegexpGroups
from nbautoeval.args import Args

######################################## pythonid
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
pythonid_regexp = "[a-zA-Z_]\w*"
# @END@

# @BEG@ name=pythonid more=v2
# on peut aussi bien sûr l'écrire en clair
pythonid_bis = "[a-zA-Z_][a-zA-Z0-9_]*"
# @END@

exo_pythonid = ExerciseRegexp(
    'pythonid', pythonid_regexp,
    [Args(x) for x in pythonid_strings],
    nb_examples = 8)

pythonid_ko = "\w+"

######################################## agenda
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
agenda_regexp = r"\A(?P<prenom>[-\w]*):(?P<nom>[-\w]+):?\Z"
# @END@

agenda_groups = ['nom', 'prenom']

exo_agenda = ExerciseRegexpGroups(
    'agenda', agenda_regexp, agenda_groups,
    [Args(x) for x in agenda_strings],
    nb_examples = 0)

######################################## phone
phone_strings = [
    "0123456789",
    "01234567890",
    "012345678",
    "1234567890",
    "+33123456789",
    "+3312345678",
    "+330123456789",
]

# @BEG@ name=phone more=regexp
# idem concernant le \Z final
#
# il faut bien backslasher le + dans le +33
# car sinon cela veut dire 'un ou plusieurs'
#
phone_regexp = r"(\+33|0)(?P<number>[0-9]{9})\Z"
# @END@

phone_groups = ['number']

exo_phone = ExerciseRegexpGroups(
    'phone', phone_regexp, phone_groups,
    [Args(x) for x in phone_strings],
    nb_examples = 0)

######################################## url
url_strings = """
http://www.google.com/a/b
HttPS://www.google.com:8080/a/b
http://user@www.google.com/a/b
FTP://username:hispass@www.google.com/
ssh://missing.ending.slash
gopher://unsupported.proto.col/
http:///missing/hostname/
""".split()

# @BEG@ name=url more=regexp
# en ignorant la casse on pourra ne mentionner les noms de protocoles
# qu'en minuscules
i_flag = "(?i)"

# pour élaborer la chaine (proto1|proto2|...)
protos_list = ['http', 'https', 'ftp', 'ssh', ] 
protos      = "(?P<proto>" + "|".join(protos_list) + ")"

# à l'intérieur de la zone 'user/password', la partie
# password est optionnelle - mais on ne veut pas le ':' dans
# le groupe 'password' - il nous faut deux groupes
password    = r"(:(?P<password>[^:]+))?"

# la partie user-password elle-même est optionnelle
user        = r"((?P<user>\w+){password}@)?".format(**locals())

# pour le hostname on accepte des lettres, chiffres, underscore et '.'
# attention à backslaher . car sinon ceci va matcher tout y compris /
hostname    = r"(?P<hostname>[\w\.]+)"

# le port est optionnel
port        = r"(:(?P<port>\d+))?"

# après le premier slash
path        = r"(?P<path>.*)"

# on assemble le tout
url = i_flag + protos + "://" + user + hostname + port + '/' + path
# @END@

groups = [ 'proto', 'user', 'password', 'hostname', 'port', 'path' ]

exo_url = ExerciseRegexpGroups(
    'url', url, groups,
    [Args(x) for x in url_strings],
    nb_examples=0,
)

url_ko = i_flag + protos + "://" + hostname + '/' + path
