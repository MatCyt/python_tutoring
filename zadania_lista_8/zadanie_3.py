import sys



def stworz_ciag_list(n):
    ciag = [i / (i + 1) for i in range(n)]
    return ciag


def stworz_ciag_gen(n):
    ciag = (i / (i + 1) for i in range(n))
    return ciag


ciag_list = stworz_ciag_list(5)
ciag_gen = stworz_ciag_gen(5)

print(sys.getsizeof(ciag_list))
print(sys.getsizeof(ciag_gen))