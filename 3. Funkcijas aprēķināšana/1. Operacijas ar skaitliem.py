# Programmas nosaukums: Dažas operācijas ar diviem veseliem skaitļiem
# 1. uzdevums
# Uzdevuma formulējums: Izveidot programmu, kurā ievadot divus veselus skaitļus, tiek iegūta šo skaitļu summa (+), starpība (-), reizinājums (*), dalījums (/), veselais dalījums (//) un dalīšanas atlikums (%).
# Programmas autors: Vladislavs Babaņins
# Versija 1.4

print("\"Dažas operācijas ar diviem veseliem skaitļiem\"\nVersija 1.4\n") # Programmas nosaukums un vērsija parādas

a=int(input("Ievadi pirmo veselo skaitļi ===>")) # Pieprasa skaitļi a un input'u => integer
b=int(input("Ievadi otro veselo skaitļi ===>")) # Pieprasa skaitļi b un input'u => integer

print(str(a) + "+" + str(b) + "=" + str(a+b) + " Summa") # Vienā rinda programma saskaita a un b un ievāda to tekstā str() veidā
print(str(a) + "-" + str(b) + "=" + str(a-b) + " Starpība") # Pēc analoģijas izdarīts tas pats visām nepieciešāmam operācijām
print(str(b) + "-" + str(a) + "=" + str(b-a) + " Starpība")
print(str(a) + "*" + str(b) + "=" + str(a*b) + " Reizinājums")
print(str(a) + "/" + str(b) + "=" + str(a/b) + " Dalījums")
print(str(b) + "/" + str(a) + "=" + str(b/a) + " Dalījums")
print(str(a) + "//" + str(b) + "=" + str(a//b) + " Veselais dalījums")
print(str(b) + "//" + str(a) + "=" + str(b//a) + " Veselais dalījums")
print(str(a) + "%" + str(b) + "=" + str(a%b) + " Dalīšanas atlikums")
print(str(b) + "%" + str(a) + "=" + str(b%a) + " Dalīšanas atlikums")