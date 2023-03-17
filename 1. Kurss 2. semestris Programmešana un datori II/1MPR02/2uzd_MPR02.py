# Programmas nosaukums: Kombinācijas
# 2. uzdevums (1MPR02_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas aprēķina C(n,m) izmantojot ciklu un rekursiju.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


def is_natural_or_zero(n):
    # Pārbauda vai simbolu virkne ir naturāls skaitlis vai nulle, vai nav.
    # Ja ir naturāls skaitlis vai nulle, tad True. Ja nav tad False.
    # n - simbolu virkne (str), kuru pārbauda.
    if str(n).isdigit() and float(n) == int(n) and int(n) >= 0:
        return True
    else:
        return False


def kombinacijas_cikls(n, m):
    # Aprēķina kombinācijas skaitu C(n,m) izmantojot ciklu. n >= m
    # n - naturāls skaitlis vai nulle (no cik) n ir "apakšā"
    # m - naturāls skaitlis vai nulle (pa cik) m ir "augšā"

        if m > n:
            return False

        elif m == 0 or m == n:
            return 1

        fn = 1
        for i in range(2, n + 1):
            fn = fn * i

        fm = 1
        for i in range(2, m + 1):
            fm = fm * i

        fnm = 1
        for i in range(2, n - m + 1):
            fnm = fnm * i

        return fn / fm / fnm


def kombinacijas_rekursija(n, m):
    # Aprēķina kombinācijas skaitu C(n,m) izmantojot rekursiju. n >= m
    # n - naturāls skaitlis vai nulle (no cik) n ir "apakšā"
    # m - naturāls skaitlis vai nulle (pa cik) m ir "augšā"
        if m > n:
            return False

        if m == 0 or m == n:
            return 1
        return kombinacijas_rekursija(n - 1, m - 1) + kombinacijas_rekursija(n - 1, m)


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


n = input("Ievadiet naturalo skaitli vai nulli!\nn ==> ")

if not is_natural_or_zero(n):
    print("Kļūda! Tika ievadīti nekorekti dati!")
    quit()

m = input("Ievadiet naturalo skaitli vai nulli!\nm ==> ")

if not is_natural_or_zero(m):
    print("Kļūda! Tika ievadīti nekorekti dati!")
    quit()

n = int(n)
m = int(m)

if kombinacijas_cikls(n, m) == False or kombinacijas_rekursija(n, m) == False:
    print("Kļūda! m < n")
else:
    print("C(" + str(n) + ", " + str(m) + ") = " + str(int(kombinacijas_cikls(n, m))) + " (ar ciklu)")
    print("C(" + str(n) + ", " + str(m) + ") = " + str(kombinacijas_rekursija(n, m)) + " (ar rekursiju)")
