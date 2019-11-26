# stałe
import turtle
length = 150


# 5.3 zmodyfikuj go tak, aby narysował wielokąt foremny, którego liczba boków podana jest przez użytkownika
n_sides = eval(input('Podaj ilość boków: ')) # ilosc boków

angle = 180 - (((n_sides-2) * 180) / n_sides)

turtle.speed(20) # ustal predkosc zolwia

# powtorz n_sides razy
for i in range(n_sides):
    turtle.forward(length) # narysuj linie o danej dlugosci
    turtle.right(angle)       # obroc sie w prawo o dany kat

turtle.mainloop() # nie zamykaj okna po narysowaniu