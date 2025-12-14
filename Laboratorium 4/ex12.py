# --- DANE WEJŚCIOWE ---
A = [
    [3.0, 0.0, 6.0],
    [1.0, 2.0, 8.0],
    [4.0, 5.0, -2.0]
]

b = [-12.0, -12.0, 39.0]


# --- FUNKCJA POMOCNICZA: WYPISYWANIE MACIERZY ---
def print_system(M, step_name):
    print(f"\n--- {step_name} ---")
    n = len(M)
    for row in M:
        # Formatowanie: | a1 a2 a3 | b |
        left_side = "  ".join(f"{x:6.2f}" for x in row[:-1])
        right_side = f"{row[-1]:6.2f}"
        print(f"| {left_side} | {right_side} |")


# --- ALGORYTM ELIMINACJI GAUSSA ---
n = len(b)

# 1. Tworzenie macierzy rozszerzonej
M = [row[:] + [b[i]] for i, row in enumerate(A)]

print_system(M, "Macierz Początkowa")

# 2. Eliminacja w przód
for k in range(n):
    # --- WYBÓR ELEMENTU GŁÓWNEGO ---
    max_row = k
    for i in range(k + 1, n):
        if abs(M[i][k]) > abs(M[max_row][k]):
            max_row = i

    # Zamiana wierszy
    if max_row != k:
        M[k], M[max_row] = M[max_row], M[k]
        print_system(M, f"Krok {k + 1}: Zamiana wiersza {k + 1} z {max_row + 1}")
    else:
        print(f"\n---        Krok {k + 1}: Brak zamiany        ---")

    # --- ZEROWANIE POD PRZEKĄTNĄ ---
    for i in range(k + 1, n):
        factor = M[i][k] / M[k][k]
        # Operacja wierszowa: Wiersz_i = Wiersz_i - factor * Wiersz_k
        for j in range(k, n + 1):
            M[i][j] -= factor * M[k][j]

    print_system(M, f"Macierz po eliminacji w kolumnie {k + 1}")

# 3. Podstawianie
x = [0] * n
for i in range(n - 1, -1, -1):
    suma = sum(M[i][j] * x[j] for j in range(i + 1, n))
    x[i] = (M[i][n] - suma) / M[i][i]

# --- WYNIK KOŃCOWY ---
print("\n=== ROZWIĄZANIE UKŁADU ===")
for i in range(n):
    print(f"x{i + 1} = {x[i]:.2f}")