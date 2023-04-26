# Programmas nosaukums: Galveno diagonaļu summa matricai
# 1. uzdevums (1MPR09_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas nodrošina kvadrātiskas matricas elementu ievadi, aprēķina visu "diagonāļu", kas paralēlas
# galvenai diagonālei summu nodrukā uz ekrāna pašu matricu un "tās diagonāļu" elementu summu.
# Izvades formāts:
#   1   2   3  |
#   4   5   6  |  3
#   7   8   9  |  8
#  ━━━━━━━━━━━━━━━
#       7   12 | 15
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import numpy


def ievade(n, m):
    # Prasa lietotājam ievadīt visas matricas elementus. Matricas elementi var būt tikai vesēlie skaitļi.
    # Ja tiek ievadīt nevesels skaitlis vai simbolu virkne, tad prasa ievādīt tikmēr, kamēr neievadīs pareizi.
    # Atgriež NumPy masīvu ar lietotāja ievadītajiem veseliem elementiem.
    # n - matricas (divdimensiju masīva) rindas skaits
    # m - matricas (divdimensiju masīva) kolonnas skaits
    a = numpy.empty((n, m))
    for i in range(n):
        for j in range(m):
            t = input("Ievadiet matricas elementu a(" + str(i) + "," + str(j) + ") ===> ")
            while is_whole(t) == False:
                t = input("Kļūda! Ievadītam skaitlim jābūt veselam!\nIevadiet matricas elementu a(" + str(i) + "," + str(j) + ") ===> ")
            t = int(t)
            a[i, j] = t
    # Atgriezt NumPy masīvu ar ievadītiem veseliem elementiem
    return a


def izvade_matricu_ar_diagonalu_summam(a):
    # Atgriež simbolu virkni, kura repzenetē "glītu diagonāļu summu". Labi atspoguļo tikai skaitļus līdz 999.
    # Piemēram:
    # 3  -1  -2  |
    # 2   3   4  |  -2
    # 5   6   7  |  3
    # ━━━━━━━━━━━━━━━
    #      5   8 | 13
    # a - divdimensijas masīvs (kvadrātiska matrica), kurai sameklējam diagonaļu summu izmantojot funkciju "diagonalu_summa"

    # a.ndim # dimensiju skaits
    # a.shape # kortežs ar masīva izmēriem

    n = a.shape[0]  # x axis
    m = a.shape[1]  # y axis
    s = ""
    c = diagonalu_summa(a)
    for i in range(n):
        for j in range(m):
            s = s + "{:4d}".format(int(a[i, j]))
        if i == 0:
            s = s + "  |  \n"
            len1 = len(s) - 3
            continue
        s = s + "  |  " + str(int((c[-1 * i]))) + "\n"

    s = s + "  " + "━" * (len1) + "\n"

    k = 0
    for i in range(n):
        if i == 0:
            s = s + "    "
            continue
        s = s + "   " + str(int((c[i])))
        k += 1

    s = s + " | " + str(int((c[k + 1])))

    return s


def diagonalu_summa(a):
    # Atgriež divdimensijas masīvu, kur labājā un apaksējā stūri elementi atspoguļo kvadrātiskas matricas diagonaļu summu
    # Ja nav iespējams aprēķināt, tad atgriež "Kļūda"
    # a - divdimensijas masīvs (kvadrātiska matrica)
    n = a.shape[0]
    m = a.shape[1]
    if m == n:
        c = numpy.zeros(2 * n)
        for k in range(1, 2 * n):
            s = 0
            if k <= n:
                # Apakšsumma
                for j in range(k):
                    s = s + a[n - k + j, j]
            else:
                # augšsumma
                for j in range(k - n, n):
                    s = s + a[n + j - k, j]
            c[k] = s
        return c
    else:
        return "Kļūda"


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


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


n = input("Ievadiet kvadrātiskas matricas izmēru ===> ")
while is_natural(n) == False:
    n = input("Kļūda! Ievadītam skaitlim jābūt naturālam!\nIevadiet kvadrātiskas matricas izmēru ===> ")
n = int(n)

a = ievade(n, n)

print("")
print(izvade_matricu_ar_diagonalu_summam(a))
