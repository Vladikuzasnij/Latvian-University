# Programmas nosaukums: Kalkulators
# 4. uzdevums (1MPR11_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas izveido klasi Kalkulators, kas satur 4 statiskās metodes četru aritmētisko darbību veikšanai.
# Ievadiet 2 skaitļus un veiciet ar tiem 4 aritmētiskās darbības, izmantojot iepriekš izveidotās klases statiskās metodes.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


class Kalkulators:
    # Kalkulatora klase

    @staticmethod
    def saskaitit(a, b):
        # Saskaita a un b
        # a - float skaitlis
        # b - float skaitlis
        return a + b

    @staticmethod
    def atnemt(a, b):
        # Atņem a un b
        # a - float skaitlis
        # b - float skaitlis
        return a - b

    @staticmethod
    def reizinat(a, b):
        # Sareizina a un b
        # a - float skaitlis
        # b - float skaitlis
        return a * b

    @staticmethod
    def dalit(a, b):
        # Izdala a ar b
        # a - float skaitlis
        # b - float skaitlis
        if a == 0 and b == 0:
            return "Nav definēts"
        if a != 0 and b == 0:
            return "Nedrīkst dalīt ar 0"
        return a / b


class Check:
    # Klase ar visam funkcijam, kuri ir noderīgi ievaddates pārbaudei.

    @staticmethod
    def is_real(value):
        # Pārbauda vai simbolu virkne (value) ir reāls skaitlis no (-inf, +inf).
        # value - str, simbolu virkne, kurā reprezente skaitļi.
        try:
            float(value)
            return True
        except:
            return False

    @staticmethod
    def is_real_positive(value):
        # Pārbauda vai simbolu virkne (value) ir reāls pozitīvs skaitlis no (0, +inf).
        # value - str, simbolu virkne, kurā reprezente skaitļi.
        try:
            value = float(value)
            if value > 0:
                return True
            else:
                return False
            return True
        except:
            return False

    @staticmethod
    def is_real_positive_or_zero(value):
        # Pārbauda vai simbolu virkne (value) ir reāls pozitīvs skaitlis vai nulle [0, +inf).
        # value - str, simbolu virkne, kurā reprezente skaitļi.
        try:
            value = float(value)
            if value >= 0:
                return True
            else:
                return False
            return True
        except:
            return False

    @staticmethod
    def is_natural(value):
        # Pārbauda vai simbolu virkne (value) ir naturāls skaitlis 1, 2, 3, 4, 5, ...
        # value - str, simbolu virkne, kurā reprezente skaitļi.
        try:
            value = int(value)
            if value > 0:
                return True
            else:
                return False
        except:
            return False

    @staticmethod
    def is_whole(value):
        # Pārbauda vai simbolu virkne (value) ir vesels skaitlis ... -3, -2, -1, 0, 1, 2, 3 ...
        # value - str, simbolu virkne, kurā reprezente skaitļi.
        try:
            value = int(value)
            if value >= 0:
                return True
            else:
                return False
        except:
            return False

    @staticmethod
    def is_even(x):
        # Pārbauda vai simbolu virkne (value) ir pāra skaitlis 2n.
        # x - str, simbolu virkne, kurā reprezente skaitļi.
        try:
            x = int(x)
            if x % 2 == 0:
                return True
            else:
                return False
        except:
            return False

    @staticmethod
    def is_odd(x):
        # Pārbauda vai simbolu virkne (value) ir nepāra skaitlis 2n + 1.
        # x - str, simbolu virkne, kurā reprezente skaitļi.
        try:
            x = int(x)
            if x % 2 != 0:
                return True
            else:
                return False
        except:
            return False

    @staticmethod
    def is_prime(n):
        # Pārbauda vai simbolu virkne (value) ir pirmskaitlis.
        # n - str, simbolu virkne, kurā reprezente skaitļi.
        try:
            n = int(n)
        except:
            return False
        else:
            if n <= 1:
                return False
            for i in range(2, n):
                if (n % i) == 0:
                    return False
            return True

    @staticmethod
    def can_make_triangle(a, b, c):
        # Pārbauda vai no šiem skaitļiem var izveidot trijstūri.
        # a - float skaitlis intervāla (0, +inf)
        # b - float skaitlis intervāla (0, +inf)
        # c - float skaitlis intervāla (0, +inf)
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            return False
        else:
            return True

    def ievade(description, error_desciption):
        # Metode skaitļa ievādei. Jāizmanto tāda veidā: n = Check.ievade("Ievadiet --- ", "Kļūda! ---") (nevajag rakstīt ==>).
        # description - str, simbolu virkne, kurā tiek parādīta, kad tiek paprasīts ievādit skaitļi.
        # error_desciption - str, simbolu virkne, kurā tiek parādīta, kad tiek paziņota kļūda.
        n = input(description + "==> ")
        while True:
            if Check.is_real(n):  # is_real(n):  # Check.(funkcija, kas pārbauda nepieciešamo)
                return float(n)
            print(error_desciption)
            n = input(description + "==> ")


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


a = Check.ievade("Ievadiet pirmo skaitļi ", "Kļūda! Ievadītai vērtībai jābūt reālam skaitlim!")
b = Check.ievade("Ievadiet otro skaitļi ", "Kļūda! Ievadītai vērtībai jābūt reālam skaitlim!")

iekava1_l = ""
iekava1_r = ""

iekava2_l = ""
iekava2_r = ""

if a < 0:
    iekava1_l = "("
    iekava1_r = ")"
if b < 0:
    iekava2_l = "("
    iekava2_r = ")"

print()
print(iekava1_l + str(a) + iekava1_r + " + " + iekava2_l + str(b) + iekava2_r + " =", Kalkulators.saskaitit(a, b))
print(iekava1_l + str(a) + iekava1_r + " - " + iekava2_l + str(b) + iekava2_r + " =", Kalkulators.atnemt(a, b))
print(iekava1_l + str(a) + iekava1_r + " * " + iekava2_l + str(b) + iekava2_r + " =", Kalkulators.reizinat(a, b))

if Kalkulators.dalit(a, b) == "Nav definēts" or Kalkulators.dalit(a, b) == "Nedrīkst dalīt ar 0":
    sym = ""
else:
    sym = " ="

print(iekava1_l + str(a) + iekava1_r + " : " + iekava2_l + str(b) + iekava2_r + sym, Kalkulators.dalit(a, b))
