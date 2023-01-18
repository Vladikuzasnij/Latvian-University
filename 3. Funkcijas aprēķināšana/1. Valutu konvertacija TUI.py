# Programmas nosaukums: Valūtu konvertācija
# 4. uzdevums
# Uzdevuma formulējums: Izveidot programmu, kura konvertē EUR -> USD un USD -> EUR.
# Programmas autors: Vladislavs Babaņins
# Versija 1.4

# 1 USD = 1.01002 EUR
# 1 EUR = 0.98715628 USD

import math

print("\"Valūtu konvertācija\"\nVersija 1.4\n") # Programmas nosaukums


a=int(input("EUR=>USD vai USD=>EUR \nJa EUR=>USD tad 1, ja USD=>EUR tad 2 ====>")) # EUR => USD vai USD => EUR izvēle ar 1 vai 2

if a == 1: # Ja tika ievādits 1 (EUR => USD) tad izpildās komandas:
    EUR=input("EUR=>USD \nEUR vērtiba ==>") # EUR vērtību ievādišana
    EUR_to_USD=float(EUR)*0.98715628 # Valūtu konvertācija
    print("Vērtiba ir " + str(EUR_to_USD) +" USD") # Ievadīšana ekrāna
    
elif a == 2: # Ja tika ievādits 2 (USD => EUR) tad izpildās komandas:
    USD=input("USD=>EUR \nUSD vērtiba ==>") # USD vērtību ievādišana
    USD_to_EUR=float(USD)*1.01002 # Valūtu konvertācija
    print("Vērtiba ir " + str(USD_to_EUR)+" EUR") # Ievadīšana ekrāna
    
else:
    print("Error") # Ja tika ievadīts ne 1 vai 2, tad ir "Error"