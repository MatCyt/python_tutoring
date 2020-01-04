from random import randint

def celcius_to_fahrenheit(c_degrees):
    f_degree = c_degrees * 1.8 + 32
    return f_degree

def fahrenheit_to_celcius(f_degrees):
    c_degree = (f_degrees - 32) / 1.8
    return c_degree

def generate_random_celcius(n):
    ''' generate random int n times in range -273 to 200'''
    celcius_degrees = [randint(-273, 200) for i in range(1, n+1)]
    return celcius_degrees

def save_to_file(int_format, file_name):
    str_format = list(map(str, int_format))
    file_format = ','.join(str_format)
    full_file_name = file_name + '.txt'
    with open(full_file_name, "w") as f:
        f.write(file_format)

def convert_to_number(file_format):
    str_format = file_format.split(',')
    int_format = list(map(float, str_format))
    return int_format

