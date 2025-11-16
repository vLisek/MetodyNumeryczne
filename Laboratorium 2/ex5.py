# funkcja, której pierwiastek szukamy
def funkcja(x):
    return x**3 + x**2 - 3*x - 3

# metoda siecznych: obliczamy nowe przybliżenie
def nowe_przyblizenie(x0, x1):
    return x1 - funkcja(x1) * ((x1 - x0) / (funkcja(x1) - funkcja(x0)))

# dokładność obliczeń
dokladnosc = 0.0001

# początkowy przedział do szukania pierwiastka
przedzial = [1, 2]

x_poprzednie = przedzial[0]  # xn - 1
x_biezace = przedzial[1]     # xn

licznik_iteracji = 0

# wypisanie początkowych wartości
print(f"x{licznik_iteracji} = {x_poprzednie}; f(x{licznik_iteracji}) = {funkcja(x_poprzednie)}")
licznik_iteracji += 1
print(f"x{licznik_iteracji} = {x_biezace}; f(x{licznik_iteracji}) = {funkcja(x_biezace)}")

# sprawdzamy, czy w przedziale funkcja zmienia znak
if funkcja(x_poprzednie) * funkcja(x_biezace) < 0:

    while True:
        # obliczamy nowe przybliżenie
        x_nowe = nowe_przyblizenie(x_poprzednie, x_biezace)
        licznik_iteracji += 1

        # wypisanie aktualnego przybliżenia
        print(f"x{licznik_iteracji} = {x_nowe}; f(x{licznik_iteracji}) = {funkcja(x_nowe)}")

        # sprawdzamy warunek zakończenia
        if abs(funkcja(x_nowe)) <= dokladnosc:
            break

        # przechodzimy do kolejnej iteracji
        x_poprzednie, x_biezace = x_biezace, x_nowe

    print(f"\nPrzybliżone rozwiązanie: x ≈ {x_nowe}")
    print(f"Liczba iteracji: {licznik_iteracji}")

else:
    print("W podanym przedziale funkcja nie zmienia znaku – brak miejsca zerowego.")
