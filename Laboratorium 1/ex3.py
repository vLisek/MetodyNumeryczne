def f(x):
    return x**3 + x - 1

def bisekcja(left, right, eps):
    if f(left) * f(right) > 0:
        print("Brak zmiany znaku w przedziale.")
        return None, 0

    f_left = f(left)
    iteracje = 0

    while (right - left) / 2.0 > eps:
        mid = (left + right) / 2.0
        f_mid = f(mid)
        iteracje += 1

        if f_mid == 0:
            left = right = mid
            break
        if f_left * f_mid < 0:
            right = mid
        else:
            left = mid
            f_left = f_mid

    return (left + right) / 2.0, iteracje

start = 0.0
end = 1.0
dokladnosc = 0.01

pierwiastek, kroki = bisekcja(start, end, dokladnosc)

if pierwiastek is not None:
    print("Przybliżony pierwiastek:", round(pierwiastek, 4))
    print("Liczba iteracji:", kroki)
    print("Wartość f(x):", round(f(pierwiastek), 6))
else:
    print("Nie udało się znaleźć pierwiastka metodą bisekcji.")
