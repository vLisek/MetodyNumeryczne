from sympy import Symbol

# --- Ustawienia i zmienne ---
x = Symbol("x")
a, b = 1, 4              # Początek i koniec przedziału
n = 3                    # Liczba prostokątów/podziałów
f = 0.06 * (x**2) + 2    # Funkcja całkowania


# --- Obliczenia ---
h = (b - a) / n          # Szerokość prostokąta/krok

# Węzły lewostronne: a, a+h, ..., a+(n-1)h
nodes_left = [a + i * h for i in range(n)]


# Suma wartości funkcji w lewych końcach podprzedziałów
sum_f_val = sum(f.subs(x, node) for node in nodes_left)


# Wynik = szerokość * suma Wysokości
approx_val = h * sum_f_val


print(f"Całka [{a}, {b}] z (0.06 x^2 + 2) dx")
print(f"Wynik metody prostokątów lewostronnych ≈ {float(approx_val)}")