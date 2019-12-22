# Stwórz moduł ciag_arytmetyczny.py zawierający funkcje, które dla podanych a1 (pierwszy wyraz ciągu), r (różnica) oraz n zwracają:

def ciag_arytmetyczny(a1, r, n):
    '''zwraca n-ty wyraz ciągu oraz sumę pierwszych n wyrazów

    parametry:
    a1 : pierwszy wyraz ciągu
    r : roznica
    n : ilość wyrazów w ciągu

    '''
    an = a1 + (n - 1) * r
    an_sum = sum(list(range(a1, an + r, r)))
    print(list(range(a1, an + r, r)))
    return an, an_sum


