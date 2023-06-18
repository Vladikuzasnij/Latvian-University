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

            paz = True
            #print(i[0])
            for i in self.__kopa:
                #print(i[0])
                #print(elements)
                if i[0] == elements[0]:
                    paz = False
                
                #if i == elements:
                #    paz = False
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






        
        
        
def check_vards(vards):
    alfabets = ["A", "Ā", "B", "C", "Č", "D", "E", "Ē", "F", "G", "Ģ", "H", "I", "Ī", "J", "K", "Ķ", "L", "Ļ", "M", "N", "Ņ", "O", "P", "R", "S", "Š", "T", "U", "Ū", "V", "Z", "Ž"]
    for i in range(len(vards)):
        if vards == "X":
            return "X"
        if vards[i] not in alfabets:
            return False
        else:
            pass
    return True

#vardi = ""

vardi = Kopa()
def input_latvian_word():
    global vardi

    x = input("Ievadiet latviešu vārdu ar lieliem burtiem ==> ")
    paz = True
    while paz:
        if check_vards(x) == "X":

            vardi.izdrukat()
            paz = False
            

        if check_vards(x) == False:
            x = input("KĻŪDA! Ievadiet latviešu vārdu ar lieliem burtiem ==> ")
            #print(check_vards(x))
        
        elif check_vards(x) == True:
            vardi.pievienot(x)
            return x
    
'''
kopa1 = Kopa()
kopa1.pievienot("LABI")   
kopa1.pievienot("OKAY")   
kopa1.pievienot("LAKI")   
kopa1.saturs()
kopa1.izdrukat()
'''
        

a = input_latvian_word()
while a != "X":
    a = input_latvian_word()
  
vardi.izdrukat()
    
