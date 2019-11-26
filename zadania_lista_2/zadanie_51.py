slubowanie = """
Wstępując do wspólnoty akademickiej Uniwersytetu Wrocławskiego, ślubuję uroczyście:
- zdobywać wiedzę i umiejętności,
- postępować zgodnie z prawem, tradycją i dobrymi obyczajami akademickimi,
- dbać o dobre imię Uniwersytetu Wrocławskiego i godność studenta.
"""

print(slubowanie)


# Popraw zmienną slubowanie, aby tekst zaczynał się wielką literą.
print(slubowanie.capitalize())
print(slubowanie[1].lower() + slubowanie[2:])

# Korzystając z funkcji count sprawdź, ile razy występuje spójnik "i".
print(slubowanie.count(' i '))

# Korzystając z in sprawdź, czy słowo "Uniwersytet" występuje w tekście.
print('Uniwersytet' in slubowanie)

# Korzystając z funkcji str.split:
# stwórz listę wyrazów występujących w tekście (30 słów => 30 elementów)
print(slubowanie.split())

# stwórz listę, której każdy element odpowiada jednej linijce tekstu
print(slubowanie.split('\n'))