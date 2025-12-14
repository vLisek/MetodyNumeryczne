from sympy import Symbol, exp, sin, diff, Abs

# --- Ustawienia i zmienne ---
x = Symbol("x")
a, b = -3, 1             # Początek i koniec przedziału
n = 4                    # Liczba podprzedziałów (musi być parzysta)
f = sin(x) * exp(-3 * x) + x**3  # Funkcja całkowania


# --- Węzły podziału i krok ---
h = (b - a) / n          # Krok całkowania
# Węzły: x0, x1, ..., xn
nodes = [a + i * h for i in range(n + 1)]


# --- Metoda Simpsona (Wzór 1/3) ---
S_even, S_odd = 0, 0


# Sumowanie wartości funkcji dla węzłów wewnętrznych (od i=1 do n-1)
for i in range(1, n):
    val = f.subs(x, nodes[i])
    if i % 2 == 0:
        S_even += val * 2 # Wagi: 2 (indeksy parzyste)
    else:
        S_odd += val * 4  # Wagi: 4 (indeksy nieparzyste)


# Wynik = (h/3) * [ f(a) + f(b) + 2*S_even + 4*S_odd ]
val_approx = (h / 3) * (f.subs(x, a) + f.subs(x, b) + S_even + S_odd)

print(f"Całka [{a}, {b}] z sin(x)*e^(-3x) + x^3 dx")
print(f"Wynik metody parabol ≈ {float(val_approx)}")


# --- Szacowanie błędu ---
f_4 = diff(f, x, 4)
M4_est = max(Abs(f_4.subs(x, a)), Abs(f_4.subs(x, b)))
error_est = ((b - a) * (h ** 4) / 180) * M4_est


print(f"Szacowany błąd maksymalny (z uproszczonym M4) ≈ {float(error_est)}")