# Korzystając z range utwórz listę zawierającą wszystkie wielokrotności liczby 3 mniejsze od 100.

x = list(range(1, 100, 3))
print(type(x))
print(x)

# Korzystając z del usuń co trzeci element (zaczynając od piątego).
del x[4::3]
print(x)

# Sprawdź definicję funkcji wbudowanej sum (help(sum)). Wykorzystaj ją oraz funkcję len, aby wyliczyć średnią arytmetyczną otrzymanej listy.
help(sum)

mean_x = sum(x) / len(x)
print(mean_x)