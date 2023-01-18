# Programmas nosaukums: 6. uzd MPR10
# 6. uzdevums MPR10
# Uzdevuma formulējums: Sastādīt programmu, kas noskaidro, cik pilnu kvadrātu (1x1 vienība) satur riņķis ar rādiusu R. Skaitli R ievada lietotājs.
# Versija 1.0

import math

r=float(input("Ievadiet riņķa rādiusu ==> "))
r1=int(r)
s=0

for i in range (1, r1):
    x=round(math.sqrt(r*r-i*i))
    if x*x+i*i==r*r:
        s=s+4*x
    else:
        s=s+int(math.sqrt(r*r-i*i))*4

print(str(s) + " pilno kvadrātu 1x1 satur riņķis ar rādiusu " + str(r) + " vienības")        