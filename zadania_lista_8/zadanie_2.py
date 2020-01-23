
import argparse

def stworz_ciag(n):
    ciag = (i / (i + 1) for i in range(n))
    return ciag

def zapisz_do_pliku(ciag):
    with open('zadanie_1.txt', 'w') as f:
        for n in ciag:
            f.write('{}\n'.format(n))

if __name__ == '__main__':
    my_parser = argparse.ArgumentParser(description='dlugosc ciagu')
    my_parser.add_argument('n', type=int)
    args = my_parser.parse_args()

    ciag = stworz_ciag(args.n)

    # zapisz_do_pliku(ciag)
    print(ciag)
    for i in range(args.n):
        print(next(ciag))

