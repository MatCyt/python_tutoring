# Napisz funkcję, która dla podanego n i c0 wyznacza pierwsze wystąpienie liczby 1 w ciągu Collatza.

def collatz_pierwsza_jedynka(c0, n):
    ciag = [c0]
    for i in range(1, n):
        if c0 % 2 == 0:
            c1 = c0 / 2
        else:
            c1 = 3*c0 + 1
        c0 = c1
        ciag.append(int(c1))

    if 1 in ciag:
        return ciag.index(1)
    else:
        print('w tym ciągu nie ma 1')


collatz_pierwsza_jedynka(11,15)
collatz_pierwsza_jedynka(1,5)
collatz_pierwsza_jedynka(11,5)