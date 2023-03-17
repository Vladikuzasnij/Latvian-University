# Programmas nosaukums: PU2 MPR15
# PU2 MPR15
# Uzdevuma formulējums: 
'''
Sastādīt programmu, kas pārbauda vai ievadīta korekta e-pasta adrese. Simbolu virknes iebūvētās funkcijas izmantot nedrīkst, izņemot simbolu virknes caurskatīšanu pa vienam simbolam. 
Pieņemsim, ka korektā e-pasta adresē:
1) jābut tieši vienam @ simbolam
2) jābūt vismaz 1 rakstzīmei pirms un aiz simbola @ un punkta .
3) ir ne vairāk kā 256 rakstzīmes
4) ir jāsākas ar burtu vai ciparu
5) atsevišķie vārdi var saturēt tikai latīņu burtus, ciparus un pasvītrojuma rakstzīmi _
'''
# Versija 1.0


def is_valid_email(email):
    # pārbauda, vai e-pasts ir īsāks par 256 rakstzīmēm
    if len(email) > 256:
        return False
    
    symbol_at_count = 0 # @ simbolu skaits, (sākuma ir 0) ja != 1 tad False
    dot_count = 0       # punktu . skaits. (Sākuma ir 0)
    
    if email[0] == "_": # Jo ir jāsakas ar burtu vai ciparu (pārbaude uz visiem legāliem burtiem ir tālak)
        return False
    
    for i in range(0,len(email)):
        if email[i] == "@"  :
            symbol_at_count += 1
            # pārbauda, vai ir vismaz 1 rakstzīme pirms simbola @
            if i == 0:
                return False
            # pārbauda, vai ir vismaz 1 rakstzīme pēc simbola @
            if i == len(email) - 1:
                return False
            if email[i+1] == ".": # pārbauda, pēc @ nav ., ja ir tad False
                return False                   
            
        elif email[i] == ".":
            dot_count += 1
            # pārbauda, vai ir vismaz 1 rakstzīme pirms punkta
            if i == 0:
                return False
            # pārbauda, vai ir vismaz 1 rakstzīme pēc punkta
            if i == len(email) - 1:
                return False
            
            if email[i+1] == ".": # pārbauda, pēc punkta nav otrā punkta, ja ir tad False
                return False
            
            if email[i+1] == "@": # pārbauda, pēc punkta nav @, ja ir tad False
                return False
            
        elif not ( email[i] == "q" or email[i] == "w" or email[i] == "e" or email[i] == "r" or
                   email[i] == "t" or email[i] == "y" or email[i] == "u" or email[i] == "i" or
                   email[i] == "o" or email[i] == "p" or email[i] == "a" or email[i] == "s" or
                   email[i] == "d" or email[i] == "f" or email[i] == "g" or email[i] == "h" or
                   email[i] == "j" or email[i] == "k" or email[i] == "l" or email[i] == "z" or
                   email[i] == "x" or email[i] == "c" or email[i] == "v" or email[i] == "b" or
                   email[i] == "n" or email[i] == "m" or
                  
                   email[i] == "Q" or email[i] == "W" or email[i] == "E" or email[i] == "R" or
                   email[i] == "T" or email[i] == "Y" or email[i] == "U" or email[i] == "I" or
                   email[i] == "O" or email[i] == "P" or email[i] == "A" or email[i] == "S" or
                   email[i] == "D" or email[i] == "F" or email[i] == "G" or email[i] == "H" or
                   email[i] == "J" or email[i] == "K" or email[i] == "L" or email[i] == "Z" or
                   email[i] == "X" or email[i] == "C" or email[i] == "V" or email[i] == "B" or
                   email[i] == "N" or email[i] == "M" or
                   
                   email[i] == "1" or email[i] == "2" or email[i] == "3" or email[i] == "4" or
                   email[i] == "5" or email[i] == "6" or email[i] == "7" or email[i] == "8" or
                   email[i] == "9" or email[i] == "0" or
                   
                   email[i] == "_" or email[i] == "."):
            
            # atsevišķie vārdi var saturēt tikai latīņu burtus, ciparus un pasvītrojuma rakstzīmi _
            
            return False

            
    if symbol_at_count != 1: # Jābut tieši vienam @ simbolam
        return False
    if dot_count == 0: # jābut vismaz vienam punktam. @inbox.lv @lu.lv
        return False
  
    return True

# ----------------- galvenā programma

email = input("Ievadiet derīgo e-pastu => ")

is_valid_email(email)
while True:
    if is_valid_email(email) == False:
        email = input("\nTas nav korekts e-pasts!\nIevadiet derīgo e-pastu => ")
        is_valid_email(email)
    else:
        print("Tas ir korekts e-pasts!")
        break