from random import randint

def celcius_to_fahrenheit(c_degrees):
    f_degree = c_degrees * 1.8 + 32
    return f_degree

def fahrenheit_to_celcius(f_degrees):
    c_degree = (f_degrees - 32) / 1.8
    return c_degree

def generate_random_celcius(n):
    ''' generate random int n times in range -273 to 200'''
    celcius_degrees = [randint(-273, 200) for i in range(0, n)]
    return celcius_degrees

def save_to_file(file_content, file_name, file_extension = 'txt'):
    ''' save degrees to file, converting them to string

    parameters:
    file_content : iterable object
    file_name : end name of the txt file

    '''

    str_format = list(map(str, file_content))
    file_format = ','.join(str_format)
    full_file_name = '{}.{}'.format(file_name, file_extension)
    with open(full_file_name, "w") as f:
        f.write(file_format)

def convert_to_number(file_content):
    content_splitted = file_content.split(',')
    float_list = list(map(float, content_splitted))
    return float_list

