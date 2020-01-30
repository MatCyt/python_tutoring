# Napisz skrypt, który wymaga dwóch argumentów z linii komend:
# python append.py file text
# Program powinien:
# dodać text na koniec pliku file (od nowej linii)
# stworzyć file, jeśli nie istnieje
# zwracać odpowiedni komunikat i przerywać pracę programu, gdy podana została zła liczba argumentów

import argparse
import os


# initiate argparse
my_parser = argparse.ArgumentParser(description='plik oraz wartość tekstowa')

my_parser.add_argument('file', type=str, help='nazwa pliku')
my_parser.add_argument('text', type=str, help='tekst do dolaczenia')

args = my_parser.parse_args()

# write to file
full_file_name = args.file + '.txt'

if os.path.exists(full_file_name):
    edit_mode = 'a'
else:
    edit_mode = 'w'

with open(full_file_name, edit_mode) as f:
    new_text = f.write(args.text)
