# Programmas nosaukums: Klase trijstūris
# 3. uzdevums (1MPR11_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas izveido klasi Trijstūris, kas satur 3 laukus, kas glabā trijstūra malu garumus
# un metodes - laukums, perimetrs, ievilktā riņķa rādiuss un apvilktā riņķa rādiuss, izmantojot šo klasi
# izveidojiet objektus un nodrukājiet šo objektu laukumus, perimetrus un ievilktās un apvilktās riņķa rādiusus.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import math


class Trijsturis:
    # Trijstūra klase.
    def __init__(self, a, b, c):
        # Iniciālizē a, b, c.
        # a - trijstūra pirmās malas garums.
        # b - trijstūra otrais malas garums.
        # c - trijstūra trešais malas garums.
        # self - trijstūris.
        self.a = a
        self.b = b
        self.c = c

    def pusperimetrs(self):
        # Aprēķina trijstūra pusperimetru.
        p = (self.a + self.b + self.c) / 2
        return p

    def laukums(self):
        # Aprēķina trijstūra laukumu ar Herona formulu.
        p = Trijsturis.pusperimetrs(self)
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))  # math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))  # self.garums * self.platums

    def perimetrs(self):
        # Aprēķina trijstūra perimetru.
        return self.a + self.b + self.c

    def ievilkta_rinka_radiuss(self):
        # Aprēķina trijstūra ievilkta riņķa līnijas rādiusu r.
        return Trijsturis.laukums(self) / Trijsturis.pusperimetrs(self)  # regulāram r = (a*sqrt(3))/6

    def apvilkta_rinka_radiuss(self):
        # Aprēķina trijstūra apvilkta riņķa līnijas rādiusu R.
        return self.a * self.b * self.c / (4 * Trijsturis.laukums(self))  # regulāram R = (a*sqrt(3))/6


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
            if Check.is_real_positive(n):  # is_real(n):  # Check.(funkcija, kas pārbauda nepieciešamo)
                return float(n)
            print(error_desciption)
            n = input(description + "==> ")


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


a = Check.ievade("Ievadiet trijstūra pirmas malas garumu ", "Kļūda! Ievadītai vērtībai jābūt reālam pozitīvam skaitlim!")
b = Check.ievade("Ievadiet trijstūra otras malas garumu ", "Kļūda! Ievadītai vērtībai jābūt reālam pozitīvam skaitlim!")
c = Check.ievade("Ievadiet trijstūra trešas malas garumu ", "Kļūda! Ievadītai vērtībai jābūt reālam pozitīvam skaitlim!")

if Check.can_make_triangle(a, b, c):
    trijsturis = Trijsturis(a, b, c)
    print("\nJūs ievadījāt trijstūri ar malas garumiem " + str(a) + ", " + str(b) + ", " + str(c))
    print("\nTrijstūra perimetrs. P =", trijsturis.perimetrs())
    print("Trijstūra laukums. S =", trijsturis.laukums())
    print("Trijstūra ievilktas riņķa līnijas rādiuss. r =", trijsturis.ievilkta_rinka_radiuss())
    print("Trijstūra apvilktas riņķa līnijas rādiuss. R =", trijsturis.apvilkta_rinka_radiuss())
else:
    print("\nTrijstūris ar malam " + str(a) + ", " + str(b) + ", " + str(c) + " neeksistē!")


