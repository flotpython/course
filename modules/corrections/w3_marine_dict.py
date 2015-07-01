# -*- coding: utf-8 -*-
from exercice_function import ExerciceFunction
from args import Args

# @BEG@ week=3 sequence=2 name=index
def index(bateaux):
    """
    Calcule sous la forme d'un dictionnaire indexé par les ids
    un index de tous les bateaux présents dans la liste en argument
    Comme les données étendues et abrégées ont toutes leur id 
    en première position on peut en fait utiliser ce code
    avec les deux types de données
    """
    # c'est une simple compréhension de dictionnaire
    return {bateau[0]:bateau for bateau in bateaux}
# @END@

# @BEG@ week=3 sequence=2 name=index
def index2(bateaux):
    """
    La même chose mais de manière itérative
    """
    # si on veut décortiquer
    resultat = {}
    for bateau in bateaux:
        resultat [bateau[0]] = bateau
    return resultat
# @END@

class ExerciceIndex(ExerciceFunction):

    # on surcharge correction pour capturer les arguments
    def correction(self, student_index, bateaux):
        self.datasets = [Args(bateaux)]
        return ExerciceFunction.correction(self, student_index)

    # une fonction pour exposer le resultat attendu
    def resultat(self, bateaux):
        return self.solution(bateaux)

exo_index = ExerciceIndex(index, "inputs_gets_overridden")
    

# @BEG@ week=3 sequence=2 name=merge
def merge(extended, abbreviated):
    """
    Consolide des données étendues et des données abrégées
    comme décrit dans l'énoncé
    Le coût de cette fonction est linéaire dans la taille 
    des données (longueur des listes)
    """
    # on initialise le résultat avec un dictionnaire vide
    result = {}
    # pour les données étendues
    for ship in extended:
        # on affecte les 6 premiers champs
        # et on ignore les champs de rang 6 et au delà
        id, latitude, longitude, timestamp, name, country = ship[:6]
        # on crée une entrée dans le résultat, 
        # avec la mesure correspondant aux données étendues
        result[id] = [name, country, (latitude, longitude, timestamp)]
    # maintenant on peut compléter le résultat avec les données abrégées
    for id, latitude, longitude, timestamp in abbreviated:
        # et avec les hypothèses on sait que le bateau a déjà été 
        # inscrit dans le résultat, donc result[id] doit déjà exister
        # et on peut se contenter d'ajouter ls mesure abrégée
        # dans l'entrée correspondant dans result
        result[id].append((latitude, longitude, timestamp))
    # et retourner le résultat
    return result
# @END@

# @BEG@ week=3 sequence=2 name=merge
def merge2(extended, abbreviated):
    """
    Une deuxième version, linéaire également
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

# @BEG@ week=3 sequence=2 name=merge
def merge3(extended, abbreviated):
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

class ExerciceMerge(ExerciceFunction):

    # on surcharge correction pour capturer les arguments
    def correction(self, student_merge, extended, abbreviated):
        self.datasets = [Args(extended, abbreviated)]
        return ExerciceFunction.correction(self, student_merge)

    # une fonction pour exposer le resultat attendu
    def resultat(self, extended, abbreviated):
        return self.solution(extended, abbreviated)

exo_merge = ExerciceMerge(merge, "inputs_gets_overridden")
    
