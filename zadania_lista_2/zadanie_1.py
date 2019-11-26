x = (1, 2, 3, 4, 'piec', 'szesc', 'siedem', 'osiem', 'dziewiec')

print(x[0:3])

print(x[-2:])

print(x[2::2])

print(len(x))

print(len(x[-2]))

print(x[:5] + (5, 6) + x[-3:])
print(x[:5], (5, 6), x[-3:])