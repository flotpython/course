# -*- coding: utf-8 -*-
from exercice_function import ExerciceRegexp, ExerciceRegexpGroups
from args import Args

######################################## pythonid
germs = [ 'aa1', 'A1a', '1Aa']
pythonid_strings = [ 'a', '_', '__', '-', ] + germs [:]
for germ in germs:
    for i in range (len(germ)):
        for seed in '-_':
            pythonid_strings.append(germ[:i]+seed+germ[i:])

# @BEG@ 6 6 regexp_pythonid
# un identificateur commence par une lettre ou un underscore
# et peut être suivi par n'importe quel nombre de
# lettre, chiffre ou underscore, ce qui se trouve être \w
# si on ne se met pas en mode unicode
regexp_pythonid = "[a-zA-Z_]\w*"
# @END@

# @BEG@ 6 6 regexp_pythonid
# on peut aussi bien sûr l'écrire en clair
regexp_pythonid2 = "[a-zA-Z_][a-zA-Z0-9_]*"
# @END@

exo_pythonid = ExerciceRegexp('pythonid', regexp_pythonid,
                              [Args(x) for x in pythonid_strings],
                              exemple_how_many = 8)

######################################## specials
# on ne prend pas le dernier pour le premier exo
specials_strings = [ '__y3s__', '_n0__', '___n0__',
                     '__0no__', '__n0_', '__n0___',
                     '__y3s_too__', '__y__', ]

# @BEG@ 6 6 regexp_specials
# il faut commencer par exactement 2 underscores
# donc le caractère suivant doit être une lettre
# ensuite on peut mettre ce qu'on veut comme alphanumérique,
# mais avant les deux derniers underscores on ne peut pas avoir
# un underscore
# enfin pour traiter le cas où la partie centrale est réduite
# à un seul caractère, on met une option - avec ()? 
regexp_specials = "__[a-zA-Z](\w*[a-zA-Z0-9])?__"
# @END@

exo_specials = ExerciceRegexp('specials', regexp_specials,
                               [Args(x) for x in specials_strings],
                               exemple_how_many = 0)

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

# @BEG@ 6 6 regexp_url
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
regexp_url = i_flag + protos + "://" + user + hostname + port + '/' + path
# @END@

groups = [ 'proto', 'user', 'password', 'hostname', 'port', 'path' ]

exo_url = ExerciceRegexpGroups(
    'url', regexp_url, groups,
    [Args(x) for x in url_strings],
    exemple_how_many=0,
    exemple_columns = (1000,1000),
    correction_columns=(1000,1000,1000),
)


