# Programmas nosaukums: Burbuļa kārtošanas metode
# 5. uzdevums (1MPR05_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas pieprasa lietotājam ievadīt N skaitļus un sakārto tos dilstošā (neaugošā) secībā, izmantojot burbuļa kārtošanas metodi un uz ekrāna izvada sakārtoto skaitļu masīvu un veikto salīdzināšanas skaitu.
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


def burbulis_uzlabotais(a):
    # Burbulis (uzlabotais) kartošanas metode
    # Sakarto masīva elementus dilstoša (neaugoša) secība un
    # izvada paveikto salīdzīnašanas skaits, lai sakārtot masīvu. Izmanto burbuļa metodi (uzlaboto)
    # a - masīvs
    skaititajs = 0
    n = len(a)
    i = n - 1
    paz = True
    while paz:
        paz = False
        for j in range(0, i):
            skaititajs = skaititajs + 1
            if a[j] < a[j + 1]:
                paz = True
                x = a[j]
                a[j] = a[j + 1]
                a[j + 1] = x
        i = i - 1
    print(skaititajs)


def izvade(x):
    # Izvada masīva elementus pēc kārtas līdz pedējam
    # x - masīvs
    n = len(x)
    s = str(x[0])
    for i in range(1, n):
        s = s + ", " + str(x[i])
    print(s)


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
    # Pārbauda vai x ir vesels skaitlis
    # x - pārbaudama simbolu virkne
    # i - elements pēc kārtas
    while True:
        try:
            x = int(x)
        except:
            x = input("Kļūda! Ievadiet " + str(i) + ".elementu ===> ")
        else:
            return int(x)


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


m = input("Ievadiet masīva izmēru N ===> ")

while is_natural(m) == False:
    m = input("Masīva izmērs ir naturāls skaitlis!\nIevadiet masīva izmēru N ===> ")

m = int(m)
b = izveidot_masivu_ar_garumu(m)

print("Paveikts salīdzīnašanas skaits, lai sakārtot masīvu:")
burbulis_uzlabotais(b)  # Salidzinašanas skaits
print("Sakārtots skaitļu masīvs dilstoša (neaugoša) secība:")
izvade(b)
