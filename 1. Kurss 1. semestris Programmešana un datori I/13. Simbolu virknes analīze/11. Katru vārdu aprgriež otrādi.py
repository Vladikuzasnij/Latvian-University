# Programmas nosaukums: 1. uzd MPR12
# 1. uzdevums MPR13
# Uzdevuma formulējums: Sastādīt programmu, kas lietotāja ievadītājā simbolu virknē katru vārdu apgriež otrādi. Zināms, ka lietotāja ievadītajā simbolu virknē katrs vārds viens no otra ir atdalīts tieši ar vienu tukšumu.
# Versija 1.0

x = input("Ievadi simbolu virkni ===> ")

x = x.strip()
n = len(x)

v = ""
sv = ""

for i in range(n): # for s in x
    if x[i] != " " :  # s ! = ""
        v = x[i] + v # v = s + v
        
    else:
        sv = sv + v + " "
        v = ""
sv = sv + v

print(sv)