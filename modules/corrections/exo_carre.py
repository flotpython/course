from nbautoeval import Args, ExerciseFunction, PPrintCallRenderer


##############################
# @BEG@ name=carre
def carre(line):
    # on enlève les espaces et les tabulations
    line = line.replace(' ', '').replace('\t','')
    # la ligne suivante fait le plus gros du travail
    # d'abord on appelle split() pour découper selon les ';'
    # dans le cas où on a des ';' en trop, on obtient dans le
    #    résultat du split un 'token' vide, que l'on ignore
    #    ici avec la clause 'if token'
    # enfin on convertit tous les tokens restants en entiers avec int()
    entiers = [int(token) for token in line.split(";")
               # en éliminant les entrées vides qui correspondent
               # à des point-virgules en trop
               if token]
    # il n'y a plus qu'à mettre au carré, retraduire en strings,
    # et à recoudre le tout avec join et ':'
    return ":".join([str(entier**2) for entier in entiers])
# @END@


# @BEG@ name=carre more=bis
def carre_bis(line):
    # pareil mais avec, à la place des compréhensions
    # des expressions génératrices que - rassurez-vous -
    # l'on n'a pas vues encore, on en parlera en semaine 5
    # le point que je veux illustrer ici c'est que c'est
    # exactement le même code mais avec () au lieu de []
    line = line.replace(' ', '').replace('\t','')
    entiers = (int(token) for token in line.split(";")
               if token)
    return ":".join(str(entier**2) for entier in entiers)
# @END@


# @BEG@ name=carre more=ter
def carre_ter(ligne):
    # On extrait toutes les valeurs séparées par des points-
    # virgules, on les nettoie avec la méthode strip
    # et on stocke le résultat dans une liste
    liste_valeurs = [t.strip() for t in ligne.split(';')]
    # Il ne reste plus qu'à calculer les carrés pour les
    # valeurs valides (non vides) et les remettre dans une str
    return ":".join([str(int(v)**2) for v in liste_valeurs if v])
# @END@


inputs_carre = [
    Args("1;2;3"),
    Args(" 2 ;  5;6;"),
    Args("; 12 ;  -23;\t60; 1\t"),
    Args("; -12 ; ; -23; 1 ;;\t"),
]


exo_carre = ExerciseFunction(
    carre, inputs_carre,
    nb_examples=0,
    call_renderer=PPrintCallRenderer(show_function=False, width=40)
    )


def carre_ko(s):
    return ":".join( str(i**2) for i in
                     (int(token) for token in s.split(';')))
