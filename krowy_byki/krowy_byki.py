# TODO main

# 1235
# 5558
# 5555


# COWS AND BULLS
import random


def get_random():
    random_number = random.randint(1000, 9999)
    return list(str(random_number))


def get_input():
    while True:
        player_guess = input('Make your guess: ')
        if len(player_guess) != 4:
            print('This is not a correct value. 4 digits only')
            continue
            
        else:
            return list(player_guess)
            break

def count_cows(random_number, player_guess):
    cows = [digit for i, digit in enumerate(random_number) if digit == player_guess[i]]
    random_number_left = [digit for i, digit in enumerate(random_number) if digit != player_guess[i]]
    player_guess_left = [digit for i, digit in enumerate(player_guess) if digit != random_number[i]]
    n_cows = len(cows)
    return n_cows, random_number_left, player_guess_left

def count_bulls(random_left, guess_left):
    n_bulls = 0
    for digit in guess_left:
        if digit in random_left:
            n_bulls += 1
            random_left.remove(digit)
    return n_bulls


# FUNKCJA | krowy i byki
    # porównaj wylosowana i input
    # dodaj krowę za poprawne miejsce i liczbę
    # dodaj byka za poprawną liczbę
    # zwróć odpowiedni format
    # zlicz ilość prób
    # pytaj dalej

# funkcja | sprawdzenie czy kończyć grę

# zakończ kiedy będzie odpowiednia ilość



# main = main
# liczba = FUN 1
random_number = get_random()

# stoper = 0
play_game = 0

while play_game = 0:
    # FUN input - pętla z while żeby sprawdzać czy input jest zgodny?
    # FUN krowy_byki
    # FUN sprawdź czy koniec

# zakończ