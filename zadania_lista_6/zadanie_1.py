
def ciag_geometryczny(a1, q, n):
    ciag = [a1]

    for i in range(1, n):
        a2 = q * ciag[-1]
        ciag.append(a2)

    return ciag

def znajdz_liczby_parzyste(lista):
    lista_parzysta = [cyfra for cyfra in lista if cyfra % 2 == 0]
    return lista_parzysta

ciag = ciag_geometryczny(1, 2, 5)

print(ciag)

print(znajdz_liczby_parzyste(ciag))