
# Unzip i zamiana
x = [1, 2]

a, b = x
print(a, b)

a, b = b, a
print(a, b)

# Splat
x = "Python"

print(x)
print(*x) # zip/unzip działa na wszystkich sekwencjach

# Unzip i splat
lista = [1, 2, 3, 4, 5]

# a, b = lista # ValueError: too many values to unpack (expected 2)
a, *b = lista # a = lista[0], b = reszta
print(a, b)

a, *b, c = lista # a, b[0], b[1], b[2], c
print(a, b, c)

# Pakowanie - zip - stworzenie pary tupli z dwóch list
x = [1, 2, 3]
y = ['a', 'b', 'c']

zipped = zip(x, y) # pary (x[i], y[i])

print(*zipped)
print(zipped)


# other
lista = [[1, 2, 3], [4, 5, 6]]
for k, l, i in lista:
    print(k)

# dodanie indexu do listy - enumarate
# domyślnie indexuje od 0
lista = [1, 2, 3, 4, 5]
for index, i in enumerate(lista):
    print(str(index + 1) + '. ', i)