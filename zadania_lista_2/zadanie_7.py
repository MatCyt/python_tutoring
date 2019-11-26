# Zapoznaj się z dokumentacją funkcji id.

# Wykonaj następujące polecenia:

x = 2
y = x
print(x, y, id(x), id(y))
y = 3
print(x, y, id(x), id(y))

# Wykonaj następujące polecenia:

x = [1,2]
y = x
print(x, y, id(x), id(y))
y[1] = 3
print(x, y, id(x), id(y))

# Wyjaśnij, dlaczego modyfikacja listy y zmienia wartość listy x, ale nie dzieje się tak w przypadku int.