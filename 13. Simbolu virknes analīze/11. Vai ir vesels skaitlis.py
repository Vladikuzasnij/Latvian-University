# Programmas nosaukums: 3. uzd MPR12
# 3. uzdevums MPR13
# Uzdevuma formulējums: Sastādīt testa programmu, kas pārbauda divos veidos (patstāvīgi analizējot simbolu virkni un izmantojot priekšraksta try ... except iespējas), vai ievadītā simbolu virkne ir vesels skaitlis.
# Versija 1.0

# Programma neparbauda skaitļus ar komatiem.

a=1
while a<=3:
    x = input("\nIevadi simbolu virkni ===> ")
    x=x.strip()
    
    if len(x)<1 or x=="." or x=="+" or x=="-":
        print("Ievadīta simbolu virkne nav vesels skaitlis (patstāvīgi analizējot simbolu virkni)")
        
    else:
        if (x[0]=="-") or (x[0]=="+"):
            y=1
        else:
            y=0
        p=0
        r=0
        for i in range(y,len(x)):
            s=x[i]
            if s==".":
                p = p+1
            elif (s<"0" or s>"9"):
                r = r+1
        if (p == 0) and r==0:
            print("Ievadīta simbolu virkne ir vesels skaitlis (patstāvīgi analizējot simbolu virkni)")
            
        else:
            print("Ievadīta simbolu virkne nav vesels skaitlis (patstāvīgi analizējot simbolu virkni)")
    
    # Šeit nav uzskaitīts 2,2 skaitlis par skaitli
    try :
        
        b = int(x)

    except :
        print("Ievadīta simbolu virkne nav vesels skaitlis (izmantojot try/except)")
        a=a+1

    else:
        print("Ievadīta simbolu virkne ir vesels skaitlis (izmantojot try/except)")
        quit()
    
print("\nEs ar tādu 'gudru' lietotāju nesadarbošos!")