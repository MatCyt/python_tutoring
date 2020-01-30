# Napisz funkcję, która liczy objętość prostopadłościanu. 
# Funkcja powinna przyjmować trzy argumenty, które są długościami krawędzi. 
# Wywołana z jednym argumentem powinna się domyślić, że chodzi o sześcian, czyli:

# funkcja(a)       zwraca objętość sześcianu
# funkcja(a, b, c) zwraca objętość prostopadłościanu



def oblicz_objetosc(*args):
    if len(args) == 1:
        objetosc = args[0] ** 3
        return objetosc
    elif len(args) == 3:
        objetosc = args[0] * args[1] * args[2]
        return objetosc
    else:
        return('wprowadz 1 albo 3 argumenty')


a = oblicz_objetosc(1,2,3)
b = oblicz_objetosc(2)
c = oblicz_objetosc(1,2)

print(a,b,c)