import math

# nasza funkcja f(x) = sin(x) - x/2
def funkcja(x):
    return math.sin(x) - (x / 2)

# pochodna pierwszego stopnia f'(x)
def pochodna_pierwsza(x):
    return math.cos(x) - 0.5

# pochodna drugiego stopnia f''(x)
def pochodna_druga(x):
    return -math.sin(x)

# dokładność obliczeń (epsilon)
dokladnosc = 0.01

# przedział, w którym szukamy miejsca zerowego
przedzial = [math.pi / 2, math.pi]
licznik_iteracji = 0  # licznik kroków
x_biezace = None      # punkt bieżący (xn)
x_nastepne = None     # kolejne przybliżenie (xn + 1)

if funkcja(przedzial[0]) * funkcja(przedzial[1]) < 0:

    # wybór punktu startowego (x0) – reguła: f(x0) * f''(x0) > 0
    if funkcja(przedzial[0]) * pochodna_druga(przedzial[0]) > 0:
        x_biezace = przedzial[0]
    elif funkcja(przedzial[1]) * pochodna_druga(przedzial[1]) > 0:
        x_biezace = przedzial[1]
    else:
        raise ValueError("Nie można dobrać punktu początkowego")

    print(f"x{licznik_iteracji} = {x_biezace:.5f}")

    while True:
        # obliczamy nowe przybliżenie wg wzoru: xn + 1 = xn - f(xn) / f'(xn)
        x_nastepne = x_biezace - (funkcja(x_biezace) / pochodna_pierwsza(x_biezace))
        licznik_iteracji += 1
        print(f"x{licznik_iteracji} = {x_nastepne:.5f}")

        # sprawdzamy, czy osiągnęliśmy wymaganą dokładność
        if abs(funkcja(x_nastepne)) <= dokladnosc:
            break

        # przechodzimy do kolejnej iteracji
        x_biezace = x_nastepne

    # wypisanie wyniku
    print(f"\nPrzybliżone rozwiązanie: x ≈ {x_nastepne:.5f}")
    print(f"Liczba iteracji: {licznik_iteracji}")

else:
    print("W podanym przedziale funkcja nie zmienia znaku – brak miejsca zerowego.")
