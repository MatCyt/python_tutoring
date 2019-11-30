# Napisz funkcję, która z podanych liczb (ilość dowolna) znajduje najmniejszą.
# Uwaga: Możesz wykorzystać funkcję z zadania 2.

# Opcja 1
def ktora_najmniejsza(*args):
    print(min(list(args)))

ktora_najmniejsza(5, 12, 14, 6, 1)

# Opcja 2
def ktora_najmniejsza(*args):
    minimum = args[0]
    for arg in args:
        if arg < minimum:
            minimum = arg

    print(minimum)


ktora_najmniejsza(5, 12, 14, 6, 1)