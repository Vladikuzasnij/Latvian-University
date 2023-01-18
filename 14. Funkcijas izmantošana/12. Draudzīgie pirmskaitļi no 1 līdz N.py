# Programmas nosaukums: 2. uzd MPR14
# 2. uzdevums MPR14
# Uzdevuma formulējums: Sastādīt programmu, kas nodrukā visus “draudzīgos” pirmskaitļu pārus no 1 līdz N. Par draudzīgu pirmskaitļu pāri tādus divus pirmskaitļus, kuru starpība ir 2. Naturālo skaitli N ievada lietotājs un ievades procesā drīkst kļūdīties ne vairāk kā 3 reizes.
# Versija 1.0

import math

def vaipirmskaitlis (n):
    M = round(math.sqrt(n))+1
    for i in range(2, M):
        if n % i == 0:
            return False
    return True

def draugi(x,y):
    if abs(x-y)==2:
        return True
    else:
        return False


print("Programma nodrukā visus “draudzīgos” pirmskaitļu pārus no 1 līdz N.\nPar draudzīgu pirmskaitļu pāri tādus divus pirmskaitļus, kuru starpība ir 2.\n")


M=0
while M<=3:
    
    if M==0:
        x=input("Ievadiet naturālo skaitli N => ")
    elif M==1 or M==2:
        x=input("Tas nav naturāls skaitlis. Ievadiet naturālo skaitli N => ")
    elif M==3:
        x=input("Jūs 3 reizes kļūdījāties. Beidzam sadarbību!")
        quit()
        
    try:
        x = int(x)
        a = 1/x
        b=math.sqrt(x)

    except:
        M=M+1

    else:
        if x<5:
            print("Pāru nav")
            break
        else:

            sv=""
            b = 3
            for i in range (5, x+1, 2):
                if vaipirmskaitlis(i):
                    a = b
                    b = i
                    if draugi (a,b):
                        sv = sv + (str(a) + " " + str(b)) + "\n"

            print(sv)
            break