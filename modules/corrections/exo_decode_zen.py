# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


# @BEG@ name=decode_zen no_example=skip
# le module this est implémenté comme une petite énigme
# comme le laissent entrevoir les indices, on y trouve
# (*) dans l'attribut 's' une version encodée du manifeste
# (*) dans l'attribut 'd' le code à utiliser pour décoder
#
# ce qui veut dire qu'en première approximation on pourrait
# énumérer les caractères du manifeste en faisant
# (this.d[c] for c in this.s)
#
# mais ce serait le cas seulement si le code agissait sur
# tous les caractères; comme ce n'est pas le cas il faut
# laisser intacts les caractères de this.s qui ne sont pas
# dans this.d

def decode_zen(this_module):
    """
    décode le zen de python à partir du module this
    """
    # la version encodée du manifeste
    encoded = this_module.s
    # le dictionnaire qui implémente le code
    code = this_module.d
    # si un caractère est dans le code, on applique le code
    # sinon on garde le caractère tel quel
    # aussi, on appelle 'join' pour refaire une chaîne à partir
    # de la liste des caractères décodés
    return ''.join(code[c] if c in code else c for c in encoded)
# @END@


# @BEG@ name=decode_zen more=bis
# une autre version un peu plus courte
#
# on utilise la méthode get d'un dictionnaire, qui permet de spécifier
# (en second argument) quelle valeur on veut utiliser dans les cas où la
# clé n'est pas présente dans le dictionnaire
#
# dict.get(key, default)
# retourne dict[key] si elle est présente, et default sinon

def decode_zen_bis(this_module):
    """
    une autre version un peu plus courte
    """
    return "".join(this_module.d.get(c, c) for c in this_module.s)
# @END@


import this

class ExoDecodeZen(ExerciseFunction):
    def correction(self, student_decode_zen):
        args_obj = Args(this)
        self.datasets = [ args_obj ]
        return ExerciseFunction.correction(self, student_decode_zen)

    def resultat(self, this):
        return self.solution(this)

# cannot copy nor deepcopy a module
exo_decode_zen = ExoDecodeZen(
    decode_zen, "inputs_gets_overridden",
    copy_mode='none',
    layout='text', layout_args=(None, 'xx-small', 'xx-small'),
    call_layout='void', render_name=False,
    font_size='x-small', header_font_size='small',
    )



def decode_zen_ko(this_module):
    return "".join([this_module.d.get(c, ' ') for c in this_module.s])
