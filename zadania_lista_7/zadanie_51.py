import argparse

# parser
my_parser = argparse.ArgumentParser(description='read txt files in different modes')

my_parser.add_argument('file', type=str, help='text file to read')
my_parser.add_argument('-m', type=int, help='reading mode: 0, 1 or 2', choices=[0, 1, 2], default=0)

args = my_parser.parse_args()

# read file
full_file_name = args.file + '.txt'

with open(full_file_name, "r") as f:
    full_text = f.read()

lines = full_text.split('\n')

if args.m == 1:
    for i in lines:
        if i[0] != '#':
            print(i)
elif args.m == 2:
    for i, l in enumerate(lines):
        print(str(i) + '. ', l)
else:
    print(full_text)



