# Use conversion module to create celcius.txt in which n randomly generated temperatures will be stored
# Let the n be the CLI input. Script should detect if the user CLI argument is not an integer

import argparse
from conversion import generate_random_celcius
from conversion import save_to_file


# argarse for arguments - number of different celcius degrees
my_parser = argparse.ArgumentParser(description='number of different celcius degrees')
my_parser.add_argument('n', type=int, help='number of c_degrees', default=4)
args = my_parser.parse_args()


celcius_degrees = generate_random_celcius(args.n)

save_to_file(celcius_degrees, 'celcius')

