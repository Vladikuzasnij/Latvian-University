# Programmas nosaukums: 1.uzdevums
# 1.uzdevums MPR6
# Uzdevuma formulējums: Izveidot programmu, kas atrisina vienādojumu sistēmu. ... Koeficientus a, b, c, d, e ievada lietotajs
# Programmas autors: Vladislavs Babaņins
# Versija 1.4

import math
import sys

print("ax^2 + by^2 + c = 0\ndx^2 + ey + f = 0\n")

a = float(input("Ievadiet a ===> "))
b = float(input("Ievadiet b ===> "))

c = float(input("Ievadiet c ===> "))
d = float(input("Ievadiet d ===> "))

e = float(input("Ievadiet e ===> "))
f = float(input("Ievadiet f ===> "))

a_di = d*b
b_di = -1*a*e
c_di = d*c-a*f

D = (b_di)*(b_di) - 4*(a_di)*(c_di)

if D < 0:
    print("Nav atrisinājumu")
    sys.exit(0)

elif d==0:
    print("Nav atrisinājumu")
    sys.exit(0)

elif a==0:
    print("Nav atrisinājumu")
    sys.exit(0)

else:
    y1 = (-1*(b_di) + math.sqrt(D))/(2*a_di)
    y2 = (-1*(b_di) - math.sqrt(D))/(2*a_di)

    
    k1 = (-1*c-b*y1*y1)/a
    k2 = (-1*c-b*y2*y2)/a

    if k2 > 0 and k1 > 0:

        x1 = math.sqrt(k1)
        x2 = -1*math.sqrt(k1)

        x3 = math.sqrt(k2)
        x4 = -1*math.sqrt(k2)
        
        print("x1 = " + str(x1) + " y1 = " + str(y1) + " x2 = " + str(x2) + " y2 = " + str(y2) )
        print("x3 = " + str(x3) + " y2 = " + str(y2) + " x4 = " + str(x4) + " y2 = " + str(y2) )

    else:
        print("Nav atrisinājumu")
        sys.exit(0)

