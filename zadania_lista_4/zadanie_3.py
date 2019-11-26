# Napisz funkcję, która z podanych liczb (ilość dowolna) znajduje najmniejszą.
# Uwaga: Możesz wykorzystać funkcję z zadania 2.

def ktora_najmniejsza(*args):
    print(min(list(args)))

ktora_najmniejsza(5, 12, 14, 6, 1)