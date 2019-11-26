# Napisz funkcję, która wypisze na ekranie n pierwszych wyrazów ciągu Fibonacciego.
# Pierwszy wyraz jest równy 0, drugi jest równy 1, każdy następny jest sumą dwóch poprzednich.

def fibonacci(ilosc_elementow):
    if ilosc_elementow == 0:
        return(0)
    elif ilosc_elementow == 1:
        return(1)
    elif ilosc_elementow == 2:
        return(1)
    else:
        return(fibonacci(ilosc_elementow-1) + fibonacci(ilosc_elementow-2))


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(6))



def fibonacci2(n): 
    a = 0
    b = 1
    if n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(2,n): 
            c = a + b 
            a = b 
            b = c 
        return b 
  
print(fibonacci2(0))
print(fibonacci2(1))
print(fibonacci2(2))
print(fibonacci2(6))