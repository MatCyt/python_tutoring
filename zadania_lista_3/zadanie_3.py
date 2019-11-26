#!/usr/bin/env python

# lista zakupów
grocery = ['jajka', 'mleko', 'chleb', 'maslo', 'piwo']
# ilość sztuk
n_items = {}
# zakazane produkty
prohibited = ['wódka', 'piwo', 'wino']

# w pętli pytamy użytkownika, ile sztuk danego produktu chce kupić
for product in grocery:
    if product in prohibited:
        n_items[product] = 0
    else:
        ilosc = input("Podaj ilość {}: ".format(product))
        n_items[product] = ilosc

    # wydrukuj na ekranie komunikat: "Produkt [nazwa produktu]: sztuk = "
    # pobierz liczbę od użytkownika i zapisz w n_items dla danego produktu
    # pomiń produkty zakazane (i automatycznie przyjmij ilość = 0)

# w pętli wydrukuj: [lp]. [nazwa produktu]: [ilość]
# czyli np.: 1. jajka: 5 itd.

for indeks, (p, i) in enumerate(n_items.items()):
    print('{}. {}: {}'.format(indeks + 1, p, i))

