from conversion import convert_to_number

with open("celcius.txt", "r") as f:
    celcius_raw = f.read()

with open("fahrenheit.txt", "r") as f:
    fahrenheit_raw = f.read()


celcius_int = convert_to_number(celcius_raw)
fahrenheit_int = convert_to_number(fahrenheit_raw)

c_to_kelvin = list(map(lambda x: x + 273.15, celcius_int))
f_to_kelvin = list(map(lambda x: (x + 459.67) * (5/9), fahrenheit_int))

ck_round = list(map(round, c_to_kelvin))
fk_round = list(map(round, f_to_kelvin))

if ck_round == fk_round:
    print('celcius and fahrenheits temperatures are identical')