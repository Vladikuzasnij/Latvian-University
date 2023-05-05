# Programmas nosaukums: Klase taisnstūris
# 2. uzdevums (1MPR11_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas izveido klasi Taisnstūris, kas satur laukus - garums un platums
# un metodes - laukums un perimetrs. Izmantojot šo klasi izveidojiet objektus un nodrukājiet šo objektu laukumus un perimetrus.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


class Taisnsturis:
    # Klase taisnstūra laukuma un perimetra aprēķināšanos.
    def __init__(self, garums, platums):
        self.garums = garums
        self.platums = platums

    def laukums(self):
        # Aprēķina taisnstūra laukumu, reizinot tā garumu ar tā platumu.
        return self.garums * self.platums

    def perimetrs(self):
        # Aprēķina taisnstūra perimetru, saskaitot garumu un platumu un reizinot ar 2.
        return (self.garums + self.platums) * 2


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

    def ievade(description, error_desciption):
        # Metode skaitļa ievādei. Jāizmanto tāda veidā: n = Check.ievade("Ievadiet --- ", "Kļūda! ---") (nevajag rakstīt ==>).
        # description - str, simbolu virkne, kurā tiek parādīta, kad tiek paprasīts ievādit skaitļi.
        # error_desciption - str, simbolu virkne, kurā tiek parādīta, kad tiek paziņota kļūda.
        n = input(description + "==> ")
        while True:
            if Check.is_real_positive(n):  # is_real(n):  # Check.(funkcija, kas pārbauda nepieciešamo)
                return float(n)
            print(error_desciption)
            n = input(description + "==> ")


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


n = Check.ievade("Ievadiet taisnstūra garumu ", "Kļūda! Ievadītai vērtībai jābūt reālam pozitīvam skaitlim!")
m = Check.ievade("Ievadiet taisnstūra platumu ", "Kļūda! Ievadītai vērtībai jābūt reālam pozitīvam skaitlim!")

taisnsturis = Taisnsturis(n, m)

print("\nTaisnstūra perimetrs. P =", taisnsturis.perimetrs())
print("Taisnstūra laukums. S =", taisnsturis.laukums())

