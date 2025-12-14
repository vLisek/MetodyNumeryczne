from sympy import Symbol, simplify

# --- DANE WEJŚCIOWE ---
x_nodes = [1, 2, 3]
y_nodes = [5, 7, 6]

# --- (WALIDACJA) ---
if len(x_nodes) != len(y_nodes):
    raise ValueError("Tablice x i y muszą mieć tę samą długość!")

if len(set(x_nodes)) != len(x_nodes):
    raise ValueError("Węzły x muszą być unikalne!")

n = len(x_nodes)
if n < 2:
    raise ValueError("Potrzeba minimum 2 punktów do interpolacji.")


# --- (Metoda Newtona) ---
# Inicjalizacja macierzy zerami (n x n)
coef = [[0] * n for _ in range(n)]

# Wypełnienie pierwszej kolumny (wartości y)
for i in range(n):
    coef[i][0] = y_nodes[i]

# Obliczanie różnic dzielonych
# Pętla po kolumnach (j) i wierszach (i)
for j in range(1, n):
    for i in range(n - j):
        # Wzór: (f[i+1...j] - f[i...j-1]) / (x[i+j] - x[i])
        licznik = coef[i+1][j-1] - coef[i][j-1]
        mianownik = x_nodes[i+j] - x_nodes[i]
        coef[i][j] = licznik / mianownik

# Główna przekątna to nasze współczynniki b0, b1, b2...
wspolczynniki = coef[0]

# --- BUDOWANIE WIELOMIANU ---
x = Symbol('x')
P_x = wspolczynniki[0]
iloczyn_x = 1

for i in range(1, n):
    iloczyn_x *= (x - x_nodes[i-1]) # Kolejne mnożenia (x-x0), (x-x0)(x-x1)...
    P_x += wspolczynniki[i] * iloczyn_x

# --- WYNIK ---
print(f"Dane wejściowe:\n   X={x_nodes}, Y={y_nodes}\n")
print(f"Obliczone współczynniki różnic dzielonych:\n   {wspolczynniki}\n")
print(f"Wielomian interpolacyjny:\n   {simplify(P_x)}\n")

# Sprawdzenie
print(f"Sprawdzenie dla x=2:\n   {simplify(P_x).subs(x, 2)}")