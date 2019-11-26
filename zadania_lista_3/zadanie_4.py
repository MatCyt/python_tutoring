# losuje liczbę całkowitą mniejszą od 100 (help(random.randint))
# pyta użytkownika o odgadnięcie liczby
# informuje użytkownika, czy podana przez niego liczba jest:
# dużo mniejsza (różnica > 50)
# mniejsza (różnica > 10)
# trochę mniejsza
# trochę większa
# większa (różnica > 10)
# dużo większa (różnica > 50)
# program się kończy, gdy użytkownik odgadnie wylosowaną liczbę

import random

wylosowana = random.randint(1, 99)

print(wylosowana)

while True:
    zgd = int(input('Podaj liczbę:'))
    roznica = abs(wylosowana - zgd)
    if zgd < wylosowana:
        if roznica > 50:
            print('duzo mniejsza')
        elif roznica > 10:
            print('mniejsza')
        else:
            print('troche mniejsza')
    elif zgd > wylosowana:
        if roznica > 50:
            print('duzo wieksza')
        elif roznica > 10:
            print('wieksza')
        else:
            print('troche wieksza')
    else:
        print('gratulacje!')
        break