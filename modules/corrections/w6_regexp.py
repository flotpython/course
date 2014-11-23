from exercice import ExerciceRegexpGroups

inputs_urls = """
http://www.google.com/
https://www.google.com:8080/
http://user@www.google.com/
ftp://username:hispass@www.google.com/
""".split()


# @BEG@ urls 6 6

protos_list = ['http', 'https', 'ftp'] 

protos      = "(?P<proto>" + "|".join(protos_list) + ")"

user        = r"(?:(?P<user>\w+)(:(?P<password>[^:]+))@)?"

hostname    = r"(?P<hostname>[\w_.]+)"

port        = r"(:(?P<port>\d+))?"

regexp_urls = protos + "://" + user + hostname + port

# @END@

groups = [ 'proto', 'user', 'password', 'hostname', 'port' ]

exo_urls = ExerciceRegexpGroups('urls', regexp_urls, groups,
                                inputs_urls,
                                exemple_how_many=0,
                                correction_columns=(1000,1000,1000),
                            )


