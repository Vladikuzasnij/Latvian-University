# Programmas nosaukums: 2. uzd MPR12
# 2. uzdevums MPR12
# Uzdevuma formulējums: Sastādit programmu, kura zīmē "Fibonači eglīti". Iespējami garākā zara garumu ievada lietotājs.
# Versija 1.0

d = int(input("Ievadi lielākā zara garumu ===> "))

a = 1
b = 1
c = a + b
garums = 1

# ------ Maksimālo garumu noteikšana

k=1
while k != 0:
    
    if c>d:
        garums=b*2 # *2, jo eglītei ir divas puses. Tāpēc, lai reķinātu tukšumus mums
        k=0 # cikla apstāšanai
        
    a = b
    b = c
    c = a + b # Fibonači virkne
    
# ------ 

#--------------Pirmais zars (augšējais - pirmā rinda)    

tuksumi = " " * int((garums-len("**"))//2)    # Tukšumu skaitīšana. Dalām ar 2 jo tukšumi ir no divām pusēm. Nakāmajā rindā tas ir parādīts
egles_pirmais_zars = tuksumi + "**" + tuksumi
print(egles_pirmais_zars)

#--------------   

# ----- Parējo zaru noteikšana

a = 1
b = 1
c = 1 # mainīgie Fibonači virknei

egle = ""

while c <= d :
    
    zars = "**"*c                                 # No kā ir veidots zars
    tuksumi = " " * int((garums-len(zars))//2)      # Tukšumu skaitīšana. Dalām ar 2 jo tukšumi ir no divām pusēm. Nakāmajā rindā tas ir parādīts
    egle = egle + tuksumi + zars + tuksumi + "\n" # ______****______
    
    a = b
    b = c
    c = a + b

print(egle)
