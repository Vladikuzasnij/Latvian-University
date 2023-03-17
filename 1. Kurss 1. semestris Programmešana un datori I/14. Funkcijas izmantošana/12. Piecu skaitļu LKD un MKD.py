# Programmas nosaukums: 1. uzd MPR14
# 1. uzdevums MPR14
# Uzdevuma formulējums: Sastādīt programmu, kas atrod 5 naturālo skaitļu lielāko kopīgo dalītāju un mazāko kopīgo dalāmo. Skaitļus ievada lietotājs, bet aprēķini tiek veikti tikai tad, ja lietotājs ir ievadījis naturālus skaitļus, pretējā gadījumā tiek izvadīts atbilstošs paziņojums.
# Versija 1.0

import math

# Divu skaitļu gcd atrāšana
def my_gcd(a,b):
    
    while b != 0 :
        c = a % b
        a = b
        b = c

    return a

# Divu skaitļu lcm atrāšana
# lcm (a, b) = a*b/(gcd (a,b))
def my_lcm(a,b):

    return a*b/my_gcd(a,b)

print("Programma atrod 5 naturālo skaitļu lielāko kopīgo dalītāju un mazāko kopīgo dalāmo.\nIevadiet naturālus skaitļus!\n")
x = input("Ievadi 1.skaitli ===> ") # skaitlis a
y = input("Ievadi 2.skaitli ===> ") # skaitlis b
z = input("Ievadi 3.skaitli ===> ")
w = input("Ievadi 4.skaitli ===> ")
q = input("Ievadi 5.skaitli ===> ")

#skaitļu parbaude vai viņi ir veseli pozitivie skaitļi (dalam ar 0 un sqrt()) tests.
M=0
while M<=3:
    
    if M==1 or M==2:
        #print("Viens no ievadītajiem skaitliem nav naturāls skaitlis!")
        x = input("Ievadi 1.skaitli ===> ") # skaitlis a
        y = input("Ievadi 2.skaitli ===> ") # skaitlis b
        z = input("Ievadi 3.skaitli ===> ")
        w = input("Ievadi 4.skaitli ===> ")
        q = input("Ievadi 5.skaitli ===> ")
    elif M==3:
        print("Jūs 3 reizes kļūdījāties. Beidzam sadarbību!")
        quit()    
        
    try:
        x = int(x)
        a = 1/x
        b=math.sqrt(x)

        y = int(y)
        c = 1/y
        d = math.sqrt(y)

        z = int(z)
        e = 1/z
        f = math.sqrt(z)

        w = int(w)
        g = 1/w
        h = math.sqrt(w)

        q = int(q)
        k = 1/q
        v = math.sqrt(q)

    except:
        M=M+1
        print("\nViens no ievadītajiem skaitļiem nav naturāls skaitlis!\n")
        

    else:
        #noteiksim gcd no 5 skaitliem
        t=my_gcd(x,y)
        u=my_gcd(t,z)
        l=my_gcd(u,w)
        v=my_gcd(l,q)
        #print(v)
        #print("gcd(" + str(x) + ", " + str(y) + ", " + str(z) + ", " + str(w) + ", " + str(q) + ") = " + str(v))
        print("LKD(" + str(x) + ", " + str(y) + ", " + str(z) + ", " + str(w) + ", " + str(q) + ") = " + str(v))

        #noteiksim lcm no 5 skaitliem
        a=my_lcm(x,y)
        s=my_lcm(a,z)
        d=my_lcm(s,w)
        g=my_lcm(d,q)
        #print(g)
        # print("lcm(" + str(x) + ", " + str(y) + ", " + str(z) + ", " + str(w) + ", " + str(q) + ") = " + str(g))
        print("MKD(" + str(x) + ", " + str(y) + ", " + str(z) + ", " + str(w) + ", " + str(q) + ") = " + str(g))
        break
