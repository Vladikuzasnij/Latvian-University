# Programmas nosaukums: 5. uzd MPR12
# 5. uzdevums MPR12
# Uzdevuma formulējums: Sastādīt programmu, kas aprēķina laukumu, kuru ierobežo divas parabolas. Parabolu koeficientus un precizitāti ievada lietotājs.
# Versija 1.0

import math

print("Programma noteic laukumu kuru ierobežo divas parabolas:\ny = ax^2 + bx + c \ny = dx^2 + ex + f\n")

a1 = float(input("Ievadi a ===> "))
b1 = float(input("Ievadi b ===> "))
c1 = float(input("Ievadi c ===> "))

a2 = float(input("Ievadi d ===> "))
b2 = float(input("Ievadi e ===> "))
c2 = float(input("Ievadi f ===> "))

pr =  float(input("Ievadi precizitāti ===> "))

a = a1 - a2
b = b1 - b2
c = c1 - c2

if a == 0 :
    print("Laukums ir 0")
    quit()
else :
    d = b * b - 4 * a * c # Diskriminants
    if d < 0:
        print("Laukums ir 0") # Kvadratvienādojumam realu saknu nav jo divam parabolam nav krustpunktu, tāpēc laukums neveidojas.
        quit()
    elif d == 0 :
        x12 = -b / 2 / a
        print("Laukums ir 0") # jo divas parabolas krustpunkts ir tikai viens, tāpēc laukums neveidojas.
        quit()
    else :
        x1 = (-b + math.sqrt(d)) / (2 * a) # Parabolu krustpunkti
        x2 = (-b - math.sqrt(d)) / 2 / a
        
# ---------  laukums zem pirmās funkcijas  

a = x1 
b = x2


s1 = 0
n = 2
x = (b - a) / n
s2 = 0

for i in range (n) :
    y = a+i*x
    s2 = s2 + (a1*y*y + b1*y + c1)*x
n = n * 2

while abs(s1 - s2) > pr :
    s1 = s2
    x = (b - a) / n
    s2 = 0
    for i in range (n) :
        y = a+i*x
        s2 = s2 + (a1*y*y + b1*y + c1)*x
    n = n * 2

S1 = s2

# --------- laukums zem otras funkcijas

a = x1 
b = x2


s1 = 0
n = 2
x = (b - a) / n
s2 = 0

for i in range (n) :
    y = a+i*x
    s2 = s2 + (a2*y*y + b2*y + c2)*x
n = n * 2

while abs(s1 - s2) > pr :
    s1 = s2
    x = (b - a) / n
    s2 = 0
    for i in range (n) :
        y = a+i*x
        s2 = s2 + (a2*y*y + b2*y + c2)*x
    n = n * 2
    
    
S2 = s2

S_kop = abs(S1 - S2)

print("\nLaukums, kuru ierobežo divas parabolas, ir vienāds ar:\n" + str(S_kop))
print("Rezultāts ir iegūts ar precizitāti:\n" + str(pr))
