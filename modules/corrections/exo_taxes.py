from nbautoeval import Args, ExerciseFunction


# @BEG@ name=taxes
# une solution très élégante proposée par adrienollier

# les tranches en ordre décroissant
bareme = (
    (150_000, 45),
    (50_000, 40),
    (12_500, 20),
    (0, 0),
)

def taxes(revenu):
    """
    U.K. income taxes calculator
    https://www.gov.uk/income-tax-rates
    """
    montant = 0
    for seuil, taux in bareme:
        if revenu > seuil:
            montant += (revenu - seuil) * taux // 100
            revenu = seuil
    return montant
# @END@


# @BEG@ name=taxes more=bis  latex_size=footnotesize

# cette solution est plus pataude; je la retiens
# parce qu'elle montre un cas de for .. else ..
# qui ne soit pas trop tiré par les cheveux
# quoique

bands = [
    # à partir de 0. le taux est nul
    (0, 0.),
    # jusqu'à 12 500 où il devient de 20%
    (12_500, 20/100),
    # etc.
    (50_000, 40/100),
    (150_000, 45/100),
]

def taxes_bis(income):
    """
    Utilise un for avec un else
    """
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
    return int(amount)
# @END@


# pas dans les corrigés, ce sera suffisant
# @ BEG @ name=taxes more=ter
# Une autre version proposée aussi par adrienollier
# qui contourne la difficulté en utilisant
# habilement math.inf
# nombre infini qui est supérieur à tous les nombres

import math

TaxRate2 = (
    (0, 12_500, 0),
    (12_501, 50_000, 20),
    (50_001, 150_000, 40),
    (150_001, math.inf, 45),
)

def taxes_ter(income):

    due = 0
    for floor, ceiling, rate in TaxRate2:
        due += (min(income, ceiling) - floor + 1) * rate / 100
        if income <= ceiling:
            return int(due)


def taxes_ko(income):
    return (income - 12_500) * 20/100


taxes_values = [ 0, 50_000, 12_500, 5_000,
                 16_500, 30_000, 100_000, 150_000, 200_000, 12_504
]

taxes_inputs = [Args(v) for v in taxes_values]

exo_taxes = ExerciseFunction(taxes, taxes_inputs, nb_examples=2)

if __name__ == '__main__':
    for value in taxes_values:
        tax = taxes(value)
        print(f"{value} -> {tax}")
