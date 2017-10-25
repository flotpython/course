# -*- coding: utf-8 -*-
from nbautoeval.exercise_regexp import ExerciseRegexp, ExerciseRegexpGroups
from nbautoeval.args import Args


phone_strings = [
    "0123456789",
    "01234567890",
    "012345678",
    "1234567890",
    "+33123456789",
    "+3312345678",
    "+330123456789",
]


# @BEG@ name=phone more=regexp
# idem concernant le \Z final
#
# il faut bien backslasher le + dans le +33
# car sinon cela veut dire 'un ou plusieurs'
#
phone = r"(\+33|0)(?P<number>[0-9]{9})\Z"
# @END@


phone_groups = ['number']


exo_phone = ExerciseRegexpGroups(
    'phone', phone, phone_groups,
    [Args(x) for x in phone_strings],
    nb_examples = 0)


phone_ko = r"(\+33|0)(?P<number>[0-9]{8})\Z"
