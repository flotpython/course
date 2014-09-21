# -*- coding: iso-8859-15 -*-

from corrections.tools import correction_as_table, exemple_as_table

def multi_tri (listes):
    "trie toutes les sous-listes"
    for liste in listes:
        liste.sort()
    return listes

multi_tri_inputs = [
    [ [ [ 40, 12, 25], [ 'spam', 'egg', 'bacon' ], ], ],
    [ [ [ 32, 45], [ 200, 12 ], [-25, 37] ], ],
    [ [ [ ], range(10) ] ],
]

def correction_multi_tri (multi_tri_student):
    return correction_as_table (multi_tri_student, multi_tri, multi_tri_inputs,
                                columns = (40,40,40))


def exemple_multi_tri ():
    return exemple_as_table ('multi_tri',multi_tri, multi_tri_inputs, columns = (60,60))

####################
def multi_tri_reverse (listes, reverses):
    """trie toutes les sous listes, dans une direction
    precisée par le second argument"""
    for liste, reverse in zip(listes, reverses):
        liste.sort(reverse=reverse)
    return listes

multi_tri_reverse_inputs = [ 
    [ [ [1,2], [3,4] ], [ True, False] ],
    [ [ [1,2], [3,4] ], ( True, True ) ],
    [ [ [1,2], [3,4] ], [ False, True] ],
    [ [ [1,2], [3,4] ], [ False, False] ],
    [ [ [ 32, 45], [ 200, 12 ], [-25, 37] ], [ True, False, True] ],
    [ [ [ ], range(10) ], [False, True ], ],
]

def correction_multi_tri_reverse (multi_tri_reverse_student):
    return correction_as_table (multi_tri_reverse_student, multi_tri_reverse, multi_tri_reverse_inputs,
                                columns = (40,40,40))

def exemple_multi_tri_reverse ():
    return exemple_as_table ('multi_tri_reverse',multi_tri_reverse, multi_tri_reverse_inputs, columns = (60,60), how_many=2)
