from nbautoeval import Args, ExerciseFunction, CallRenderer, PPrintRenderer


# @BEG@ name=aplatir
def aplatir(conteneurs):
    "retourne une liste des éléments des éléments de conteneurs"
    # on peut concaténer les éléments de deuxième niveau
    # par une simple imbrication de deux compréhensions de liste
    return [element for conteneur in conteneurs for element in conteneur]
# @END@


# @BEG@ name=aplatir more=bis
from itertools import chain

def aplatir_bis(conteneurs):
    # une utilisation astucieuse de itertools.chain
    return list(chain(*conteneurs))
# @END@


def aplatir_ko(conteneurs):
    return conteneurs


aplatir_inputs = [
    Args([]),
    Args([(1,)]),
    Args(([1],)),
    Args([(0, 6, 2), [1, ('a', 4), 5]]),
    Args(([ 1, [2, 3]], ('a', 'b', 'c'))),
    Args(([ 1, 6 ], ('c', 'b'), [2, 3])),
    Args((( 1, [2, 3]), [], ('a'), ['b', 'c'])),
]


exo_aplatir = ExerciseFunction(
    aplatir, aplatir_inputs, nb_examples=0,
#    call_renderer=CallRenderer(show_function=False),
    result_renderer=PPrintRenderer(width=20),
    font_size='x-small',
)
