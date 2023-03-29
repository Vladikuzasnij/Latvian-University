# Programmas nosaukums: Trīs masīvu apvienošana
# Papilduzdevums 1 (1MPR07_Vladislavs_Babaņins)
# Uzdevuma formulējums: Lietotājs ievada trīs sakārtotus masīvus, bet nav zināms, kurš no tiem ir sakārtots augošā vai dilstošā secībā.
# Lineārā laikā apvienot visus trīs masīvus vienā augošā secībā sakārtotā masīvā un izvadīt to uz ekrāna.
# Versija 1.0


import numpy


def izveidot_masivu_ar_garumu(n):
    # Izveido masīvu ar noradīto garumu n
    # n - naturāls skaitlis
    a = numpy.arange(n)
    for i in range(n):
        b = input("Ievadiet " + str(i) + ".elementu ===> ")
        b = is_whole(b, i)
        a[i] = b
    return a


def izvade(x):
    # Izvada masīva elementus pēc kārtas līdz pēdējam
    # x - viendimensijas masīvs
    n = len(x)
    s = str(x[0])
    for i in range(1, n):
        s = s + ", " + str(x[i])
    print(s)


def is_whole(x, i):
    # Pārbauda vai simbolu virkne ir vesels skaitlis un ja nē, tad paprasa ievadīt to vēlreiz (bezgalīgi daudz ievades)
    # Ja simbolu virkne ir vesels skaitlis, tad atgriež to kā int(x)
    # x - pārbaudāma simbolu virkne
    # i - i-tajs elements
    while True:
        try:
            x = int(x)
        except:
            x = input("Kļūda! Ievadiet " + str(i) + ".elementu ===> ")
        else:
            return int(x)


def is_natural(n):
    # Pārbauda vai simbolu virkne ir naturāls skaitlis vai nav
    # Ja ir naturāls skaitlis, tad True. Ja nav tad False.
    # n - simbolu virkne, kuru pārbauda.
    if str(n).isdigit() and float(n) == int(n) and int(n) > 0:
        return True
    else:
        return False


def apvieno(a, b):
    # Apvieno divus sakārtotus masīvus a un b, un sakārto tos
    # Ātrums - lineārs laiks o(n)
    # a - viendimensijas masīvs
    # b - viendimensijas masīvs
    ga = len(a)
    gb = len(b)
    gc = ga + gb
    c = numpy.arange(gc)
    ia = 0
    ib = 0
    ic = 0
    while (ia < ga) and (ib < gb):
        if a[ia] < b[ib]:
            c[ic] = a[ia]
            ia = ia + 1
        else:
            c[ic] = b[ib]
            ib = ib + 1
        ic = ic + 1
    if ia < ga:
        for i in range(ia, ga):
            c[ic] = a[i]
            ic = ic + 1
    else:
        for i in range(ib, gb):
            c[ic] = b[i]
            ic = ic + 1
    return c


def reverse(masivs):
    # Pārkarto masīvā visus elementus pretēji
    # masivs - viendimensijas masīvs
    start_index = 0
    end_index = len(masivs) - 1

    while end_index > start_index:
        temp = masivs[start_index]
        masivs[start_index] = masivs[end_index]
        masivs[end_index] = temp

        start_index = start_index + 1
        end_index = end_index - 1

    return masivs


def is_ascending(n):  # vai nedilstoša?
    # Pārbauda vai masīvs ir augošs (nedilstošs)
    # Ja masīvs ir nedilstošs (nav augošs), tad return True
    # Ja masīvs nav nedilstošs (nav augošs), tad return False
    # n - viendimensijas masīvs
    if len(n) == 1:
        return True

    for i in range(0, len(n)):
        if i < len(n) - 1 and n[i] > n[i + 1]:
            return False  # Nē, nav augoša, nav nedilstoša, nav konstanta (varētu būt augoša, vai nekāda)

    return True  # Jā, ir augoša (vai nedilstoša)


def is_descending(n):  # vai neaugoša?
    # Pārbauda vai masīvs ir dilstošs (neaugošs)
    # Ja masīvs ir neaugošs (nav dilstošs), tad return True
    # Ja masīvs nav neaugošs (nav dilstošs), tad return False
    # n - viendimensijas masīvs
    if len(n) == 1:
        return True

    for i in range(0, len(n)):
        if i < len(n) - 1 and n[i] < n[i + 1]:
            return False  # Nē, nav dilstoša, nav neaugoša, nav konstanta (varētu būt augoša, vai nekāda)

    return True  # Jā, ir dilstoša (vai neaugoša)


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


m = input("Ievadiet 1. masīva izmēru ===> ")

while is_natural(m) == False:
    m = input("Masīva izmērs ir naturāls skaitlis!\nIevadiet masīva izmēru N ===> ")

m = int(m)

print("\nIevadiet sakārota augoša (nedilstoša) vai dilstoša (neaugoša) secība masīva skaitļus!")
a = izveidot_masivu_ar_garumu(m)

if is_ascending(a) == False and is_descending(a) == False:  # tad nekāda
    print("\nKļūda!\nPirmais ievadītais masīvs:")
    izvade(a)
    print("Nav ne augoši sakārtots, nav ne dilstoši sakārtots!")
    quit()


n = input("\nIevadiet 2. masīva izmēru ===> ")

while is_natural(n) == False:
    n = input("Masīva izmērs ir naturāls skaitlis!\nIevadiet masīva izmēru N ===> ")

n = int(n)

print("Ievadiet sakārota augoša (nedilstoša) vai dilstoša (neaugoša) secība masīva skaitļus!")
b = izveidot_masivu_ar_garumu(n)

if is_ascending(b) == False and is_descending(b) == False:
    print("\nKļūda!\nOtrais ievadītais masīvs:")
    izvade(b)
    print("Nav ne augoši sakārtots, nav ne dilstoši sakārtots!")
    quit()


k = input("\nIevadiet 3. masīva izmēru ===> ")

while is_natural(k) == False:
    n = input("Masīva izmērs ir naturāls skaitlis!\nIevadiet masīva izmēru N ===> ")

k = int(k)

print("\nIevadiet sakārota augoša (nedilstoša) vai dilstoša (neaugoša) secība masīva skaitļus!")
c = izveidot_masivu_ar_garumu(k)

if is_ascending(c) == False and is_descending(c) == False:
    print("\nKļūda!\nTrešais ievadītais masīvs:")
    izvade(c)
    print("Nav ne augoši sakārtots, nav ne dilstoši sakārtots!")
    quit()


print("\nPirmais sakārtots masīvs:")
izvade(a)
print("\nOtrais sakārtots masīvs:")
izvade(b)
print("\nTrešais sakārtots masīvs:")
izvade(c)


if is_ascending(a) == False:
    reverse(a)
if is_ascending(b) == False:
    reverse(b)
if is_ascending(c) == False:
    reverse(c)


ab = apvieno(a, b)
abc = apvieno(ab, c)


print("\nApvienots augošā (nedilstoša) secība sakārtots masīvs:")
izvade(abc)
