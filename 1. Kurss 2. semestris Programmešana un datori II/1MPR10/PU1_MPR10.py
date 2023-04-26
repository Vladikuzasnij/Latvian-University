# Programmas nosaukums: Keno loterijas izloze ar laimesto sadalījumu
# 5. uzdevums (1MPR10_Vladislavs_Babaņins)
# Uzdevuma formulējums: Papildināt 5.uzdevumā realizēto Keno loterijas izlozi ar laimestu sadali.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0

# Avots: https://www.latloto.lv/lv/keno/
# Noteikumi: https://www.latloto.lv/lv/page/view/2695


import numpy
import random


def is_natural_and_less_than_10(n):
    # Pārbauda vai simbolu virkne ir naturāls skaitlis vai nav.
    # Ja ir naturāls skaitlis, tad True. Ja nav tad False.
    # n - simbolu virkne, kuru pārbauda.

    if str(n).isdigit() and float(n) == int(n) and int(n) > 0 and int(n) < 11:
        return True
    else:
        return False


def ievadiet_n_skaitlus_seta(n, max_num):
    # Procedura kura ļauj ievādit n skaitļus un ieliekt tos kop (set'ā)
    # Atgriež jau aizpildīto kopu (set'u) a ar lietotāja ievādītajiem naturāliem skaitliem robēžas no 1 līdz max_num ieskaitot.
    # n - cik skaitļus ievādīt lietotājam (int)
    # max_num - maksimālais skaitlis līdz kuram tiek veikta loterija (int)

    a = set()
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


def speles_likmes():
    # Paprasam izvēlēties spēlēs likmi no piedāvātiem.
    # Pārbauda to, vai tāda eksistē un atgriež to, kā float.

    while True:
        n = input("Izvēlēties, Jūsu spēles likmi € ==> ")
        try:
            float(n)
        except:
            print("Kļūda! Ievādiet reālo likmi no piedāvatiem!")
        else:
            n = float(n)
            if n == 0.2:
                likme = 0.2
                return likme

            elif n == 0.3:
                likme = 0.3
                return likme

            elif n == 0.5:
                likme = 0.5
                return likme

            elif n == 1:
                likme = 1
                return likme

            elif n == 2:
                likme = 2
                return likme

            elif n == 3:
                likme = 3
                return likme

            elif n == 5:
                likme = 5
                return likme

            elif n == 10:
                likme = 10
                return likme

            else:
                print("Kļūda! Ievādiet likmi no piedāvatiem!")


def laimestu_matrica(izveleto_skaits, atmineto_skaits):
    # Atgriež reizinātāju pamatojoties uz laimestu sadalījuma matricas.
    # Reizinātajs ir atkarīgs no tā, cik skaitļus jus izvēlējaties un cik jus atminējat.
    # Reizinātāji ir pārādīta šājā matricā.

    laimesti = numpy.array([[0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
                            [1.5, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 4.5, 1, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 8, 1, 1, 0, 0, 0, 0, 0],
                            [0, 0, 0, 20, 2, 2, 1, 0, 0, 0],
                            [0, 0, 0, 0, 45, 12, 3, 3, 1, 1],
                            [0, 0, 0, 0, 0, 175, 30, 5, 2, 2],
                            [0, 0, 0, 0, 0, 0, 700, 100, 40, 5],
                            [0, 0, 0, 0, 0, 0, 0, 3000, 350, 55],
                            [0, 0, 0, 0, 0, 0, 0, 0, 10000, 550],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 60000]])

    reizinatajs = laimesti[atmineto_skaits, izveleto_skaits - 1]  # Izvēlāmies nepieciešāmo rūtiņu un tas arī būs reizinātajs.

    return reizinatajs


def naudas_balva(likme, reizinatajs):
    # Atgriež naudas balvu likmi reizinot ar reizinātaju.
    # likme - likme (float reāls skaitlis lielāks par 0, piemēram,
    # 0.20
    # 0.30
    # 0.50
    # 1.00
    # 2.00
    # 3.00
    # 5.00
    # 10.00)
    # reizinātajs - float reāls skaitlis lielāks vai vienāds par 0

    return likme * reizinatajs


def random_set_numbers_skaita_n_from_1_to_m(n, m):
    # Atgriež kopu ar n nejaušiem skaitļiem, kuri neatkartojas no 1 līdz m. [1, m].
    # n - cik nejaušus skaitļus vajag loterijai
    # m - kāda ir augšēja robeža skaitlim, kuru vajadzīgi uzminēt (vislielākais iespējamais skaitlis loterija)

    a = set()
    while len(a) < n:
        b = random.randint(1, m)
        if b not in a:
            a.add(b)

    return a


def cik_atminejat(a, b):
    # Atgriež cik skaitļus Jūs laimējat (atrod kopas šķēlumu)
    # a - set (kopa) - nejauši izveidota kopa (jāizveido ar funkciju random_set_numbers_1_to_35(a)).
    # b - set (kopa) - cilvēka izvēlētie skaitļi kopā.

    x = a.intersection(b)
    len1 = len(x)

    return len1


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


def izlozu_skaits():
    # Paprasam izvēlēties izložu skaitu no piedāvātiem.
    # Pārbauda to, vai tāda eksistē un atgriež to, kā float.

    while True:
        n = input("Izvēlēties, izložu skaitu ==> ")
        try:
            int(n)
        except:
            print("Kļūda! Ievādiet reālo izložu skaitu no piedāvatiem!")
        else:
            n = int(n)
            if n == 1:
                izlozu_skaits = 1
                return izlozu_skaits

            elif n == 2:
                izlozu_skaits = 2
                return izlozu_skaits

            elif n == 3:
                izlozu_skaits = 3
                return izlozu_skaits

            elif n == 4:
                izlozu_skaits = 4
                return izlozu_skaits

            elif n == 6:
                izlozu_skaits = 6
                return izlozu_skaits

            elif n == 12:
                izlozu_skaits = 12
                return izlozu_skaits

            elif n == 21:
                izlozu_skaits = 21
                return izlozu_skaits

            else:
                print("Kļūda! Ievādiet izložu skaitu no piedāvatiem!")


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


n = input("Izvēlēties, cik skaitļus nosvītrot (no 1 līdz 10) ==> ")
while not is_natural_and_less_than_10(n):
    n = input("Kļūda! Izvēlēties, cik skaitļus nosvītrot (no 1 līdz 10) ==> ")
print("Ievādiet Jūsu skaitļus. Skaitlim jābūt veselam skaitlim no 1 līdz 62.")
n = int(n)

rezultats = random_set_numbers_skaita_n_from_1_to_m(20, 62)
# print("TESTĒŠANAI:")  # TESTĒŠANAI
# print_set(rezultats)  # TESTĒŠANAI

players_numbers = ievadiet_n_skaitlus_seta(n, 62)

print("\nSpēles likmes:\n0.20 €\n0.30 €\n0.50 €\n1.00 €\n2.00 €\n3.00 €\n5.00 €\n10.00 €\n")
likme = speles_likmes()

print("\nIzložu skaits:\n1\n2\n3\n4\n6\n12\n21\n")
piedalisanas_reizes = izlozu_skaits()

print("\nJūsu skaitļi:")
print_set(players_numbers)

total_laimests = 0

for i in range(piedalisanas_reizes):

    rezultats = random_set_numbers_skaita_n_from_1_to_m(20, 62)  # Noņemt testēšanai
    print("\nIzlozētie skaitļi:")
    print_set(rezultats)

    atmineto_skaits = cik_atminejat(players_numbers, rezultats)

    if atmineto_skaits == 1:  # Pareizam locijumam
        word = " skaitļi."
    else:
        word = " skaitļus."

    print("\nJūs atminējat " + str(atmineto_skaits) + word)
    reizinatajs = laimestu_matrica(n, atmineto_skaits)
    print("Reizinātājs:", reizinatajs)

    laimests = naudas_balva(likme, reizinatajs)
    print("Jūsu laimests:", laimests, "€")
    total_laimests += laimests

    if piedalisanas_reizes == 1:
        pass
    elif i + 1 == piedalisanas_reizes:
        if piedalisanas_reizes == 21:  # Pareizam locijumam
            word = "izlozi"
        else:
            word = "izlozem"
        print("\nJūsu kopējais laimests par", piedalisanas_reizes, word, "ir:", total_laimests, "€")
