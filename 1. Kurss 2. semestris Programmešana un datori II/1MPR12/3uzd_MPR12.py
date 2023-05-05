# Programmas nosaukums: Dažādu figuru apkārtmērs un laukums ar polimorfismu.
# 3. uzdevums (1MPR12_Vladislavs_Babaņins)
# Uzdevuma formulējums: Uzdevums par polimorfismu. Jums jāizveido programma, kas ļauj izveidot dažādas figūras un nosaka tās apkārtmēru un laukumu.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import math


class Taisnsturis:
    # Taisnstūris.
    def __init__(self, garums, platums):
        self.garums = garums
        self.platums = platums

    def perimetrs(self):
        # Aprēķina taisnstūra perimetru.
        return (self.garums + self.platums) * 2

    def laukums(self):
        # Aprēķina taisnstūra laukumu.
        return self.garums * self.platums


class Regular_pentagon:
    # Regulārs piecstūris.
    def __init__(self, side_length):
        self.side_length = side_length

    def perimetrs(self):
        # Aprēķina regulāra piecstūra perimetru.
        return 5 * self.side_length

    def laukums(self):
        # Aprēķina regulāra piecstūra laukumu.
        return ((math.sqrt(5) * math.sqrt(5 + 2 * math.sqrt(5))) / 4) * (self.side_length * self.side_length)
        # Formulas avots:
        # https://en.wikipedia.org/wiki/Pentagon


class Regular_hexagon:
    # Regulārs sešstūris.
    def __init__(self, side_length):
        self.side_length = side_length

    def perimetrs(self):
        # Aprēķina regulāra sešstūra perimetru.
        return 6 * self.side_length

    def laukums(self):
        # Aprēķina regulāra sešstūra laukumu.
        return (3 * math.sqrt(3) / 2) * (self.side_length * self.side_length)


class Regular_polygon:
    # Regulārs n-stūris.
    def __init__(self, side_length, num_sides):
        # num_sides - n-stūra malu skaits (vai leņķu skaits) n-stūra n skaitlis.
        # side_lenght - vienas malas garums.
        self.side_length = side_length
        self.num_sides = num_sides

    def perimetrs(self):
        # Aprēķina regulāra n-stūra perimetru.
        return self.num_sides * self.side_length

    def laukums(self):
        # Aprēķina regulāra n-stūra laukumu.
        return 0.25 * self.num_sides * self.side_length * self.side_length / math.tan(math.pi / self.num_sides)
        # Formulas avots:
        # https://en.wikipedia.org/wiki/Regular_polygon


class Trapece:
    def __init__(self, a, b, c, d):
        # Iniciālizē a, b, c, d.
        # a - trapeces pirmās malas garums.
        # b - trapeces otrais malas garums.
        # c - trapeces trešais malas garums.
        # d - trapeces trešais malas garums.
        # self - trapece.
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimetrs(self):
        # Aprēķina trijstūra perimetru.
        return self.a + self.b + self.c + self.d

    def laukums(self):
        # Aprēķina trapeces laukumu
        d = self.b - self.a
        k = (d * d + self.c * self.c - self.d * self.d) / (2 * self.c * d)
        k = k * k
        t = 1 - k
        m = math.sqrt(t)
        p = ((self.a + self.b) / 2) * self.c
        return p * m
        # Laukuma formulas avots:
        # https://math.stackexchange.com/questions/2637690/is-there-a-formula-to-calculate-the-area-of-a-trapezoid-knowing-the-length-of-al


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


class Rinkis:
    def __init__(self, radiuss):
        self.radiuss = radiuss

    def perimetrs(self):
        # Aprēķina riņķa līnijas perimetru (riņķa līnijas garumu) ar formulu pi*r*r = pi*r^2.
        return 6.283 * self.radiuss  # 2*pi*r

    def laukums(self):
        # Aprēķina riņķa līnijas laukumu ar formulu pi*r*r = pi*r^2.
        return 3.1415 * self.radiuss * self.radiuss  # pi*r*r = pi*r^2


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


def izdrukat_laukumu(figura):
    print("Šīs figūras laukums ir:", figura.laukums())


def izdrukat_perimetru(figura):
    print("Šīs figūras perimetrs ir:", figura.perimetrs())


f1 = Rinkis(1)
f2 = Taisnsturis(1, 2)
f3 = Trijsturis(1, 1, 1)
f4 = Trapece(11, 6.403, 5.385, 5)
f5 = Regular_pentagon(1)
f6 = Regular_hexagon(1)
f7 = Regular_polygon(1, 8)
f8 = Regular_polygon(1, 3)
f9 = Regular_polygon(1, 10)
f10 = Regular_polygon(1, 4)

print("Riņķis ar rādiusu 1:")
izdrukat_perimetru(f1)
izdrukat_laukumu(f1)
print()

print("Taisnstūris(1,2):")
izdrukat_perimetru(f2)
izdrukat_laukumu(f2)
print()

print("Trijsturis(1, 1, 1):")
izdrukat_perimetru(f3)
izdrukat_laukumu(f3)
print()

print("Trapece(11, 6,403, 5,385, 5):")
izdrukat_perimetru(f4)
izdrukat_laukumu(f4)
print()

print("Regulārs piecstūris(1):")
izdrukat_perimetru(f5)
izdrukat_laukumu(f5)
print()

print("Regulārs sešstūris(1):")
izdrukat_perimetru(f6)
izdrukat_laukumu(f6)
print()

print("Regulārs 8-stūris(1):")
izdrukat_perimetru(f7)
izdrukat_laukumu(f7)
print()

print("Regulārs 3-stūris(1):")
izdrukat_perimetru(f8)
izdrukat_laukumu(f8)
print()

print("Regulārs 10-stūris(1):")
izdrukat_perimetru(f9)
izdrukat_laukumu(f9)
print()

print("Regulārs 4-stūris(1):")
izdrukat_perimetru(f10)
izdrukat_laukumu(f10)
print()
