from random import randint

def celcius_to_fahrenheit(c_degrees):
    f_degrees = c_degrees * 1.8 + 32
    return f_degrees

def fahrenheit_to_celcius(f_degrees):
    c_degrees = (f_degrees - 32) / 1.8
    return c_degrees

def generate_random_celcius(n):
    ''' generate random int n times in range -273 to 200'''
    celcius_degrees = [randint(-273, 200) for i in range(1, n+1)]
    return celcius_degrees



