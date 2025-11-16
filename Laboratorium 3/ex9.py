from sympy import Symbol, exp, sin, diff

# --- Funkcja wyznaczająca podział przedziału na równe części ---
def wyznacz_punkty(liczba_przedzialow, lewy_koniec, prawy_koniec):
    lista_punktow = []
    for nr in range(liczba_przedzialow + 1):
        punkt = lewy_koniec + (nr / liczba_przedzialow) * (prawy_koniec - lewy_koniec)
        lista_punktow.append(punkt)
    return lista_punktow


# --- Dane podstawowe ---
zmienna_symboliczna = Symbol('x')

poczatek_przedzialu = -3
koniec_przedzialu = 1

# Funkcja całkowana
funkcja_calkowana = sin(zmienna_symboliczna) * exp(-3 * zmienna_symboliczna) + zmienna_symboliczna**3

# Liczba podprzedziałów (musi być parzysta!)
liczba_przedzialow = 4

# Krok całkowania
dlugosc_kroku = (koniec_przedzialu - poczatek_przedzialu) / liczba_przedzialow

# Węzły
wezly_calkowania = wyznacz_punkty(liczba_przedzialow, poczatek_przedzialu, koniec_przedzialu)

# --- Metoda parabol (Simpsona) ---
suma_wartosci_parzyste = 0
suma_wartosci_nieparzyste = 0

for numer in range(1, liczba_przedzialow):
    wartosc = funkcja_calkowana.subs(zmienna_symboliczna, wezly_calkowania[numer])
    if numer % 2 == 0:      # indeks parzysty
        suma_wartosci_parzyste += wartosc
    else:                    # indeks nieparzysty
        suma_wartosci_nieparzyste += wartosc

wynik_metody_simpsona = (
    funkcja_calkowana.subs(zmienna_symboliczna, poczatek_przedzialu)
    + funkcja_calkowana.subs(zmienna_symboliczna, koniec_przedzialu)
    + 2 * suma_wartosci_parzyste
    + 4 * suma_wartosci_nieparzyste
) * (dlugosc_kroku / 3)

print(f"Całka [{poczatek_przedzialu}, {koniec_przedzialu}] z sin(x)*e^(-3x) + x^3 dx")
print(f"Wynik metody parabol ≈ {float(wynik_metody_simpsona)}")


# --- Obliczanie błędu maksymalnego ---
pochodna_1 = diff(funkcja_calkowana, zmienna_symboliczna)
pochodna_2 = diff(pochodna_1, zmienna_symboliczna)
pochodna_3 = diff(pochodna_2, zmienna_symboliczna)
pochodna_4 = diff(pochodna_3, zmienna_symboliczna)

# Uproszczone oszacowanie – maksimum na końcach przedziału
maksymalna_wartosc_pochodnej_4 = max(
    abs(pochodna_4.subs(zmienna_symboliczna, poczatek_przedzialu)),
    abs(pochodna_4.subs(zmienna_symboliczna, koniec_przedzialu))
)

blad_maxymalny = ((koniec_przedzialu - poczatek_przedzialu) * (dlugosc_kroku ** 4)) / 180 * maksymalna_wartosc_pochodnej_4

print(f"Szacowany błąd maksymalny ≈ {float(blad_maxymalny)}")
