# Use conversion module
# Read celcius.txt, convert temperatures and save as fahrenheit.txt

from conversion import celcius_to_fahrenheit
from conversion import save_to_file
from conversion import convert_to_number

with open("celcius.txt", "r") as f:
    celcius_raw = f.read()

celcius_int = convert_to_number(celcius_raw)

fahrenheit = list(map(celcius_to_fahrenheit, celcius_int))

save_to_file(fahrenheit, 'fahrenheit')
