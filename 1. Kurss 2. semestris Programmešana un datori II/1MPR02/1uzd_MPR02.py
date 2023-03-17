# Programmas nosaukums: Faktorials
# 1. uzdevums (1MPR02_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas aprēķina N! divos veidos - izmantojot ciklu un rekursiju.
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


def factorial_cikls(n):
    # Aprēķina n faktoriāla vērtību izmantojot ciklu.
    # ja ir naturāls skaitlis vai nulle, tad return n!
    # ja nav naturāls skaitlis vai nulle, tad return False.
    # n - simbolu virkne (str).
    if is_natural_or_zero(n):
        n = int(n)
        a = 1
        while n >= 1:
            a = a * n
            n = n - 1
        return a
    else:
        return False


def factorial_rekursija(n):
    # Aprēķina n faktoriāla vērtību izmantojot rekursiju.
    # ja ir naturāls skaitlis vai nulle tad return n!
    # ja nav naturāls skaitlis vai nulle tad return False.
    # n - simbolu virkne (str).

    if is_natural_or_zero(n): # pārbauda vai ir naturāls skaitlis vai nulle, ja nav tad return False
        n = int(n)
        if n >= 0:
            if n == 0:
                return 1
            return factorial_rekursija(n - 1) * n
        else:
            return False
    else:
        return False


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


n = input("Ievadiet naturālu skaitli vai nulli!\nN ==> ")
while factorial_cikls(n) == False or factorial_rekursija(n) == False:
    n = input("Kļūda! Tas nav naturāls skaitlis vai nulle.\nIevadiet naturālu skaitli vai nulli!\nN ==> ")
print(n + "! = " + str(factorial_cikls(n)) + " (ar ciklu)")
print(n + "! = " + str(factorial_rekursija(n)) + " (ar rekursiju)")
