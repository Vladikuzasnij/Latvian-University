# Programmas nosaukums: 1. uzd MPR15
# 1. uzdevums MPR15
# Uzdevuma formulējums: Sastādīt programmu, kas nosaka punkta (XX, YY) koordinātas, ja zināms punkta (X, Y) koordinātas un rādiuss R, ko lietotājs ievada no tastatūras. Uzdevums risināms programmu strukturējot izmantojot funkcijas.
# Versija 1.0

import math

def is_real_number(x):
    while True:
        try:
            x = float(x)
        except:
            x = input("Mēģini vēlreiz ===> ")
        else:
            return float(x)
        
def is_real_positive_number(x):
    while True:
        try:
            x = float(x)
        except:
            x = input("Mēģini vēlreiz ===> ")
        else:
            if x <= 0:
                x = input("Mēģini vēlreiz ===> ")
            else:
                return float(x)
            
def lidzibas_koeficients(x,y,r):
    hipotenuzes_garums = math.sqrt(x*x + y*y) 
    k = r/hipotenuzes_garums # k - līdzības koeficients, r - rādiuss
    return k

def koordinatas_aprekinasana(a,k): # koordinātas aprēķināšana pēc līdzības koeficienta un vienas malas
    return a*k

# ----------------------------------------------

print("Programma nosaka punkta (XX, YY) koordinātas, ja zināms punkta (X, Y) koordinātas un rādiuss R, ko lietotājs ievada no tastatūras.\n")

x = input("Ievadiet X koordinātu ===> ")
x = is_real_number(x)

y = input("Ievadiet Y koordinātu ===> ")
y = is_real_number(y)

if x == 0 and y == 0:
    print("Nav iespējami noteikt")
    quit()

r = input("Ievadiet rādiusu R ===> ")
r = is_real_positive_number(r)

k = lidzibas_koeficients(x,y,r)

x_koordinatas = koordinatas_aprekinasana(x,k)
y_koordinatas = koordinatas_aprekinasana(y,k)

print("\n(XX, YY) = (" + str(x_koordinatas) + ", " + str(y_koordinatas) + ")")