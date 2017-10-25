# -*- coding: utf-8 -*-
from nbautoeval.exercise_regexp import ExerciseRegexp, ExerciseRegexpGroups
from nbautoeval.args import Args

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
