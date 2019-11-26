# Korzystając z funkcji sys.getsizeof sprawdź, ile pamięci zajmuje:

import sys

print(sys.getsizeof(0))
print(sys.getsizeof(2**100))
print(sys.getsizeof(2**1000))

# Sprawdź, ile pamięci zajmują: True i False. Czy jest to wynik, którego się spodziewałeś?
print(sys.getsizeof(True))
print(sys.getsizeof(False))

# Zapoznaj się z dokumentacją funkcji isinstance.

# Wykonaj następujące polecenia:

print(isinstance(0, int))
print(isinstance(0, float))
print(isinstance(0.0, float))
print(isinstance(True, bool))
print(isinstance(True, int))

# Wyjaśnij rozmiar True i False.
