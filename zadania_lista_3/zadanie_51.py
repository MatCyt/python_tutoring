# stałe
import turtle
length = 150


# 5.1 zmodyfikuj go tak, aby narysował trójkąt równoboczny
n_sides = 3 # ilosc boków

turtle.speed(20) # ustal predkosc zolwia

# powtorz n_sides razy
for i in range(n_sides):
    turtle.forward(length) # narysuj linie o danej dlugosci
    turtle.right(120)       # obroc sie w prawo o dany kat

turtle.mainloop() # nie zamykaj okna po narysowaniu