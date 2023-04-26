# Programmas nosaukums: Latloto
# 3. uzdevums (1MPR10_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas realizē Latloto 5 no 35 izlozi, nodrošina lietot vienā loterijas
# biļetē norādīto piecu skaitli ievadi un paziņo par laimestu:
# Ja uzminēti 5 skaitli, tad paziņo "Lielais laimests"
# Ja uzminēti 4 skaitļi, tad paziņo "Vidējais laimests"
# Ja uzminēti 3 skaitļi, tad paziņo "Mazais laimests"
# Ja citādi, tad paziņo "Nav laimesta".
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import random


def random_set_numbers_1_to_35():
    # Atgriež kopu ar nejaušiem skaitļiem kuri neatkartojas no 1 līdz 35. [1, 35].
    # a - set (kopa) - tukša kopa.

    a = set()
    while len(a) < 5:
        b = random.randint(1, 35)
        if b not in a:
            a.add(b)

    return a


def ievadiet_n_skaitlus_seta(n, max_num):
    # Procedura kura ļauj ievādit n skaitļus un ieliekt tos kop (set'ā)
    # n - cik skaitļus ievādīt lietotājam (int)
    # max_num - maksimālais skaitlis līdz kuram tiek veikta loterija (int)

    a = set()  # a - tukša kopa (set)
    for i in range(1, n + 1):
        while True:
            b = input("Ievadiet " + str(i) + ". skaitli ==> ")
            try:
                b = int(b)
                if b < 1 or b > max_num:
                    print("Skaitlim jābūt veselam skaitlim no 1 līdz " + str(max_num) + ".")
                elif b in a:
                    print("Šis skaitlis jau eksistē, lūdzu ievadiet citu skaitli!")
                else:
                    a.add(b)
                    break
            except ValueError:
                print("Ievadei jābūt skaitlim!")
                continue

    return a


def laimests_5_35_izloze(a, b):
    # a - set (kopa) - nejauši izveidota kopa (jāizveido ar funkciju random_set_numbers_1_to_35(a)).
    # b - set (kopa) - cilvēka izvēlētie skaitļi kopā.

    x = a.intersection(b)
    len1 = len(x)

    if len1 == 5:
        return "Lielais laimests"
    elif len1 == 4:
        return "Vidējais laimests"
    elif len1 == 3:
        return "Mazais laimests"
    else:
        return "Nav laimesta"


def cik_atminejat(a, b):
    # Atgriež cik skaitļus Jūs laimējat (atrod kopas šķēlumu)
    # a - set (kopa) - nejauši izveidota kopa (jāizveido ar funkciju random_set_numbers_1_to_35(a)).
    # b - set (kopa) - cilvēka izvēlētie skaitļi kopā.

    x = a.intersection(b)
    len1 = len(x)

    return len1


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


def print_set(a):
    # Izvada (print) uz ekrāna kopu. Bet tas to neatgriež.
    # Jāizsauc vienkarši print_set(a)
    # a - kopa (set)

    elements = sort_ievietosana_augosa(list(a))
    # Iterējam cauri elementu indeksiem un izdrukājiem tos, atdalot tos ar komatiem
    for i in range(len(elements)):
        if i == len(elements) - 1:
            # Ja elements ir pēdējais, izdrukām to bez komata
            print(elements[i])
        else:
            # Ja elements nav pēdējais, izdrukājam to ar komatu. end="", lai nebūtu pārejas uz jauno rindu kā \n
            print(str(elements[i]) + ", ", end="")


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


a = random_set_numbers_1_to_35()

print("Sveicināti 'Latloto' 5 no 35 izloze!\n\nIevadiet savus skaitļus no 1 līdz 35.\nJā uzminēsiet 5 skaitļus, tad dabūsiet 'Lielo laimestu'\nJā uzminēsiet 4 skaitļus, tad dabūsiet 'Vidējo laimestu'\nJā uzminēsiet 3 skaitļus, tad dabūsiet 'Mazo laimestu'\nCitādi nav laimesta.\n")
# print("TESTĒŠANAI:", a)  # TESTĒŠANAI (laimēto skaitļu set izvādīt)

b = ievadiet_n_skaitlus_seta(5, 35)
print("\nJūsu izvēlētie skaitļi:")
print_set(b)

print("\nIzlozētie skaitļi:")
print_set(a)
atmineto_skaits = cik_atminejat(a, b)

if atmineto_skaits == 1:  # Pareizam locijumam
    word = "skaitļi"
else:
    word = "skaitļus"

print("\nJūs atminējat " + str(atmineto_skaits) + " " + word + " no 5.")
print("\nJūsu laimests:")
print(laimests_5_35_izloze(a, b))
