# Niech poczatek i koniec będą całkowitymi zmiennymi globalnymi. 
# Napisz pętlę while, która drukuje na ekranie liczby całkowite ze zbioru [poczatek, koniec].

poczatek = 1
koniec = 10

while poczatek <= koniec:
    print(poczatek)
    poczatek += 1


def drukuj_zbior(start, stop):
    global poczatek, koniec
    poczatek, koniec = start, stop
    while poczatek <= koniec:
        print(poczatek)
        poczatek += 1

    print(poczatek)
    print(koniec)


drukuj_zbior(5, 15)