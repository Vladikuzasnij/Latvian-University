# Programmas nosaukums: Pārbauda vai masīvs satur frāzi
# 5. uzdevums (1MPR07_Vladislavs_Babaņins)
# Uzdevuma formulējums: Jums ir jāizveido viendimensijas masīvs ar 10 000 elementu.
# Šī masīva elementi ir uz labu laimi ģenerētas simbolu virknes (vārdi) garumā no 3 līdz 8 simboliem un sastāv tikai no
# lielajiem latīņu alfabēta burtiem. Pēc šī masīva izveides Jums jāveic visas nepieciešamās darbības, lai varētu ātri (ne sliktāk kā logaritmiskā laikā)
# pārbaudīt, vai šis masīvs satur vai nesatur lietotāja ievadīto frāzi.
# Versija 1.0

import numpy
import random


def atrais(a, sv, bv):  # sv = 0, bv = len(a)
    # Sakārto masīvu augoša secība
    # Kārtošanas tiek izmantota Hoara (ātrais) metode (quicksort)
    # a - viendimensijas masīvs
    # sv - sākuma vērtība
    # bv - beigu vērtība
    if sv < bv:
        i = sv
        j = bv
        solis = -1
        lv = True
        while i != j:
            if lv == (a[i] > a[j]):
                x = a[i]
                a[i] = a[j]
                a[j] = x
                x = i
                i = j
                j = x
                lv = not lv
                solis = -solis
            j = j + solis
        atrais(a, sv, i - 1)
        atrais(a, i + 1, bv)


def vards():
    # Ģenerē vārdus ar garumu no 3 līdz 8 (garums - uz labu laimi) un ģenerē to vārdu ar lieliem latiņu alfabēta burtiem
    # Atgriež vienu izveidotu vārdu
    r = random.randint(3, 8)
    v = ""
    for i in range(r):
        v += chr(random.randint(65, 90))  # ASCII 65;90
    return v


def masivs(length):
    # Aizpildā masīvu ar vārdiem atsaucoties uz "vards()". Atgriež aizpildīto masīvu.
    # length - viendimensijas masīva garums
    mas = numpy.empty(length, dtype=object)
    for j in range(length):
        mas[j] = vards()
    # print(mas)
    return mas


def meklet(a, b):
    # Sameklē a masīva b skaitļi (vai vārdu). Atgriež to vērtību, kur viņa atrodas pēc index. Ja nav tādas vērtības masīva, tad atgriež -1.
    # a - viendimensijas masīvs
    # b - to ko mēs meklējam (skaitlis vai vārds (str))
    l = 0
    r = len(a) - 1
    while (l <= r):
        i = (l + r) // 2
        if a[i] == b:
            break
        elif a[i] < b:
            l = i + 1
        else:
            r = i - 1
    if a[i] == b:
        return i
    else:
        return -1


def izvade(x):
    # Izvada masīva elementus pēc kārtas līdz pedējam
    # x - viendimensijas masīvs
    n = len(x)
    s = str(x[0])
    for i in range(1, n):
        s = s + ", " + str(x[i])
    print(s)


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


lenght = 10000
a = masivs(lenght)

atrais(a, 0, len(a) - 1)

print("Uz labu laimi izveidotie vārdi:")
izvade(a)
print("")

m = input("Ievadi meklējamo ===> ")

vieta = meklet(a, m)

if vieta == -1:
    print("Meklējamais vārds " + str(m) + " nav atrasts.")
else:
    print("Meklējamais ir " + str(vieta) + ". vietā.")

