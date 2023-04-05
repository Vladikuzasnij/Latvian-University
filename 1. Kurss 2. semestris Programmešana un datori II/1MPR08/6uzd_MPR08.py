# Programmas nosaukums: Matricas reizinājums un matricu atbilstošo elementu reizinājums
# 6. uzdevums (1MPR08_Vladislavs_Babaņins)
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
            # s = s + "   " + str(int(a[i,j])) #"{:8.2f}".format(a[i,j], dtype=int)
        s = s + "\n"
    return s


def matricas_izvade_4_cipari(m):
    # Izvada divdimensijas masīvu tabulas veidā tā, ka neviens no matricas elementiem nesastāv no ne vairāk kā 4 cipariem
    # Tiek nodrošināta matricas elementu izvade_matrica_int tabulas veidā, pieņemot, ka neviens no matricas elementiem nesastāv no ne vairāk kā 4 cipariem
    # Atgriež matricas elementu izvade_matrica_int tabulas veidā
    # m - divdimensijas masīvs
    nm = (numpy.shape(m))
    sv = ""
    for x in range(nm[0]):
        for y in range(nm[1]):
            for i in range(5 - len(str(m[x, y]))):
                sv = sv + " "
            sv = sv + str(m[x, y])
        sv = sv + "\n"
    nn = len(sv)
    return sv[:nn - 1]


def check_fake_matrix_multiplication(n1, m1, n2, m2):
    # Pārbauda vai divas matricas (divdimensiju masīvi) ir ar vienādu izmēru. Pārbauda vai sakrīt 1.matricas rindas skaits ar 2.matricas rindas skaitu.
    # un pārbauda vai 1.matricas kolonnu skaits sakrīt ar 2.matricas kolonnu skaitu. Ja abas prasības izpildās, tad return True. Ja kaut viena neizpildās, tad return False.
    # Tiek izmantota, lai pārbaudītu vai var sareizināt matricas atbilstošus elementus vai nē.
    # n1 - 1.matricas rindu skaits
    # m1 - 1.matricas kolonnu skaits
    # n2 - 2.matricas rindu skaits
    # m2 - 2.matricas kolonnu skaits
    if n1 == n2 and m1 == m2:
        return True
    else:
        return False


def check_matrix_multiplication(n1, m1, n2, m2):
    # Pārbauda vai 1.matricas kolonnu skaits sakrīt ar 2.matricas rindu skaitu. Ja sakrīt, tad return True. Ja nē, tad return False.
    # Tiek izmantots, lai pārbaudītu vai ir iespējams sareizināt divas matricas.
    # n1 - 1.matricas rindu skaits (tā ne uz ko neietekme)
    # m1 - 1.matricas kolonnu skaits
    # n2 - 2.matricas rindu skaits
    # m2 - 2.matricas kolonnu skaits (tā ne uz ko neietekme)
    if m1 == n2:
        return True
    else:
        return False


def matrix_multiplication_integer(a, b):
    # Sareizina divu divdimensijas masīvus (divas matricas) a ar b.
    # Atgriež divdimensiju masīvu, vai ja nevar sareizināt atgriež "Kļūda"
    # a - divdimensijas masīvs
    # b - divdimensijas masīvs
    n1 = a.shape[0]
    m1 = a.shape[1]
    n2 = b.shape[0]
    m2 = b.shape[1]
    if m1 == n2:
        c = numpy.zeros((n1, m2), numpy.int_)
        for i in range(n1):
            for j in range(m2):
                for k in range(m1):
                    c[i, j] = c[i, j] + a[i, k] * b[k, j]
        return c
    else:
        return "Kļūda"


def fake_matrix_multiplication(a, b):
    # Sareizina divas matricas atbilstošus elementus un atgriež atbilstošu divdimensiju masīvu
    # a - divdimensiju masīvs
    # b - divdimensiju masīvs
    c = numpy.empty((n1, m1), dtype=int)

    for i in range(n1):
        for j in range(m2):
            c[i, j] = a[i][j] * b[i][j]

    return c


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


n1 = input("Ievadiet 1.matricas rindu skaitu ===> ")
while is_natural(n1) == False:
    n1 = input("Kļūda! Matricas rindu skaitam jābut naturālam skaitlim!\nIevadiet 1.matricas rindu skaitu ===> ")
n1 = int(n1)

m1 = input("Ievadiet 1.matricas kolonnu skaitu ===> ")
while is_natural(m1) == False:
    m1 = input("Kļūda! Matricas kolonnu skaitam jābut naturālam skaitlim!\nIevadiet 1.matricas kolonnu skaitu ===> ")
m1 = int(m1)

a = ievade_matrica(n1, m1)


n2 = input("\nIevadiet 2.matricas rindu skaitu ===> ")
while is_natural(n2) == False:
    n2 = input("Kļūda! Matricas rindu skaitam jābut naturālam skaitlim!\nIevadiet 2.matricas rindu skaitu ===> ")
n2 = int(n2)

m2 = input("Ievadiet 2.matricas kolonnu skaitu ===> ")
while is_natural(m2) == False:
    m2 = input("Kļūda! Matricas kolonnu skaitam jābut naturālam skaitlim!\nIevadiet 2.matricas kolonnu skaitu ===> ")
m2 = int(m2)

b = ievade_matrica(n2, m2)


print("\nPirmā ievadīta matrica:")
print(matricas_izvade_4_cipari(a))

print("\nOtrā ievadīta matrica:")
print(matricas_izvade_4_cipari(b))


if check_fake_matrix_multiplication(n1, m1, n2, m2):
    print("\nAbu matricu atbilstošās elementu reizinājums:")
    c = fake_matrix_multiplication(a, b)
    print(matricas_izvade_4_cipari(c))
else:
    print("\nKļūda! Šādas matricas nevar sareizināt atbilstošus elementus.")


if check_matrix_multiplication(n1, m1, n2, m2):
    print("\nDivu matricu reizinājums:")
    d = matrix_multiplication_integer(a, b)
    print(matricas_izvade_4_cipari(d))
else:
    print("\nKļūda! Šādas matricas nevar sareizināt, jo 1.matricas kolonnu skaits nav vienāds ar 2.matricas rindas skaitu.")
