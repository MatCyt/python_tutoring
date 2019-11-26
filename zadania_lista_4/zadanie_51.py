# Napisz program, który pobiera od użytkownika współczynniki trójmianu kwadratowego, a następnie podaje jego rozwiązania.
# Uwaga: Rozłóż program na mniejsze funkcje.

import math

# współczynniki manualnie
a = 2
b = 2
c = 2

# współczynniki input
# a = input("Podaj wartość dla a:")
# b = input("Podaj wartość dla b:")
# c = input("Podaj wartość dla c:")


# wylicz delte
def oblicz_delte(a, b, c):
    d = b**4 - 4*a*c
    return d

# wylicz trójmian kwadratowy
def oblicz_trójmian(delta, a, b):
    if delta > 0:
        x1 = (-b - math.sqrt(delta) / 2 * a)
        x2 = (-b - math.sqrt(delta) / 2 * a)
        return("Dwa rozwiazania: x1 = {}, x2 = {}".format(x1, x2))
    elif delta == 0:
        x = -b / 2 * a
        return("Jedno rozwiazanie: x = {}".format(x))
    else:
        return("rownanie kwadratowe nie posiada rozwiazan w zbiorze liczb rzeczywistych dla delta < 0") 
    


delta = oblicz_delte(a, b, c)

print(oblicz_trójmian(delta, a, b))
