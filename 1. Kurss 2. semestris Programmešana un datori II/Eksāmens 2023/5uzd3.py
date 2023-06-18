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
            while paz:
                for i in self.__kopa:
                    print(i[0])
                    print(elements)
                    
                    if i[0] == elements[0]:
                        #self.__kopa.pop(i[0])
                        #self.__kopa.append(elements[0])
                        paz = False
                    
                    #self.__kopa[i] = elements[0]#.#nonemt(i[0])
                    #self.__kopa.append(elements[0])
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
    # Pārbauda vai tiek ievadīts naturāls skaitlis no 0 līdz 9. Ja nav, tad paprasa ievadīt to velreiz. Bezgalīgi daudz ievades.
    # i - tiek izmantots kosmetiski, lai pielāgotu programmas ziņojumu katrai ievadei. str(i) + ".ciparu => "
    
    x = input("Ievadiet latviešu vārdu ar lieliem burtiem ==> ")
    while True:
        if check_vards(x) == "X":
            #vardi = vardi.pievienot(x)
            vardi.izdrukat()
            #vardi = vardi.add(x)
            #quit() 
        if check_vards(x) == False:
            x = input("KĻŪDA! Ievadiet latviešu vārdu ar lieliem burtiem ==> ")
            #print(check_vards(x))
        
        elif check_vards(x) == True:
            vardi.pievienot(x)
            #return x

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

    
'''
while a != "X":
    a = input_latvian_word()
    if a == "X":
        quit()
if a == "X":
    quit()
'''
'''
def input_vards():
    vardi = ""
    vards = input("Ievadiet vardu ar lieliem burtiem ==> ")
    
    #if vards == "X":
    #    return vardi #vardi
    while vards != "X":
        while check_vards(vards) == False:
            vards = input("KĻŪDA! Ievadiet vardu ar lieliem burtiem ==> ")
            if vards == "X":
                vardi = vardi + vards
                return vardi #vardi 
            
    vardi = vardi + vards
    return vardi
    #vardi = vardi + vards
    #return vardi

a = input_vards()
print(a)
'''