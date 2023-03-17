# Programmas nosaukums: Formulas no statistikas
# 1. uzdevums (1MPR05_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas pieprasa lietotājam ievadīt N skaitļus un atrod šo skaitļu virknes
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import numpy
import math


def is_natural(n):
    # Pārbauda vai simbolu virkne ir naturāls skaitlis vai nav
    # Ja ir naturāls skaitlis, tad True. Ja nav tad False.
    # n - simbolu virkne, kuru pārbauda.
    if str(n).isdigit() and float(n) == int(n) and int(n) > 0:
        return True
    else:
        return False


def izveidot_masivu_ar_garumu(n):
    # Izveido masīvu ar noradīto garumu n
    # n - naturāls skaitlis
    a = numpy.arange(n)
    for i in range(n):
        b = input("Ievadiet " + str(i) + ".elementu ===> ")
        b = is_whole(b, i)
        a[i] = b
    return a


def is_whole(x, i):  # Bezgalīgi daudz reizes ievāda
    while True:
        try:
            x = int(x)
        except:
            x = input("Kļūda! Ievadiet " + str(i) + ".elementu ===> ")
        else:
            return int(x)


def izvade(x):
    # Izvada masīva elementus pēc kārtas līdz pedējam
    # x - masīvs
    n = len(x)
    s = str(x[0])
    for i in range(1, n):
        s = s + ", " + str(x[i])
    return s


def videjais_aritmetiskais(x):
    # Aprēķina masīva vidējo aritmētisko
    # x - masīvs
    n = len(x)
    t = 0
    for i in range(0, n):
        t = t + x[i]

    return t / n


def videjais_kvadratiskais(x):
    # Aprēķina masīva videjo kvadrātisko
    # x - masīvs
    n = len(x)
    t = 0
    for i in range(0, n):
        t = t + x[i] * x[i]

    return math.sqrt(t / n)


def videjais_harmoniskais(x):
    # Aprēķina masīva videjo harmonisko
    # x - masīvs
    n = len(x)
    t = 0

    for i in range(0, n):

        if x[i] == 0:
            return "Kļūda! Dalīšana ar 0"
        elif is_natural(x[i]):
            t = t + 1 / x[i]
        else:
            return "Kļūda! Visiem skaitļiem jābut pozitīviem!"

    return n / t


def videjais_geometriskais(x):
    # Aprēķina masīva videjo ģeomētrisko
    # x - masīvs
    n = len(x)
    s = 1

    for i in x:
        s = s * i

    if n % 2 == 0:  # Pārbauda vai n-sakne ir pāra skaitlis
        if s >= 0:  # Ja n-sakne pāra skaitlis, tad pārbaudam vai nav negatīvs, ja ir tad nevaram aprēķināt
            k = math.pow(s, (1 / n))  # ja ir pozitīvs vai 0, tad viss ir labi, varam aprēķināt pāra-sakni no pozitīvas vērtības
        else:
            k = "Nevar aprēķināt reālos skaitļos"  # ja ir negatīvs un n-sakne ir pāra skaitlis, tad nevaram to aprēķināt reālos skaitlos
    else:
        k = numpy.sign(s) * (numpy.abs(s)) ** (1 / n)  # ja n-sakne ir nepāra skaitlis, tad aprēķināt to šādi (parasta pow(a,b) funkcija nedarbojas ar tādiem skaitliem)

    return k


def videjas_linearas_novirzes_vertiba(x):
    # Aprēķina masīva vidējās absolūtās jeb vidējās lineārās novirzes vērtību
    # x - masīvs
    n = len(x)
    t = 0
    k = 0
    for i in range(0, n):
        t = t + x[i]

    c = t / n

    for i in range(0, n):
        k = k + abs(x[i] - c)

    return k / n


def standartnovirze(x):
    # Aprēķina masīva standartnovirzi
    # x - masīvs
    n = len(x)
    t = 0
    k = 0
    for i in range(0, n):
        t = t + x[i]

    c = t / n

    for i in range(0, n):
        k = k + (x[i] - c) * (x[i] - c)

    return math.sqrt(k / n)


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


n = input("Ievadiet masīva izmēru N ===> ")

while is_natural(n) == False:
    n = input("Masīva izmērs ir naturāls skaitlis!\nIevadiet masīva izmēru N ===> ")

n = izveidot_masivu_ar_garumu(int(n))

print("\nSkaitļu virknes " + izvade(n))
print("Vidējais aritmētiskais: " + str(videjais_aritmetiskais(n)))
print("Vidējais kvadratiskais: " + str(videjais_kvadratiskais(n)))
print("Vidējais harmoniskais: " + str(videjais_harmoniskais(n)))
print("Vidējais ģeomētriskais: " + str(videjais_geometriskais(n)))
print("Vidējās absolūtās jeb vidējās lineārās novirzes vērtība: " + str(videjas_linearas_novirzes_vertiba(n)))
print("Standartnovīrze: " + str(standartnovirze(n)))
