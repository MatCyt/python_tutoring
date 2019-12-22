from ciag_arytmetyczny import ciag_arytmetyczny

poczatek = int(input('Podaj początek ciągu: '))
roznica = int(input('Podaj roznice: '))
ilosc_n = int(input('Podaj ilosc elementow: '))

an, an_sum = ciag_arytmetyczny(poczatek, roznica, ilosc_n)

print(an)
print(an_sum)