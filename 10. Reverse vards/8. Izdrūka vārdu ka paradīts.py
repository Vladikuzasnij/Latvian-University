# Programmas nosaukums: 2. uzd MPR10
# 2. uzdevums MPR10
# Uzdevuma formulējums: Sastādīt programmu, kas lietotāja ievadīto vārdu izkārto kā parādīts piemērā.
# Versija 1.0


x=input("Ievadi simbolu virkni => ")
n=len(x)
for i in range (n):
    print(x[i:n]+x[0:i])