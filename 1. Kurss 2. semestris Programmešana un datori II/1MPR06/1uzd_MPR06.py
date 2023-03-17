# Programmas nosaukums: Četras kārtošanas algoritmi
# 1. uzdevums (1MPR06_Vladislavs_Babaņins)
# Uzdevuma formulējums: Realizēt 4 kārtošanas algoritmus, kas sakārto masīva elementus dilstošā (neaugošā) secībā (5 punkti):
# 1.1. Atspoles metode
# 1.2. Ievietošanas metode
# 1.3. Šella metode
# 1.4. Hoara jeb ātrās kārtošanas metode
# NB! Nedrīkst rakstīt algoritmu, kas vispirms sakārto masīvu augošā secībā un pēc tam to nodrukā apgrieztā secībā!
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import numpy
import random
import math


def is_natural(n):
    # Pārbauda vai simbolu virkne ir naturāls skaitlis vai nav
    # Ja ir naturāls skaitlis, tad True. Ja nav tad False.
    # n - simbolu virkne, kuru pārbauda.
    if str(n).isdigit() and float(n) == int(n) and int(n) > 0:
        return True
    else:
        return False


def sort_atspole_dilstosa(a):
    # Sakārto masīvu dilstoša secība un atgriež salīdzināšanas skaitu, lai sakārtotu masīvu
    # Kārtošanas tiek izmantota atspoles metode
    # a - viendimensijas masīvs
    n = len(a)
    count = 0
    for i in range(1, n):
        if a[i - 1] < a[i]:
            for j in range(i, 0, -1):
                count += 1
                if a[j - 1] < a[j]:
                    x = a[j]
                    a[j] = a[j - 1]
                    a[j - 1] = x
                else:
                    count += 1
                    break
    return count


def sort_ievietosana_dilstosa(a):
    # Sakārto masīvu dilstoša secība un atgriež salīdzināšanas skaitu, lai sakārtotu masīvu
    # Kārtošanas tiek izmantota ievietošanas metode (insertion sort)
    # a - viendimensijas masīvs
    n = len(a)
    sk = 0
    for i in range(1, n):
        sk = sk + 1
        if a[i - 1] < a[i]:
            x = a[i]
            j = i
            sk = sk + 1
            while a[j - 1] < x:
                a[j] = a[j - 1]
                j = j - 1
                if j == 0:
                    break
                sk = sk + 1
            a[j] = x
    return sk


def sort_sella_dilstosa(a):
    # Sakārto masīvu dilstoša secība un atgriež salīdzināšanas skaitu, lai sakārtotu masīvu
    # Kārtošanas tiek izmantota Šellas metode (Shell sort)
    # a - viendimensijas masīvs
    sk = 0
    n = len(a)
    solis = (3**math.floor(math.log(2 * n + 1, 3)) - 1) // 2
    while solis >= 1:
        for k in range(0, solis):
            for i in range(solis + k, n, solis):
                if a[i - solis] < a[i]:
                    x = a[i]
                    j = i
                    while j >= solis + k and a[j - solis] < x:
                        a[j] = a[j - solis]
                        j = j - solis
                        sk = sk + 1
                    a[j] = x
                sk = sk + 1
        solis = (solis - 1) // 3

    return sk


def sort_atrais_dilstosa(a, sv, bv):
    # Sakārto masīvu dilstoša secība un atgriež salīdzināšanas skaitu, lai sakārtotu masīvu
    # Kārtošanas tiek izmantota Hoara (ātrais) metode (quicksort)
    # a - viendimensijas masīvs
    # sv - sākuma vērtība
    # bv - beigu vērtība
    p = 0
    if sv < bv:
        i = sv
        j = bv
        solis = -1
        lv = True
        while i != j:
            if lv == (a[i] < a[j]):
                x = a[i]
                a[i] = a[j]
                a[j] = x
                x = i
                i = j
                j = x
                lv = not lv
                solis = -solis
            p += 1
            j = j + solis
        p1 = sort_atrais_dilstosa(a, sv, i - 1)
        p2 = sort_atrais_dilstosa(a, i + 1, bv)
        p = p + p1 + p2
    return p


def izvadit_masivu_un_salidzinasanas_skaitu(x, sal):
    # Izvada salīdzināšanas skaitu un izvada masīva elementus ar komatiem
    # x - viendimensijas masīvs
    # sal - int skaitlis
    n = len(x)
    s = str(x[0])
    for i in range(1, n):
        s = s + ", " + str(x[i])
    return str(sal) + " salīdzināšanas - " + s


def izvadit_masivu(x):
    # Izvada masīva elementus ar komatiem
    # x - viendimensijas masīvs
    n = len(x)
    s = str(x[0])
    for i in range(1, n):
        s = s + ", " + str(x[i])
    return s


def samaisit(masivs):
    # Samaisa masīva elementus (funkcija tiek izmantota, lai no sakārtota masīva numpy.arange(n + 1) izveidot nesakārtotu (unsort)
    # masivs - viendimensijas masīvs
    i = 0
    while i < len(masivs) // 2:
        x = random.randint(1, len(masivs) - 1)
        y = random.randint(1, len(masivs) - 1)
        temp = masivs[x]
        masivs[x] = masivs[y]
        masivs[y] = temp
        i = i + 1
    return masivs


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


n = input("Ievadiet masīva izmēru N ===> ")

while is_natural(n) == False:
    n = input("Masīva izmērs ir naturāls skaitlis!\nIevadiet masīva izmēru N ===> ")

n = int(n)
a = numpy.arange(n + 1)

samaisit(a)
print("\nSākotnējais masīvs:")
print(izvadit_masivu(a))

y = numpy.copy(a)
z = numpy.copy(a)
k = numpy.copy(a)
p = numpy.copy(a)

sorted_b = sort_atspole_dilstosa(y)
print("\nKārtošana ar atspoles metodi:")
print(izvadit_masivu_un_salidzinasanas_skaitu(y, sorted_b))

sorted_c = sort_ievietosana_dilstosa(z)
print("\nKārtošana ar ievietošanas metodi:")
print(izvadit_masivu_un_salidzinasanas_skaitu(z, sorted_c))

sorted_d = sort_sella_dilstosa(p)
print("\nKārtošana ar Šella metodi:")
print(izvadit_masivu_un_salidzinasanas_skaitu(p, sorted_d))

sorted_e = sort_atrais_dilstosa(k, 0, len(a) - 1)
print("\nKārtošana ar Hoara (ātrais) metodi:")
print(izvadit_masivu_un_salidzinasanas_skaitu(k, sorted_e))
