# Programmas nosaukums:
# 2. uzdevums (1MPR10_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas nodrošina matricas ievadi, atrod inverso matricu, izmantojot adjunktu metodi un izvada uz ekrāna gan doto,
# gan atrasto inverso matricu.
# Zināšanai: A^-1 = 1/detA * ( A')^T, kur A' ir matricas adjunktu matrica.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import numpy


def determinants(x):
    # Rekursīvi atrod matricas x determinanta vērtību.
    # Atgriež determinanta vērtību kā skaitļi no matricas x.
    # x - kvadrātiska n x n divdimensijas numpy masīvs (matrica ar izmēriem n x n)

    n = len(x)
    if n == 1:
        return x[0, 0]
    det = 0
    zime = 1
    for i in range(n):
        xx = numpy.empty((n - 1, n - 1))
        for j in range(1, n):
            z = 0
            for k in range(n):
                if k != i:
                    xx[j - 1, z] = x[j, k]
                    z = z + 1
        y = determinants(xx)
        det = det + zime * x[0, i] * y
        zime = -zime  # + - + - + ...
    return det


def is_natural(n):
    # Pārbauda vai simbolu virkne ir naturāls skaitlis vai nav
    # Ja ir naturāls skaitlis, tad True. Ja nav tad False.
    # n - simbolu virkne, kuru pārbauda.

    if str(n).isdigit() and float(n) == int(n) and int(n) > 0:
        return True
    else:
        return False


def ievade_matrica_float(n, m):
    # Lietotājs var ievādīt nXm matricas elementus un funkcija atgriež divdimensijas masīvu ar n rindam un m kolonnam ar ievadītām vērtībam.
    # Ievādītas vērtības ir reālas vērtības (matricas elementi varētu būt float)
    # Glīti izvada atkarīgi no tas, cik ir nepieciešams starpes likt.
    # n - naturāls skaitlis, kurš nosaka matricas rindas skaitu
    # m - naturāls skaitlis, kurš nosaka matricas kolonnas skaitu

    a = numpy.empty((n, m), dtype=float)

    for i in range(n):
        for j in range(m):
            temp = input("Ievadiet matricas elememtu A(" + str(i) + "," + str(j) + ") ===> ")
            while is_real_check(temp) == False:
                temp = input("Kļūda! Ievadītais elements nav skaitlis!\nIevadiet matricas elememtu A(" + str(i) + "," + str(j) + ") ===> ")

            a[i, j] = float(temp)

    return a


def is_real_check(n):
    # Pārbauda vai simbolu virkne ir reāls skaitlis vai nav.
    # Atgriež True, ja tas ir reāls skaitlis (float).
    # Atgriež False, ja tas nav reāls skaitlis (float).
    # n - pārbaudāma simbolu virkne.

    try:
        float(n)
    except:
        return False
    else:
        return True


def matrix_to_string_float(matrix):
    # Atgriež matricas virknes attēlojumu, kur katra rinda ir atdalīta ar \n.
    # Ja vērtība ir vesels skaitlis, tā tiek attēlota bez komata. Pretējā gadījumā tas tiek attēlots ar komatu.
    # Funkcija atrod arī maksimālo vērtību garumu matricā un papildina nepieciešamus skaitļus ar tujšumiem " ", lai tie būtu pareizi izlīdzināti.
    # matrix - matrica (divdimensijas numpy masīvs ar izmēriem n x m).

    rindas = len(matrix)
    kolonnas = len(matrix[0])
    max_len = 0

    for i in range(rindas):  # atrod max_len, lai uzzinātu cik atkāpes ir nepieciešāmas
        for j in range(kolonnas):
            value = matrix[i][j]
            if value == int(value):
                value_len = len(str(int(value)))
            else:
                value_len = len(str(float(value)))
            if value_len > max_len:
                max_len = value_len

    sv = ""
    # izveido matricas virknes attēlojumu, kur katra rinda ir atdalīta ar \n un izlidzina to pēc skaitļa ar maksimālu garumu
    for i in range(rindas):
        for j in range(kolonnas):
            value = matrix[i][j]
            if value == int(value):
                value = int(value)
            else:
                value = str(float(value))
            atkape = " " * (max_len - len(str(value)))
            sv += atkape + str(value)
            if j < kolonnas - 1:
                sv = sv + " "
        sv = sv + "\n"

    return sv


def transponenta(a):
    # Atgriež transponētu matricu a b[i, j] = a[j, i]
    # a - divdimensijas masīvs (matrica)

    n = a.shape[0]  # x axis
    m = a.shape[1]  # y axis
    b = numpy.empty((m, n))
    for i in range(m):
        for j in range(n):
            b[i, j] = a[j, i]
    return b


def adjugate_matrix(a):
    # Atgriež dotās kvadrātmatricas a adjunktu matricu a*.
    # a - nXn divdimensijas masīvs (kvadrātmatrica)

    n = a.shape[0]

    if n == 1:
        # Ja matrica is 1x1, tas adjunktu matrica ir tas paša matrica
        return a

    adj = numpy.zeros((n, n))  # Izveidojam tukšo mainīgu ar nullem, kura būs adjunktu matrica a* matricai a
    for i in range(n):
        for j in range(n):
            # Izveidojam paligmatricu, noņemot rinda i un kolonnu j no sākotnējās matricas a
            paligmatrica = []
            for k in range(n):
                if k != i:
                    rinda = []
                    for l in range(n):
                        if l != j:
                            rinda.append(a[k, l])
                    paligmatrica.append(rinda)

            # Konvertējam paligmatricu par NumPy masīvu
            paligmatrica = numpy.array(paligmatrica)
            # Aprēķinam paligmatricas determinantu
            det = determinants(paligmatrica)
            # Reizinām determinantu ar (-1)^(i+j)
            zime = (-1) ** (i + j)
            # Adjunktas matricas elements (i,j) tas ir determinants no palīgmatricas ar zimes reizinājumu (-1 vai +1)
            adj[i, j] = det * zime

    return adj


def inverse_matrix_by_def(a):
    # Atgriež inverso matrīcu (divdimensijas masīvu) izmantojot transponenta, determinants un adjugate_matrix funckijas
    # a - divdimensijas masīvs (kvadrātiska matrica)

    adj = adjugate_matrix(a)
    transponent_adj_matrix = transponenta(adj)
    det = determinants(a)
    if det == 0:
        return "Neēksiste"
    else:
        inverse_det = 1 / determinants(a)
        inverse_a = inverse_det * transponent_adj_matrix
        return inverse_a


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


n = input("Ievadiet kvadrātiskas matricas izmēru, kurai gribat atrast invērsu matricu ==> ")
while not is_natural(n):
    n = input("Kļūda! Ievadiet kvadrātiskas matricas izmēru, kurai gribat atrast invērsu matricu ==> ")
n = int(n)

a = ievade_matrica_float(n, n)

print("\nJūsu ievadīta matrica A:")
print(matrix_to_string_float(a))

print("Atrāsta invērsa matrica A^-1:")
inversa = inverse_matrix_by_def(a)

if str(inversa) == "Neēksiste":
    print("Matricai A neēksistē invērsa matrica A^-1.")
else:
    print(matrix_to_string_float(inversa))
