# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args


# @BEG@ name=taxes latex_size=footnotesize
# la définition des différentes tranches
bands = [
    # à partir de 0. le taux est nul
    (0, 0.),
    # jusqu'à 11 500 où il devient de 20%
    (11_500, 20/100),
    # etc.
    (45_000, 40/100),
    (150_000, 45/100),
]


def taxes(income):
    """
    U.K. income taxes calculator
    https://www.gov.uk/income-tax-rates

    utilise un for avec un break
    """
    # on accumule les morceaux
    amount = 0
    
    # en faisant ce zip un peu étrange, on va
    # considérer les couples de tuples consécutifs dans
    # la liste bands
    for (band1, rate1), (band2, _) in zip(bands, bands[1:]):
        # le salaire est au-delà de cette tranche
        if income >= band2:
            amount += (band2-band1) * rate1
        # le salaire est dans cette tranche
        else:
            amount += (income-band1) * rate1
            # du coup on peut sortir du for par un break
            # et on ne passera pas par le else du for
            break
    # on ne passe ici qu'avec les salaires dans la dernière tranche
    # en effet pour les autres on est sorti du for par un break
    else:
        band_top, rate_top = bands[-1]
        amount += (income - band_top) * rate_top
    return(int(amount))
# @END@


# @BEG@ name=taxes more=bis
# Une version proposée par adrienollier
# qui contourne la difficulté en utilisant
# habilement math.inf
# nombre infini qui est supérieur à tous les nombres

import math

TaxRate = (
    (0, 11_500, 0),
    (11_501, 45_000, 20),
    (45_001, 150_000, 40),
    (150_001, math.inf, 45),
)

def taxes_bis(income):

    due = 0
    for floor, ceiling, rate in TaxRate:
        due += (min(income, ceiling) - floor + 1) * rate / 100
        if income <= ceiling:
            return int(due)
# @END@

# @BEG@ name=taxes more=ter
# La même chose mais améliorée pour éviter les
# répétitions dans le tuple qui sert de base au calcul

import math
tax_rate_nodup = (
    (11_500, 0),
    (45_000, 20),
    (150_000, 40),
    (math.inf, 45),
)

# calculer ce qui s'appelle TaxRate dans la solution taxes_bis
b1, r1 = tax_rate_nodup[0]

tax_rate = [ (0., b1, r1) ]
tax_rate += [    
    (b1, b2, r2)
      for (b1, _), (b2, r2) in zip(tax_rate_nodup, tax_rate_nodup[1:])
]

# à ce stade on peut utiliser le code de taxes_bis
# presque à l'identique
def taxes_ter(income):

    due = 0
    for floor, ceiling, rate in tax_rate:
        due += (min(income, ceiling) - floor) * rate / 100
        if income <= ceiling:
            return int(due)
# @END@

def taxes_ko(income):
    return (income - 11_500) * 20/100


taxes_values = [ 0, 45_000, 11_500, 5_000,
                 16_500, 30_000, 100_000, 150_000, 200_000, 11_504
]

taxes_inputs = [Args(v) for v in taxes_values]

exo_taxes = ExerciseFunction(taxes, taxes_inputs, nb_examples=2)
    
if __name__ == '__main__':
    for value in taxes_values:
        tax = taxes(value)
        print(f"{value} -> {tax}")
