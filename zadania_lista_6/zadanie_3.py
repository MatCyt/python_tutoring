# czy z podanych liczb da się zbudować trójkąt (jeśli nie to wypisz stosowny komunikat i przerwij działanie programu)
# obwód trójkąta
# pole trójkąta
# informację czy trójkąt jest równoboczny, równoramienny czy różnoboczny
# informację czy trójkąt jest prostokątny, ostrokątny czy rozwartokątny
# napisz funkcje, która wyrysuje zadany trójkąt używając biblioteki turtle (Wsk. Twierdzenie Cosinusów)
# Uwaga: W przypadku złej liczby argumentów program powinien wyświetlić odpowiedni komunikat i zakończyć działanie.

import math
import sys
boki_trojkata = sys.argv[1:]
# a, b, c = boki_trojkata

test = [1,2,3]
test2 = [4,5,6]

def sprawdzenie_bokow(boki):
    for i in boki:
        pozostale = [x for x in boki if x != i]
        if sum(pozostale) <= i:
            return 'Z podanych boków nie da się zbudować trójkąta'
            exit()
        return True


def oblicz_obwod_trojkata(a, b, c):
    obwod = a + b + c
    text_output = print('Obwód trójkąta: {}'.format(obwod))
    return text_output

def oblicz_pole_trojkata(a,b,c):
    p = (a + b + c) / 2
    pole = math.sqrt(p*(p-a)*(p-b)*(p-c))
    pole_round = round(pole, 2)
    text_output = print('Pole trójkąta: {}'.format(pole_round))
    return text_output

def sprawdz_ramiona(a, b, c):
    if a == b and b == c:
        return 'Trójkąt równoboczny'
    elif a == b or b == c:
        return 'Trójkąt równoramienny'
    else:
        return 'Trójkąt różnoramienny'

def sprawdz_katy(boki):
    naj = max(boki)
    boki.remove(naj)
    poz1, poz2 = boki
    if naj**2 > (poz1**2 + poz2**2):
        return 'Trójkąt jest rozwartokątny'
    elif naj**2 == (poz1**2 + poz2**2):
        return 'Trójkąt jest prostokątny'
    else:
        return 'Trójkąt jest ostrokątny'

def narysuj_trojkat(a,b,c):
