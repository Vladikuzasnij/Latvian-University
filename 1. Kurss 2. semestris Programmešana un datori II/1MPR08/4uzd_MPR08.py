# Programmas nosaukums: Lielo skaitļu reizināšana
# 4. uzdevums (1MPR08_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas realizē lielo naturālo skaitļu (vismaz ar 50 cipariem) reizināšanu,
# izmantojot naivo skolas reizināšanas algoritmu.
# Jāveic ievaddatu korektuma pārbaude!
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import numpy


def is_natural_or_zero_long(s):
    # Pārbauda vai simbolu virkne reprezentē naturālo skaitli vai 0, vai nē.
    # Atgriež True, ja virkne reprezentē naturālo skaitli.
    # Atgriež False, ja nereprezentē naturālo skaitli.
    # s - pārbaudama simbolu virkne

    # Noņema no virknes visas sākuma vai beigu atstarpes
    s = s.strip()

    # Pārbauda, vai virkne ir tukša
    if len(s) == 0:
        return False

    # Iet cikliski cauri katrām simbolam simbolu virknē (string'ā)
    for c in s:
        # Ja kāda rakstzīme nav cipars, virkne neatspoguļo naturālu skaitli. return False
        if not c.isdigit():
            return False

    # Virkne atspoguļo naturālu skaitli, ja ietu cauri ciklas netika pamanīts not .isdigit()
    return True


def izvade_bez_komatiem_kopigi(x):
    # Izvada masīva elementus pēc kārtas līdz pedējam kopīgi bez komatiem (izmanto, lai izvadītu masīvu kā vienu str skaitli)
    # x - viendimensijas masīvs
    n = len(x)
    s = str(x[0])
    for i in range(1, n):
        s = s + "" + str(x[i])

    s = s[::-1]
    print(s)


def parveide_sv_to_mas(sv, m):
    # Transformē simbolu virkni masīvā ar noradīto garumu. Ja garums ir lielāks nekā simbolu virkne, tad beigās tiek pieliktas 0
    # sv - simbolu virkne, kura sastāv no cipariem
    # m - (vēlamais masīva garums) garums, līdz kurām vajag transformēt simbolu virkni sarakstā. Ja garums ir lielāks nekā simbolu virkne, tad beigās tiek pieliktas 0
    n = len(sv)
    a = numpy.arange(m)
    for i in range(n):
        a[i] = int(sv[-i - 1])
    for i in range(n, m):
        a[i] = 0
    return a


def parveide_mas_to_sv(a):
    # Transformē masīvu simbolu virknē pretējā secībā. Ja masīvā priekšā ir 0, tad tas tiek noņemtas
    # a - viendimensijas masīvs
    n = len(a)
    sv = ""
    for i in range(n):
        sv = str(a[i]) + sv

    try:  # try/except gadījumam ja a * 0, a - jebkurš skaitlis
        while sv[0] == "0":
            sv = sv[1:]
        return sv

    except IndexError:  # Tas ir nepieciešams gadījumam ja lietotājs ievadīs a *  0 = 0, a - jebkurš skaitlis
        return "0"  # bez šim rindām būtu kļūda, kad a * 0, a - jebkurš skaitlis


def reizinasana(a, b):
    # Sareizina masīvu a ar b izmantojot str. Jāizmanto lielo skaitļu (vismaz ar 50 cipariem) reizināšanai
    # a - viendimensijas masīvs
    # b - viendimensijas masīvs

    a = a[::-1]
    b = b[::-1]
    n1 = len(a)
    n2 = len(b)
    if n1 > n2:
        n = n1
    else:
        n = n2

    m1 = parveide_sv_to_mas(a, n)
    m2 = parveide_sv_to_mas(b, n)
    m3 = numpy.zeros(2 * n, dtype=numpy.int_)
    s = 0
    for j in range(2 * n - 1):
        for i in range(n):
            if (0 <= j - i) and (j - i <= n - 1):
                s = s + m1[i] * m2[j - i]
        m3[j] = s % 10
        s = s // 10
    m3[n * 2 - 1] = s

    return parveide_mas_to_sv(m3)


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


a = input("Ievadiet 1.reizinātāju ===> ")
while is_natural_or_zero_long(a) == False:
    a = input("Kļūda! Ievadītam skaitlim jābūt naturālam vai 0.\nIevadiet 1.reizinātāju ===> ")

a = parveide_sv_to_mas(a, len(a))


b = input("Ievadiet 2.reizinātāju ===> ")
while is_natural_or_zero_long(b) == False:
    b = input("Kļūda! Ievadītam skaitlim jābūt naturālam vai 0.\nIevadiet 1.reizinātāju ===> ")

b = parveide_sv_to_mas(b, len(b))


print("")
izvade_bez_komatiem_kopigi(a)
print("*")
izvade_bez_komatiem_kopigi(b)
print("=")
print(reizinasana(a, b))
