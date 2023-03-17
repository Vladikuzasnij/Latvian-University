# Programmas nosaukums: 4.uzdevums
# 4.uzdevums MPR7
# Uzdevuma formulējums: Izveidot programmu, kas jebkuru lietotāja ievadīto datumu intervālā no Kristus dzimšanas (no 1. gada) līdz 2100. gadam nodrukā uz ekrāna ar vārdiem, norādot arī datumam atbilstošo dienas nosaukumu. Kalendāra reformas var neievērot. Piemēram, ceturtdiena, tūkstoši deviņi simti sešdesmit pieci gada četrpadsmit janvāris. Ja kādā gadījumā skaitļu galotnes neatbildīs gramatikas likumiem, tā netiks uzskatīta par kļūdu.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0

import sys

# G -gads
# M - mēnesis
# D - datums 

G = int(input("Ievadiet gadu ===> "))
M = int(input("Ievadiet mēnesi ===> "))
D = int(input("Ievadiet datumu ===> "))

if G < 1 or G > 2100:
    print("Kalendārs darbojas intervāla no 1.gada līdz 2100.gadam")
    sys.exit(0)

if M < 1 or M > 12:
    print("Tāds datums neeksistē")
    sys.exit(0)

if D < 1 or D > 31:
    print("Tāds datums neeksistē")
    sys.exit(0)
    

if  M == 4 and D > 30:
    print("Tāds datums neeksistē")
    sys.exit(0)

if  M == 6 and D > 30:
    print("Tāds datums neeksistē")
    sys.exit(0)

if  M == 9 and D > 30:
    print("Tāds datums neeksistē")
    sys.exit(0)

if  M == 11 and D > 30:
    print("Tāds datums neeksistē")
    sys.exit(0)

if M == 1:
    month="janvārī"
if M == 2:
    month="februārī"
if M == 3:
    month="martā"
if M == 4:
    month="aprīli"
if M == 5:
    month="maijā"
if M == 6:
    month="jūnijā"
if M == 7:
    month="jūlijā"
if M == 8:
    month="augustā"
if M == 9:
    month="septembrī"
if M == 10:
    month="oktobrī"
if M == 11:
    month="novembrī"
if M == 12:
    month="decembrī"

x = (G-1)*365 + (G-1)//4 - (G-1)//100 + (G-1)//400 # pagajušo dienu skaits


if G == 1900:
    F = 29

elif (G % 400) == 0:
    F = 29
    
elif (G % 100) == 0:
    F = 28

elif (G % 4) == 0:
    F = 29

else:
    F = 28

if M == 2 and D > F:
    print("Tāds datums neeksistē")
    sys.exit(0)    

match M:
    
    case 1 :
        
        d1 = D + x
    
    case 2 :
        d1 = D + x + 31
        
    case 3 :
        d1 = D + x + 31 + F
        
    case 4 :
        d1 = D + x + 31 + F + 31
        
    case 5 :
        d1 = D + x + 31 + F + 31 + 30
        
    case 6 :
        d1 = D + x + 31 + F + 31 + 30 + 31
        
    case 7 :
        d1 = D + x + 31 + F + 31 + 30 + 31 + 30
        
    case 8 :
        d1 = D + x + 31 + F + 31 + 30 + 31 + 30 + 31
        
    case 9 :
        d1 = D + x + 31 + F + 31 + 30 + 31 + 30 + 31 + 31
        
    case 10 :
        d1 = D + x + 31 + F + 31 + 30 + 31 + 30 + 31 + 31 + 30
        
    case 11 :
        d1 = D + x + 31 + F + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
        
    case 12 :
        d1 = D + x + 31 + F + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30    

SimboluVirkne = ""
    
match d1 % 7 :
    case 4:
        SimboluVirkne = SimboluVirkne + "Ceturtdiena, "
    case 5 :
        SimboluVirkne = SimboluVirkne + "Piektdiena, "
    case 6 :
        SimboluVirkne = SimboluVirkne + "Sestdiena, "
    case 0 :
        SimboluVirkne = SimboluVirkne + "Svētdiena, "
    case 1 :
        SimboluVirkne = SimboluVirkne + "Pirmdiena, "
    case 2 :
        SimboluVirkne = SimboluVirkne + "Otrdiena, "
    case 3 :
        SimboluVirkne = SimboluVirkne + "Trešdiena, "

Tukstosi = G // 1000
Simti = G // 100
Vieni = G % 10
PirmieDiviCipari =  G // 10
T = PirmieDiviCipari % 10
Desmiti = G % 100
        


match Tukstosi:
            
            case 1 :
                SimboluVirkne = SimboluVirkne + "vieni tukstoši"
            
            case 2 :
                SimboluVirkne = SimboluVirkne + "divi tukstoši"
                
            case _:
                SimboluVirkne = SimboluVirkne + ""


match Simti:
            
            case 1 | 11 | 21:
                SimboluVirkne = SimboluVirkne + " vieni simti"
            
            case 2 | 12 | 22 :
                SimboluVirkne = SimboluVirkne + " divi simti"
            
            case 3 | 13 | 23:
                SimboluVirkne = SimboluVirkne + " trīs simti"
            
            case 4 | 14 | 24:
                SimboluVirkne = SimboluVirkne + " četri simti"
                
            case 5 | 15 | 25:
                SimboluVirkne = SimboluVirkne + " pieci simti"     
                
            case 6 | 16 | 26:
                SimboluVirkne = SimboluVirkne + " seši simti"                
            
            case 7 | 17 | 27:
                SimboluVirkne = SimboluVirkne + " septiņi simti"      
                
            case 8 | 18 | 28:
                SimboluVirkne = SimboluVirkne + " astoņi simti"
        
            case 9 | 19 | 29:
                SimboluVirkne = SimboluVirkne + " deviņi simti"
                
            case _:
                SimboluVirkne = SimboluVirkne + ""
        
if T == 1 :
            match Desmiti:
                case 10:
                    SimboluVirkne = SimboluVirkne + " desmit"                       
                case 11:
                    SimboluVirkne = SimboluVirkne + " vienpadsmit"
                case 12:
                    SimboluVirkne = SimboluVirkne + " divpadsmit"
                case 13:
                    SimboluVirkne = SimboluVirkne + " trīspadsmit"
                case 14:
                    SimboluVirkne = SimboluVirkne + " četrpadsmit"
                case 15:
                    SimboluVirkne = SimboluVirkne + " piecpadsmit"
                case 16:
                    SimboluVirkne = SimboluVirkne + " sešpadsmit"
                case 17:
                    SimboluVirkne = SimboluVirkne + " septiņpadsmit"
                case 18:
                    SimboluVirkne = SimboluVirkne + " astoņpadsmit"
                case 19:
                    SimboluVirkne = SimboluVirkne + " deviņpadsmit"             
        
else:
            
    
            match Desmiti: # Desmiti
                
                case 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 :
                    SimboluVirkne = SimboluVirkne + " divdesmit"
                
                case 30 | 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 :
                    SimboluVirkne = SimboluVirkne + " trīsdesmit"
                
                case 40 | 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49:
                    SimboluVirkne = SimboluVirkne + " četrdesmit"
                
                case 50 | 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59:
                    SimboluVirkne = SimboluVirkne + " piecdesmit"
                    
                case 60 | 61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 | 69:
                    SimboluVirkne = SimboluVirkne + " sešdesmit"     
                    
                case 70 | 71 | 72 | 73 | 74 | 75 | 76 | 77 | 78 | 79:
                    SimboluVirkne = SimboluVirkne + " septiņdesmit"                
                
                case 80 | 81 | 82 | 83 | 84 | 85 | 86 | 87 | 88 | 89:
                    SimboluVirkne = SimboluVirkne + " astoņdesmit"      
                    
                case 90 | 91 | 92 | 93 | 94 | 95 | 96 | 97 | 98 | 99:
                    SimboluVirkne = SimboluVirkne + " deviņdesmit"
                    
                case _:
                    SimboluVirkne = SimboluVirkne + ""            
    
            match Vieni:
                
                case 1 :
                    SimboluVirkne = SimboluVirkne + " viens"
                
                case 2 :
                    SimboluVirkne = SimboluVirkne + " divi"
                
                case 3:
                    SimboluVirkne = SimboluVirkne + " trīs"
                
                case 4:
                    SimboluVirkne = SimboluVirkne + " četri"
                    
                case 5:
                    SimboluVirkne = SimboluVirkne + " pieci"     
                    
                case 6:
                    SimboluVirkne = SimboluVirkne + " seši"                
                
                case 7:
                    SimboluVirkne = SimboluVirkne + " septiņi"      
                    
                case 8:
                    SimboluVirkne = SimboluVirkne + " astoņi"
            
                case 9:
                    SimboluVirkne = SimboluVirkne + " deviņi"
                    
                case _:
                    SimboluVirkne = SimboluVirkne + ""
                
                
SimboluVirkne = SimboluVirkne + " gada " + month
print(SimboluVirkne)