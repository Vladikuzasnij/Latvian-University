# Programmas nosaukums: 2.uzdevums
# 2.uzdevums MPR6
# Uzdevuma formulējums: Izveidot programmu, kas atrisina vienādojumu sistēmu. ... Koeficientus a, b, c un d ievada lietotājs.
# Programmas autors: Vladislavs Babaņins
# Versija 1.6

import math

print("ax^2 + ay^2 + b = 0\ncxy + d = 0\n")

a = float(input("Ievadiet a ===> "))
b = float(input("Ievadiet b ===> "))

c = float(input("Ievadiet c ===> "))
d = float(input("Ievadiet d ===> "))

if a==0 or c==0 :
    print("Specgadījums")

else:
    zemsakne1 = (-b/a) - ((2*d)/c)
    zemsakne2 = (-b/a) + ((2*d)/c)

    if zemsakne1 < 0 or zemsakne2 < 0 :
        print("Nav atrisinājumu realos skaitļos")

    else:
        p1= math.sqrt(zemsakne1)
        p2= math.sqrt(zemsakne2)

        x = (-p1 + p2)/2
        y = (-p1 - p2)/2

        if abs(x) == abs(y):
            print("x1 = " +str(x) + " y1 = " + str(y))
            print("x2 = " +str(-x) + " y2 = " + str(-y))
            
        if abs(x) != abs(y):
            print("")
            print("x1 = " + str(x) + " y1 = " + str(y))
            print("x2 = " + str(y) + " y2 = " + str(x))
            print("x3 = " + str(-x) + " y3 = " + str(-y))
            print("x4 = " + str(-y) + " y4 = " + str(-x))
