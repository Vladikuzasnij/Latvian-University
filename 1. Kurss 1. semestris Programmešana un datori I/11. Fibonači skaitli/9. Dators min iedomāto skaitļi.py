# Programmas nosaukums: 1. uzd PU1 MPR11
# 1. uzd PU1 MPR11
# Uzdevuma formulējums: Sastādīt programmu, kas nodrošina, ka dators pēc iepriekš aprakstītā algoritma min lietotāja iedomāto skaitli no 1 līdz N minēšanu. Skaitli N ievada lietotājs. Minēšana uz labu laimi - 1 punkts, minēšana ar mazāko nepareizo atbilžu skaitu (vispārīgajā gadījumā) - 3 punkti.
# Versija 1.0

import random
import math


min_diapazons = 1

try:
    max_diapazons = int(input("Programma minēs skaitļi intervalā [1, N] veseļos skaitļos \nIevadiet skaitļi N (maksimālo skaitļi, lai noteiktu diapazonu) \n==> "))
    print("\nIedomajiet veselo skaitļi no 1 līdz " + str(max_diapazons))
    print("\nJa mans minetāis skaitlis ir mazāks vai lielāks par jūsu iedomāto skaitļi, ievadiet attiecīgi “<” vai “>”, un, ja es uzminēju pareizi, ievadiet “=”")

except ValueError:
    print("Nepareiza ievade! Ievadiet veselo skaitļi!")
    quit(0)
    
    
rnd = math.floor(max_diapazons/2)
sk = 1
atbilde = ""


while 1 > 0:
    print("\nJūsu iedomatais skaitlis ir:\n" + str(rnd) + "\nvai es minēju? Intervāls no", min_diapazons, "līdz", max_diapazons)
    
    atbilde = input("Atbilde (>, <, =): ")
    
    if atbilde == "=":
        print("Es minēju jūsu skaitļi " + str(rnd) + " no " + str(sk) + " reizes. Spēle beigusies.")
        break
    
    elif atbilde == "<":
        max_diapazons = rnd - 1
        
        try:
            rnd = random.randint(min_diapazons, max_diapazons)
            sk = sk + 1
        except:
            print("Tā nevar būt! Tu melo! Es ar tevi vairs nespēlēšos!")
            break
            
    elif atbilde == ">":
        min_diapazons = rnd + 1
        
        try:
            rnd = random.randint(min_diapazons, max_diapazons)
            sk = sk + 1
        except:
            print("Tā nevar būt! Tu melo! Es ar tevi vairs nespēlēšos!")
            break
        
    else:
        print("Nepareiza ievade! Ievadiet: '<', '>' vai '='")