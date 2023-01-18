# Programmas nosaukums: 4. uzd MPR12
# 4. uzdevums MPR12
# Uzdevuma formulējums: Sastādīt programmu, kura aprēķina laukumu zem funkcijas y=ax^3+bx^2+cx+d grafika intervalā [u,w] ar 1) taisnstūru metodi 2) trapeču metodi. a, b, c, d, u, w un precizitāti ievada lietotājs. Salīdzināt abas metodes pēc veikto iterāciju skaita pie vienas un tās pašas precizitātes.
# Versija 1.0

print("Programma noteic laukumu zem funkcijas y = ax^3 + bx^2 + cx + d intervāla [u,w].\nJa laukums ir zem X ass, tad laukums ir negatīvs.\n")

q = float(input("Ievadi a ===> "))
w = float(input("Ievadi b ===> "))
e = float(input("Ievadi c ===> "))
r = float(input("Ievadi d ===> "))

a = float(input("Ievadi sākumpunktu u ===> "))
b = float(input("Ievadi galapunktu w ===> "))

pr = float(input("Ievadi precizitāti ===> "))


#------------------- ar taisnsturiem

s2 = 0
n=2
paz = True
while paz :
    s1 = s2
    x = (b - a) / n
    s2 = 0
    for i in range (n) :
        y=a+i*x
        s2 = s2 + (y*y*y*q+y*y*w+y*e+r) * x
    n = n * 2
    if abs(s1 - s2) < pr :
        paz = False

print("\nS ar taisnturiem = " + str(s2))
print("Iterāciju skaits: " + str(n) + "\n")


#------------------- ar trapecem

n = 2
s2 = 0

paz = True
while paz :
    s1 = s2
    x = (b - a) / n
    s2 = 0
    c = a*a*a*q+a*a*w+a*e+r
    for i in range (1,n+1) :
        y=a+x*i
        d = y*y*y*q+y*y*w+y*e+r
        s2 = s2 + x * (c + d) / 2
        c = d
    n = n * 2
    if abs(s1 - s2) < pr :
        paz = False
        
print("S ar trapecem = " + str(s2))
print("Iterāciju skaits: " + str(n))