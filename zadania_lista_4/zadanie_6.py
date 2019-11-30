
# Napisz funkcję, która przyjmuje dowolną liczbę argumentów pozycyjnych oraz kluczowych.
# 1 -> wartość pierwszego argumentu

# Niech funkcja drukuje argumenty kluczowe w formie listy:
# nazwa (klucz) -> wartość

# MAIN SOLUTION
def print_everything(*args, **kwargs):
    '''

    :param args:
    :param kwargs:
    :return:
    '''

    # for args
    for position, arg in enumerate(args):
        print("{} -> {}".format(position + 1, arg))

    # for kwargs
    for key, value in kwargs.items():
        print("nazwa {} -> {}".format(key, value))


print_everything(1, 2, 'a', 'b', klucz1 = '22', klucz2 = '33')


# ADDITIONAL SOLUTION
def print_everything_add(*args, **kwargs):
    kwargs_list = [ [key, kwarg] for key, kwarg in kwargs.items() ]
    all_arguments = list(args) + kwargs_list

    for position, value in enumerate(all_arguments):
        print, print("{} -> {}".format(position, value))


print_everything_add(1, 2, 'a', 'b', klucz1 = '22', klucz2 = '33')
