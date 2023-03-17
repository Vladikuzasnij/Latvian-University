# Programmas nosaukums: 3.uzdevums
# 3.uzdevums MPR7
# Uzdevuma formulējums: Izveidot programmu, kas lietotāja ievadīto naturālo skaitli no 1 līdz 999 nodrukā uz ekrāna ar vārdiem.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0


x = int(input("Ievadiet naturālo skaitli no 1 līdz 999\n===> "))

if x < 1 or x > 999:
    print("Nepareizi ievadīti dati")

else:
    Simti = x // 100
    Vieni = x % 10
    PirmieDiviCipari =  x // 10
    D = PirmieDiviCipari % 10
    Desmiti = x % 100
    
    SimboluVirkne = ""


    match Simti:
        
        case 1 :
            SimboluVirkne = SimboluVirkne + "vieni simti"
        
        case 2 :
            SimboluVirkne = SimboluVirkne + "divi simti"
        
        case 3:
            SimboluVirkne = SimboluVirkne + "trīs simti"
        
        case 4:
            SimboluVirkne = SimboluVirkne + "četri simti"
            
        case 5:
            SimboluVirkne = SimboluVirkne + "pieci simti"     
            
        case 6:
            SimboluVirkne = SimboluVirkne + "seši simti"                
        
        case 7:
            SimboluVirkne = SimboluVirkne + "septiņi simti"      
            
        case 8:
            SimboluVirkne = SimboluVirkne + "astoņi simti"
    
        case 9:
            SimboluVirkne = SimboluVirkne + "deviņi simti"
            
        case _:
            SimboluVirkne = SimboluVirkne + ""
    
    if D == 1 :
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
        

        match Desmiti:        
            
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

    print(SimboluVirkne)