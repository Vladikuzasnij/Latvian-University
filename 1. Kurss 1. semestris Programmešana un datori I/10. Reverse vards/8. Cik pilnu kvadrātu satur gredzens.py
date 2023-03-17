# Programmas nosaukums: 7. uzd MPR10
# 7. uzdevums MPR10
# Uzdevuma formulējums: Sastādīt programmu, kas noskaidro, cik pilnu kvadrātu (1x1 vienība) satur gredzens, kura iekšējais rādiuss ir R1, bet ārējais rādiuss ir R2. Skaitļus R1 un R2 ievada lietotājs.
# Versija 1.0

import math
import sys

def check_squares(a, b):
    n = 0
    if r1*r1 >= (a+1)*(a+1) + b*b >= r2*r2 and r1*r1 >= a*a + (b+1)*(b+1) >= r2*r2 and r1*r1 >= (a+1)*(a+1) + (b+1)*(b+1) >= r2*r2:
        n+=1

    if r1*r1 >= (a+1)*(a+1) + b*b >= r2*r2 and r1*r1 >= (a+1)*(a+1) + (b-1)*(b-1) >= r2*r2 and r1*r1 >= a*a + (b-1)*(b-1) >= r2*r2:
        n+=1
        
    if r1*r1 >= a*a + (b+1)*(b+1) >= r2*r2 and r1*r1 >= (a-1)*(a-1) + b*b >= r2*r2 and r1*r1 >= (a-1)*(a-1) + (b+1)*(b+1) >= r2*r2:
        n+=1
        
    if r1*r1 >= a*a + (b-1)*(b-1) >= r2*r2 and r1*r1 >= (a-1)*(a-1) + b*b >= r2*r2 and r1*r1 >= (a-1)*(a-1) + (b-1)*(b-1) >= r2*r2:
        n+=1
        
    return n

r1 = float(input("Ievadiet gredzena arējo rādiusu ==> "))
r2 = float(input("Ievadiet gredzena iekšējo rādiusu ==> "))


if r1 < 0 or r2 < 0 :
    print("Dati nav ievadīti atbilstoši nosacījumiem")
    sys.exit(0)


a = math.floor(r1)
b = -math.floor(r1)

number_of_squares = 0

while a >= -r1:
    b = -math.floor(r1)
    while b <= r1:
        if r1*r1 >= a*a + b*b >= r2*r2:
            
            number_of_squares += check_squares(a, b)
        b+=1
    a-=1
    
print(str(int(number_of_squares/4)) + " pilno kvadrātu ir gredzenā")