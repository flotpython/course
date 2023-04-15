from nbautoeval import Args, ExerciseFunction, PPrintCallRenderer, PPrintRenderer


# load all the data
import json

with open("data/marine-e2-ext.json") as feed:
    extended_full = json.load(feed)

with open("data/marine-e2-abb.json") as feed:
    abbreviated_full = json.load(feed)

from .exo_marine_dict import simplify
extended_full = [ simplify(e) for e in extended_full ]


# @BEG@ name=diff latex_size=footnotesize no_example=skip
def diff(extended, abbreviated):
    """Calcule comme demandé dans l'exercice, et sous formes d'ensembles
    (*) les noms des bateaux seulement dans extended
    (*) les noms des bateaux présents dans les deux listes
    (*) les ids des bateaux seulement dans abbreviated
    """

    ### on n'utilise que des ensembles dans tous l'exercice

    # les ids de tous les bateaux dans extended
    # avec ce qu'on a vu jusqu'ici le moyen le plus naturel
    # consiste à calculer une compréhension de liste
    # et à la traduire en ensemble comme ceci
    extended_ids = set([ship[0] for ship in extended])

    # les ids de tous les bateaux dans abbreviated
    # je fais exprès de ne pas mettre les []
    # de la compréhension de liste, c'est pour vous introduire
    # les expressions génératrices - voir semaine 5
    abbreviated_ids = set(ship[0] for ship in abbreviated)

    # les ids des bateaux seulement dans abbreviated
    # une difference d'ensembles
    abbreviated_only_ids = abbreviated_ids - extended_ids

    # les ids des bateaux dans les deux listes
    # une intersection d'ensembles
    both_ids = abbreviated_ids & extended_ids

    # les ids des bateaux seulement dans extended
    # ditto
    extended_only_ids = extended_ids - abbreviated_ids

    # pour les deux catégories où c'est possible
    # on recalcule les noms des bateaux
    # par une compréhension d'ensemble
    both_names = \
        set([ship[4] for ship in extended if ship[0] in both_ids])
    extended_only_names = \
        set([ship[4] for ship in extended if ship[0] in extended_only_ids])
    # enfin on retourne les 3 ensembles sous forme d'un tuple
    return extended_only_names, both_names, abbreviated_only_ids
# @END@


# @BEG@ name=diff latex_size=footnotesize more=bis
def diff_bis(extended, abbreviated):
    """
    Même code mais qui utilise les compréhensions d'ensemble
    que l'on n'a pas encore vues - à nouveau, voir semaine 5
    mais vous allez voir que c'est assez intuitif
    """
    extended_ids = {ship[0] for ship in extended}
    abbreviated_ids = {ship[0] for ship in abbreviated}

    abbreviated_only_ids = abbreviated_ids - extended_ids
    both_ids = abbreviated_ids & extended_ids
    extended_only_ids = extended_ids - abbreviated_ids

    both_names = \
          {ship[4] for ship in extended if ship[0] in both_ids}
    extended_only_names = \
          {ship[4] for ship in extended if ship[0] in extended_only_ids}

    return extended_only_names, both_names, abbreviated_only_ids
# @END@


# @BEG@ name=diff latex_size=footnotesize more=ter
def diff_ter(extended, abbreviated):
    """
    Idem sans les calculs d'ensembles intermédiaires
    en utilisant les conditions dans les compréhensions
    """
    extended_ids =     {ship[0] for ship in extended}
    abbreviated_ids =  {ship[0] for ship in abbreviated}
    abbreviated_only = {ship[0] for ship in abbreviated
                        if ship[0] not in extended_ids}
    extended_only =    {ship[4] for ship in extended
                        if ship[0] not in abbreviated_ids}
    both =             {ship[4] for ship in extended
                        if ship[0] in abbreviated_ids}
    return extended_only, both, abbreviated_only
# @END@


# @BEG@ name=diff latex_size=footnotesize more=quater
def diff_quater(extended, abbreviated):
    """
    Idem sans indices
    """
    extended_ids =     {id for id, *_ in extended}
    abbreviated_ids =  {id for id, *_ in abbreviated}
    abbreviated_only = {id for id, *_ in abbreviated
                        if id not in extended_ids}
    extended_only =    {name for id, _, _, _, name, *_ in extended
                        if id not in abbreviated_ids}
    both =             {name for id, _, _, _, name, *_ in extended
                        if id in abbreviated_ids}
    return extended_only, both, abbreviated_only
# @END@


# une version qui ne marche pas pour la validation
def diff_ko(extended, abbreviated):
     extended_ids =     {ship[0] for ship in extended}
     abbreviated_only = {ship[0] for ship in abbreviated if ship[0] not in extended_ids}
     extended_only =    {ship[4] for ship in extended    if ship[0] not in abbreviated_only}
     both =             {ship[4] for ship in extended    if ship[0] in abbreviated_only}
     return extended_only, both, abbreviated_only


########## expose simpler set of data for clearer correction
# keep only 2 items in each category (ext_only, abb_only, and both)
selection = 2
e_o_names, b_names, a_o_ids = diff(extended_full, abbreviated_full)
# find (selection?) entries in extended_full with the first name in e_o_n
names = set()
for i in range(selection): names.add(e_o_names.pop())
e_o = [ e for e in extended_full if e[4] in names ]
#print(f"e_o has {len(e_o)} elts")


# find (selection?) entries in extended_full with the first name in b_n
names = set()
ids = set()
b_e = []
for i in range(selection):
    names.add(b_names.pop())
for e in extended_full:
    if e[4] in names:
        b_e.append(e)
        ids.add(e[0])
#print(f"b_e has {len(b_e)} elts")


# find (selection?) entries in abbreviated_full about the boats in b_e
b_a = [ a for a in abbreviated_full if a[0] in ids ]
#print(f"b_a has {len(b_a)} elts")


# find (selection) entries in abbreviated_full with the first id in a_o_i
ids = set()
for i in range(selection):
    ids.add(a_o_ids.pop())
a_o = [ a for a in abbreviated_full if a[0] in ids ]
#print(f"a_o has {len(a_o)} elts")

extended = e_o + b_e
abbreviated = b_a + a_o


##############################
# on passe des copies pour éviter qu'un bout de code ne pollue
# tout l'exercice en modifiant le master
import copy

# a single dataset is enough
class ExoDiff(ExerciseFunction):

    def correction(self, student_diff, extended=extended, abbreviated=abbreviated):
        self.datasets = [Args(extended, abbreviated).clone('deep')]
        return ExerciseFunction.correction(self, student_diff)

    def resultat(self, extended, abbreviated):
        return self.solution(extended, abbreviated)

exo_diff = ExoDiff(
    diff, "inputs_gets_overridden",
    font_size='x-small',
    call_renderer=PPrintCallRenderer(width=20),
    result_renderer=PPrintRenderer(width=30),
)


##############################
# one-shot code
# purify entries
# remove duplicates of different ships with the same name
def purify(filename):
    with open(filename) as feed:
        extended = json.load(feed)
    duplicate_ids = set()
    hash_name_to_id = {}
    for e in extended:
        id = e[0]
        name = e[4]
        if name not in hash_name_to_id:
            hash_name_to_id[name] = id
        else:
            previous_id = hash_name_to_id[name]
            if id != previous_id:
                print(f"Found duplicate {id} and {previous_id} -> {name}")
                duplicate_ids.add(id)

    print(f"Input has {len(extended)} entries")
    print(f"Found {len(duplicate_ids)} duplicate ids")
    purified = [ e for e in extended
                 if e[0] not in duplicate_ids ]
    print(f"Purified has {len(purified)} entries")

    pure_filename = filename + ".pure"
    with open(pure_filename, 'w') as store:
        json.dump(purified, store)
    print(f"Wrote {pure_filename}")
