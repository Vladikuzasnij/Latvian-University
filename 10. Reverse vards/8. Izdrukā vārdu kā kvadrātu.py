# Programmas nosaukums: 3. uzd MPR10
# 3. uzdevums MPR10
# Uzdevuma formulējums: Sastādīt programmu, kas lietotāja ievadīto vārdu izkārto ka parādīts piemērā.
# Versija 1.0

x = str(input("Ievādi vārdu => "))

n = len(x)

print(x)

for i in range (1, n-1):
    sv = x[i]
    
    sv = sv + (n-2)*" "
    
    sv = sv + x[n-1-i]
    print(sv)
    
sv = ""

for i in x:
    sv = i + sv
print(sv)