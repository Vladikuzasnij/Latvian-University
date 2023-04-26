# Programmas nosaukums: "Bilešu paradīze" (tekstuāls režims)
# 2. uzdevums (1MPR09_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas realizē teātra bilešu iegādi līdzīgi kā "Bilešu paradīze".
# Ar šādiem papildus atvieglojumiem.
# 1. teātra skatītāju zālē ir N rindu un M sēdvietu. M un N vērtības ievada lietotājs.
# 2. uzsākot iepirkšanos apmēram 50% biļešu ir pārdotas.
# 3. vienā reizē var nopirkt tikai vienu biļeti, ievadot izvēlēto rindas un sēdvietas numuru.
# 4. ja izvēlēta sēdvieta ir brīva, tā tiek atzīmēta kā aizņemta un pāriet pie nākamās biļetes iegādes, bet, ja izvēlēta vieta ir aizņemta,
# tad uz ekrāna tiek paradīta informācija par visām sēdvietām un pieprasīta atkārtota sēdvietas izvēle.
# 5. Biļešu iegāde tiek atkārtta, kāmer lietotājs ievada 0.rindu un 0.kolonnu vai visas biļetes ir izpārdotas.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import numpy
import random


def create_random_2array(n, m):
    # Atgriež divdimensiju masīvu, kur visi elementi ir vai nu 0, vai 1 un aptuvēni 50% no visu elementu skaita ir 1.
    # n - divdimensiju masīva rindu skaits
    # m - divdimensiju masīva kolonnu skaits (sēdvietu skaits)
    a = numpy.ones((n, m))
    num_ones = int(n * m * 0.5)
    ones_count = 0
    for i in range(n):
        for j in range(m):
            if ones_count < num_ones and random.random() < 0.5:
                a[i][j] = 0
                ones_count += 1
    return a


def add_numeration_to_matrix(a):
    # Pievieno rindas un kolonnu numerāciju matricai un atgriež simbolu virkni ar matricas elementiem un ir rindas un kolonnas numerācija
    # a - divdimensijas masīvs
    s = ""
    len1 = a.shape[1]
    for j in range(len1 + 1):
        s = s + "{:3d}".format(j)  # izmantot formāta norādītāju, lai nodrošinātu nepieciešāmu atstarpi
    s += "\n"  # pievienot jaunu rindiņu pēc pirmās rindas

    n = a.shape[0]
    for i in range(n):
        s = s + "{:3d}".format(i + 1)  # rindas numurs
        for j in range(len1):
            s = s + "  " + a[i, j]
            #s = s + "{:3.0f}".format(a[i, j])
        s += "\n"  # pievienot jaunu rindiņu pēc pirmās rindas

    return s


def choose_what_change_to_one(a, sk):
    # Biļetes pirkšanai. Ja viss ir izpārdots (ja visi ir 1), tad print("Izpārdots!\n")
    # Var izvelēties, kuru ciparu izmainīt uz 1.
    # 1 -> 1 (vieta aizņemta)
    # 0 -> 1 (print("\nBiļete nopirkta!\n"))
    # a - divdimensijas masīvs (matrica)
    # sk - vieninieku skaits. Ja ir lielāks nekā n x m, tad izpārdots.

    n, m = a.shape

    if sk >= n * m:
        print("\nŠodien viss ir izpārdots!\n")
        return

    while True:
        r = input("Ievadiet vēlamo rindas numuru biļetes nopirkšanai ==> ")
        while not is_natural_or_zero(r):
            r = input("Kļūda! Ievadiet vēlamo naturālo rindas numuru biļetes nopirkšanai ==> ")
        r = int(r)

        s = input("Ievadiet vēlamo sēdvietu numuru ==> ")
        while not is_natural_or_zero(s):
            s = input("Kļūda! Ievadiet vēlamo naturālo sēdvietu numuru biļetes nopirkšanai ==> ")
        s = int(s)

        try:
            if r == 0 and s == 0:
                return print("Paldies, ka izmantojāt mūsu pakalpojumus!")

            elif r == 0 or s == 0:
                print("\nNekorekta ievade!\n")
                print(add_numeration_to_matrix(replace_ones_to_a_zeros_to_b(a)))

            elif a[r - 1, s - 1] == 1:
                print("\nJusu izvēlēta vieta " + str(r) + ".rindā " + str(s) + ".sēdvietā ir aizņemta!\n")
                print(add_numeration_to_matrix(replace_ones_to_a_zeros_to_b(a)))

            elif a[r - 1, s - 1] == 0:
                a[r - 1, s - 1] = 1
                print("\nBiļete nopirkta! Jūsu vieta ir " + str(r) + ".rindā " + str(s) + ".sēdvietā.\n")
                print(add_numeration_to_matrix(replace_ones_to_a_zeros_to_b(a)))
                sk += 1

            if sk >= n * m:
                print("Šodien viss ir izpārdots!\n")
                print(add_numeration_to_matrix(replace_ones_to_a_zeros_to_b(a)))
                return
        except IndexError:
            print("\nIr jāievāda reālu sēdvietu!\nUz redzēšanos!")
            quit()


def count_ones(a):
    # Saskaita vieninieku skaitu noteiktā masīvā a un atgriež to int skaitļi
    # a - divdimensijas masīvs (matrica)
    count = 0
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            if a[i, j] == 1:
                count += 1
    return count


def replace_ones_to_a_zeros_to_b(arr):
    # Izmaina visus divdimensija masīva vieniniekus to A, bet nulles to B
    # 1 -> A
    # 0 -> B
    # arr - divdimensijas masīvs (matrica)
    new_arr = numpy.empty(arr.shape, dtype='str')
    new_arr[arr == 1] = 'A'
    new_arr[arr == 0] = 'B'
    return new_arr


def is_natural(n):
    # Pārbauda vai simbolu virkne ir naturāls skaitlis vai nav
    # Ja ir naturāls skaitlis, tad True. Ja nav tad False.
    # n - simbolu virkne, kuru pārbauda.
    if str(n).isdigit() and float(n) == int(n) and int(n) > 0:
        return True
    else:
        return False


def is_natural_or_zero(n):
    # Pārbauda vai simbolu virkne ir naturāls skaitlis vai nulle, vai nav
    # Ja ir naturāls skaitlis vai nulle, tad True. Ja nav tad False.
    # n - simbolu virkne, kuru pārbauda.
    if str(n).isdigit() and float(n) == int(n) and int(n) >= 0:
        return True
    else:
        return False


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


n = input("Ievadiet kopējo rindu skaitu teātrī ==> ")
while not is_natural(n):
    n = input("Kļūda! Ievadiet kopējo naturālu rindu skaitu teātrī ==> ")
n = int(n)

m = input("Ievadiet kopējo sēdvietu skaitu teātrī ==> ")
while not is_natural(m):
    m = input("Kļūda! Ievadiet kopējo naturālu rindu skaitu teātrī ==> ")
m = int(m)

a = create_random_2array(n, m)
b = add_numeration_to_matrix(replace_ones_to_a_zeros_to_b(a))

print("")
sk = count_ones(a)
print(b)
print("Sveicinām teātri!\nŠeit var nopirkt biļeti uz izrādi!\n\nIziešanai no sistēmas ievadiet rindas numuru: 0, sēdvietu: 0")
choose_what_change_to_one(a, sk)

