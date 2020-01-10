
# COWS AND BULLS
import random

def get_random():
    ''' draw random four digit number '''
    random_number = random.randint(1000, 9999)
    return list(str(random_number))


def get_input():
    ''' ask player for four digit input '''
    while True:
        player_guess = input('Make your guess: ')
        if len(player_guess) != 4:
            print('This is not a correct value. 4 digits only')
        else:
            return list(player_guess)

def count_cows(random_number, player_guess):
    ''' match random rumber with player guess, counts numbers matched both for value and index position

    :param random_number: 4 digit number as str, output of get_random()
    :param player_guess: 4 digit number as str, output of get_input()
    '''
    cows = [digit for i, digit in enumerate(random_number) if digit == player_guess[i]]
    random_number_left = [digit for i, digit in enumerate(random_number) if digit != player_guess[i]]
    player_guess_left = [digit for i, digit in enumerate(player_guess) if digit != random_number[i]]
    n_cows = len(cows)
    return n_cows, random_number_left, player_guess_left

def count_bulls(random_left, guess_left):
    ''' counts match of numbers in terms of unique values

    :param random_left: unmatched number of values for random_number - count_cows() return
    :param guess_left: unmatched number of values for player_guess -  count_cows() return
    '''
    n_bulls = 0
    for digit in guess_left:
        if digit in random_left:
            n_bulls += 1
            random_left.remove(digit)
    return n_bulls

if __name__ == "__main__":
    random_number = get_random()
    trials = 1
    while True:
        player_guess = get_input()
        if player_guess != random_number:
            n_cows, random_left, guess_left = count_cows(random_number, player_guess)
            n_bulls = count_bulls(random_left, guess_left)
            trials += 1
            print('Krowy: {}, Byki: {}'.format(n_cows, n_bulls))
        else:
            print('You won! Number of trials: {}'.format(trials))
            break

