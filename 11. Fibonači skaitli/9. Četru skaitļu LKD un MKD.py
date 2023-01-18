# Programmas nosaukums: 2. uzd MPR11
# 2. uzdevums MPR11
# Uzdevuma formulējums: Sastādīt programmu, kas atrod 4 naturālo skaitļu lielāko kopīgo dalītāju un mazāko kopīgo dalāmo. Skaitļus ievada lietotājs.
# Versija 1.0

#----------------

# Uzdevumu skicē:

# 4 skaitli:
# a b c d
# lcm (a, b) = f
# f c d
# lcm (f, c) = g
# g d
# lcm (g, d) = lcm (a, b, c, d)

# Lai atrāstu lcm diviem skaitliem:
# a b
# gcd (a, b) = c
# lcm (а b) = a * b / c
# gcd var atrāst pēc Eiklīda algoritma

#--------------------------

# Uzdevumu plāns

# Četri skaitli
# a b c d
# 1) gcd(a, b) = C
# 2) lcm (a, b) = a*b/C = f
# 3) gcd(f, c) = D
# 4) lcm(f, c) = f*c/D = g
# 5) gcd(g, d) = K
# 6) lcm(g, d) = g*d/K
# 7) lcm(g, d) = lcm(a, b, c, d) (tas vajag printēt)
# 8) lcm(a,b) = f
# 9) lcm(c,d) = n
# 10) lcm(a,b,c,d) = lcm(f,n) (tas vajag printēt)

import math

x = int(input("Ievadi 1.skaitli ===> ")) # skaitlis a
y = int(input("Ievadi 2.skaitli ===> ")) # skaitlis b

if x<=0 or y<=0:
    print("Ievadiet pozitivo veselo skaitli!")
    quit()

A1 = x
B1 = y

#----------
# aprēķini 
# gcd (a, b) = C
# lcm (a, b) = f

a = x
b = y

while b != 0 :
    c = a % b
    a = b
    b = c

LKD12 = a       # gcd (a,b) = C       
MKD12 = (x*y)/a # lcm (a, b) = a*b/C
f = MKD12       # lcm (a, b) = f

#----------

# aprēķini 
# gcd(f, c) = D
# lcm(f, c) = g

x = int(input("Ievadi 3.skaitli ===> ")) # skaitlis c

if x<=0:
    print("Ievadiet pozitivo veselo skaitli!")
    quit()
    
C1 = x
y = f
a = x
b = y

while b != 0 :
    c = a % b
    a = b
    b = c

LKDfc = a        # gcd(f, c) = D
MKDfc = (x*y)/a  # lcm(f, c) = f*c/D = g
g = MKDfc        # lcm(f, c) = g
x = g


#----------

# aprēķini 
# gcd(g, d) = K
# lcm(g, d) = lcm(a, b, c, d)

y = int(input("Ievadi 4.skaitli ===> ")) # skaitlis d

if y<=0:
    print("Ievadiet pozitivo veselo skaitli!")
    quit()
    
D1 = y

a = x
b = y

while b != 0 :
    c = a % b
    a = b
    b = c


LKDgd = a              # gcd(g, d) = K
MKDgd = int((x*y)/a)

#----------

print("\nMazākais kopīgais dalāmais MKD = " + str(MKDgd)) 
print("lcm(" + str(A1) + ", " + str(B1) + ", " + str(C1) + ", " + str(D1) + ") = " + str(MKDgd) + "\n")

#----------
# aprēķini 
# lcm(c,d) = n
# lcm(c,d) = n

a = C1
b = D1

while b != 0 :
    c = a % b
    a = b
    b = c


LKD34 = a # lcm(c,d) = n

a = LKD12 # lcm(a,b) = f
b = LKD34 # lcm(c,d) = n

#----------
# aprēķini 
# lcm(a,b,c,d) = lcm(f,n)


while b != 0 :
    c = a % b
    a = b
    b = c

LKDkop = a    # lcm(a,b,c,d) = lcm(f,n)

#----------

print("Lielākais kopīgais dalītājs LKD = " + str(LKDkop)) 
print("gcd(" + str(A1) + ", " + str(B1) + ", " + str(C1) + ", " + str(D1) + ") = " + str(LKDkop) + "\n")