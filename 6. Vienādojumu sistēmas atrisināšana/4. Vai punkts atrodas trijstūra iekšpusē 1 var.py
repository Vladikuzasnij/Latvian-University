# Programmas nosaukums: 5.uzdevums
# 5.uzdevums MPR6 (1 metode)
# Uzdevuma formulējums: Izveidot programmu, kas, pēc lietotāja ievadītajām trijstūra virsotņu A(x1, y1), B(x2, y2) un C(x3, y3), un punkta D(x4, y4) koordinātām, noskaidro un paziņo, vai punkts D atrodas trijstūra ABC iekšpusē. 1 metode.
# Programmas autors: Vladislavs Babaņins
# Versija 1.3

import math

x1 = float(input("Ievadi X1 ===> "))
y1 = float(input("Ievadi Y1 ===> "))
x2 = float(input("Ievadi X2 ===> "))
y2 = float(input("Ievadi Y2 ===> "))
x3 = float(input("Ievadi X3 ===> "))
y3 = float(input("Ievadi Y3 ===> "))
x4 = float(input("Ievadi X4 ===> "))
y4 = float(input("Ievadi Y4 ===> "))

ab = math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
bc = math.sqrt((x2-x3)*(x2-x3)+(y2-y3)*(y2-y3))
ac = math.sqrt((x1-x3)*(x1-x3)+(y1-y3)*(y1-y3))
ad = math.sqrt((x1-x4)*(x1-x4)+(y1-y4)*(y1-y4))
bd = math.sqrt((x2-x4)*(x2-x4)+(y2-y4)*(y2-y4))
cd = math.sqrt((x3-x4)*(x3-x4)+(y3-y4)*(y3-y4))


z1 = (x4 - x1) * (y2 - y1) - (x2 - x1) * (y4 - y1)
z2 = (x3 - x1) * (y2 - y1) - (x2 - x1) * (y3 - y1)
z3 = (x4 - x2) * (y3 - y2) - (x3 - x2) * (y4 - y2)
z4 = (x1 - x2) * (y3 - y2) - (x3 - x2) * (y1 - y2)
z5 = (x4 - x3) * (y1 - y3) - (x1 - x3) * (y4 - y3)
z6 = (x2 - x3) * (y1 - y3) - (x1 - x3) * (y2 - y3)

if (z1*z2 > 0) and (z3*z4 > 0) and (z5*z6 > 0) :
    
    print("Punkts D atrodas trijstūra iekšpusē")

else :
    print("Punkts D neatrodas trijstūra iekšpusē")