# Programmas nosaukums: 1. uzd MPR12
# 1. uzdevums MPR12
# Uzdevuma formulējums: Sastādit programmu, kas aprēķina cos(x) ar lietotāja norādīto precizitāti, ja pieņemam, ka un precizitāti nosaka pēdējais saskaitāmais. Skaitli X un precizitāti ievada lietotājs.
# Versija 1.0

x = float(input("Ievadi funkcijas argumentu ===> "))
pr = float(input("Ievadi precizitāti ===> "))

z = 1
s = 1
n = 0
y = 1

while abs(y) > pr:
    z = -z
    n = n + 1
    y = y * x * x / 2 / n / (2 * n - 1)
    s = s + z * y
    
print("сos(" + str(x) + ") = " + str(s) + " ar precizitāti " + str(pr))