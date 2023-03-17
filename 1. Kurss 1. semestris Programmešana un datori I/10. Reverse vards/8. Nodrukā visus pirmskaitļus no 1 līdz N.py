# Programmas nosaukums: 4. uzd MPR10
# 4. uzdevums MPR10
# Uzdevuma formulējums: Sastādīt programmu, kas nodrukā visus pirmskaitļus no 1 līdz N. Skaitli N ievada lietotājs.
# Versija 1.0

import math
import sys

x = int(input("Programmā nodrukā visus pirmskaitļus no 1 līdz N. Ievadiet naturālo skaitļi N ==> "))

if x < 1:
    print("Tas nav naturāls skaitlis")
    sys.exit(0)
    
if x == 1:
    print("1 nav naturāls skaitlis")
    sys.exit(0)

for a in range (1, x+1):
    if a > 1:
        for i in range (2, a):
            if (a % i) == 0:
                break
        else:
            print(a)