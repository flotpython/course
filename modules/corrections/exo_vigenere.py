# pylint: disable=c0111

from nbautoeval import Args, ExerciseFunction, PPrintCallRenderer

# @BEG@ name=cesar latex_size=footnotesize

# pour passer des majuscules aux minuscules, il faut ajouter
# 97-65=32
import string

UPPER_TO_LOWER = ord('a') - ord('A')


def cesar(clear, key, encode=True):
    """
    retourne l'encryption du caractere <clear> par la clé <key>

    le caractère <key> doit être un caractère alphabétique ASCII
    c'est à dire que son ord() est entre ceux de 'a' et 'z' ou
    entre ceux de 'A' et 'Z'
    """

    if clear not in string.ascii_letters:
        return clear

    # le codepoint de la clé
    okey = ord(key)
    # on normalise la clé pour être dans les minuscules
    if key.isupper():
        okey += UPPER_TO_LOWER

    # la variable offset est un entier entre 1 et 26 qui indique
    # de combien on doit décaler; dans le tout premier
    # exemple, avec une clé qui vaut 'C' offset va valoir 3
    offset = (okey - ord('a') + 1)

    # si on encode, il faut ajouter l'offset,
    # et si on décode, il faut le retrancher
    if not encode:
        offset = -offset

    # ne reste plus qu'à faire le modulo
    # sauf que les bornes ne sont pas les mêmes
    # pour les majuscules ou pour les minuscules
    bottom = ord('A') if clear.isupper() else ord('a')

    return chr(bottom + (ord(clear) - bottom + offset) % 26)
# @END@


# @BEG@ name=cesar more=bis latex_size=footnotesize
from itertools import chain

# une autre approche entièrement consiste à précalculer
# toutes les valeurs et les ranger dans un dictionnaire
# qui va être haché par le tuple
# (clear, key)
# ça ne demande que 4 * 26 * 26 entrées dans le dictionnaire
# c'est à dire environ 2500 entrées, ce n'est pas grand chose

# on commence par le cas où le texte et la clé sont minuscules
# on rappelle que ord('a')=97
# avec nos définitions, une clé implique un décalage
# de (ord(k)-96), car une clé A signifie un décalage de 1
# par contre pour faire les calculs modulo 26
# il faut faire (ord(c)-97) de façon à ce que A=0 et Z=25
ENCODED_LOWER_LOWER = {
    (c, k): chr((ord(c) - 97 + ord(k) - 96) % 26 + 97)
    for c in string.ascii_lowercase
    for k in string.ascii_lowercase
}

# maintenant on peut facilement en déduire la table
# pour un texte en minuscule et une clé en majuscule
# il suffit d'appliquer ENCODED_LOWER_LOWER avec la clé minuscule
ENCODED_LOWER_UPPER = {
    (c, k): ENCODED_LOWER_LOWER[(c, k.lower())]
    for c in string.ascii_lowercase
    for k in string.ascii_uppercase
}
# @END@

# @BEG@ name=cesar more=bis continued=true latex_size=footnotesize

# enfin pour le cas où le texte est en majuscule, on
# va considérer l'union des deux premières tables
# (que l'on va balayer avec itertools.chain sur leurs items())
# et dire que pour encoder un caractère majuscule, on
# n'a qu'à prendre encoder la minuscule et mettre le résultat en majuscule
ENCODED_UPPER = {
    (c.upper(), k): value.upper()
    for (c, k), value in chain(ENCODED_LOWER_LOWER.items(),
                               ENCODED_LOWER_UPPER.items())
}

# maintenant on n'a plus qu'à construire
# l'union de ces 3 dictionnaires
ENCODE_LOOKUP = {}
ENCODE_LOOKUP.update(ENCODED_LOWER_LOWER)
ENCODE_LOOKUP.update(ENCODED_LOWER_UPPER)
ENCODE_LOOKUP.update(ENCODED_UPPER)

# et alors pour calculer la table inverse,
# c'est extrêmement simple, on dit que
# decode(encoded, key) == clear
# ssi
# encode(clear, key) == encoded
DECODE_LOOKUP = {
    (encoded, key): clear for (clear, key), encoded
    in ENCODE_LOOKUP.items()
}

# et maintenant pour faire le travail il suffit de
# faire exactement **UNE** recherche dans la table qui va bien
# ce qui est plus efficace en principe que la première approche
# si le couple (texte, clé) n'est pas trouvé alors on renvoie texte tel quel
def cesar_bis(clear, key, encode=True):
    lookup = ENCODE_LOOKUP if encode else DECODE_LOOKUP
    return lookup.get((clear, key), clear)
# @END@


inputs_cesar = [
    Args('=', 'C'),
    Args('A', 'C'),
    Args('a', 'C'),
    Args('A', 'c'),
    Args('D', 'C', encode=False),
    Args('A', 'L'),
    Args('Z', 'L'),
    Args('a', 'c'),
    Args('N', 'L'),
    Args('O', 'L'),
    Args('D', 'C', encode=False),
    Args('D', 'c', encode=False),
    Args('D', 'c', encode=False),
]

for c in 'aNz':
    for k in 'cJTx':
        for encode in True, False:
            inputs_cesar.append(Args(c, k, encode))


exo_cesar = ExerciseFunction(
    cesar, inputs_cesar,
    nb_examples = 6,
)

def cesar_ko(*args, **kwds):
    1/0
####################

# @BEG@ name=vigenere
from itertools import cycle

# grâce à une combinaison de zip et de itertools.cycle
# on peut itérer sur
# d'une part, le message
# et d'autre part, sur la clé, en boucle
#
# notez que
# (*) cycle ne s'arrête jamais
# (*) mais zip, lui, s'arrête au plus court de ses (ici deux)
#     ingrédients
# ce qui fait que zip(message, cycle(cle))
# fait exactement ce dont on a besoin

def vigenere(clear, key, encode=True):
    return "".join(
        cesar(c, k, encode)
        for c, k in zip(clear, cycle(key))
    )
# @END@

inputs_vigenere = [
    Args('ce message', 'cle'),
    Args('fq pqxvmlh', 'CLE', False),
    Args('une charogne', 'baudelaire'),
    Args("Rappelez-vous l'objet", 'Charles'),
    Args("que nous vîmes", 'baudelaire'),
]

exo_vigenere = ExerciseFunction(
    vigenere, inputs_vigenere,
    nb_examples=2,
    call_renderer=PPrintCallRenderer(width=25),
)

def vigenere_ko(*args, **kwds):
    1/0
