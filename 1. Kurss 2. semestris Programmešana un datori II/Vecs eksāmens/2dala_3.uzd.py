# simetriska matrica

import numpy


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


def ievade_matrica_sim(n, m):
    # Lietotājs var ievādīt nXm matricas elementus un funkcija atgriež divdimensijas masīvu ar n rindam un m kolonnam ar ievadītām vērtībam
    # n - naturāls skaitlis, kurš nosaka matricas rindas skaitu
    # m - naturāls skaitlis, kurš nosaka matricas kolonnas skaitu
    a = numpy.empty((n, m))
    for i in range(n):
        for j in range(m):
            if i == j or i > j:
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
            s = s + "{:8.0f}".format(int(a[i, j]))
        s = s + "\n"
    return s


def make_symmetrical(a):
    n = a.shape[0]
    m = a.shape[1]
    b = numpy.empty((m, n))

    for i in range(m):
        for j in range(n):
            if i < j:
                b[i, j] = a[j, i]
            elif i > j or i == j:
                b[i, j] = a[i, j]
    return b


n = int(input("Ievadiet matricas izmēru ==> "))
a = ievade_matrica_sim(n, n)
print("Jānīša matrica pirms atjaunošanas")
print(izvade_matrica_int(a))
print("Jānīša matrica pēc atjaunošanas")
sim_a = make_symmetrical(a)
print(izvade_matrica_int(sim_a))

'''
import numpy


def ievade(n):
    # funkcija realizē divdimensiju masīva ievadi
    a = numpy.empty((n, n))
    for i in range(n):
        for j in range(n):
            if i == j or i > j:

                a[i, j] = input("ievadi matricas elememtu (" + str(i) + "," + str(j) + ") ===> ")

    return a


def izvade(a):
    # funkcija nodrošina matricas glītu izvadi
    n = a.shape[0]  # x axis
    m = a.shape[1]  # y axis
    s = ""
    for i in range(n):
        for j in range(m):
            s = s + "{:6.0f}".format(a[i, j])
        s = s + "\n"
    return s


def aizpilda(a):
    # funkcija aizpilda matricas tukšās vietas
    n = a.shape[0]
    m = a.shape[1]
    b = numpy.empty((m, n))

    for i in range(m):
        for j in range(n):
            if i < j:
                # aizpilda tukšās vietas transponējot
                b[i, j] = a[j, i]
            elif i > j or i == j:
                # ieraksta ievadīto matricu
                b[i, j] = a[i, j]
    return b


# galvenā programma
n = int(input("Ievadiet matricas izmēru ==> "))
a = ievade(n)
print("Jānīša matrica pirms atjaunošanas")
print(izvade(a))
print("Jānīša matrica pēc atjaunošanas")
print(izvade(aizpilda(a)))
'''
