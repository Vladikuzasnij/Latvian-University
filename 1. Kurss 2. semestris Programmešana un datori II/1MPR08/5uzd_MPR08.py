# Programmas nosaukums: Matricas max un min elements
# 5. uzdevums (1MPR08_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas nodrošina divdimensiju matricas elementu ievadi,
# kas ir veseli skaitļi. Matricas rindu un kolonnu skaitu ievada lietotājs.
# Pēc matricas elementu ievades tiek nodrošināta matricas elementu izvade_matrica_int tabulas veidā,
# pieņemot, ka neviens no matricas elementiem nesastāv no ne vairāk kā 4 cipariem, kā arī
# lielāko un mazāko matricas elementa vērtību un tā atrašanās vietu, noradot atbilstošo rindu un kolonnu.
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


def is_whole(n):
    # Pārbauda vai simbolu virkne ir vesels skaitlis vai nav
    # Ja ir vesels skaitlis, tad True. Ja nav tad False.
    # n - simbolu virkne, kuru pārbauda.
    try:
        n = int(n)
    except:
        return False
    else:
        return True


def ievade_matrica(n, m):
    # Lietotājs var ievādīt nXm matricas elementus un funkcija atgriež divdimensijas masīvu ar n rindam un m kolonnam ar ievadītām vērtībam
    # n - naturāls skaitlis, kurš nosaka matricas rindas skaitu
    # m - naturāls skaitlis, kurš nosaka matricas kolonnas skaitu
    a = numpy.empty((n, m), dtype=int)
    for i in range(n):
        for j in range(m):
            temp = input("Ievadiet matricas elememtu a(" + str(i) + "," + str(j) + ") ===> ")
            while is_whole(temp) == False:
                temp = input("Kļūda! Ievadītais elements nav vesels skaitlis!\nIevadiet matricas elememtu a(" + str(i) + "," + str(j) + ") ===> ")
            a[i, j] = int(temp)
    return a


def izvade_matrica_int(a):
    # Atgriež divdimensiju masīvu (matricu), tabulas veidā, str formāta, kur katra rinda ir atdalīta ar jauno rindkopu
    # a - divdimensijas masīvs (matrica)
    n = a.shape[0]  # "x axis" masīva izmēri
    m = a.shape[1]  # "y axis" masīva izmēri

    s = ""
    for i in range(n):
        for j in range(m):
            s = s + "{:8.2f}".format(int(a[i, j]))
        s = s + "\n"
    return s


def matricas_izvade_4_cipari(m):
    # Izvada divdimensijas masīvu tabulas veidā tā, ka neviens no matricas elementiem nesastāv no ne vairāk kā 4 cipariem
    # Tiek nodrošināta matricas elementu izvade tabulas veidā, pieņemot, ka neviens no matricas elementiem nesastāv no ne vairāk kā 4 cipariem
    # Atgriež matricas elementu izvade tabulas veidā
    # m - divdimensijas masīvs
    nm = numpy.shape(m)
    sv = ""
    for x in range(nm[0]):
        for y in range(nm[1]):
            for i in range(5 - len(str(m[x, y]))):
                sv = sv + " "
            sv = sv + str(m[x, y])
        sv = sv + "\n"
    nn = len(sv)
    return sv[:nn - 1]


def max_value_in_2_dimensional_array_and_its_coords(a):
    # Atgriež tuple (max_value, coords) ar divdimensijas masīva (matricas) maksimālo elementu vērtību un tas koordinātu [i,j] pēc rindām un kolonnam
    # Atgriež maksimālo vērtību un kur tā vērtība atrodas pēc koordinātam
    # a - divdimensijas masīvs
    max_value = a[0][0]
    coords = [0, 0]

    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] > max_value:
                max_value = a[i][j]
                coords = [i, j]

    return (max_value, coords)


def min_value_in_2_dimensional_array_and_its_coords(a):
    # Atgriež kortežu (tuple) (min_value, coords) ar divdimensijas masīva (matricas) minimālo elementu vērtību un tas koordinātu [i,j] pēc rindām un kolonnam
    # Atgriež minimālo vērtību un kur tā vērtība atrodas pēc koordinātam
    # a - divdimensijas masīvs
    min_value = a[0][0]
    coords = [0, 0]
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] < min_value:
                min_value = a[i][j]
                coords = [i, j]

    return (min_value, coords)


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


n = input("Ievadiet matricas rindu skaitu ===> ")
while is_natural(n) == False:
    n = input("Kļūda! Matricas rindu skaitam jābūt naturālam skaitlim!\nIevadiet matricas rindu skaitu ===> ")
n = int(n)


m = input("Ievadiet matricas kolonnu skaitu ===> ")
while is_natural(m) == False:
    m = input("Kļūda! Matricas kolonnu skaitam jābūt naturālam skaitlim!\nIevadiet matricas kolonnu skaitu ===> ")
m = int(m)

a = ievade_matrica(n, m)

print(matricas_izvade_4_cipari(a))

max_value_and_coord = max_value_in_2_dimensional_array_and_its_coords(a)
min_value_and_coord = min_value_in_2_dimensional_array_and_its_coords(a)

print("Mazākais elements ir " + str(min_value_and_coord[0]) + ", un tas atrodas " + str(min_value_and_coord[1][0] + 1) + ".rindas un " + str(min_value_and_coord[1][1] + 1) + ".kolonnas krustpunktā.")
print("Lielākais elements ir " + str(max_value_and_coord[0]) + ", un tas atrodas " + str(max_value_and_coord[1][0] + 1) + ".rindas un " + str(max_value_and_coord[1][1] + 1) + ".kolonnas krustpunktā.")
