from sympy import Symbol, sqrt, diff, Abs

# --- Ustawienia i zmienne ---
x, a, b, n = Symbol("x"), 0, 1, 3
f = sqrt(1 + x)         # Funkcja całkowania
h = (b - a) / n         # Krok całkowania
nodes = [a + i * h for i in range(n + 1)] # Węzły podziału


# --- Metoda trapezów ---
# Suma f(x_i) dla węzłów wewnętrznych (i = 1 do n - 1)
S = sum(f.subs(x, nodes[i]) for i in range(1, n))


# Dodanie końców przedziału (wagi 1/2)
S += (f.subs(x, a) + f.subs(x, b)) / 2
val = h * S             # Wynik przybliżony


print(f"Całka [{a}, {b}] z sqrt(1+x) dx")
print(f"Wynik metody trapezów ≈ {float(val)}")


# --- Szacowanie błędu ---
f_pp = diff(f, x, 2)    # Druga pochodna

# Maksimum |f''(x)| w [a,b]. Dla tej f, jest w x=a.
M2 = Abs(f_pp.subs(x, a))

# Obliczanie błędu
error = ((b - a)**3 / (12 * n**2)) * M2

print(f"Szacowany błąd ≈ {float(error)}")