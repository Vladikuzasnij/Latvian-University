# Programmas nosaukums: Viendimensijas masīva izveidi.
# 4. uzdevums (1MPR04_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas organizē viendimensijas masīva izveidi, datu ievadi un izvadi, lielākās un mazākās vērtības atrašanu. Masīva izmēru N ievada lietotājs.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import numpy


def is_natural(n):
    # Pārbauda vai simbolu virkne ir naturāls skaitlis vai nav
    # Ja ir naturāls skaitlis, tad True. Ja nav tad False.
    # n - simbolu virkne, kuru pārbauda.
    if str(n).isdigit() and float(n) == int(n) and int(n) > 0:
        return True
    else:
        return False


n = input("Ievadiet masīva izmēru N ===> ")

while is_natural(n) == False:
    n = input("Masīva izmērs ir naturāls skaitlis!\nIevadiet masīva izmēru N ===> ")

n = int(n)
a = numpy.arange(n)

for i in range(n):
    a[i] = int(input("Ievadi " + str(i) + ".elementu ===> "))

print("Masīva elementi ievadīšanas secībā:")
for i in range(n):
    print(a[i])

print("Masīva minimālais elements: " + str(min(a)))
print("Masīva maksimālais elements: " + str(max(a)))
