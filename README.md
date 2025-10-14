# Metody Numeryczne

## 📚 Spis treści
- [Laboratorium 1 (06.10.2025)](#laboratorium-1)
- [Laboratorium 2 (20.10.2025)](#laboratorium-2)
- [Laboratorium 3 (03.11.2025)](#laboratorium-3)

---

## Laboratorium 1

### 📌 Zadania:
1. Schemat Hornera – wyznaczanie wartości wielomianu w punkcie.  
2. Schemat Hornera – dzielenie wielomianu przez dwumian.

---

### 🧠 1. Schemat Hornera - wyznaczanie wartości wielomianu w punkcie.

```python
import numpy as numpy

def horner_eval(coeffs, x):
    wynik = 0
    for a in coeffs:
        wynik = wynik * x + a
    return wynik

wspolczynniki = [2, 3, -5, 7]  # 2x^3 + 3x^2 - 5x + 7
punkt = 4

print("\nObliczanie wartości wielomianu metodą Hornera:")
print("Współczynniki wielomianu:", wspolczynniki)
print("Punkt x:", punkt)
print("\nWynik (Horner):", horner_eval(wspolczynniki, punkt))
print("Wynik (numpy.polyval):", numpy.polyval(wspolczynniki, punkt))
```

Wynik:
```
Obliczanie wartości wielomianu metodą Hornera:
Współczynniki wielomianu: [2, 3, -5, 7]
Punkt x: 4

Wynik (Horner): 163
Wynik (numpy.polyval): 163
```

---

### 🧠 2. Schemat Hornera – dzielenie wielomianu przez dwumian.

```python
import numpy as numpy

def horner_dzielenie_przez_dwumian(wspolczynniki, x):
    wspolczynniki = list(wspolczynniki)
    iloraz = []
    wartosc = 0

    for i, wsp in enumerate(wspolczynniki):
        if i == 0:
            wartosc = wsp
        else:
            wartosc = wsp + x * wartosc
        if i < len(wspolczynniki) - 1:
            iloraz.append(wartosc)

    reszta = wartosc
    return iloraz, reszta


wielomian = [2, 3, -5, 7]  # 2x^3 + 3x^2 - 5x + 7
a = 2                      # dzielimy przez (x - 2)

iloraz_horner, reszta_horner = horner_dzielenie_przez_dwumian(wielomian, a)
iloraz_numpy, reszta_numpy = numpy.polydiv(wielomian, [1, -a])

print("\nDzielenie wielomianu metodą Hornera:")
print("Współczynniki wielomianu:", wielomian)
print("Dzielnik: (x -", a, ")")
print("Iloraz (metoda Hornera):", iloraz_horner)
print("Reszta (metoda Hornera):", reszta_horner)

print("\nPorównanie z numpy.polydiv:")
print("Iloraz (numpy):", iloraz_numpy.tolist())
print("Reszta (numpy):", reszta_numpy.tolist())
```

Wynik:
```
Dzielenie wielomianu metodą Hornera:
Współczynniki wielomianu: [2, 3, -5, 7]
Dzielnik: (x - 2 )
Iloraz (metoda Hornera): [2, 7, 9]
Reszta (metoda Hornera): 25

Porównanie z numpy.polydiv:
Iloraz (numpy): [2.0, 7.0, 9.0]
Reszta (numpy): [25.0]
```

[🔝 Powrót do spisu treści](#-spis-treści)

---

## Laboratorium 2
Opis laboratorium 2...

[🔝 Powrót do spisu treści](#-spis-treści)

---

## Laboratorium 3
Opis laboratorium 3...

[🔝 Powrót do spisu treści](#-spis-treści)
