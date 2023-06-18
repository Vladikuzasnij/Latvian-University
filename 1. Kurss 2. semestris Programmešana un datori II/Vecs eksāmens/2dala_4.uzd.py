# izloze

import random


def izloze(cik, nocik):  # cik == 5, nocik == 35
    v = set()
    for i in range(1, nocik + 1):
        v.add(i)
    k = set()
    for i in range(cik):
        b = random.choice(list(v))
        v.remove(b)
        k.add(b)

    return k


def again_izloze(kopa):
    # funkcija veic atkārtotu vienas lodītes lozēšanu un pievieno to izlozēto lodīšu kopai
    nejausi = random.randint(1, 35)
    for nejausi in kopa:
        nejausi = random.randint(1, 35)
    kopa.add(nejausi)
    return kopa


def sort_ievietosana_augosa(a):
    # Sakārto masīvu augoša secība un atgriež salīdzināšanas skaitu, lai sakārtotu masīvu
    # Kārtošanas tiek izmantota ievietošanas metode (insertion sort)
    # a - viendimensijas masīvs
    n = len(a)
    for i in range(1, n):
        if a[i - 1] > a[i]:
            x = a[i]
            j = i
            while a[j - 1] > x:
                a[j] = a[j - 1]
                j = j - 1
                if j == 0:
                    break
            a[j] = x
    return a


def izvade(a):
    # funkcija nodrošina datu glītu izvadi simbolu virknes formā
    a = sort_ievietosana_augosa(list(a))
    sv = ""
    for i in range(len(a)):

        if i < len(a) - 1:
            sv = sv + str(a[i]) + " "
        else:
            sv = sv + str(a[i])
    return sv


def main_izloze():
    # galvenā programma
    jan_lodites = izloze(5, 35)  # jānīša izlozētās lodītes
    # print(jan_lodites)
    peter_lodites = izloze(5, 35)  # pēterīša izlozētās lodītes
    laimests = 1024
    tries = 1
    kopigas_lodites = jan_lodites.intersection(peter_lodites)  # kopīgās lodītes
    # ja šķēluma kopas garums ir 5, tātad izlozētas vienādas lodītes
    if len(kopigas_lodites) == 5:
        pass  # laimest = 1024
        # tries = 1
    else:
        # ja šķēluma kopas garums nav pieci, tad lozē papildus lodītes
        while len(kopigas_lodites) < 5:
            again_izloze(jan_lodites)
            again_izloze(peter_lodites)
            kopigas_lodites = jan_lodites.intersection(peter_lodites)
        else:
            i = len(jan_lodites) - 5  # aprēķina kāpinātāju laimesta aprēķināšanai
            tries = i + tries
            laimests = laimests / 2**i

    return (laimests, tries, jan_lodites, peter_lodites, kopigas_lodites)


# rezultāta izvade
galv_izloze = main_izloze()
# print(galv_izloze[1])
print(str(galv_izloze[1]) + ". meginajumi tika izdarīti, kamēr netika izvilktas piecas kopīgas lodītes.")
#print("Tika izdarīti", tries, "mēģinājumi.")
print("Jānītis izvilka lodītes: " + str(izvade(galv_izloze[2])))
print("Pēterītis izvilka lodītes: " + str(izvade(galv_izloze[3])))
print("Kopīgās lodītes: " + str(izvade(galv_izloze[4])))
formattets_laimests = "{:.2f}".format(galv_izloze[0])
print("Laimests: " + formattets_laimests + " EUR")


'''
import random


def lodisuIzloze():
    # funkcija veic sākotnējo piecu lodīšu izlozi
    b = set()
    for i in range(5):
        l = random.randint(1, 35)
    while l in b:
        l = random.randint(1, 35)
    b.add(l)
    return b


def atkartotaIzloze(b):
    # funkcija veic atkārtotu vienas lodītes lozēšanu un pievieno to izlozēto lodīšu kopai
    l = random.randint(1, 35)
    while l in b:
        l = random.randint(1, 35)
    b.add(l)
    return b


def izvade(a):
    # funkcija nodrošina datu glītu izvadi simbolu virknes formā
    a = sorted(a)
    sv = ""
    for i in range(len(a)):

        if i < len(a) - 1:
            sv = sv + str(a[i]) + ","
        else:
            sv = sv + str(a[i])
    return sv


# galvenā programma
janisaL = lodisuIzloze()  # jānīša izlozētās lodītes
peterisaL = lodisuIzloze()  # pēterīša izlozētās lodītes
laimests = 1024
meginajumi = 1
x = janisaL.intersection(peterisaL)  # kopīgās lodītes
# ja šķēluma kopas garums ir 5, tātad izlozētas vienādas lodītes
if len(x) == 5:
    laimests = laimests
    meginajumi = meginajumi
else:
    # ja šķēluma kopas garums nav pieci, tad lozē papildus lodītes
    while len(x) < 5:
        atkartotaIzloze(janisaL)
        atkartotaIzloze(peterisaL)
        x = janisaL.intersection(peterisaL)
    else:
        i = len(janisaL) - 5  # aprēķina kāpinātāju laimesta aprēķināšanai
        meginajumi = i + meginajumi
        laimests = laimests / 2**i

# rezultāta izvade
print("Tika izdarīti", meginajumi, "mēģinājumi.")
print("Jānītis izvilka lodītes -", izvade(janisaL))
print("Pēterītis izvilka lodītes -", izvade(peterisaL))
print("Kopīgās lodītes -", izvade(x))
print("Laimests - EUR", "{:0.2f}".format(laimests))
'''
