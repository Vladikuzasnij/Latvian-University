# Programmas nosaukums: 2.uzdevums
# 2.uzdevums MPR7
# Uzdevuma formulējums: Izveidot programmu, kas pēc lietotāja ievadītās dzimšanas dienas un mēneša nosaka, kāda ir viņa horoskopa zīme.
# Programmas autors: Vladislavs Babaņins
# Versija 1.0

print("Horoskopa zīmes noteikšana")

print(("\n1 - Janvāris\n2 - Februāris\n3 - Marts\n4 - Aprīlis\n5 - Maijs\n6 - Jūnijs\n7 - Jūlijs\n8 - Augusts\n9 - Septembris\n10 - Oktobris\n11 - Novembris\n12 - Decembris\n"))
m = int(input("Ievadiet savu dzimšanas mēnesi ===> "))
d = int(input("Ievadi savu dzimšanas datumu ===> "))

if d > 31 or d < 1:
    print("Nepareizi ievādīti dati")

else:
    Hor = "Jūsu horoskopa zīme: "

    match m :
        case 1 :
            if d<20 :
                print(Hor + "Mežāzis")
            else :
                print(Hor + "Ūdensvīrs")
        
        case 2 :
            if d<19 :
                print(Hor + "Ūdensvīrs")
                
            elif d == 30:
                print("\n30. februāris ir bijis trīs reizes pasaules vēsturē dažās valstīs,\nlai gan pēc Gregora kalendāra februārī ir 28 dienas parastajā gadāvai 29 dienas garajā gadā.")
            
            elif d > 29:
                print("Nepareizi ievādīti dati")
                        
            else :
                print(Hor + "Zivis")
        
        case 3 :
            if d<21 :
                print(Hor + "Zivis")
            else :
                print(Hor + "Auns")
        
        case 4 :
            if d<20 :
                print(Hor + "Auns")
                
            elif d<31:
                print(Hor + "Vērsis")
                
            else:
                print("Nepareizi ievādīti dati")
        
        case 5 :
            if d<21 :
                print(Hor + "Vērsis")
            else :
                print(Hor + "Dvīņi")
    
        case 6 :
            if d<22 :
                print(Hor + "Dvīņi")
            elif d<31:
                print(Hor + "Vēzis")
            else:
                print("Nepareizi ievādīti dati")                
    
        case 7 :
            if d<23 :
                print(Hor + "Vēzis")
            else :
                print(Hor + "Lauva")
    
        case 8 :
            if d<23 :
                print(Hor + "Vēzis")
            else :
                print(Hor + "Jaunava")
    
        case 9 :
            if d<23 :
                print(Hor + "Jaunava")
                
            elif d<31:
                print(Hor + "Svari")
            else :
                print("Nepareizi ievādīti dati") 
        
        case 10 :
            if d<23 :
                print(Hor + "Svari")
        
            else :
                print(Hor + "Skorpions")
            
        case 11 :
    
            if d<23 :
                print(Hor + "Skorpions")
            
            elif d<31:
                print(Hor + "Strēlnieks")
        
            else :
                print("Nepareizi ievādīti dati") 

        
        case 12 :
        
            if d<22 :
                print(Hor + "Strēlnieks")
            else :
                print(Hor + "Mežāzis")
        
        case other:
            print("Nepareizi ievādīti dati")