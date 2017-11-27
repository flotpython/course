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
    calcule l'impôt sur le revenu
    en U.K. selon le barême 
    https://www.gov.uk/income-tax-rates

    utilise un for avec un break
    """
    # on accumule les morceaux
    amount = 0
    # en faisant ce zip un peu étrange, on va
    # considérer les couples de tuples consécutifs dans
    # la liste bands
    for (b1, rate1), (b2, _) in zip(bands, bands[1:]):
        #print(f"{b1:6} {b2:6}", end=' ')
        # le salaire est au-delà de cette tranche
        if income >= b2:
            delta = (b2-b1) * rate1
            #print(f"(1) base = {b2-b1}, rate = {rate1} -> {delta}")
            amount += delta
        # le salaire est dans cette tranche
        else:
            delta = (income-b1) * rate1
            #print(f"(2) base = {income-b1}, rate = {rate1} -> {delta}")
            amount += delta
            # du coup on peut sortir du for par un break
            # et on ne passera pas par le else du for
            break
    # on ne passe ici qu'avec les salaires dans la dernière tranche
    # en effet pour les autres on est sorti du for par un break
    else:
        btop, rate_top = bands[-1]
        #print(f"{btop:6} {6*'.'}", end=' ')
        delta = (income - btop) * rate_top
        #print(f"(3) base = {income-btop}, rate = {rate1} -> {delta}")
        amount += delta
    return(int(amount))
# @END@


# @BEG@ name=taxes more=bis
# exactement le même sans le bavardage et le debug
def taxes_bis(income):
    """
    U.K. income taxes calculator
    """
    amount = 0
    for (band1, rate), (band2, _) in zip(bands, bands[1:]):
        if income >= band2:
            amount += (band2 - band1) * rate
        else:
            amount += (income - band1) * rate
            break
    else:
        band_top, rate = bands[-1]
        amount += (income - band_top) * rate
    return int(amount)
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
