# Programmas nosaukums: Divu punktu novietojums attiecība pret taisni
# 1.lekcijas papilduzdevums.
# Uzdevuma formulējums: Izveidot programmu un uzzīmēt blokshēmu, kas paziņo par divu punktu novietojumu attiecība pret taisnei Ax + By + C = 0 Punktu koordinātas A(x1, y1) un B(x2, y2) ievada lietotājs kā arī A, B un C koeficientus.
# Programmas autors: Vladislavs Babaņins
# Versija 2.0

print("Ax + By + C = 0\nA(x1,y1) B(x2,y2)\n")

a = float(input("Ievadi A ===> "))
b = float(input("Ievadi B ===> "))
c = float(input("Ievadi C ===> "))
x1 = float(input("Ievadi x1 ===> "))
y1 = float(input("Ievadi y1 ===> "))
x2 = float(input("Ievadi x2 ===> "))
y2 = float(input("Ievadi y2 ===> "))

z1 = a*x1 + b*y1 + c
z2 = a*x2 + b*y2 + c

if z1 == 0 and z2 == 0:
    
    print("Divi punkti ir uz vienas taisnes")
    
elif z1 == 0 or z2 == 0:
    print("Viens punkts ir uz taisnes, otrais punkts nav uz taisnes")
    
elif z1*z2 > 0:
    print("Atrodas vienā puse no taisnes")
    
else:
    print("Punkti nav vienā pusē taisnei")