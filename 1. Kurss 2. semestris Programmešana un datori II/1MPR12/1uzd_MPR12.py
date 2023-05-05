# Programmas nosaukums: Klase "Kopa"
# 1. uzdevums (1MPR12_Vladislavs_Babaņins)
# Uzdevuma formulējums: Izveidot vienu vai vairākas klases, kas neizmantojot Python iebūvēto datu struktūru kopa (set),
# bet izmanto kādu citu datu struktūru, piemēram, saraksts vai masīvs, realizē kopu izveidi un tipiskākās darbības ar tām.
# Skat. lekcijas konspektu par kopām.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


import copy
import random


class Kopa:
    # Klase kopa.
    def __init__(self):
        # Inicializēsim tukšo kopu.
        # self - kopa (objekts Kopa()).

        self.__kopa = []

    def saturs(self):
        # Atgriež kopas saturu.
        # self - kopa (objekts Kopa()).

        return self.__kopa

    def izdrukat(self):
        # Izdrukā glīta veidā kopas saturu.
        # Tukša kopa tiek attēlota ar Ø simbolu.
        # Piemēram, izdrūka { 1 2 3 }.
        # self - kopa (objekts Kopa()).

        sk = len(self.__kopa)
        if sk == 0:
            sv = "Ø"  # Tukša kopa ∅
        else:
            sv = "{ "
            for i in self.__kopa:
                sv = sv + str(i) + " "
            sv = sv + "}"
        print(sv)

    def pievienot(self, elements):
        # Ļauj pievienot vai nu vienu elementu kopai, vai nu elementus kā list (sarakstu), vai tuple (kortežu).
        # Piemēram, a.pievienot([1, 3, 4]), vai b.pievienot((1, 2, 3)), vai c.pievienot(2).
        # self - kopa (objekts Kopa()).
        # elements - elements vai elementi, kurus gribam pievienot kopai.

        if type(elements) == list:
            for el in elements:
                if el not in self.__kopa:
                    self.__kopa.append(el)

        elif type(elements) == tuple:
            for el in elements:
                if el not in self.__kopa:
                    self.__kopa.append(el)
        else:
            paz = True
            for i in self.__kopa:
                if i == elements:
                    paz = False
            if paz:
                self.__kopa.append(elements)

    def izmest(self, elements):
        # Nodzēs norādītu vienu elementu (elements) no kopas.
        # Ja tāda elementa nav, tad neko nenodzēs.
        # Līdzīgs set discard.
        # self - kopa (objekts Kopa()).
        # elements - elements vai elementi, kurus gribam pievienot kopai.

        for i in self.__kopa:
            if i == elements:
                self.__kopa.remove(elements)

    def nonemt(self, elements):
        # Nodzēs norādītu vienu elementu (elements) no kopas.
        # Ja tāda elementa nav, tad raise ValueError, ka tāds elements nav kopā.
        # Līdzīgs set remove.
        # self - kopa (objekts Kopa()).
        # elements - elements vai elementi, kurus gribam pievienot kopai.

        if elements not in self.__kopa:
            raise ValueError(f"{elements} nav kopā. Nevar noņemt elementu, kuru nav. Izmantojiet 'izmest'.")  # is not in the kopa

        for i in self.__kopa:
            if i == elements:
                self.__kopa.remove(elements)

    def vai_pieder(self, elements):
        # Pārbauda vai kopai piedēr norādītais elements.
        # Atgriež True, ja norādītais elements piedēr kopai.
        # Atgriež False, ja norādītais elements nepiedēr kopai.
        # self - kopa (objekts Kopa()).
        # elements - elements vai elementi, kurus gribam pievienot kopai.

        for i in self.__kopa:
            if i == elements:
                return True
        return False

    def izdzest(self):
        # Pārverš kopu par tukšo kopu un atgriež to.
        # self - kopa (objekts Kopa()).

        self.__kopa = []
        return self.__kopa

    def atjaunot(self, elements):
        # Vai pārmainīt visas vērtības kopai.
        # Piemēram, a.update([4, 5, 6, 7]).
        # Atjauno kopu līdzīgi, ka set update.
        # self - kopa (objekts Kopa()).
        # elements - elements vai elementi, kurus gribam pievienot kopai.

        self.__kopa = []

        if type(elements) == list:
            for el in elements:
                if el not in self.__kopa:
                    self.__kopa.append(el)

        elif type(elements) == tuple:
            for el in elements:
                if el not in self.__kopa:
                    self.__kopa.append(el)
        else:
            paz = True
            for i in self.__kopa:
                if i == elements:
                    paz = False
            if paz:
                self.__kopa.append(elements)

    def pop(self):
        # Atgriež vienu nejaušu elementu no kopas.
        # Paņem nejaušu kopas elementu līdzīgi, ka set pop.
        # Ja mēģināsim izņemt nejaušu elementu no tukšas kopas, tad print("Kļūda! Nevar izņemt elementu no tukšas kopas.").
        # self - kopa (objekts Kopa()).

        try:
            a = random.choice(self.__kopa)
        except:
            print("Kļūda! Nevar izņemt elementu no tukšas kopas.")  # Raise Exception
        else:
            self.__kopa.remove(a)
            return a

    @staticmethod
    def apvienot(a, b):
        # Apvieno divas kopas a un b.
        # A U B
        # a - 1.kopa (objekts Kopa()).
        # b - 2.kopa (objekts Kopa()).

        c = copy.deepcopy(a)
        x = a.saturs()
        y = b.saturs()
        for i in y:
            if i not in x:
                c.pievienot(i)
        return c

    # Var izmantot arī šo metodi, "apvienot1" nevis "apvienot".
    # Metode "apvienot1" neizmanto deepcopy.
    '''
    def apvienot1(a, b): # tas pats, bet bez deepcopy
        c = Kopa()
        x = a.saturs()
        y = b.saturs()
        for z in x:
            c.pievienot(z)
        for z in y:
            if z not in x:
                c.pievienot(z)
                
        return c
    '''

    @staticmethod
    def vai_parklajas(a, b):
        # Pārbauda vai divas kopas a un b pārklājas.
        # Atgriež True, ja kopas pārklājas (ir vismaz viens kopīgs elements).
        # Atgriež False, ja kopas nepārklājas (nav nevienā kopīga elementa).
        # a - 1.kopa (objekts Kopa()).
        # b - 2.kopa (objekts Kopa()).

        c = Kopa()
        x = a.saturs()
        y = b.saturs()
        tuksa_kopa = Kopa()

        d = c.skelums(a, b)
        if Kopa.vai_vienadas(d, tuksa_kopa):
            return False
        return True

    @staticmethod
    def vai_neparklajas(a, b):
        # Pārbauda vai divas kopas a un b nepārklājas (tas pats kā vai_parklajas, bet tikai negācija).
        # Atgriež False, ja kopas pārklājas (ir vismaz viens kopīgs elements).
        # Atgriež True, ja kopas nepārklājas (nav nevienā kopīga elementa).
        # a - 1.kopa (objekts Kopa()).
        # b - 2.kopa (objekts Kopa()).

        c = Kopa()
        x = a.saturs()
        y = b.saturs()
        tuksa_kopa = Kopa()

        d = c.skelums(a, b)
        if Kopa.vai_vienadas(d, tuksa_kopa):
            return True
        return False

    @staticmethod
    def skelums(a, b):
        # Atgriež kopas a un b šķēlumu (A ∩ B).
        # a - 1.kopa (objekts Kopa()).
        # b - 2.kopa (objekts Kopa()).

        c = Kopa()
        x = a.saturs()
        y = b.saturs()
        for i in x:
            if i in y:
                c.pievienot(i)
        return c

    @staticmethod
    def simetriska_starpiba(a, b):
        # Atgriež kopas a un b simetrisku starpību (A △ B).
        # Pēc formulas: A △ B = (A \ B) U (B \ A).
        # a - 1.kopa (objekts Kopa()).
        # b - 2.kopa (objekts Kopa()).

        c = Kopa()
        d = Kopa.starpiba(a, b)
        f = Kopa.starpiba(b, a)
        c = Kopa.apvienot(d, f)
        return c

    @staticmethod
    def starpiba(a, b):
        # Atgriež kopas a un b starpību (A \ B).
        # a - 1.kopa (objekts Kopa()).
        # b - 2.kopa (objekts Kopa()).

        c = Kopa()
        x = a.saturs()
        y = b.saturs()
        for i in x:
            if i not in y:
                c.pievienot(i)
        return c

    @staticmethod
    def vai_vienadas(a, b):
        # Pārbauda vai divas kopas a un b ir vienādas (A == B).
        # Atgriež True, ja divas kopas ir vienādas.
        # Atgriež False, ja divas kopas nav vienādas.
        # a - 1.kopa (objekts Kopa()).
        # b - 2.kopa (objekts Kopa()).

        x = a.saturs()
        y = b.saturs()
        for i in x:
            if i not in y:
                return False

        for i in y:
            if i not in x:
                return False

        return True

    @staticmethod
    def vai_nav_vienadas(a, b):
        # Pārbauda vai divas kopas a un b nav vienādas (A != B).
        # Atgriež True, ja divas kopas nav vienādas.
        # Atgriež False, ja divas kopas ir vienādas.
        # a - 1.kopa (objekts Kopa()).
        # b - 2.kopa (objekts Kopa()).

        x = a.saturs()
        y = b.saturs()
        for i in x:
            if i not in y:
                return True

        for i in x:
            if i not in y:
                return True

        return False

    @staticmethod
    def vai_apakskopa(a, b):
        # Pārbauda vai a ir apakškopa b. A ⊆ B.
        # Atgriež True, ja a ir apakškopa b.
        # Atgriež False, ja a nav apakškopa b.
        # a - 1.kopa (objekts Kopa()).
        # b - 2.kopa (objekts Kopa()).

        x = a.saturs()
        y = b.saturs()
        for i in x:
            if i not in y:
                return False
        return True

    @staticmethod
    def vai_stingra_apakskopa(a, b):
        # Pārbauda vai a ir stingra apakškopa b. A ⊂ B. (ja A un B ir vienādas kopas, tad A nav stingra apakškopa B).
        # Atgriež True, ja a ir stingra apakškopa b.
        # Atgriež False, ja a nav stingra apakškopa b.
        # a - 1.kopa (objekts Kopa()).
        # b - 2.kopa (objekts Kopa()).

        x = a.saturs()
        y = b.saturs()
        for i in x:
            if i not in y:
                return False

        if Kopa.vai_vienadas(a, b):
            print(Kopa.vai_vienadas(a, b))
            return False
        else:
            return True


# ---------------------------------------------------------
# Galvenā programmas daļa
# ---------------------------------------------------------


# Pārbauda klases metodes.
kopa1 = Kopa()
kopa1.pievienot(5)
kopa1.pievienot(6)
kopa1.pievienot(3)
kopa1.pievienot(3)  # Pārbaudam vai pievienos vienādus elementus pa vienam.
print("1.kopa:")
kopa1.izdrukat()
print()

kopa2 = Kopa()
kopa2.pievienot([1, 2, 3, 3])  # Pārbaudam vai pievienos vienādus elementus sarakstā (nepievienos).
print("2.kopa:")
kopa2.izdrukat()
print()

kopa3 = Kopa()
kopa3.pievienot((10, 11))  # Pārbaudam vai pievienos vienādus elementus sarakstā (nepievienos).
print("3.kopa:")
kopa3.izdrukat()
print()

kopa4 = Kopa()
kopa4.pievienot(15)
kopa4.pievienot(16)
print("4.kopa:")
kopa4.izdrukat()
print()

print("Izdzēš 3.kopu (pārverš par tukšu kopu).")
kopa3.izdzest()  # Tāgad pārvēršam par tukšu kopu.
print("3.kopa:")
kopa3.izdrukat()
print()

pop1_no_kopas_4 = kopa4.pop()  # ar izveidoto pop funkciju paņēmam vienu nejaušu elementu no kopas un tas tiek nodzēsts sākotnēja kopā. (tiek definēta klasē neizmantojot set pop).
print("Pirmais nejauši paņemts elements no 4.kopas (un tas tika izņemts ara):")
print(pop1_no_kopas_4)
print()

print("4.kopa, kad mēs nejauši izņēmam nejauši elementu '" + str(pop1_no_kopas_4) + "' :")
kopa4.izdrukat()
print()

pop2_no_kopas_4 = kopa4.pop()  # ar izveidoto pop funkciju paņēmam vel vienu nejaušu elementu no kopas un tas tiek nodzēsts sākotnēja kopā.
print("Otrais nejauši paņemts elements no 4.kopas (un tas tika izņemts ara):")
print(pop2_no_kopas_4)
print()

print("4.kopa, kad mēs nejauši izņēmam elementu '" + str(pop2_no_kopas_4) + "' :")
kopa4.izdrukat()
print()

print("4.kopa, kad mēs nejauši izņēmam vel vienu elementu:")
pop3_no_kopas_4 = kopa4.pop()
print()

print("4.kopa:")
kopa4.izdrukat()
print()

print("Izveidojam jaunu 5.kopu:")
kopa5 = Kopa()
kopa5.izdrukat()
print()

print("Izveidojam jaunu 6.kopu:")
kopa6 = Kopa()
kopa6.pievienot(1)
kopa6.pievienot(2)
kopa6.pievienot(3)
kopa6.pievienot(3)
kopa6.izdrukat()
print()

kopa5.pievienot([1, 2, 4])
print("Pievienojam 5.kopai elementus 1, 2, 4:")
kopa5.izdrukat()
print()

kopa5.pievienot([1, 3, 4])
print("Pievienojam 5.kopai elementus 1, 3, 4:")
kopa5.izdrukat()
print()

kopa5.atjaunot((10, 12, 13))
print("Atjaunojam 5.kopu, nodzēsam visus elementus kopā un piešķīram jaunus elementus 10, 12, 13:")
kopa5.izdrukat()
print()

kopa5.atjaunot(10)
print("Atjaunojam 5.kopu, nodzēsam visus elementus kopā un piešķīram jaunu elementu 10:")
kopa5.izdrukat()
print()

kopa5.atjaunot([])
print("Atjaunojam 5.kopu, nodzēsam visus elementus kopā:")
kopa5.izdrukat()
print()

kopa5.atjaunot([2, 3, 4])
print("Atjaunojam 5.kopu, nodzēsam visus elementus kopā un piešķīram jaunus elementus 2, 3, 4:")
kopa5.izdrukat()
print()

print("5.kopa:")
kopa5.izdrukat()
print()

print("6.kopa:")
kopa6.izdrukat()
print()

a = Kopa.apvienot(kopa5, kopa6)
print("5.kopas apvienojums ar 6.kopu:")
a.izdrukat()
print()

a = Kopa.skelums(kopa5, kopa6)
print("5.kopas šķēlums ar 6.kopu:")
a.izdrukat()
print()

a = Kopa.simetriska_starpiba(kopa5, kopa6)
print("5.kopas simetriska starpība ar 6.kopu:")
a.izdrukat()
print()

a = Kopa.starpiba(kopa5, kopa6)
print("5.kopas starpība ar 6.kopu:")
a.izdrukat()
print()

a = Kopa.vai_parklajas(kopa5, kopa6)
print("Vai 5.kopa pārklajas ar 6.kopu:")
print(a)  # uzrakstīs True vai False
print()

a = Kopa.vai_neparklajas(kopa5, kopa6)
print("Vai 5.kopa nepārklajas ar 6.kopu:")
print(a)  # uzrakstīs True vai False
print()

a = Kopa.vai_vienadas(kopa5, kopa6)
print("Vai 5.kopa ir vienāda ar 6.kopu:")
print(a)  # uzrakstīs True vai False
print()

a = Kopa.vai_nav_vienadas(kopa5, kopa6)
print("Vai 5.kopa nav vienāda ar 6.kopu:")
print(a)  # uzrakstīs True vai False
print()

a = Kopa.vai_stingra_apakskopa(kopa5, kopa6)
print("Vai 5.kopa ir stingra apakškopa 6.kopai:")
print(a)
print()

a = Kopa.vai_apakskopa(kopa5, kopa6)
print("Vai 5.kopa ir 6.kopas apakškopa:")
print(a)  # uzrakstīs True vai False
print()

n = 2
a = kopa5.vai_pieder(n)
print("Vai 5.kopai")
kopa5.izdrukat()
print("pieder elements " + str(n) + ":")
print(a)  # uzrakstīs True vai False
print()

n = 6
a = kopa6.vai_pieder(n)
print("Vai 6.kopai")
kopa6.izdrukat()
print("pieder elements " + str(n) + ":")
print(a)  # uzrakstīs True vai False
print()

kopa7 = Kopa()
kopa7.pievienot(1)
kopa7.pievienot(2)
kopa7.pievienot(3)

print("7.kopa:")
kopa7.izdrukat()
print()

print("Izmest '1' no 7.kopas.")
kopa7.izmest(1)
print("7.kopa:")
kopa7.izdrukat()
print()

print("Izmest '14' no 7.kopas.")
kopa7.izmest(14)
print("7.kopa:")
kopa7.izdrukat()
print()

print("Noņemt '2' no 7.kopas.")
kopa7.nonemt(2)
print("7.kopa:")
kopa7.izdrukat()
print()

print("Noņemt '3' no 7.kopas.")
kopa7.nonemt(3)
print("7.kopa:")
kopa7.izdrukat()
print()

kopa8 = Kopa()
kopa8.pievienot("a")
kopa8.pievienot("b")
kopa8.pievienot(["c", "d", 5])
print("8.kopa:")
kopa8.izdrukat()
