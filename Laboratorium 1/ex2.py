import numpy as numpy

def horner_dzielenie_przez_dwumian(wspolczynniki, x):
    wspolczynniki = list(wspolczynniki)
    iloraz = []
    wartosc = 0

    for i, wsp in enumerate(wspolczynniki):
        if i == 0:
            wartosc = wsp
        else:
            wartosc = wsp + x * wartosc
        if i < len(wspolczynniki) - 1:
            iloraz.append(wartosc)

    reszta = wartosc
    return iloraz, reszta


wielomian = [2, 3, -5, 7]  # 2x^3 + 3x^2 - 5x + 7
a = 2                      # dzielimy przez (x - 2)

iloraz_horner, reszta_horner = horner_dzielenie_przez_dwumian(wielomian, a)
iloraz_numpy, reszta_numpy = numpy.polydiv(wielomian, [1, -a])

print("\nDzielenie wielomianu metodą Hornera:")
print("Współczynniki wielomianu:", wielomian)
print("Dzielnik: (x -", a, ")")
print("Iloraz (metoda Hornera):", iloraz_horner)
print("Reszta (metoda Hornera):", reszta_horner)

print("\nPorównanie z numpy.polydiv:")
print("Iloraz (numpy):", iloraz_numpy.tolist())
print("Reszta (numpy):", reszta_numpy.tolist())