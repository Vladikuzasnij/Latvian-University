# Programmas nosaukums: Trīs punktu novietojums attiecība pret taisni
# 2.lekcijas papilduzdevums.
# Uzdevuma formulējums: Izveidot programmu un uzzīmēt blokshēmu, kas paziņo par trīs punktu novietojumu attiecība pret taisnei Ax + By + C = 0 Punktu koordinātas A(x1, y1) un B(x2, y2) C(x3, y3) ievada lietotājs kā arī A, B un C koeficientus.
# Programmas autors: Vladislavs Babaņins
# Versija 3.2

print("Ax + By + C = 0\nA(x1,y1) B(x2,y2) C(x3,y3)\n")

a = float(input("Ievadi A ===> "))
b = float(input("Ievadi B ===> "))
c = float(input("Ievadi C ===> "))

x1 = float(input("Ievadi x1 ===> "))
y1 = float(input("Ievadi y1 ===> "))

x2 = float(input("Ievadi x2 ===> "))
y2 = float(input("Ievadi y2 ===> "))

x3 = float(input("Ievadi x3 ===> "))
y3 = float(input("Ievadi y3 ===> "))

z1 = a*x1 + b*y1 + c
z2 = a*x2 + b*y2 + c
z3 = a*x3 + b*y3 + c

if z1 == 0 and z2 == 0 and z3 == 0:
    print("Trīs punkti ir uz vienas taisnes")
    
elif (z1 == 0 and z2 == 0) or (z2 == 0 and z3 == 0) or (z3 == 0 and z1 == 0):
    print("Divi punkti ir uz taisnes, bet trešais nav uz taisnes")
    
elif (z1 == 0 and z2*z3 > 0) or (z2 == 0 and z1*z3 > 0) or (z3 == 0 and z1*z2 > 0):
    print("Viens uz taisnes, divi pārejie ir vienā puse no taisnes")
    
elif (z1 == 0 and z2*z3 < 0) or (z2 == 0 and z1*z3 < 0) or (z3 == 0 and z1*z2 < 0):
    print("Viens uz taisnes, divi pārejie ir pretējas puses no taisnes")
    
elif (z1*z2>0) and (z1*z3>0):
    print("Visi trīs punkti ir vienā puse no taisnes")

else:
    print("Divi punkti ir vienā puse no taisnes, trešais punkts ir pretēja puse no taisnes")