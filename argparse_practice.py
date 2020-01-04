# https://realpython.com/command-line-interfaces-python-argparse/


import argparse

# INITIALIZE PARSER
my_parser = argparse.ArgumentParser(description='number of different celcius degrees')

# ADD ARGUMENTS
# obligatory argument of type int
my_parser.add_argument('a', type=int, help='a arg')

# optional argument (- before) of type str
my_parser.add_argument('-b', type=str, help='b arg')

# optional argument with default value
my_parser.add_argument('-c', type=int, help='c arg', default=123)

# add argument and store it (this is the default)
my_parser.add_argument('-d', type=str, help='b arg', action='store')

# add argument and store true or false if it is present
my_parser.add_argument('-e', help='b arg', action='store_true')
my_parser.add_argument('-f', help='b arg', action='store_false')

# set a limit of allowed values for an argument
my_parser.add_argument('-g', action='store', choices=['head', 'tail'])

# add argument with flexible number of values
my_parser.add_argument('-h', type=int, help='b arg', nargs='*')

# Parse all argument together
args = my_parser.parse_args()

# Use the arguments
print(args) # as namespace
print(vars(args)) # as dictionary
print(args.a) # one by one
print(args.c)

# use python script.py -h to show help
