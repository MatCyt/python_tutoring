# czy z podanych liczb da się zbudować trójkąt (jeśli nie to wypisz stosowny komunikat i przerwij działanie programu)
# obwód trójkąta
# pole trójkąta
# informację czy trójkąt jest równoboczny, równoramienny czy różnoboczny
# informację czy trójkąt jest prostokątny, ostrokątny czy rozwartokątny
# napisz funkcje, która wyrysuje zadany trójkąt używając biblioteki turtle (Wsk. Twierdzenie Cosinusów)
# Uwaga: W przypadku złej liczby argumentów program powinien wyświetlić odpowiedni komunikat i zakończyć działanie.


import sys
import turtle as t
from math import acos, degrees, sqrt


def sprawdzenie_argumentow(boki):
    if len(boki) != 3:
        sys.exit('Zła liczba argumentów')


def sprawdzenie_bokow(boki):
    for i in boki:
        pozostale = [x for x in boki if x != i]
        if sum(pozostale) <= i:
            sys.exit('Zła długość boków')


def oblicz_obwod_trojkata(a, b, c):
    obwod = a + b + c
    text_output = 'Obwód trójkąta: {}'.format(obwod)
    return text_output


def oblicz_pole_trojkata(a, b, c):
    p = (a + b + c) / 2
    pole = sqrt(p*(p-a)*(p-b)*(p-c))
    pole_round = round(pole, 2)
    text_output = 'Pole trójkąta: {}'.format(pole_round)
    return text_output


def podaj_typ_ramiona(a, b, c):
    if a == b and b == c:
        return 'Trójkąt równoboczny'
    elif a == b or b == c:
        return 'Trójkąt równoramienny'
    else:
        return 'Trójkąt różnoramienny'


def podaj_typ_katy(boki):
    naj = max(boki)
    boki_kopia = boki
    boki_kopia.remove(naj)
    poz1, poz2 = boki
    if naj**2 > (poz1**2 + poz2**2):
        return 'Trójkąt jest rozwartokątny'
    elif naj**2 == (poz1**2 + poz2**2):
        return 'Trójkąt jest prostokątny'
    else:
        return 'Trójkąt jest ostrokątny'

# https://www.mathsisfun.com/algebra/trig-solving-sss-triangles.html

def wylicz_katy(a, b, c):
    cos_c = (a*a + b*b - c*c) / (2*a*b)
    cos_a = (b*b + c*c - a*a) / (2*b*c)
    cos_b = (c*c + a*a - b*b) / (2*c*a)
    kat_a = round(degrees(acos(cos_a)), 0)
    kat_b = round(degrees(acos(cos_b)), 0)
    kat_c = round(degrees(acos(cos_c)), 0)
    return kat_a, kat_b, kat_c


def narysuj_trojkat(a, b, c):
    kat_a, kat_b, kat_c = wylicz_katy(a, b, c)

    t.forward(a*10)
    t.right(180-kat_b)
    t.forward(c*10)
    t.right(180-kat_a)
    t.forward(b*10)

    t.mainloop()
    t.bye()



if __name__ == "__main__":

    boki_trojkata = sys.argv[1:]
    boki_trojkata = list(map(int, boki_trojkata))

    sprawdzenie_argumentow(boki_trojkata)
    sprawdzenie_bokow(boki_trojkata)

    a, b, c = boki_trojkata

    print(oblicz_obwod_trojkata(a, b, c))
    print(oblicz_pole_trojkata(a, b, c))
    print(podaj_typ_katy(boki_trojkata))
    print(podaj_typ_ramiona(a, b, c))

    narysuj_trojkat(a, b, c)
