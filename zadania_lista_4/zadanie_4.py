# Napisz funkcję, która wypisze na ekranie n pierwszych wyrazów ciągu Fibonacciego.
# Pierwszy wyraz jest równy 0, drugi jest równy 1, każdy następny jest sumą dwóch poprzednich.


def fibonacci(n):
    a, b = 0, 1
    if n == 0: 
        return a 
    elif n == 1: 
        return b
    for i in range(2, n):
        a, b = b, a + b
    return b
  
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(6))