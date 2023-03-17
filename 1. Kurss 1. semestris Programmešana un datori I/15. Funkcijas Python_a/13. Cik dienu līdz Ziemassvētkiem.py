# Programmas nosaukums: 2. uzd MPR15
# 2. uzdevums MPR15
# Uzdevuma formulējums: Sastādīt programmu, kas pēc ievadīta datuma nosaka, cik dienu ir palicis līdz Ziemassvētku vakaram (24. decembrim). Datuma ievades pieļaujamais formāts ir DD.MM.GGGG. un tas tiek ievadīts kā simbolu virkne. Datuma apstrādes iebūvētās funkcijas izmantot nedrīkst.
# Versija 1.0


def date_check(DD_MM_GGGG_):

    DD_ = DD_MM_GGGG_[0:3]
    
    MM_ = DD_MM_GGGG_[3:6]
    
    GGGG_ = DD_MM_GGGG_[6:11]
    
    DD = DD_MM_GGGG_[0:2]
    
    MM = DD_MM_GGGG_[3:5]
    
    GGGG = DD_MM_GGGG_[6:10]
    
    # --------------- simbolu virknes garums ir precīzi 11 simboli. DD.MM.GGGG.
    if len(DD_MM_GGGG_) != 11:
        return False  
    
    if DD_[2:3] != "." or MM_[2:3] != "." or GGGG_[4:5] != ".":
        return False
    
    if DD_MM_GGGG_.count('.') !=3:
        return False
    
    try:
        
        DD = int(DD)
        b = 1/DD # 00.MM.GGGG.
        
        MM = int(MM)
        c = 1/MM # DD.00.GGGG.
        
        GGGG = int(GGGG)
        d = 1/GGGG # DD.MM.0000.
        
    except:
        return False
        #print("Tāds datums neeksistē")
        #quit()
        
    else:
        pass
        
    DD = int(DD) # Parveidojam int, lai uzzinātu vai tas ir lielāk par 31 vai mazāks vai vienāds ar 0, tad tāds datums neeksistē 
    if  DD > 31 or DD <= 0 :
        return False
        #print("Tāds datums neeksistē")
        #quit()
        
    MM = int(MM) # Parveidojam int, lai uzzinātu vai tas ir lielāk par 12 vai mazāks vai vienāds ar 0, tad tāds datums neeksistē 
    
    if  MM > 12 or MM <= 0:
        return False
        #print("Tāds datums neeksistē")
        #quit()
        
    GGGG = int(GGGG)  # Parveidojam int, lai uzzinātu vai tas ir mazāks vai vienāds ar 0, tad tāds datums neeksistē 
    
    if  GGGG <= 0:
        return False
        #print("Tāds datums neeksistē")
        #quit()
    
    if  MM == 4 and DD > 30: # Aprilī maksimāli ir tikai 30 dienas.
        return False
        #print("Tāds datums neeksistē")
        #quit()
    
    if  MM == 6 and DD > 30: # Jūnija maksimāli ir tikai 30 dienas.
        return False
        #print("Tāds datums neeksistē")
        #quit()
    
    if  MM == 9 and DD > 30: # Septembrī maksimāli ir tikai 30 dienas.
        return False
        #print("Tāds datums neeksistē")
        #quit()
    
    if  MM == 11 and DD > 30: # Novembrī maksimāli ir tikai 30 dienas.
        return False
        #print("Tāds datums neeksistē")
        #quit()
    

    
    F = 28 #default # Dienu skaits Februāri
    
    if (GGGG % 400) == 0: # Ja garais gad tad februarī dienu skaits ir 29
        F = 29
        
    elif (GGGG % 100) == 0: # Ja isais gads tad februarī dienu skaits ir 28
        F = 28
    
    elif (GGGG % 4) == 0: # Ja garais gad tad februarī dienu skaits ir 29
        F = 29
    
    else:
        F = 28 # Ja isais gads tad februarī dienu skaits ir 28
    
    if MM == 2 and DD > F: # Lai noteiktu vai ir pareizi ievadīti dati
        return False

def leap_year(GGGG): # Noteicam vai gads (int) ir garais gads vai nav)
    # F = 28 # default
    GGGG = int(GGGG)
    if (GGGG % 400) == 0:
        return True # F = 29
        
    elif (GGGG % 100) == 0:
        return False # F = 28
    
    elif (GGGG % 4) == 0:
        return True # F = 29
    
    else:
        return False # F = 28 


def day_count(Year, MM, DD): # Skaitam cik ir pagajušas dienas no 1. gada līdz ievadītam datumam
    F = 28
    days = 0
    days_year = 0
    
    days_year = (Year-1)*365 + (Year-1)//4 - (Year-1)//100 + (Year-1)//400 # pagajušo dienu skaits
    
    if leap_year(GGGG) == False:
        F = 28
    else:
        F = 29
        
    if MM == "01" :
        days = days_year + DD # only january
        return days
    if MM == "02" : # MM == 2
        
        days = days_year + DD + 31 # + all of january
        return days
    if MM == "03" : # MM == 3
            
        days = days_year + DD + 31 + F  # + all of january and february      
        return days
    if MM == "04" :
                
        days = days_year + DD + 31 + F + 31
        return days
    if MM == "05" :
                    
        days = days_year + DD + 31 + F + 31 + 30
        return days
    if MM == "06" :
                        
        days = days_year + DD + 31 + F + 31 + 30 + 31  
        return days
    if MM == "07" :
                            
        days = days_year + DD + 31 + F + 31 + 30 + 31 + 30
        return days
    if MM == "08" :
                                
        days = days_year + DD + 31 + F + 31 + 30 + 31 + 30 + 31
        return days
    if MM == "09" :
                                    
        days = days_year + DD + 31 + F + 31 + 30 + 31 + 30 + 31 + 31
        return days
    if MM == "10" :
                                        
        days = days_year + DD + 31 + F + 31 + 30 + 31 + 30 + 31 + 31 + 30
        return days
    if MM == "11" :
                                            
        days = days_year + DD + 31 + F + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
        return days
    if MM == "12" :
                                                
        days = days_year + DD + 31 + F + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30
        return days 
    #return days





# -------------------------------------------------- galvenā programma 
DD_MM_GGGG_ = input("Ievadiet DD.MM.GGGG. ==> ")

if date_check(DD_MM_GGGG_) == False: # Ja kaut vienu pārbaudi neizturēja, tad tāds datums neeksistē
    print("Tāds datums neeksistē")
    quit()
    
DD = DD_MM_GGGG_[0:2]    
MM = DD_MM_GGGG_[3:5]
GGGG = DD_MM_GGGG_[6:10]

if int(DD) == 24 and MM == "12": # Ja ievada 24.decembrī uzreiz
    print("Šajā dienā ir Ziemassvētku vakars! (24.decembrīs)") 
    
elif (day_count(int(GGGG), str(MM), int(DD))) < (day_count(int(GGGG), str("12"), int(24))):
    
    remaining_days_until_christmas = (day_count(int(GGGG), str("12"), int(24))) - (day_count(int(GGGG), str(MM), int(DD))) # Ja pirms Ziemāssvetkiem, tad atņemsim cik
    # print(remaining_days_until_christmas)                                                                                # ir pagājis no 1.gada 1.janvāri līdz šai ievadītam datumam un līdz šīs gāda Ziemāssvētkiem. Tad iegūsim nepieciešamo dienu skaitu
    print("Līdz Ziemassvētkiem ir palikušas " + str(remaining_days_until_christmas) + " dienas.")

else: # Ja (day_count(int(GGGG), str(MM), int(DD))) > (day_count(int(GGGG), str("12"), int(24))):
    remaining_days_until_christmas = (day_count(int(GGGG)+1, str("12"), int(24))) - (day_count(int(GGGG), str(MM), int(DD))) # Ja pirms Ziemāssvetkiem, tad atņemsim cik ir pagājis no 1.gada 1.janvāri līdz šai ievadītam datumam un līdz šīs gāda+1 (līdz nākama gāda) Ziemāssvētkiem. 
    print("Līdz Ziemassvētkiem ir palikušas " + str(remaining_days_until_christmas) + " dienas.")                            # Tad iegūsim nepieciešamo dienu skaitu