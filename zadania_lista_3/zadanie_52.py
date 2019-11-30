# stałe
import turtle
length = 150


# 5.2 zmodyfikuj go tak, aby narysował sześciokąt foremny

n_sides = 6 # ilosc boków

turtle.speed(20) # ustal predkosc zolwia

# powtorz n_sides razy
for i in range(n_sides):
    turtle.forward(length) # narysuj linie o danej dlugosci
    turtle.right(60)       # obroc sie w prawo o dany kat

turtle.mainloop() # nie zamykaj okna po narysowaniu



