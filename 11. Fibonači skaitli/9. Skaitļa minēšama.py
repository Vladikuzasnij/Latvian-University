# Programmas nosaukums: 1. uzd MPR11
# 1. uzdevums MPR11
# Uzdevuma formulējums: Sastādīt programmu, kas nodrošina datora "iedomata" naturāla skaitļa no 1 līdz N minēšanu. Skaitli N ievada lietotajs.
# Versija 1.0

import random

print("Spēlē:\nDators 'iedomāsies' veselo skaitli no 1 līdz N un Jums būs nepieciešāms to atminēt.")
N = int(input("Ievādiet veselo skaitli N ==> "))


x = random.randint(1, N)
sk=1
y=0

y = int(input("Mini skaitļi! ==> "))

while y != x:
    if y < x:
        y = int(input("Neatminēji! Ievadi lielāko ==> "))
    elif y > x:
        y = int(input("Neatminēji! Ievadi mazako ==> "))
    sk = sk+1
    
print("Malacis! Atminēji skaitļi " + str(x) + " intervāla no 1 līdz " + str(N) + " no " + str(sk) + " reizes")