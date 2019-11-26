# Napisz funkcję, która znajduje mniejszą liczbę z dwóch podanych.

def ktora_mniejsza(a, b):
    if a < b:
        print("{} is smaller than {}".format(a, b))
    elif a == b:
        print("{} and {} are equal".format(a, b))
    else:
        print("{} is smaller than {}".format(b, a))

ktora_mniejsza(3, 6)

ktora_mniejsza(9, 2)

ktora_mniejsza(4, 4)