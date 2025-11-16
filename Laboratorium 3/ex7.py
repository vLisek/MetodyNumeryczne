from sympy import Symbol, sqrt, diff

# --- Funkcja wyznaczająca punkty podziału przedziału ---
def wyznacz_punkty(liczba_podzialow, lewy_koniec, prawy_koniec):
    lista_punktow = []
    for nr in range(liczba_podzialow + 1):
        punkt = lewy_koniec + (nr / liczba_podzialow) * (prawy_koniec - lewy_koniec)
        lista_punktow.append(punkt)
    return lista_punktow


# --- Zmienne podstawowe ---
zmienna_symboliczna = Symbol('x')
poczatek_przedzialu = 0
koniec_przedzialu = 1
liczba_przedzialow = 3

# Funkcja całkowana
funkcja_calkowana = sqrt(1 + zmienna_symboliczna)

# --- Wyznaczenie punktów podziału ---
wezly_calkowania = wyznacz_punkty(liczba_przedzialow, poczatek_przedzialu, koniec_przedzialu)

# --- Krok całkowania ---
dlugosc_kroku = (koniec_przedzialu - poczatek_przedzialu) / liczba_przedzialow

# --- Metoda trapezów ---
suma_wartosci_funkcji = 0

# Dodawanie wartości w węzłach wewnętrznych
for numer in range(1, liczba_przedzialow):
    suma_wartosci_funkcji += funkcja_calkowana.subs(zmienna_symboliczna, wezly_calkowania[numer])

# Dodanie wartości na końcach przedziału z wagą 1/2
suma_wartosci_funkcji += (
    funkcja_calkowana.subs(zmienna_symboliczna, poczatek_przedzialu)
    + funkcja_calkowana.subs(zmienna_symboliczna, koniec_przedzialu)
) / 2

# Wynik przybliżony całki
wartosc_przyblizona_calki = dlugosc_kroku * suma_wartosci_funkcji

print(f"Całka [{poczatek_przedzialu}, {koniec_przedzialu}] z sqrt(1+x) dx")
print(f"Wynik metody trapezów ≈ {float(wartosc_przyblizona_calki)}")


# --- Liczenie błędu ---
pochodna_pierwsza = diff(funkcja_calkowana, zmienna_symboliczna)
pochodna_druga = diff(pochodna_pierwsza, zmienna_symboliczna)

# Maksimum wartości bezwzględnej drugiej pochodnej w przedziale [0,1]
maksymalna_wartosc_bezwzgledna_pochodnej_drugiej = abs(pochodna_druga.subs(zmienna_symboliczna, poczatek_przedzialu))

blad_metody_trapezow = ((koniec_przedzialu - poczatek_przedzialu) ** 3 / (12 * liczba_przedzialow ** 2)) * maksymalna_wartosc_bezwzgledna_pochodnej_drugiej

print(f"Szacowany błąd ≈ {float(blad_metody_trapezow)}")
