# Programmas nosaukums: 4. uzd MPR12
# 4. uzdevums MPR13
# Uzdevuma formulējums: Sastādīt programmu, kas pārbauda divos veidos (patstāvīgi analizējot simbolu virkni un izmantojot priekšraksta try ... except iespējas), vai ievadītā simbolu virkne ir naturāls skaitlis intervālā no A un B. Skaitļus A un B ievada lietotājs pirms testējamās vērtības ievades uzsākšanas.
# Versija 1.0

import math

A = input("Ievadi skaitli A ===> ")
B = input("Ievadi skaitli B ===> ")

try:
    d = float(A)
    e = float(B)
    
except:
    print("A vai B nav skaitlis")
    quit()
    
else:   
    A=A.strip()
    B=B.strip()

    if len(A)<1 or len(B)<1 or A =="." or A=="+" or A=="-" or B =="." or B=="+" or B=="-":
        print("A vai B nav skaitlis")
        quit()
        
a=1
while a<=3:
        x = input("\nIevadi simbolu virkni ===> ")
        x=x.strip()
    
    
        if len(x)<1 or x=="." or x=="+" or x=="-":
            print("\nIevadīta simbolu virkne nav naturāls skaitlis")
    
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
            #print("Ievadīta simbolu virkne ir vesels skaitlis")
            if float(x) <= 0:
                print("Ievadīta simbolu virkne nav naturāls skaitlis (patstāvīgi analizējot simbolu virkni)")
            else:
                #print("Ievadīta simbolu virkne ir naturāls skaitlis")
    
                A = float(A)
                B = float(B)
    
                if A > B:
                    K = B
                    B = A
                    A = K        
    
                if float(x) >= float(A) and float(x) <= float(B):
                    print("Ievadīta simbolu virkne ir naturāls skaitlis intervāla no " + str(A) + " līdz " + str(B) + " (patstāvīgi analizējot simbolu virkni)")
    
                else:
                    print("Ievadīta simbolu virkne ir naturāls skaitlis, bet skaitlis nav intervāla no " + str(A) + " līdz " + str(B) + " (patstāvīgi analizējot simbolu virkni)")        
    
        else:
            print("Ievadīta simbolu virkne nav naturāls skaitlis (patstāvīgi analizējot simbolu virkni)")

        try :
            t = float(x)
            b = int(x)
            k = math.sqrt(t)
            u = 0/(float(x))
                
        except:
            print("Ievadīta simbolu virkne nav naturāls skaitlis (izmantojot try/except)")
            a=a+1
    
        else:
            if x == 0:
                print("Ievadīta simbolu virkne nav naturāls skaitlis (izmantojot try/except)")
                
            if float(x) >= float(A) and float(x) <= float(B):
                print("Ievadīta simbolu virkne ir naturāls skaitlis intervāla no " + str(A) + " līdz " + str(B) + " (izmantojot try/except)")
                quit()
            else:
                print("Ievadīta simbolu virkne ir naturāls skaitlis, bet skaitlis nav intervāla no " + str(A) + " līdz " + str(B) + " (izmantojot try/except)")
                a=a+1
                
print("\nEs ar tādu 'gudru' lietotāju nesadarbošos!")