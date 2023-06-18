# rindu, kolonnu un diagonaļu summa
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


def matrix_row_sum(a):
    # rindas summa
    b = a.shape[0]
    c = numpy.zeros(b)
    for i in range(b):
        summa = 0
        for j in range(b):
            summa = summa + a[i, j]
        c[i] = summa
    return c


def matrix_col_sum(a):
    # kolonnu summa
    b = a.shape[0]
    c = numpy.zeros(n)
    for i in range(b):
        summa = 0
        for j in range(b):
            summa = summa + a[j, i]
        c[i] = summa
    return c


def matrix_diag_sum(a):
    # diagonalu summa
    b = a.shape[0]
    c = numpy.zeros(n)
    summa = 0

    for i in range(b):
        summa = summa + a[i, i]
    c[0] = summa
    summa = 0

    for i in range(b):
        summa = summa + a[i, n - 1 - i]
    c[1] = summa

    return c


def new_matrix(a, c, e, d):
    n = a.shape[0]
    new_a = numpy.zeros((n + 2, n + 2))

    new_a[1:n + 1, 1:n + 1] = a  # centrs

    new_a[1:n + 1, 0] = d
    new_a[0, 1:n + 1] = e

    new_a[1:n + 1, -1] = d
    new_a[-1, 1:n + 1] = e

    new_a[n + 1, n + 1] = c[0]
    new_a[n + 1, 0] = c[1]
    new_a[0, n + 1] = c[1]
    new_a[0, 0] = c[0]

    return new_a


# galvenā programma
n = int(input("Ievadiet kvadrātitskas matricas izmēru ==> "))
a = ievade_matrica(n, n)
b = izvade_matrica_int(a)
print("Ievadītā matrica:")
print(b)

# print(b)
# izsauc summu funkcijas
c = matrix_diag_sum(a)
d = matrix_row_sum(a)
e = matrix_col_sum(a)
# print(c)
# print(d)
# print(e)
new_a = new_matrix(a, c, e, d)
new_b = izvade_matrica_int(new_a)
print("Jauna matrica:")
print(new_b)

'''
import numpy


def ievade(n):
    # funkcija realizē divdimensiju masīva ievadi
    a = numpy.empty((n, n))
    for i in range(n):
        for j in range(n):
            a[i, j] = int(input("ievadi matricas " + "elememtu (" + str(i) + "," + str(j) + ") ===>"))
    return a


def izvade(a):
    # funkcija realizē divdimensiju masīva izvadi
    n = a.shape[0]  # x axis
    m = a.shape[1]  # y axis
    s = ""
    for i in range(n):
        for j in range(m):
            s = s + "{:5.0f}".format(a[i, j])
        s = s + "\n"
    return s


def rinduSumma(a):
    # funkcija aprēķina matricas rindu summu
    n = a.shape[0]
    c = numpy.zeros(n)  # rezultējošais masīvs
    for i in range(n):
        s = 0
        for j in range(n):
            s = s + a[i, j]
        c[i] = s
    return c


def kolonnuSumma(a):
    # funkcija aprēķina matricas kolonnu summu
    n = a.shape[0]
    c = numpy.zeros(n)  # rezultējošais masīvs
    for i in range(n):
        s = 0
        for j in range(n):
            s = s + a[j, i]
        c[i] = s
    return c


def diagonaluSumma(a):
    # funkcija aprēķina matricas diagonāļu summu
    n = a.shape[0]
    c = numpy.zeros(n)  # c ir rezultējošais masīvs
    s = 0
    # galvenās diagonāles summa
    for i in range(n):
        s = s + a[i, i]
    c[0] = s
    s = 0
    # blakus diagonāles summa
    for i in range(n):
        s = s + a[i, n - 1 - i]
    c[1] = s
    # c[0] ir galvenās diagonāles elementu summa
    # c[1] ir blakus diagonāles elementu summa

    return c


# galvenā programma
n = int(input("Ievadiet kvadrātitskas matricas izmēru==>"))
a = ievade(n)
b = izvade(a)
print("Ievadītā matrica:")
print(b)
# izsauc summu funkcijas
c = diagonaluSumma(a)
r = rinduSumma(a)
k = kolonnuSumma(a)
# rezultāta izvadīšanas formatēšana
# jauns masīvs, kas saturēs gan ievadīto matricu, gan visas summas malās
mat = numpy.zeros((n + 2, n + 2))
for i in range(n + 2):
    # galveno diagonāļu summas
    if i == 0:
        mat[i, i] = c[0]
    elif i == n + 1:
        mat[i, 0] = c[1]
        mat[i, i] = c[0]
        mat[0, i] = c[1]
    # kolonnu un rindu summas
    else:
        mat[0, i] = k[i - 1]
        mat[n + 1, i] = k[i - 1]
        mat[i, 0] = r[i - 1]
        mat[i, n + 1] = r[i - 1]
# sākotnējās matricas ievadīšana rezultējošās matricas centrā
for j in range(n + 1):
    if i > 0 and j > 0 and i < n + 1:
        mat[i, j] = a[i - 1, j - 1]

print("Rindu un kolonnu summas")
print(izvade(mat))
'''
