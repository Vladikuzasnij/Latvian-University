# Programmas nosaukums: Divargumentu funkciju vērtība
# 2. uzdevums
# Uzdevuma formulējums: Izveidot programmu, kura aprēķina un paziņo divargumentu funkcijas vērtību. Funkcija: f(x,y) = (log2(1+cbrt(x^2)+sin(y))/(Abs(x-y)+1
# Programmas autors: Vladislavs Babaņins
# Versija 1.6

import math # Bibliotēkas math pieslēgšana

print("\"Divargumentu funkciju vērtība\"\nVersija 1.6\n") # Nosaukums un vērsija

x=int(input("Ievadi x vērtibu ===>")) 
y=int(input("Ievadi y vērtibu ===>"))

function_value=(math.log2(1+((x**2)**(1/3)))+math.sin(y))/((abs(x-y))+1) # Funkcijas vērtības apreķināšana ar funkcijas math.sin un math.log2

print("Funkcijas vērtība, kad x="+str(x)+" un y="+str(y)+", ir vienāda ar: "+str(function_value)) # Lai savienotu str un int vērtibas pārveidosim iegūto funkcijas vērtibu par str