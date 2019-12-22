# Napisz funkcję, która dla podanego n i c0 wyznacza n-ty wyraz ciągu Collatza.

def problem_collatza(c0, n):
    ciag = [c0]
    for i in range(1, n):
        if c0 % 2 == 0:
            c1 = c0 / 2
        else:
            c1 = 3*c0 + 1
        c0 = c1
        ciag.append(int(c1))

    return ciag, ciag[-1]

ciag, ciag1 = problem_collatza(11, 20)

print(ciag)
print(ciag1)
