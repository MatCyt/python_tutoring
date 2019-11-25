# Stwórz słownik, który przyporządkuje pięciu różnym produktom ich cenę. Następnie:

produkty = {"mleko":3.5, "pieczywo":4, "jajka":4.5, "maslo":3, "sok":5}

# w pętli wydrukuj na ekranie listę produktów z ceną
for p,c in produkty.items():
    print(p,c) 

# policz średnią cenę produktu

sum_p = 0
count_p = 0

for p,c in produkty.items():
    sum_p += c
    count_p +=1

print(sum_p/count_p)

# dodaj nowy produkt
produkty["kawa"] = 10

# jak się zmieniła średnia cena?

sum_p = 0
count_p = 0

for p,c in produkty.items():
    sum_p += c
    count_p +=1

print(sum_p/count_p)

# napisz funkcję, która liczy średnią cenę
def srednia_cena(produkty):
    sum_p = 0
    count_p = 0

    for produkt, cena in produkty.items():
        sum_p += cena 
        count_p += 1

    print(sum_p / count_p)

srednia_cena(produkty)

# usuń produkt
del produkty["kawa"]

# policz średnią cenę
srednia_cena(produkty)