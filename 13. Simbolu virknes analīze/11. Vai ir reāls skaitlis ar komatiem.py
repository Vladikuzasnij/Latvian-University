# Programmas nosaukums: 2. uzd MPR12
# 2. uzdevums MPR13
# Uzdevuma formulējums: Sastādīt testa programmu, kas pārbauda divos veidos (patstāvīgi analizējot simbolu virkni un izmantojot priekšraksta try ... except iespējas), vai ievadītā simbolu virkne ir reāls skaitlis.
# Versija 1.0

# Programma arī pārbauda skaitļus ar komatiem!

a=1
while a<=3:
    x = input("\nIevadi simbolu virkni ===> ")
    x=x.strip()

    if len(x)<1 or x=="." or x=="+" or x=="-" or x=="," or x[0] == "," or x[0:2] == "-," or x[0:2] == "+,":
        print("Ievadīta simbolu virkne nav reāls skaitlis (patstāvīgi analizējot simbolu virkni)")

    else:
        if (x[0]=="-") or (x[0]=="+"):
            y=1

        else:
            y=0

        p=0
        r=0

        for i in range(y,len(x)):
            s=x[i]

            if s=="." or s==",":
                p = p+1

            elif (s<"0" or s>"9"):
                r = r+1

        if (p==1 or p == 0) and r==0:
            print("Ievadīta simbolu virkne ir reāls skaitlis (patstāvīgi analizējot simbolu virkni)")

        else:
            print("Ievadīta simbolu virkne nav reāls skaitlis (patstāvīgi analizējot simbolu virkni)")



    # Ar try, except. Arī 5,2 arī tiek uzskaitīts par skaitli. Tiek izmantots if lai piemēram ,2 -,2 +,2 "skaitļus" neuzskaitītu par skaitliem

    try :
        if x[0] == "," or x[0:2] == "-," or x[0:2] == "+,":
            quit()
        x = float(x.replace(',', '.')) 
        b = float(x)

    except :
        print("Ievadīta simbolu virkne nav reāls skaitlis (izmantojot try/except)")
        a=a+1
    else:
        print("Ievadīta simbolu virkne ir reāls skaitlis (izmantojot try/except)")
        quit()
        
print("\nEs ar tādu 'gudru' lietotāju nesadarbošos!")