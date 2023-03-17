# Programmas nosaukums: 3. uzd MPR12
# 3. uzdevums MPR12
# Uzdevuma formulējums: Sastādīt programmu, kura atrod skaitļa N pirmreizinātājus. Skaitli N ievada lietotājs + glīts noformējums
# Versija 1.0

n = int(input("Ievadi naturālu skaitli ===> "))
a = n
j = 2

sv1 = str(n) + " | "

while a > 1 :
    k = 0
    
    while (a % j) == 0 :
        sv1 = str(a) + " | " + str(j)
        a = a // j
        k = k + 1
        print(sv1)
        
    j = j + 1
    
print("1 | 1")    
