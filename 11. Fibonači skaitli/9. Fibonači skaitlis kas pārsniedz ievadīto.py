# Programmas nosaukums: 3. uzd MPR11
# 3. uzdevums MPR11
# Uzdevuma formulējums: Sastādīt programmu, kas nosaka mazāko Fibonači skaitli, kas pārsniedz lietotāja ievadīto skaitli N.
# Versija 1.0

print("Programma nosaka mazāko Fibonači skaitli (skaitli no Fibonači virknes), kas pārsniedz lietotāja ievadīto skaitli N.")
n = float(input("Ievadiet skaitli N ==> "))

b=1
a=1
c=0         # a,b=b,a+b (ja to izmantojam, tad nevajadzēs izmantot palīgmainīgo c)

while n>=a: # kāmer n>=a, tad 
   
            # a,b=b,a+b
            # var arī to konstrukciju izmantot
   c = a + b
   a = b
   b = c
    
print("Mazakais Fibonači skaitlis, kas pārsniedz skaitli " + str(n) + " ir " + str(a))