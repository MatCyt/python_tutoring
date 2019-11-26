# PRZYKLAD
lista = []
for i in range(10):
    lista.append(i)

print(lista)

lista2 = [i for i in range(10)]

print(lista2)

# Wykorzystaj listę składaną (list comprehension), aby stworzyć sekwencję kwadratów liczb naturalnych mniejszych od 100.
# Następnie (korzystając z enumerate) wydrukuj na ekranie:

lista3 = [i**2 for i in range(10)]

print(lista3)