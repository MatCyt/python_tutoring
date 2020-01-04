# Use conversion module to create celcius.txt in which n randomly generated temperatures will be stored
# Let the n be the CLI input. Script should detect if the user CLI argument is not an integer

import argparse
from conversion import generate_random_celcius

# argarse for arguments - number of different celcius degrees
my_parser = argparse.ArgumentParser(description='number of different celcius degrees')
my_parser.add_argument('n', type=int, help='number of c_degrees', default=4)
args = my_parser.parse_args()

celcius_degrees = generate_random_celcius(args.n)

# generate text file to save them
for n in celcius_degrees:
    with open("celcius.txt", "w") as f:
        f.write(str(n))

