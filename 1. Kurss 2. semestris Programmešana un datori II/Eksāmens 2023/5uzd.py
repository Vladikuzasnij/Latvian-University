class Kopa:
    # Klase kopa.
    def __init__(self):
        # Inicializēsim tukšo kopu.
        # self - kopa (objekts Kopa()).

        self.kopa = []

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


def input_latvian_word():
    # Pārbauda vai tiek ievadīts naturāls skaitlis no 0 līdz 9. Ja nav, tad paprasa ievadīt to velreiz. Bezgalīgi daudz ievades.
    # i - tiek izmantots kosmetiski, lai pielāgotu programmas ziņojumu katrai ievadei. str(i) + ".ciparu => "
    vardi = Words()
    x = input("Ievadiet latviešu vārdu ar lieliem burtiem ==> ")
    while True:
        if check_vards(x) == "X":
            vardi = vardi.pievienot(x)
            vardi.izdrukat()
            #vardi = vardi.add(x)
            #quit() 
        if check_vards(x) == False:
            x = input("KĻŪDA! Ievadiet latviešu vārdu ar lieliem burtiem ==> ")
            #print(check_vards(x))
        
        elif check_vards(x) == True:
            
            return x
        
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