import numpy as numpy

def horner_eval(coeffs, x):
    wynik = 0
    for a in coeffs:
        wynik = wynik * x + a
    return wynik

wspolczynniki = [2, 3, -5, 7]  # 2x^3 + 3x^2 - 5x + 7
punkt = 4

print("\nObliczanie wartości wielomianu metodą Hornera:")
print("Współczynniki wielomianu:", wspolczynniki)
print("Punkt x:", punkt)
print("\nWynik (Horner):", horner_eval(wspolczynniki, punkt))
print("Wynik (numpy.polyval):", numpy.polyval(wspolczynniki, punkt))