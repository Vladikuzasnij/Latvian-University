# Programmas nosaukums: Temperatūras konvertācija
# 7. uzdevums (MPR4)
# Uzdevuma formulējums: Sastādīt programmu, kas pieprasa ievadīt temperatūras skaitlisko vērtību un mērvienību, un veic konvertāciju uz citām mērvienībām.
# Programmas autors: Vladislavs Babaņins
# Versija 1.4

print("\"Temperatūras konvertācija\"\nVersija 1.4\n") # Programmas nosaukums


a=int(input("Izvēlies kādu mērvienību grībi konvertēt citās!\n°C, °F, K\n\nJa °C tad 1, ja °F tad 2, ja K tad 3 ====> ")) # EUR => USD vai USD => EUR izvēle ar 1 vai 2

if a == 1:
    C=input("Ievādi temperatūras skaitlisko vērtibu!\n°C = ")
    
    if float(C)>=-273.15:
        
        C_to_F = 1.8*float(C) + 32
        C_to_K = float(C) + 273.15
        print(str(C) + " °C = " + str(C_to_F) +" °F") # Ievadīšana ekrāna
        print(str(C) + " °C = " + str(C_to_K) +" K") # Ievadīšana ekrāna
   
    else:
        print("Error. Vērtiba ir mazāka nekā absolūtā nulle.")
        
if a == 2:
    F=input("°F = ")
    
    if float(F)>=-459.67:
        
        F_to_C=((float(F)-32)/1.8) # Temperatūru konvertācija
        F_to_K=(float(F)+459.67)/1.8 # Temperatūru konvertācija
        print(str(F) + " °F = " + str(F_to_C) +" °C") # Ievadīšana ekrāna
        print(str(F) + " °F = " + str(F_to_K) +" K") # Ievadīšana ekrāna
    
    else:
        print("Error. Vērtiba ir mazāka nekā absolūtā nulle.")    
    
if a == 3: # Ja tika ievādits 3 tad izpildās komandas:
    K=input("K = ") # K vērtību ievādišana
    
    if float(K)>=0: # Absolūtas nulles pārbaudīšana
        
        K_to_C=float(K)-273.15 # Temperatūru konvertācija
        K_to_F=1.8*(float(K))-459.67 # Temperatūru konvertācija
        print(str(K) + " K = " + str(K_to_C) +" °C") # Ievadīšana ekrāna
        print(str(K) + " K = " + str(K_to_F) +" °F") # Ievadīšana ekrāna
    
    else:
        print("Error. Vērtiba ir mazāka nekā absolūtā nulle.")
    
if a!=1 and a!=2 and a!=3:
    print("Error") # Ja tika ievadīts ne 1, ne 2, ne 3, tad ir "Error"