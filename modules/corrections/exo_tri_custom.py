from nbautoeval import Args, ExerciseFunction, PPrintRenderer, PPrintCallRenderer


# @BEG@ name=tri_custom
def tri_custom(liste):
    """
    trie une liste en fonction du critère de l'énoncé
    """
    # pour le critère de tri on s'appuie sur l'ordre dans les tuples
    # c'est-à-dire
    # ((1, 2) <= (1, 2, 0) <= (1, 3) <= (2, 0)) == True
    # du coup il suffit que la fonction critère renvoie
    # selon la présence de p2, un tuple de 2 ou 3 éléments
    def custom_key(item):
        if 'p2' in item:
            return (item['p'], item['n'], item['p2'])
        return (item['p'], item['n'])
    liste.sort(key=custom_key)
    return liste
# @END@

# @BEG@ name=tri_custom more=bis
def tri_custom_bis(liste):
    """
    tri avec une fonction lambda et une expression conditionnelle
    """
    # la même chose avec une lambda
    # l'expression conditionnelle est nécessaire ici, car
    # dans une lambda on est limité à des expressions
    liste.sort(key=lambda d: (d['p'], d['n'], d['p2']) 
                              if 'p2' in d
                              else (d['p'], d['n']))
    return liste
# @END@

# @BEG@ name=tri_custom more=ter
def tri_custom_ter(liste):
    """
    tri avec une fonction lambda et une compréhension de tuple
    """
    # sous cette forme, tout devient plus simple si on devait 
    # avoir d'autres colonnes à prendre en compte
    keys = ('p', 'n', 'p2')
    liste.sort(key=lambda d: tuple(d[k] for k in keys if k in d))
    return liste
# @END@

items1 = [
    dict(n='Martin', p='Jean'),
    dict(n='Martin', p='Jeanne'),
    dict(n='Martin', p='Jeanne', p2='Marie'),
    dict(n='Martin', p='Jean', p2='Pierre'),
    dict(n='Martin', p='Jean', p2='Paul'),
    dict(n='Martin', p='Jeanneot'),
    dict(n='Dupont', p='Alex'),
    dict(n='Dupont', p='Laura'),
    dict(n='Dupont', p='Laura', p2='Marie'),
    dict(n='Dupont', p='Alex', p2='Pierre'),
    dict(n='Dupont', p='Alex', p2='Paul'),
    dict(n='Dupont', p='Alexandre'),
]

items2 = [
    dict(n='Smith', p='Bob'),
    dict(n='Smith', p='Bob', p2='Paul'),
    dict(n='Smith', p='Charlie'),
    dict(n='Smith', p='John'),
    dict(n='Forbes', p='Bob'),
    dict(n='Forbes', p='Charlie'),
    dict(n='Forbes', p='John'),
]

items3 = items1 + items2

"""
to generate the actual inputs
import random

inputs = []
for i in range(3):
    for template in [items1, items2, items3]:
        input = template[:]
        random.shuffle(input)
        inputs.append(input)

inputs
"""

inputs = [[{'n': 'Dupont', 'p': 'Laura', 'p2': 'Marie'},
  {'n': 'Martin', 'p': 'Jean'},
  {'n': 'Martin', 'p': 'Jeanneot'},
  {'n': 'Dupont', 'p': 'Alex'},
  {'n': 'Martin', 'p': 'Jean', 'p2': 'Pierre'},
  {'n': 'Martin', 'p': 'Jeanne'},
  {'n': 'Dupont', 'p': 'Alexandre'},
  {'n': 'Dupont', 'p': 'Alex', 'p2': 'Pierre'},
  {'n': 'Martin', 'p': 'Jeanne', 'p2': 'Marie'},
  {'n': 'Dupont', 'p': 'Alex', 'p2': 'Paul'},
  {'n': 'Martin', 'p': 'Jean', 'p2': 'Paul'},
  {'n': 'Dupont', 'p': 'Laura'}],
 [{'n': 'Smith', 'p': 'Bob'},
  {'n': 'Smith', 'p': 'Charlie'},
  {'n': 'Smith', 'p': 'Bob', 'p2': 'Paul'},
  {'n': 'Smith', 'p': 'John'},
  {'n': 'Forbes', 'p': 'John'},
  {'n': 'Forbes', 'p': 'Charlie'},
  {'n': 'Forbes', 'p': 'Bob'}],
 [{'n': 'Smith', 'p': 'Bob'},
  {'n': 'Martin', 'p': 'Jean', 'p2': 'Paul'},
  {'n': 'Smith', 'p': 'John'},
  {'n': 'Martin', 'p': 'Jean', 'p2': 'Pierre'},
  {'n': 'Forbes', 'p': 'Bob'},
  {'n': 'Forbes', 'p': 'Charlie'},
  {'n': 'Dupont', 'p': 'Laura'},
  {'n': 'Smith', 'p': 'Charlie'},
  {'n': 'Martin', 'p': 'Jeanne'},
  {'n': 'Martin', 'p': 'Jean'},
  {'n': 'Dupont', 'p': 'Alex', 'p2': 'Paul'},
  {'n': 'Martin', 'p': 'Jeanneot'},
  {'n': 'Dupont', 'p': 'Alex'},
  {'n': 'Dupont', 'p': 'Alexandre'},
  {'n': 'Dupont', 'p': 'Alex', 'p2': 'Pierre'},
  {'n': 'Dupont', 'p': 'Laura', 'p2': 'Marie'},
  {'n': 'Martin', 'p': 'Jeanne', 'p2': 'Marie'},
  {'n': 'Forbes', 'p': 'John'},
  {'n': 'Smith', 'p': 'Bob', 'p2': 'Paul'}],
 [{'n': 'Dupont', 'p': 'Alex', 'p2': 'Paul'},
  {'n': 'Dupont', 'p': 'Laura', 'p2': 'Marie'},
  {'n': 'Martin', 'p': 'Jeanneot'},
  {'n': 'Martin', 'p': 'Jeanne'},
  {'n': 'Dupont', 'p': 'Alex', 'p2': 'Pierre'},
  {'n': 'Dupont', 'p': 'Laura'},
  {'n': 'Martin', 'p': 'Jeanne', 'p2': 'Marie'},
  {'n': 'Martin', 'p': 'Jean', 'p2': 'Pierre'},
  {'n': 'Dupont', 'p': 'Alexandre'},
  {'n': 'Martin', 'p': 'Jean', 'p2': 'Paul'},
  {'n': 'Dupont', 'p': 'Alex'},
  {'n': 'Martin', 'p': 'Jean'}],
 [{'n': 'Smith', 'p': 'Bob', 'p2': 'Paul'},
  {'n': 'Forbes', 'p': 'Bob'},
  {'n': 'Forbes', 'p': 'Charlie'},
  {'n': 'Smith', 'p': 'Charlie'},
  {'n': 'Smith', 'p': 'John'},
  {'n': 'Forbes', 'p': 'John'},
  {'n': 'Smith', 'p': 'Bob'}],
 [{'n': 'Dupont', 'p': 'Laura'},
  {'n': 'Smith', 'p': 'John'},
  {'n': 'Martin', 'p': 'Jean'},
  {'n': 'Dupont', 'p': 'Alex', 'p2': 'Paul'},
  {'n': 'Smith', 'p': 'Charlie'},
  {'n': 'Martin', 'p': 'Jeanne', 'p2': 'Marie'},
  {'n': 'Forbes', 'p': 'Bob'},
  {'n': 'Martin', 'p': 'Jean', 'p2': 'Paul'},
  {'n': 'Dupont', 'p': 'Laura', 'p2': 'Marie'},
  {'n': 'Dupont', 'p': 'Alexandre'},
  {'n': 'Martin', 'p': 'Jean', 'p2': 'Pierre'},
  {'n': 'Martin', 'p': 'Jeanne'},
  {'n': 'Smith', 'p': 'Bob', 'p2': 'Paul'},
  {'n': 'Dupont', 'p': 'Alex'},
  {'n': 'Martin', 'p': 'Jeanneot'},
  {'n': 'Forbes', 'p': 'John'},
  {'n': 'Dupont', 'p': 'Alex', 'p2': 'Pierre'},
  {'n': 'Smith', 'p': 'Bob'},
  {'n': 'Forbes', 'p': 'Charlie'}],
 [{'n': 'Dupont', 'p': 'Alex', 'p2': 'Pierre'},
  {'n': 'Dupont', 'p': 'Alex'},
  {'n': 'Martin', 'p': 'Jeanneot'},
  {'n': 'Martin', 'p': 'Jeanne', 'p2': 'Marie'},
  {'n': 'Martin', 'p': 'Jean', 'p2': 'Pierre'},
  {'n': 'Martin', 'p': 'Jeanne'},
  {'n': 'Dupont', 'p': 'Alexandre'},
  {'n': 'Martin', 'p': 'Jean'},
  {'n': 'Dupont', 'p': 'Laura', 'p2': 'Marie'},
  {'n': 'Dupont', 'p': 'Laura'},
  {'n': 'Martin', 'p': 'Jean', 'p2': 'Paul'},
  {'n': 'Dupont', 'p': 'Alex', 'p2': 'Paul'}],
 [{'n': 'Smith', 'p': 'John'},
  {'n': 'Forbes', 'p': 'Bob'},
  {'n': 'Forbes', 'p': 'Charlie'},
  {'n': 'Smith', 'p': 'Bob'},
  {'n': 'Smith', 'p': 'Charlie'},
  {'n': 'Forbes', 'p': 'John'},
  {'n': 'Smith', 'p': 'Bob', 'p2': 'Paul'}],
 [{'n': 'Smith', 'p': 'Bob'},
  {'n': 'Dupont', 'p': 'Laura'},
  {'n': 'Martin', 'p': 'Jeanne', 'p2': 'Marie'},
  {'n': 'Dupont', 'p': 'Alex'},
  {'n': 'Martin', 'p': 'Jeanne'},
  {'n': 'Dupont', 'p': 'Alex', 'p2': 'Paul'},
  {'n': 'Smith', 'p': 'John'},
  {'n': 'Smith', 'p': 'Charlie'},
  {'n': 'Smith', 'p': 'Bob', 'p2': 'Paul'},
  {'n': 'Forbes', 'p': 'Bob'},
  {'n': 'Martin', 'p': 'Jeanneot'},
  {'n': 'Martin', 'p': 'Jean', 'p2': 'Paul'},
  {'n': 'Forbes', 'p': 'Charlie'},
  {'n': 'Martin', 'p': 'Jean', 'p2': 'Pierre'},
  {'n': 'Dupont', 'p': 'Alexandre'},
  {'n': 'Dupont', 'p': 'Laura', 'p2': 'Marie'},
  {'n': 'Forbes', 'p': 'John'},
  {'n': 'Martin', 'p': 'Jean'},
  {'n': 'Dupont', 'p': 'Alex', 'p2': 'Pierre'}]]





inputs_tri_custom = [
    Args(input) for input in inputs
]

exo_tri_custom = ExerciseFunction(
    tri_custom, inputs_tri_custom,
    call_renderer=PPrintCallRenderer(width=24),
    result_renderer=PPrintRenderer(width=30),
    font_size='small',
)


def tri_custom_ko(liste):
    sort(liste)
    return liste
