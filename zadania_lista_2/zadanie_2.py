x = ['Kasia', 'Basia', 'Marek', 'Darek']

x.append('Jozek')

x.extend(['Ania', 'Basia'])

# x.sort()
print(sorted(x))

print(x)

print(x[3])
print(x[:2])
print(x[-2:])

print(x)
x.remove('Basia') # usuwa pierwsze wystąpienie
print(x)

print(len(x))

y = tuple(x)
print(y)

z = list(y)