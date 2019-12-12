import sys
sys.path.insert(0, "c:/Users/mcytrowski/Desktop/python_tutoring/zadania_lista_5")

from ciag_arytmetyczny import ciag_arytmetyczny

poczatek = int(input('Podaj początek ciągu: '))
roznica = int(input('Podaj roznice: '))
ilosc_n = int(input('Podaj ilosc elementow: '))

print(ciag_arytmetyczny(poczatek, roznica, ilosc_n)[0])
print(ciag_arytmetyczny(poczatek, roznica, ilosc_n)[1])