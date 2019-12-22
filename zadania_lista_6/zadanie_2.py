def check_if_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


print(check_if_prime(9))
print(check_if_prime(11))
