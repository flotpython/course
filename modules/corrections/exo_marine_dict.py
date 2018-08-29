# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args

import json

#################### load data
# simplification is about keeping fewer entries in extended
simple_columns = 8
def simplify(entry):
    return entry[:simple_columns]

with open("data/marine-e1-ext.json") as feed:
    extended_full = json.load(feed)

with open("data/marine-e1-abb.json") as feed:
    abbreviated_full = json.load(feed)

# simplify extended entries - we don't need all these details
extended_full = [ simplify(e) for e in extended_full ]

### how many do we keep for this exercise
extract = 4

ids_all = [ t[0] for t in extended_full ]
ids_extract = ids_all[:extract]

extended = [ t for t in extended_full if t[0] in ids_extract ]
abbreviated = [ t for t in abbreviated_full if t[0] in ids_extract ]

def show():
    print("extended_full has {} {}-entries".
          format(len(extended_full), len(extended_full[0])))
    print("abbreviated_full has {} {}-entries"
          .format(len(abbreviated_full), len(abbreviated_full[0])))
    print("extended has {} entries".format(len(extended)))
    print("abbreviated has entries".format(len(abbreviated)))

#show()

def check(filename):
    with open(filename) as feed:
        extended = json.load(feed)
    ids = { t[0] for t in extended }
    full_ids = { (t[0], t[4]) for t in extended }
    print("{} has {} entries - {} different ids and {} different (id, name) tuples"
          .format(filename, len(extended),
                  len(ids), len(full_ids)))

#import glob
#for input in glob.glob("data/marine*ext*json"):
#    check(input)

#################### index
# @BEG@ name=index no_example=skip
def index(bateaux):
    """
    Calcule sous la forme d'un dictionnaire indexé par les ids
    un index de tous les bateaux présents dans la liste en argument
    Comme les données étendues et abrégées ont toutes leur id
    en première position on peut en fait utiliser ce code
    avec les deux types de données
    """
    # c'est une simple compréhension de dictionnaire
    return {bateau[0] : bateau for bateau in bateaux}
# @END@


# @BEG@ name=index more=bis
def index_bis(bateaux):
    """
    La même chose mais de manière itérative
    """
    # si on veut décortiquer
    resultat = {}
    for bateau in bateaux:
        resultat[bateau[0]] = bateau
    return resultat
# @END@



# @BEG@ name=index more=ter
def index_ter(bateaux):
    """
    Encore une autre, avec un extended unpacking
    """
    # si on veut décortiquer
    resultat = {}
    for bateau in bateaux:
        # avec un extended unpacking on peut extraire
        # le premier champ; en appelant le reste _
        # on indique qu'on n'en fera en fait rien
        id, *_ = bateau
        resultat[id] = bateau
    return resultat
# @END@




def index_ko(ships):
    return index(extended)

class ExoIndex(ExerciseFunction):

    # on surcharge correction pour capturer les arguments
    # par defaut on utilise 'abbreviated', utilisé dans le
    # notebook de validation
    def correction(self, student_index, bateaux=abbreviated):
        self.datasets = [Args(bateaux)]
        return ExerciseFunction.correction(self, student_index)

    # une fonction pour exposer le resultat attendu
    def resultat(self, bateaux):
        return self.solution(bateaux)

exo_index = ExoIndex(
    index, "inputs_gets_overridden",
    font_size='x-small', header_font_size='small',
)


##############################
##############################
# @BEG@ name=merge no_example=skip
def merge(extended, abbreviated):
    """
    Consolide des données étendues et des données abrégées
    comme décrit dans l'énoncé
    Le coût de cette fonction est linéaire dans la taille
    des données (longueur commune des deux listes)
    """
    # on initialise le résultat avec un dictionnaire vide
    result = {}
    # pour les données étendues
    # on affecte les 6 premiers champs
    # et on ignore les champs de rang 6 et au delà
    for id, latitude, longitude, timestamp, name, country, *_ in extended:
        # on crée une entrée dans le résultat,
        # avec la mesure correspondant aux données étendues
        result[id] = [name, country, (latitude, longitude, timestamp)]
    # maintenant on peut compléter le résultat avec les données abrégées
    for id, latitude, longitude, timestamp in abbreviated:
        # et avec les hypothèses on sait que le bateau a déjà été
        # inscrit dans le résultat, donc result[id] doit déjà exister
        # et on peut se contenter d'ajouter la mesure abrégée
        # dans l'entrée correspondante dans result
        result[id].append((latitude, longitude, timestamp))
    # et retourner le résultat
    return result
# @END@


# @BEG@ name=merge more=bis
def merge_bis(extended, abbreviated):
    """
    Une deuxième version, linéaire également
    mais qui utilise les indices plutôt que l'unpacking
    """
    # on initialise le résultat avec un dictionnaire vide
    result = {}
    # on remplit d'abord à partir des données étendues
    for ship in extended:
        id = ship[0]
        # on crée la liste avec le nom et le pays
        result[id] = ship[4:6]
        # on ajoute un tuple correspondant à la position
        result[id].append(tuple(ship[1:4]))
    # pareil que pour la première solution,
    # on sait d'après les hypothèses
    # que les id trouvées dans abbreviated
    # sont déja présentes dans le resultat
    for ship in abbreviated:
        id = ship[0]
        # on ajoute un tuple correspondant à la position
        result[id].append(tuple(ship[1:4]))
    return result
# @END@


# @BEG@ name=merge more=ter
def merge_ter(extended, abbreviated):
    """
    Une troisième solution
    à cause du tri que l'on fait au départ, cette
    solution n'est plus linéaire mais en O(n.log(n))
    """
    # ici on va tirer profit du fait que les id sont
    # en première position dans les deux tableaux
    # si bien que si on les trie,
    # on va mettre les deux tableaux 'en phase'
    #
    # c'est une technique qui marche dans ce cas précis
    # parce qu'on sait que les deux tableaux contiennent des données
    # pour exactement le même ensemble de bateaux
    #
    # on a deux choix, selon qu'on peut se permettre ou non de
    # modifier les données en entrée. Supposons que oui:
    extended.sort()
    abbreviated.sort()
    # si ça n'avait pas été le cas on aurait fait plutôt
    # extended = extended.sorted() et idem pour l'autre
    #
    # il ne reste plus qu'à assembler le résultat
    # en découpant des tranches
    # et en les transformant en tuples pour les positions
    # puisque c'est ce qui est demandé
    return {
        e[0] : e[4:6] + [ tuple(e[1:4]), tuple(a[1:4]) ]
        for (e,a) in zip (extended, abbreviated)
        }
# @END@

class ExoMerge(ExerciseFunction):

    # on surcharge correction pour capturer les arguments
    # idem on definit les arguments par defaut pour le code de validation
    def correction(self, student_merge,
                   extended=extended, abbreviated=abbreviated):
        self.datasets = [Args(extended, abbreviated)]
        return ExerciseFunction.correction(self, student_merge)

    # une fonction pour exposer le resultat attendu
    def resultat(self, extended, abbreviated):
        return self.solution(extended, abbreviated)

exo_merge = ExoMerge(
    merge, "inputs_gets_overridden",
    font_size='x-small', header_font_size='small',
)
