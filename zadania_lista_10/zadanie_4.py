# Napisz skrypt, który pobiera od użytkownika dowolny tekst, a następnie drukuje na ekranie liczbę występujących w nim samogłosek.

samogloski = ['a', 'e', 'i', 'o', 'u', 'y']

def drukuj_samogloski():
    user_input = input('podaj dowolny tekst: ')
    output = [l for l in list(user_input) if l in samogloski]
    print(output)

drukuj_samogloski()