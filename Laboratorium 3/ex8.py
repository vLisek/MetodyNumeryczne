from sympy import Symbol

# --- Funkcja wyznaczająca punkty podziału przedziału ---
def wyznacz_punkty(liczba_podzialow, lewy_koniec, prawy_koniec):
    lista_punktow = []
    for nr in range(liczba_podzialow + 1):
        punkt = lewy_koniec + (nr / liczba_podzialow) * (prawy_koniec - lewy_koniec)
        lista_punktow.append(punkt)
    return lista_punktow


# --- Zmienne podstawowe ---
zmienna_symboliczna = Symbol("x")
poczatek_przedzialu = 1
koniec_przedzialu = 4
liczba_prostokatow = 3

# Funkcja całkowana
funkcja_calkowana = 0.06 * (zmienna_symboliczna**2) + 2

# --- Wyznaczenie punktów podziału ---
wezly_calkowania = wyznacz_punkty(liczba_prostokatow, poczatek_przedzialu, koniec_przedzialu)

# --- Szerokość prostokąta ---
dlugosc_kroku = (koniec_przedzialu - poczatek_przedzialu) / liczba_prostokatow

# --- Metoda prostokątów lewostronnych ---
suma_wysokosci_prostokatow = 0

# Sumujemy wartości funkcji w lewych końcach podprzedziałów
for numer in range(liczba_prostokatow):
    suma_wysokosci_prostokatow += funkcja_calkowana.subs(zmienna_symboliczna, wezly_calkowania[numer])

# --- Wynik przybliżony ---
wartosc_przyblizona_calki = dlugosc_kroku * suma_wysokosci_prostokatow

print(f"Całka [{poczatek_przedzialu}, {koniec_przedzialu}] z (0.06 x^2 + 2) dx")
print(f"Wynik metody prostokątów ≈ {float(wartosc_przyblizona_calki)}")
