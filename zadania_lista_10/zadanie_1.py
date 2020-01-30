# Niech poczatek i koniec będą całkowitymi zmiennymi globalnymi. 
# Napisz pętlę for, która drukuje na ekranie liczby całkowite ze zbioru [poczatek, koniec].

poczatek = 1
koniec = 10

for i in list(range(poczatek, koniec + 1)):
    print(i)


def drukuj_zbior(start, stop):
    global poczatek, koniec
    poczatek, koniec = start, stop
    for i in list(range(poczatek, koniec + 1)):
        print(i)

    print(poczatek)
    print(koniec)


drukuj_zbior(5, 15)