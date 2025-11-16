import math

# funkcja, której pierwiastek szukamy
def funkcja(x):
    return 3*x - math.cos(x) - 1

# metoda falsi: obliczamy punkt przecięcia linii łączącej, a i b z osią X
def falsi(a, b):
    return (a * funkcja(b) - b * funkcja(a)) / (funkcja(b) - funkcja(a))

# dokładność obliczeń
dokladnosc = 0.00001

# początkowy przedział
lewy = 0.25
prawy = 0.75

# sprawdzamy, czy funkcja zmienia znak w przedziale
if funkcja(lewy) * funkcja(prawy) >= 0:
    print("Funkcja nie zmienia znaku w podanym przedziale – brak pierwiastka.")
else:
    licznik_iteracji = 1
    x_nowe = falsi(lewy, prawy)
    print(f"x{licznik_iteracji} = {x_nowe}; f(x{licznik_iteracji}) = {funkcja(x_nowe)}")

    while abs(funkcja(x_nowe)) > dokladnosc:
        # aktualizacja przedziału: zachowujemy pierwiastek w [lewy, prawy]
        if funkcja(lewy) * funkcja(x_nowe) < 0:
            prawy = x_nowe
        else:
            lewy = x_nowe

        x_nowe = falsi(lewy, prawy)
        licznik_iteracji += 1
        print(f"x{licznik_iteracji} = {x_nowe}; f(x{licznik_iteracji}) = {funkcja(x_nowe)}")

    print(f"\nPrzybliżone rozwiązanie metodą falsi: x ≈ {x_nowe}")
    print(f"Liczba iteracji: {licznik_iteracji}")
