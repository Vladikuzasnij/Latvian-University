# Programmas nosaukums: 4.uzdevums
# 4.uzdevums MPR6
# Uzdevuma formulējums: Izveidot programmu, kas, pēc lietotāja secīgi ievadītajām četrstūra virsotņu A(x1, y1), B(x2, y2), C(x3, y3) un D(x4, y4) koordinātām, noskaidro un paziņo, vai šis četrstūris ir ieliekts vai izliekts.
# Programmas autors: Vladislavs Babaņins
# Versija 2.4

# A
x1 = float(input("Ievadi X1 ===> "))
y1 = float(input("Ievadi Y1 ===> "))

# B
x2 = float(input("Ievadi X2 ===> "))
y2 = float(input("Ievadi Y2 ===> "))

# C
x3 = float(input("Ievadi X3 ===> "))
y3 = float(input("Ievadi Y3 ===> "))

# D
x4 = float(input("Ievadi X4 ===> "))
y4 = float(input("Ievadi Y4 ===> "))


#AC taisne
z1 = (x4 - x1)*(y3 - y1) - (y4 - y1)*(x3 - x1)

z2 = (x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1)

#BD taisne
z3 = (x1-x2)*(y4-y2)-(y1-y2)*(x4-x2)

z4 = (x3-x2)*(y4-y2)-(y3-y2)*(x4-x2)

if z1*z2 > 0 or z3*z4 > 0:
    print ("Izliekts")
    
    
else :
    print ("Ieliekts")

