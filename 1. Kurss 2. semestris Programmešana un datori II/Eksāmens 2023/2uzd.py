import numpy



def is_cipars(n):
    # Pārbauda vai simbolu virkne ir vesels skaitlis vai nav
    # Ja ir vesels skaitlis, tad True. Ja nav tad False.
    # n - simbolu virkne, kuru pārbauda.
    try:
        n = int(n)
    except:
        return False
    else:
        if n >= 10:
            return False
        if n <= 0:
            return False
        return True

def is_cipars_100(n):
    # Pārbauda vai simbolu virkne ir vesels skaitlis vai nav
    # Ja ir vesels skaitlis, tad True. Ja nav tad False.
    # n - simbolu virkne, kuru pārbauda.
    try:
        n = int(n)
    except:
        return False
    else:
        if n >= 101:
            return False
        if n <= 0:
            return False
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
    a = numpy.empty((n, m), dtype=numpy.int64)
    for i in range(n):
        for j in range(m):
            temp = input("Ievadiet matricas elememtu a(" + str(i) + "," + str(j) + ") ===> ")
            while is_cipars(temp) == False:
                temp = input("Kļūda! Ievadītais elements nav viencipara naturāls skaitlis!\nIevadiet matricas elememtu a(" + str(i) + "," + str(j) + ") ===> ")
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
n = input("Ievadiet kvadrātitskas matricas izmēru ==> ")

while is_cipars_100(n) == False:
    n = input("Kļūda! Ievadiet kvadrātitskas matricas izmēru ==> ")
n = int(n)

a = ievade_matrica(n, n)
b = izvade_matrica_int(a)
print("Ievadītā matrica:")
print(b)

# print(b)
# izsauc summu funkcijas
c = matrix_diag_sum(a)
d = matrix_row_sum(a)
e = matrix_col_sum(a)

new_a = new_matrix(a, c, e, d)
new_b = izvade_matrica_int(new_a)
print("Jauna matrica:")
print(new_b)