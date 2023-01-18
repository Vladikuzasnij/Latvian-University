# Programmas nosaukums: 5. uzd MPR11
# 5. uzdevums MPR11
# Uzdevuma formulējums: Sastādīt programmu, kas noskaidro, vai lietotāja secīgi ievadītā skaitļu virkne veido aritmētisko progresiju. Skaitļu virknes ievadi pārtrauc ievadot skaitli 0.
# Versija 1.0

sv = "Dota virkne ir aritmētiska progresija"

x1 = float(input("Ievadiet 1 locekli ===> "))

if x1 == 0:
    print("Šajā virknē nav elementu.") # Ja uzreiz 0 ievada
    quit()
    
x2 = float(input("Ievadiet 2 locekli ===> "))

if x2 == 0: # Ja tikai vienu elementu ievada
    print("Šajā virknē ir tikai viens elements.\nAritmētiskas progresijas tiek definētas skaitļu virknem ar vismaz diviem elementiem.")
    quit()
    
d = x2 - x1

N = 3

x = float(input( "Ievadiet " + str(N) + " locekli ===> "))


while x != 0:
    d1 = x - x2
    
    if d != d1:
        sv = "Dota virkne nav aritmētiska progresija"
        
    x2 = x
    N = N+1
    x =  float(input("Ievadiet " + str(N) + " locekli ===> "))   
else:
    print(sv)
   
   
    
if x==0: # pedējo un prikšpēdējo atņēmt
    d1 = x - x2
    if d != d1:
        sv = "Dota virkne nav aritmētiska progresija"     
else:
    print(sv)