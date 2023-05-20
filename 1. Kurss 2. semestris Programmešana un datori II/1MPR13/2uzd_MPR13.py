# Programmas nosaukums: Kompleksa skaitļi
# 2.uzdevums (1MPR13_Vladislavs_Babaņins)
# Uzdevuma formulējums: Sastādīt programmu, kas realizē pamatdarbības ar kompleksiem skaitļiem.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import math


class ComplexNumber:
    # Kompleksu skaitļu klase.
    def __init__(self, re=0, im=0):
        # Pēc noklusējuma izveido tukšu komplēksa skaitli (0 + 0i)
        # Ja ir norādots citādi, tad izveido tā, ka ievadīja lietotājs.
        self.re = re
        self.im = im

    def __repr__(self):
        # print()
        # Kompleksā skaitļu izvadīšanai lietotājam.
        if self.re != 0:  # Ja ir kāda reāla daļa, tad izvadam komplēkso skaitli ar realu daļu (neviss 0 + i*n)

            if self.im > 0 and self.im != 1:  # Ja imagināra daļa nav 1 un tā ir lielāka par 0, tad rakstām n + i, neviss n + k*i
                return f"{self.re} + {self.im}i"

            elif self.im == 1:  # Ja imagināra daļa ir 1, tad rakstām n + i, neviss n + 1*i
                return f"{self.re} + i"

            elif self.im == 0:  # Ja imagināra daļa ir 0, tad rakstām tikai reālu daļu n
                return f"{self.re}"

            elif self.im == -1:  # Ja imagināra daļa ir -1, tad rakstām n - i, neviss n - 1*i
                return f"{self.re} - i"

            else:  # Citā gadījumā rakstām n - k*i
                return f"{self.re} - {-self.im}i"

        else:  # Ja nav reālas daļas, tad nav jēgas rakstīt 0 + k*i, tad izvadam komplēkso skaitli tikai ar imagināru daļu k*i
            if self.im > 0 and self.im != 1:  # Ja imagināra daļa ir pozitīva un nav viens, tad izvadam k*i, neviss 0 + k*i
                return f"{self.im}i"

            elif self.im == 1:  # Ja imagināra daļa ir 1, tad izvadam i, neviss 0 + 1*i
                return "i"

            elif self.im == 0:  # Ja imagināra daļa ir 0, tad izvadam 0, neviss 0 + 0*i
                return "0"

            elif self.im == -1:  # Ja imagināra daļa ir 1, tad izvadam -i, neviss 0 - 1*i
                return "-i"

            else:  # Citādi izvādam -k*i (nav realas daļas un imagināra daļa ir negatīva un nav -1)
                return f"-{-self.im}i"

    def arg(self):
        # Atgriež komplēksa skaitļa argumentu.
        return math.atan2(self.im, self.re)

    def __add__(self, other):
        # +
        # Atgriež komplēksa skaitļa summu (self + other).
        real_sum = self.re + other.re
        imaginary_sum = self.im + other.im
        return ComplexNumber(real_sum, imaginary_sum)

    def __iadd__(self, other):
        # +=
        # Atgriež komplēksa skaitļa summu (self + other), bet kā __iadd__ (+=).
        # Atgriež jau eksistējošu mainīgu, neviss izveido jaunu mainīgu.
        self.re += other.re
        self.im += other.im
        return self

    def __sub__(self, other):
        # -
        # Atgriež komplēksa skaitļa starpību (self - other).
        real_diff = self.re - other.re
        imaginary_diff = self.im - other.im
        return ComplexNumber(real_diff, imaginary_diff)

    def __isub__(self, other):
        # -=
        # Atgriež komplēksa skaitļa summu (self - other), bet kā __isub__ (-=).
        # Atgriež jau eksistējošu mainīgu, neviss izveido jaunu mainīgu.
        self.re -= other.re
        self.im -= other.im
        return self

    def __mul__(self, other):
        # *
        # Atgriež komplēksa skaitļa reizinājumu (self * other).
        real_product = (self.re * other.re) - (self.im * other.im)
        imaginary_product = (self.re * other.im) + (self.im * other.re)
        return ComplexNumber(real_product, imaginary_product)

    def __imul__(self, other):
        # *=
        # Atgriež komplēksa skaitļa reizinājumu (self * other) bet kā __imul__ (*=).
        # Atgriež jau eksistējošu mainīgu, neviss izveido jaunu mainīgu.
        re1 = self.re
        im1 = self.im
        self.re = (re1 * other.re) - (im1 * other.im)
        self.im = (re1 * other.im) + (im1 * other.re)
        return self

    def __truediv__(self, other):
        # /
        # Atgriež komplēksa skaitļa dalījumu (self / other).
        denominator = (other.re * other.re) + (other.im * other.im)
        real_quotient = ((self.re * other.re) + (self.im * other.im)) / denominator
        imaginary_quotient = ((self.im * other.re) - (self.re * other.im)) / denominator
        return ComplexNumber(real_quotient, imaginary_quotient)

    def __itruediv__(self, other):
        # /=
        # Atgriež komplēksa skaitļa dalījumu (self / other) bet kā __itruediv__ (/=).
        # Atgriež jau eksistējošu mainīgu, neviss izveido jaunu mainīgu.
        denominator = (other.re ** 2) + (other.im ** 2)
        real_quotient = ((self.re * other.re) + (self.im * other.im)) / denominator
        imaginary_quotient = ((self.im * other.re) - (self.re * other.im)) / denominator
        self.re = real_quotient
        self.im = imaginary_quotient
        return self

    def __abs__(self):
        # Atgriež komplēksa skaitļa moduli.
        return math.sqrt(self.re * self.re + self.im * self.im)

    def conjugate(self):
        # Atgriež komplēksa skaitļas komplēksa saistīto skaitli.
        return ComplexNumber(self.re, -self.im)

    def __pow__(self, power):
        # Atgriež komplēksa skaitļi, kurš tika pacēlts naturāla pakāpe.
        modulus = self.__abs__() ** power
        arg = power * self.arg()
        re = modulus * math.cos(arg)
        im = modulus * math.sin(arg)
        return ComplexNumber(re, im)

    def complex_power(z, n):
        # Atgriež komplēksa skaitļi, kurš tika pacēlts pakāpe.
        r = math.sqrt(z.re**2 + z.im**2)
        theta = math.atan2(z.im, z.re)
        re = r ** n * math.cos(n * theta)
        im_part = r ** n * math.sin(n * theta)
        return ComplexNumber(re, im_part)

    def n_roots(self, n):
        # Atgriež sarakstu, ar visiem komplēksa skaitļa saknēm.
        # n - kuru sakni gribām izvilkt
        roots = []
        modulus = abs(self)
        arg = self.arg()
        for k in range(n):
            root_argument = (arg + 2 * k * math.pi) / n
            re = modulus * math.cos(root_argument)
            im_part = modulus * math.sin(root_argument)
            roots.append(ComplexNumber(re, im_part))
        return roots

    def trigonometric_form(self):
        # Izvadīt lietotājam komplēksu skaitli trigonometriskajā formā.
        r = abs(self)
        theta = self.arg()
        return f"{r:.2f}(cos({theta:.2f}) + isin({theta:.2f}))"

    def exponent_form(self):
        # Izvadīt lietotājam komplēksu skaitli eksponenciāla formā.
        modulus = abs(self)
        arg = self.arg()
        return f"{modulus} * e^({arg}i)"


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


print("Operācijas ar komplēksa skaitliem:")
num1 = ComplexNumber(-1, -4)
num2 = ComplexNumber(1, 3)
# print(num1 + num4)
print("(" + str(num1) + ") + (" + str(num2) + ") = " + str(num1 + num2))


num1 = ComplexNumber(-1, 4)
num2 = ComplexNumber(1, -3)
# print(num1 + num4)
print("(" + str(num1) + ") + (" + str(num2) + ") = " + str(num1 + num2))


num1 = ComplexNumber(2, 4)
num2 = ComplexNumber(1, -3)
# print(num1 + num4)
print("(" + str(num1) + ") + (" + str(num2) + ") = " + str(num1 + num2))


num1 = ComplexNumber(-1, -4)
num2 = ComplexNumber(-1, 3)
# print(num1 + num4)
print("(" + str(num1) + ") + (" + str(num2) + ") = " + str(num1 + num2))


num3 = ComplexNumber(19, 15)
num4 = ComplexNumber(19, 15)
# print(num3 - num4)
print("(" + str(num3) + ") - (" + str(num4) + ") = " + str(num3 - num4))


# print(num1 / num2)
# print(num3 / num4)
print("(" + str(num1) + ") / (" + str(num2) + ") = " + str(num1 / num2))
print("(" + str(num3) + ") / (" + str(num4) + ") = " + str(num3 / num4))


# print(num1 * num2)
# print(num3 * num4)
print("(" + str(num1) + ") * (" + str(num2) + ") = " + str(num1 * num2))
print("(" + str(num3) + ") * (" + str(num4) + ") = " + str(num3 * num4))


# print(abs(num1))
# print(abs(num3))
print("|" + str(num1) + "| = " + str(abs(num1)))
print("|" + str(num3) + "| = " + str(abs(num3)))


# print(conjugate(num1))
# print(conjugate(num3))
print("conj(" + str(num1) + ") = " + str(ComplexNumber.conjugate(num1)))
print("conj(" + str(num3) + ") = " + str(ComplexNumber.conjugate(num3)) + "\n")


num5 = ComplexNumber(2, 4)
num6 = ComplexNumber(3, 6)
numiadd = ComplexNumber(3, 6)
numiadd1 = ComplexNumber(3, 6)

numiadd += num5
print("Izmantojot __iadd__:")
print("(" + str(numiadd1) + ") + (" + str(num5) + ") = " + str(numiadd) + "\n")

print("Izmantojot __add__:")
num_add = num5 + num6
print("(" + str(num5) + ") + (" + str(num6) + ") = " + str(num_add) + "\n")


numisub = ComplexNumber(3, 6)
numisub1 = ComplexNumber(3, 6)
numisub -= num5

print("Izmantojot __isub__:")
print("(" + str(numisub1) + ") - (" + str(num5) + ") = " + str(numisub) + "\n")


numisub = ComplexNumber(3, 6)
numisub1 = ComplexNumber(3, 6)
numisub = numisub1 - num5

print("Izmantojot __sub__:")
print("(" + str(numisub1) + ") - (" + str(num5) + ") = " + str(numisub) + "\n")


num7 = ComplexNumber(0.5, math.sqrt(3) / 2)
num8 = ComplexNumber(5, 5)
power1 = 20
print("Komplēksa skaitļa pakāpe:")
print("(" + str(num7) + ") ** " + str(power1) + " = " + str(num7 ** 20) + "\n")


z = ComplexNumber(3, 4)
z_cubed = ComplexNumber.complex_power(z, 3)
print("Komplēksa skaitļa pakāpe:")
print("(" + str(z) + ") ** " + str(3) + " = " + str(z_cubed) + "\n")


b = ComplexNumber(0.5, math.sqrt(3) / 2)
print("Komplēksa skaitļa saknes:")
print("sqrt(" + str(b) + ") = " + str(ComplexNumber.n_roots(b, 2)) + "\n")


b = ComplexNumber(0.5, math.sqrt(3) / 2)
print("Komplēksa skaitļa saknes:")
print("sqrt(" + str(b) + ") = " + str(ComplexNumber.n_roots(b, 4)) + "\n")


c = ComplexNumber(1, 1)
print("Komplēksa saistītajs:")
print("conj(" + str(c) + ") = " + str(ComplexNumber.conjugate(c)) + "\n")


d = ComplexNumber(-1, 1)
print("Pārveidot trigonometriskā formā:")
print("(" + str(d) + ") = " + str(ComplexNumber.trigonometric_form(d)) + "\n")


print("Pārveidot eksponenciālā formā:")
t = ComplexNumber(1, math.sqrt(3) / 3)
print("(" + str(t) + ") = " + str(ComplexNumber.exponent_form(t)) + "\n")


t = ComplexNumber(1, math.sqrt(3) / 3)
print("Komplēksa skaitļa arguments:")
print("arg(" + str(t) + ") = " + str(ComplexNumber.arg(t)) + "\n")


k = ComplexNumber(1, 2)
print("Komplēksa skaitļa izvadīšana (print):")
print(k)
print()


num5 = ComplexNumber(2, 4)
numimul = ComplexNumber(3, 6)
numimul1 = ComplexNumber(3, 6)

numimul *= num5
print("Izmantojot __imul__:")
print("(" + str(numimul1) + ") * (" + str(num5) + ") = " + str(numimul) + "\n")


num5 = ComplexNumber(2, 4)
numimul = ComplexNumber(3, 6)
numimul1 = ComplexNumber(3, 6)

numimul1 = numimul * num5
print("Izmantojot __mul__:")
print("(" + str(numimul) + ") * (" + str(num5) + ") = " + str(numimul1) + "\n")


num5 = ComplexNumber(2, 4)
numidiv = ComplexNumber(3, 6)
numidiv1 = ComplexNumber(3, 6)

numidiv /= num5
print("Izmantojot __itruediv__:")
print("(" + str(numidiv1) + ") / (" + str(num5) + ") = " + str(numidiv) + "\n")


num5 = ComplexNumber(2, 4)
numidiv = ComplexNumber(3, 6)
numidiv1 = ComplexNumber(3, 6)

numidiv1 = numidiv / num5
print("Izmantojot __truediv__:")
print("(" + str(numimul) + ") / (" + str(num5) + ") = " + str(numidiv1) + "\n")


print("Jaunais komplēksa skaitlis:")
new_num = ComplexNumber()
print(new_num)
