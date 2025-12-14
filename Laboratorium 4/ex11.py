from sympy import Symbol, Matrix, simplify

# --- DANE WEJŚCIOWE ---
x_nodes = [0, 3, 6, 9, 12]
y_nodes = [4, 5, 4, 1, 2]
m = 3  # Stopień wielomianu aproksymującego

# --- (WALIDACJA) ---
if len(x_nodes) != len(y_nodes):
    raise ValueError("Tablice x i y muszą mieć tę samą długość!")

n = len(x_nodes)
# Kluczowy warunek aproksymacji. Liczba punktów musi być większa niż stopień wielomianu.
if n <= m:
    raise ValueError(f"Do aproksymacji stopnia {m} potrzeba co najmniej {m+1} punktów. Masz {n}.")


# --- BUDOWANIE UKŁADU RÓWNAŃ NORMALNYCH ---
# Szukamy wielomianu W(x) = a0 + a1 * x + ... + am * x^m
# Musimy zbudować macierz główną A i wektor wyrazów wolnych B

# 1. Obliczanie sum potęg x (potrzebne do lewej strony równania)
# Potęgi idą od 0 do 2 * m
sumy_poteg_x = []
for k in range(2 * m + 1):
    suma = sum(x**k for x in x_nodes)
    sumy_poteg_x.append(suma)

# 2. Obliczanie sum iloczynów y * x^k (potrzebne do prawej strony)
# Potęgi idą od 0 do m
sumy_yx = []
for k in range(m + 1):
    suma = sum(y * (x**k) for x, y in zip(x_nodes, y_nodes))
    sumy_yx.append(suma)

# --- MACIERZ ---
# Tworzymy macierz układu równań
macierz_glowna = []
for i in range(m + 1):
    wiersz = []
    for j in range(m + 1):
        # Indeks w tablicy sum to suma indeksów macierzy (i+j)
        wiersz.append(sumy_poteg_x[i + j])
    macierz_glowna.append(wiersz)

# --- ROZWIĄZANIE UKŁADU (SymPy) ---
# Używamy Matrix z SymPy do rozwiązania układu liniowego A * a = B
A = Matrix(macierz_glowna)
B = Matrix(sumy_yx)

# Rozwiązanie układu: a0, a1, a2, a3
wspolczynniki = A.solve(B)

# --- WYNIK ---
x = Symbol('x')
W_x = 0
for i in range(m + 1):
    W_x += wspolczynniki[i] * x**i

print(f"Dane:\n   {n} punktów, stopień m={m}\n")

coeffs_float = [float(c) for c in wspolczynniki]
print(f"Współczynniki (od a0):\n   {coeffs_float}\n")
print(f"Funkcja aproksymująca (dokładna):\n   {W_x}\n")
print(f"Funkcja aproksymująca (uproszczona):\n   {W_x.evalf(4)}") # Zaokrąglenie do 4 miejsc